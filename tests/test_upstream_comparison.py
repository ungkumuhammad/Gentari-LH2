"""Tests for scripts/run_upstream_comparison.py (liquefaction vs Haber-Bosch,
100 ktpa H2 upstream comparison), mirrored by the artifact's "Upstream" sheet.

Covers: the first-principles reaction-heat derivation, the steam-turbine credit
never being able to swallow the plant's own demand, the equal-volume vs
equal-days tank bases, the two parity solvers actually zeroing their difference
functions, and the "no fabricated numbers" invariant that the LH2 side reuses
src/lh2 primitives rather than re-implementing them.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest  # noqa: E402

import run_upstream_comparison as m  # noqa: E402
from lh2 import liquefaction  # noqa: E402


# --------------------------------------------------------------------------
# thermochemistry
# --------------------------------------------------------------------------

def test_reaction_heat_matches_the_repository_cracking_duty():
    """Synthesis heat released == cracking heat required: same reaction, both
    ways. data/carriers/chain-energy-defaults.csv carries 4.22 kWh/kg-H2 for
    the cracker's reaction duty; the synthesis credit must derive to the same
    number from the same 45.9 kJ/mol-NH3 enthalpy."""
    assert m.reaction_heat_per_kg_h2(m.Inputs()) == pytest.approx(4.22, abs=0.01)


def test_reaction_heat_is_linear_in_the_enthalpy():
    a = m.reaction_heat_per_kg_h2(m.Inputs(rxn_enthalpy_kj_per_mol_nh3=45.9))
    b = m.reaction_heat_per_kg_h2(m.Inputs(rxn_enthalpy_kj_per_mol_nh3=91.8))
    assert b == pytest.approx(2 * a)


def test_steam_credit_is_the_product_of_both_efficiencies():
    inp = m.Inputs(heat_recovery_pct=75, turbine_eff_pct=30)
    assert m.steam_credit_per_kg_h2(inp) == pytest.approx(
        m.reaction_heat_per_kg_h2(inp) * 0.75 * 0.30
    )


def test_steam_credit_can_be_switched_off_entirely():
    assert m.steam_credit_per_kg_h2(m.Inputs(steam_credit_on=False)) == 0.0


def test_credit_never_exceeds_the_synthesis_plants_own_demand():
    """Even at a physically absurd 100% recovery x 45% turbine the ammonia route
    stays a net consumer. If this ever fails the model has stopped being a
    conversion plant and become a power station."""
    inp = m.Inputs(heat_recovery_pct=100, turbine_eff_pct=45)
    n = m.evaluate_nh3(inp)
    assert n.credit_kwh < n.conversion_kwh
    assert n.net_mw > 0


# --------------------------------------------------------------------------
# mass balance
# --------------------------------------------------------------------------

def test_nh3_produced_follows_stoichiometry_net_of_the_purge_loss():
    inp = m.Inputs(hb_h2_loss_pct=2.0)
    n = m.evaluate_nh3(inp)
    assert n.carrier_kg == pytest.approx(inp.h2_ktpa * 1e6 * 0.98 * m.NH3_PER_H2)
    assert n.h2_delivered_kg == pytest.approx(n.carrier_kg / m.NH3_PER_H2)


def test_lh2_route_loses_no_hydrogen():
    """KHI reply Q15: no H2 losses in the LH2 plant concept under consideration."""
    l = m.evaluate_lh2(m.Inputs())
    assert l.h2_delivered_kg == l.h2_fed_kg


def test_hb_electricity_per_kg_delivered_is_independent_of_the_purge_loss():
    """Both the ammonia produced and the H2 delivered scale with (1 - loss), so
    the loss cancels exactly in synthesis kWh per kg H2 delivered -- it is
    always RATIO x the per-kg-NH3 figure. A regression here would mean the two
    are no longer being divided on the same basis."""
    for loss in (0.0, 2.0, 8.0):
        n = m.evaluate_nh3(m.Inputs(hb_h2_loss_pct=loss))
        assert n.conversion_kwh / n.h2_delivered_kg == pytest.approx(
            m.Inputs().hb_sec * m.NH3_PER_H2, rel=1e-9
        )


def test_on_the_equal_days_basis_the_whole_total_is_loss_independent():
    """With the tank sized off throughput, the terminal scales with production
    too, so every term in kWh/kg-delivered becomes loss-independent."""
    a = m.evaluate_nh3(m.Inputs(tank_basis="days", hb_h2_loss_pct=0.0))
    b = m.evaluate_nh3(m.Inputs(tank_basis="days", hb_h2_loss_pct=8.0))
    assert a.net_kwh_per_kg_h2 == pytest.approx(b.net_kwh_per_kg_h2, rel=1e-9)


# --------------------------------------------------------------------------
# reuse of the modelling library, not a re-implementation
# --------------------------------------------------------------------------

def test_liquefaction_energy_comes_from_the_lh2_module():
    inp = m.Inputs()
    expected = liquefaction.liquefaction_energy(
        inp.h2_ktpa * 1e6, __import__("lh2.units", fromlist=["Q_"]).Q_(inp.lh2_sec, "kWh/kg")
    ).magnitude
    assert m.evaluate_lh2(inp).conversion_kwh == pytest.approx(expected)


def test_lh2_sec_default_sits_inside_khis_disclosed_range():
    assert (
        liquefaction.KHI_SEC_LOW.magnitude
        <= m.Inputs().lh2_sec
        <= liquefaction.KHI_SEC_HIGH.magnitude
    )


# --------------------------------------------------------------------------
# terminal
# --------------------------------------------------------------------------

def test_fixed_basis_gives_both_routes_the_same_tank_volume():
    inp = m.Inputs(tank_basis="fixed", tank_m3=60_000)
    assert m.evaluate_lh2(inp).tank_m3 == m.evaluate_nh3(inp).tank_m3 == 60_000


def test_equal_volume_stores_more_hydrogen_as_ammonia():
    """682 kg/m3 at 17.75% H2 beats 70.8 kg/m3 of liquid hydrogen. The ratio is
    a property of the two densities, not of the tank size."""
    inp = m.Inputs(tank_basis="fixed")
    l, n = m.evaluate_lh2(inp), m.evaluate_nh3(inp)
    stored_ratio = (n.inventory_kg / m.NH3_PER_H2) / l.inventory_kg
    assert stored_ratio == pytest.approx(
        (inp.nh3_rho / m.NH3_PER_H2) / inp.lh2_rho, rel=1e-9
    )
    assert stored_ratio > 1.0
    assert n.days_of_cover > l.days_of_cover


def test_equal_days_basis_gives_both_routes_the_same_cover():
    inp = m.Inputs(tank_basis="days", hold_days=5.0)
    l, n = m.evaluate_lh2(inp), m.evaluate_nh3(inp)
    assert l.days_of_cover == pytest.approx(5.0)
    assert n.days_of_cover == pytest.approx(5.0)
    # ...and it is then the LH2 side that needs the bigger tank
    assert l.tank_m3 > n.tank_m3


def test_terminal_boil_off_is_charged_over_the_full_calendar_year():
    """The tank boils off whether or not the plant is running, so terminal power
    is annual energy / 8760 h, not / operating hours."""
    inp = m.Inputs(operating_hours=6000)
    l = m.evaluate_lh2(inp)
    assert l.terminal_mw == pytest.approx(l.terminal_kwh / 8760 / 1000)


def test_terminal_is_a_rounding_error_at_the_disclosed_boil_off_rate():
    l = m.evaluate_lh2(m.Inputs())
    assert l.terminal_mw / l.conversion_mw < 0.01


# --------------------------------------------------------------------------
# parity solvers
# --------------------------------------------------------------------------

def test_parity_lh2_sec_actually_equalises_the_two_routes():
    inp = m.Inputs()
    sec = m.parity_lh2_sec(inp)
    at_parity = m.evaluate_lh2(m.Inputs(lh2_sec=sec))
    assert at_parity.net_mw == pytest.approx(m.evaluate_nh3(inp).net_mw, rel=1e-9)


def test_parity_is_solved_on_power_not_on_annual_energy():
    """Conversion runs for `operating_hours`, the terminal for all 8 760 h, so
    equal annual kWh and equal MW are different equations. The charts read in
    MW, so the solvers must too -- and the two answers must differ whenever the
    plant is not on stream every hour of the year."""
    inp = m.Inputs(operating_hours=8000)
    l = m.evaluate_lh2(m.Inputs(lh2_sec=m.parity_lh2_sec(inp)))
    n = m.evaluate_nh3(inp)
    assert l.net_mw == pytest.approx(n.net_mw, rel=1e-9)
    energy_basis_sec = (
        n.conversion_kwh - n.credit_kwh + n.terminal_kwh
        - m.evaluate_lh2(inp).terminal_kwh
    ) / l.h2_fed_kg
    assert energy_basis_sec != pytest.approx(m.parity_lh2_sec(inp), rel=1e-6)


def test_parity_hb_sec_actually_equalises_the_two_routes():
    inp = m.Inputs()
    sec = m.parity_hb_sec(inp)
    at_parity = m.evaluate_nh3(m.Inputs(hb_sec=sec))
    assert at_parity.net_mw == pytest.approx(m.evaluate_lh2(inp).net_mw, rel=1e-9)


def test_parity_liquefaction_sec_sits_below_the_thermodynamic_floor():
    """The headline finding, pinned. At the defaults, matching the ammonia route
    would need a liquefier below the reversible work of liquefaction -- so no
    machine can reach it. Holds with the steam credit excluded too, which is the
    stronger form of the claim."""
    assert m.parity_lh2_sec(m.Inputs()) < m.THEORETICAL_MIN_NORMAL
    assert m.parity_lh2_sec(m.Inputs(steam_credit_on=False)) < m.THEORETICAL_MIN_PARA


def test_the_ranking_survives_a_large_error_in_the_haber_bosch_estimate():
    """The Haber-Bosch SEC is an [ESTIMATE] placeholder (decision D4). The
    conclusion is only worth stating if it tolerates that figure being badly
    wrong -- here, wrong by 2x."""
    inp = m.Inputs(hb_sec=m.Inputs().hb_sec * 2)
    assert m.evaluate_nh3(inp).net_mw < m.evaluate_lh2(inp).net_mw


def test_a_perfect_liquefier_still_loses_on_upstream_electricity():
    inp = m.Inputs(lh2_sec=m.THEORETICAL_MIN_PARA)
    assert m.evaluate_lh2(inp).net_mw > m.evaluate_nh3(inp).net_mw


# --------------------------------------------------------------------------
# scale / units
# --------------------------------------------------------------------------

def test_power_scales_linearly_with_throughput():
    a = m.evaluate_lh2(m.Inputs(h2_ktpa=100)).conversion_mw
    b = m.evaluate_lh2(m.Inputs(h2_ktpa=200)).conversion_mw
    assert b == pytest.approx(2 * a)


def test_share_of_lhv_is_consistent_with_the_per_kg_figure():
    l = m.evaluate_lh2(m.Inputs())
    assert l.share_of_h2_lhv_pct == pytest.approx(
        l.net_kwh_per_kg_h2 / m.H2_LHV_KWH * 100
    )


def test_lh2_upstream_energy_is_a_large_fraction_of_the_hydrogens_own_lhv():
    """Sanity band, not a fabricated figure: at KHI's 8-9 kWh/kg the liquefier
    alone spends roughly a quarter of the hydrogen's heating value."""
    assert 20.0 < m.evaluate_lh2(m.Inputs()).share_of_h2_lhv_pct < 35.0


def test_cli_runs_and_reports_both_routes():
    assert m.main([]) == 0
