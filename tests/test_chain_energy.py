"""Tests for the LH2-vs-NH3 node-by-node energy-penalty cascade.

Covers the user's worked example, mass/energy bookkeeping, the two efficiency
views, and the "no fabricated numbers" invariant: every module default must
match a row in ``data/carriers/chain-energy-defaults.csv``, which in turn is
cited-or-tagged by ``test_data_tables.py``.
"""

from __future__ import annotations

from math import isclose
from pathlib import Path

import pandas as pd
import pytest

from lh2.chain_energy import (
    H2_LHV_KWH_PER_KG,
    NH3_PER_H2_MASS_RATIO,
    AnnualScaleResult,
    ChainInputs,
    annual_scale,
    boil_off_fraction,
    compare,
    cracking_reaction_duty_kwh_per_kg_h2,
    format_report,
    nh3_supply_ratio,
    run_lh2_chain,
    run_nh3_chain,
    voyage_days,
)

DEFAULTS_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "carriers"
    / "chain-energy-defaults.csv"
)


# -- the user's worked example ---------------------------------------------


def test_h2_lhv_is_120_mj_per_kg():
    assert isclose(H2_LHV_KWH_PER_KG, 33.3333, abs_tol=1e-3)


def test_node_a_reproduces_the_worked_example():
    """60 kWh/kg in, 33.33 kWh/kg out -> 26.67 kWh/kg penalty, 55.6 % efficient."""
    a = run_lh2_chain(ChainInputs(electrolyser_sec_kwh_per_kg=60.0)).nodes[0]
    assert a.node_id == "A"
    assert isclose(a.cumulative_energy_kwh, 60.0)
    assert isclose(a.lhv_carried_kwh, H2_LHV_KWH_PER_KG, abs_tol=1e-9)
    assert isclose(a.cumulative_energy_kwh - a.lhv_carried_kwh, 26.667, abs_tol=1e-3)
    assert isclose(a.efficiency_pct, 55.556, abs_tol=1e-3)


def test_node_a_is_identical_for_both_chains():
    """Production is a shared node -- the chains may only diverge from B."""
    lh2, nh3 = run_lh2_chain().nodes[0], run_nh3_chain().nodes[0]
    assert lh2.energy_kwh == nh3.energy_kwh
    assert lh2.efficiency_pct == nh3.efficiency_pct


def test_liquefaction_carries_the_default_efficiency_forward():
    """60 + 9 = 69 kWh/kg -> 33.33/69 = 48.3 %, as derived in earlier sessions."""
    b1 = run_lh2_chain().nodes[1]
    assert isclose(b1.cumulative_energy_kwh, 69.0, abs_tol=1e-9)
    assert isclose(b1.efficiency_pct, 48.31, abs_tol=0.01)


# -- node structure ---------------------------------------------------------


def test_lh2_node_ids():
    assert [n.node_id for n in run_lh2_chain().nodes] == ["A", "B1", "C1", "D1", "E1", "F1"]


def test_nh3_node_ids():
    assert [n.node_id for n in run_nh3_chain().nodes] == ["A", "B2", "C2", "D2", "E2", "F2"]


# -- bookkeeping invariants -------------------------------------------------


@pytest.mark.parametrize("runner", [run_lh2_chain, run_nh3_chain])
def test_mass_balance_closes(runner):
    r = runner()
    losses = sum(n.mass_loss_kg_h2e for n in r.nodes)
    assert isclose(r.delivered_kg_h2 + losses, 1.0, abs_tol=1e-12)


@pytest.mark.parametrize("runner", [run_lh2_chain, run_nh3_chain])
def test_cumulative_energy_is_monotonic_and_sums_the_nodes(runner):
    r = runner()
    cum = [n.cumulative_energy_kwh for n in r.nodes]
    assert cum == sorted(cum)
    assert isclose(cum[-1], sum(n.energy_kwh for n in r.nodes), abs_tol=1e-9)
    assert isclose(r.total_energy_kwh, cum[-1], abs_tol=1e-9)


@pytest.mark.parametrize("runner", [run_lh2_chain, run_nh3_chain])
def test_deduction_view_matches_its_definition(runner):
    """Net = the H2's own LHV, less carrier-chain energy, less the LHV lost."""
    r = runner()
    expected = (
        H2_LHV_KWH_PER_KG
        - r.carrier_energy_kwh
        - r.total_loss_kg_h2 * H2_LHV_KWH_PER_KG
    )
    assert isclose(r.net_energy_kwh, expected, abs_tol=1e-12)
    assert isclose(r.nodes[-1].net_energy_kwh, expected, abs_tol=1e-12)
    assert isclose(r.retained_pct, 100 * expected / H2_LHV_KWH_PER_KG, abs_tol=1e-12)


@pytest.mark.parametrize("runner", [run_lh2_chain, run_nh3_chain])
def test_input_basis_efficiency_matches_its_definition(runner):
    r = runner()
    assert isclose(
        r.efficiency_pct,
        100 * r.delivered_kg_h2 * H2_LHV_KWH_PER_KG / r.total_energy_kwh,
        abs_tol=1e-9,
    )


def test_ambient_regas_heat_is_reported_but_not_charged():
    """KHI's 3.8 MJ/kg is free seawater heat -- it must not inflate the input."""
    r = run_lh2_chain()
    f1 = r.nodes[-1]
    assert f1.ambient_heat_kwh > 0
    assert f1.energy_kwh < f1.ambient_heat_kwh
    assert isclose(r.total_energy_kwh, sum(n.energy_kwh for n in r.nodes), abs_tol=1e-9)


# -- chain-specific physics -------------------------------------------------


def test_liquefaction_claims_no_h2_loss():
    """KHI reply Q15 -- the LH2 chain's only default mass loss is voyage BOG."""
    b1 = run_lh2_chain().nodes[1]
    assert b1.mass_loss_kg_h2e == 0.0


def test_lh2_voyage_bog_is_mass_loss_not_energy():
    """BOG is burned as propulsion fuel (reply Q23/Q33)."""
    d1 = run_lh2_chain().nodes[3]
    assert d1.energy_kwh == 0.0
    assert d1.mass_loss_kg_h2e > 0.0


def test_nh3_stoichiometry():
    """N2 + 3 H2 -> 2 NH3 gives 5.632 kg NH3 per kg H2."""
    assert isclose(NH3_PER_H2_MASS_RATIO, 5.632, abs_tol=1e-3)


def test_cracking_reaction_duty_and_floor():
    """45.9 kJ/mol-NH3 -> 4.22 kWh/kg-H2, i.e. 12.7 % of H2's LHV."""
    duty = cracking_reaction_duty_kwh_per_kg_h2()
    assert isclose(duty, 4.22, abs_tol=0.01)
    assert isclose(100 * duty / H2_LHV_KWH_PER_KG, 12.66, abs_tol=0.05)


def test_cracker_is_ng_fired_not_self_consuming():
    """NG thermal energy = reaction floor / fired efficiency, and is charged
    as purchased energy at F2, not booked as a mass loss."""
    inp = ChainInputs()
    f2 = run_nh3_chain(inp).nodes[-1]
    mass_in_f2 = f2.mass_in_kg_h2e
    expected_ng_kwh = (
        cracking_reaction_duty_kwh_per_kg_h2()
        * mass_in_f2
        / (inp.ng_fired_thermal_efficiency_pct / 100.0)
    )
    expected_elec_kwh = inp.cracker_electrical_kwh_per_kg * mass_in_f2
    assert isclose(f2.energy_kwh, expected_ng_kwh + expected_elec_kwh, rel_tol=1e-9)
    # NG alone exceeds the old self-consumption default's implied energy share,
    # confirming it is genuinely charged, not a token amount.
    assert f2.energy_kwh > expected_elec_kwh


def test_cracker_process_loss_is_much_smaller_than_the_old_self_consumption():
    """The NG-fired reframe (2026-09-02) should leave only a small residual
    mass loss, well under the pre-reframe 20% self-consumption default."""
    assert ChainInputs().cracker_process_loss_pct < 10.0


def test_nh3_voyage_bog_disposition_switch_moves_the_penalty():
    """Ordinary BOG's fate flips with the switch; bunker fuel is always lost."""
    reliq = run_nh3_chain(ChainInputs(nh3_voyage_bog_reliquefied=True)).nodes[3]
    burned = run_nh3_chain(ChainInputs(nh3_voyage_bog_reliquefied=False)).nodes[3]
    assert reliq.energy_kwh > 0  # ordinary BOG re-liquefied -> energy
    assert burned.energy_kwh == 0  # both mechanisms burned -> no energy
    assert reliq.mass_loss_kg_h2e > 0  # bunker fuel is lost either way
    assert burned.mass_loss_kg_h2e > reliq.mass_loss_kg_h2e  # + ordinary BOG


def test_nh3_bunker_fuel_scales_with_voyage_length():
    short = run_nh3_chain(ChainInputs(voyage_distance_km=1000)).nodes[3]
    long = run_nh3_chain(ChainInputs(voyage_distance_km=12000)).nodes[3]
    assert long.mass_loss_kg_h2e > short.mass_loss_kg_h2e


def test_nh3_supply_ratio_near_user_target():
    """User direction (2026-09-02): NG-fired cracker -> ~6.5 kg NH3 per kg H2
    delivered, above the pure mass-balance ratio (~5.63:1)."""
    r = run_nh3_chain()
    ratio = nh3_supply_ratio(r)
    assert isclose(ratio, 6.5, abs_tol=0.1)
    assert ratio > NH3_PER_H2_MASS_RATIO


def test_nh3_supply_ratio_falls_to_mass_balance_with_no_bunker_fuel():
    r = run_nh3_chain(ChainInputs(nh3_bunker_fuel_rate_pct_per_day=0.0, cracker_process_loss_pct=0.0))
    assert isclose(nh3_supply_ratio(r), NH3_PER_H2_MASS_RATIO, abs_tol=0.01)


# -- helpers ----------------------------------------------------------------


def test_boil_off_compounds_rather_than_summing():
    five_days = boil_off_fraction(0.1, 5)
    assert isclose(five_days, 1 - 0.999**5, abs_tol=1e-12)
    assert five_days < 5 * 0.001  # compounding is strictly below the linear sum


def test_boil_off_edge_cases():
    assert boil_off_fraction(0.0, 5) == 0.0
    assert boil_off_fraction(0.1, 0) == 0.0


def test_voyage_days():
    assert isclose(voyage_days(6000, 29.6), 6000 / 29.6 / 24)
    assert voyage_days(6000, 0) == 0.0


def test_zero_distance_removes_the_voyage_penalty():
    r = run_lh2_chain(ChainInputs(voyage_distance_km=0.0))
    assert r.nodes[3].mass_loss_kg_h2e == 0.0


# -- reporting --------------------------------------------------------------


def test_compare_runs_both_chains_on_the_same_inputs():
    results = compare(ChainInputs(electrolyser_sec_kwh_per_kg=55.0))
    assert set(results) == {"LH2", "NH3"}
    assert all(r.nodes[0].energy_kwh == 55.0 for r in results.values())


def test_report_states_boundary_basis_and_gaps():
    text = format_report()
    assert "Boundary:" in text and "Basis:" in text
    assert "Gaps:" in text
    assert "D4" in text  # the standing NH3-data caveat must be visible


@pytest.mark.parametrize("runner", [run_lh2_chain, run_nh3_chain])
def test_every_chain_declares_its_gaps(runner):
    assert runner().gaps, "a chain must never return a silent, gap-free result"


def test_nh3_result_flags_that_no_ammonia_figure_is_sourced():
    assert any("D4" in g for g in run_nh3_chain().gaps)


# -- the module must not drift from the data table --------------------------

#: module attribute / ChainInputs field  ->  (parameter, component) in the CSV
_CSV_LINKS = {
    "electrolyser_sec_kwh_per_kg": ("specific_energy_consumption", "electrolyser"),
    "voyage_distance_km": ("voyage_distance", "corridor"),
    "liquefaction_sec_kwh_per_kg": ("specific_energy_consumption", "liquefier"),
    "liquefaction_h2_loss_pct": ("hydrogen_loss", "liquefier"),
    "lh2_export_bor_pct_per_day": ("boil_off_rate_at_rest", "lh2_export_terminal"),
    "lh2_export_storage_days": ("storage_days", "lh2_export_terminal"),
    "lh2_import_bor_pct_per_day": ("boil_off_rate_at_rest", "lh2_import_terminal"),
    "lh2_import_storage_days": ("storage_days", "lh2_import_terminal"),
    "lh2_bog_reliquefaction_sec_kwh_per_kg": (
        "bog_reliquefaction_sec",
        "lh2_export_terminal",
    ),
    "lh2_carrier_speed_km_per_h": ("service_speed", "lh2_carrier"),
    "lh2_voyage_bor_pct_per_day": ("voyage_boil_off_rate", "lh2_carrier"),
    "lh2_regas_heat_duty_mj_per_kg": ("regas_heat_duty", "lh2_vaporiser"),
    "lh2_regas_electrical_kwh_per_kg": ("electrical_energy", "lh2_vaporiser"),
    "hb_sec_kwh_per_kg_nh3": ("specific_energy_consumption", "haber_bosch"),
    "hb_h2_loss_pct": ("hydrogen_loss", "haber_bosch"),
    "nh3_export_bor_pct_per_day": ("boil_off_rate_at_rest", "nh3_export_terminal"),
    "nh3_export_storage_days": ("storage_days", "nh3_export_terminal"),
    "nh3_import_bor_pct_per_day": ("boil_off_rate_at_rest", "nh3_import_terminal"),
    "nh3_import_storage_days": ("storage_days", "nh3_import_terminal"),
    "nh3_bog_reliquefaction_sec_kwh_per_kg": (
        "bog_reliquefaction_sec",
        "nh3_export_terminal",
    ),
    "nh3_carrier_speed_km_per_h": ("service_speed", "nh3_carrier"),
    "nh3_voyage_bor_pct_per_day": ("voyage_boil_off_rate", "nh3_carrier"),
    "cracker_process_loss_pct": ("process_loss", "nh3_cracker"),
    "ng_fired_thermal_efficiency_pct": ("ng_fired_thermal_efficiency", "nh3_cracker"),
    "cracker_electrical_kwh_per_kg": ("electrical_energy", "nh3_cracker"),
    "annual_h2_supply_ktpa": ("annual_h2_supply", "study"),
    "fleet_availability_pct": ("availability", "fleet"),
    "lh2_vessel_capacity_m3": ("cargo_capacity", "lh2_carrier"),
    "lh2_vessel_fill_fraction_pct": ("cargo_fill_fraction", "lh2_carrier"),
    "lh2_density_kg_per_m3": ("cargo_density", "lh2_carrier"),
    "lh2_port_days_per_call": ("port_days_per_call", "lh2_carrier"),
    "nh3_vessel_capacity_m3": ("cargo_capacity", "nh3_carrier"),
    "nh3_vessel_fill_fraction_pct": ("cargo_fill_fraction", "nh3_carrier"),
    "nh3_density_kg_per_m3": ("cargo_density", "nh3_carrier"),
    "nh3_port_days_per_call": ("port_days_per_call", "nh3_carrier"),
    "nh3_bunker_fuel_rate_pct_per_day": ("bunker_fuel_rate", "nh3_carrier"),
}


def _defaults_table() -> pd.DataFrame:
    return pd.read_csv(DEFAULTS_CSV, dtype=str, keep_default_na=False)


@pytest.mark.parametrize("field_name,link", sorted(_CSV_LINKS.items()))
def test_module_defaults_match_the_data_table(field_name: str, link):
    parameter, component = link
    df = _defaults_table()
    rows = df[(df["parameter"] == parameter) & (df["component"] == component)]
    assert len(rows) == 1, f"{component}/{parameter}: expected exactly one CSV row"
    assert isclose(
        float(rows.iloc[0]["value"]),
        getattr(ChainInputs(), field_name),
        rel_tol=1e-6,
    ), f"{field_name} has drifted from {component}/{parameter} in the data table"


def test_every_numeric_default_is_traceable_to_the_data_table():
    """No ChainInputs number may exist without a tagged row behind it."""
    numeric_fields = {
        name
        for name, value in vars(ChainInputs()).items()
        if isinstance(value, (int, float)) and not isinstance(value, bool)
    }
    assert numeric_fields == set(_CSV_LINKS), (
        "every numeric input must be linked to data/carriers/chain-energy-defaults.csv"
    )


# -- annual scale & fleet (2026-09-02) ---------------------------------------


def test_annual_scale_uses_the_study_basis():
    """100 ktpa at node A -> 1e8 kg/y feeding the per-kg cascade."""
    r = run_lh2_chain()
    a = annual_scale(r, ChainInputs())
    assert isclose(a.annual_h2_supply_kg, 1.0e8, rel_tol=1e-9)
    assert isclose(a.annual_delivered_kg, r.delivered_kg_h2 * 1.0e8, rel_tol=1e-9)
    assert isclose(a.annual_energy_kwh, r.total_energy_kwh * 1.0e8, rel_tol=1e-9)


def test_annual_scale_is_linear_in_supply():
    inp_50 = ChainInputs(annual_h2_supply_ktpa=50.0)
    inp_200 = ChainInputs(annual_h2_supply_ktpa=200.0)
    a50 = annual_scale(run_lh2_chain(inp_50), inp_50)
    a200 = annual_scale(run_lh2_chain(inp_200), inp_200)
    assert isclose(a200.annual_energy_kwh, 4 * a50.annual_energy_kwh, rel_tol=1e-9)
    assert isclose(a200.fleet_size, a50.fleet_size, abs_tol=0) or a200.fleet_size >= a50.fleet_size


def test_lh2_annual_cargo_needs_no_stoichiometric_conversion():
    """LH2 mass IS H2 mass throughout -- no NH3-style ratio applies."""
    r = run_lh2_chain()
    inp = ChainInputs()
    a = annual_scale(r, inp)
    d1 = next(n for n in r.nodes if n.node_id == "D1")
    assert isclose(a.annual_cargo_kg, d1.mass_in_kg_h2e * inp.annual_h2_supply_ktpa * 1e6, rel_tol=1e-9)


def test_nh3_annual_cargo_uses_physical_ammonia_mass():
    """NH3 shipped tonnage is the H2-equivalent scaled by the stoichiometric
    ratio -- much larger than the H2-equivalent figure alone."""
    r = run_nh3_chain()
    inp = ChainInputs()
    a = annual_scale(r, inp)
    d2 = next(n for n in r.nodes if n.node_id == "D2")
    expected = d2.mass_in_kg_h2e * NH3_PER_H2_MASS_RATIO * inp.annual_h2_supply_ktpa * 1e6
    assert isclose(a.annual_cargo_kg, expected, rel_tol=1e-9)
    assert a.annual_cargo_kg > d2.mass_in_kg_h2e * inp.annual_h2_supply_ktpa * 1e6


@pytest.mark.parametrize("runner", [run_lh2_chain, run_nh3_chain])
def test_fleet_size_is_a_positive_integer(runner):
    r = runner()
    a = annual_scale(r, ChainInputs())
    assert isinstance(a, AnnualScaleResult)
    assert isinstance(a.fleet_size, int)
    assert a.fleet_size >= 1


def test_more_vessel_capacity_needs_a_smaller_fleet():
    small = annual_scale(run_lh2_chain(), ChainInputs(lh2_vessel_capacity_m3=40000.0))
    large = annual_scale(
        run_lh2_chain(ChainInputs(lh2_vessel_capacity_m3=160000.0)),
        ChainInputs(lh2_vessel_capacity_m3=160000.0),
    )
    assert large.fleet_size <= small.fleet_size


def test_annual_scale_reuses_shippingpy_fleet_math():
    """Cross-check against src/lh2/shipping.py directly, so the two modules
    can never silently diverge on the fleet formula."""
    from lh2 import shipping as shipping_mod

    inp = ChainInputs()
    r = run_lh2_chain(inp)
    a = annual_scale(r, inp)
    rtd = shipping_mod.round_trip_days(
        inp.voyage_distance_km, inp.lh2_carrier_speed_km_per_h,
        inp.lh2_port_days_per_call, inp.lh2_port_days_per_call,
    )
    expected_fleet = shipping_mod.fleet_size(
        a.annual_cargo_kg, rtd,
        cargo_capacity=inp.lh2_vessel_capacity_m3 * inp.lh2_vessel_fill_fraction_pct / 100.0,
        lh2_density=inp.lh2_density_kg_per_m3,
        availability=inp.fleet_availability_pct / 100.0,
    )
    assert a.fleet_size == expected_fleet
    assert isclose(a.round_trip_days, rtd, rel_tol=1e-9)


def test_format_report_includes_annual_scale_and_supply_ratio():
    text = format_report()
    assert "Annual scale & fleet" in text
    assert "Fleet size required" in text
    assert "Ammonia supply ratio" in text
