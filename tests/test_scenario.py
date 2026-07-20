"""Tests for the KHI-based scenario calculator (``lh2.scenario`` and the
segment modules it composes: liquefaction, storage, shipping, regas,
economics).

Checks unit consistency, sensible magnitudes against KHI's disclosed figures,
and that the cardinal rule (CLAUDE.md §4) holds in code: missing CapEx/OpEx/
voyage-BOR/FX inputs must produce an explicit gap, never a fabricated number.
"""

from __future__ import annotations

import math

import pytest

from lh2 import economics, liquefaction, regas, shipping, storage
from lh2.scenario import ProjectInputs, interpolate_iae_cost_stack, run_scenario
from lh2.units import Q_


def test_liquefaction_energy_uses_khi_sec_range():
    energy_low = liquefaction.liquefaction_energy(Q_(1000, "kg"), liquefaction.KHI_SEC_LOW)
    energy_high = liquefaction.liquefaction_energy(Q_(1000, "kg"), liquefaction.KHI_SEC_HIGH)
    assert energy_low.to("kWh").magnitude == pytest.approx(8000.0)
    assert energy_high.to("kWh").magnitude == pytest.approx(9000.0)


def test_liquefaction_train_count_matches_khi_base_scale_order_of_magnitude():
    # KHI's own Base scale point: 2.5e9 Nm3/y on 7 trains.
    base_tpa = 2.5e9 * 0.0899 / 1000  # Nm3/y -> t/y via normal gas density
    n = liquefaction.train_count(base_tpa)
    assert n in (6, 7, 8)  # within one train of KHI's disclosed figure


def test_storage_boil_off_is_compounding_and_bounded():
    loss = storage.boil_off_at_rest(Q_(100_000, "kg"), days=10)
    assert 0 < loss.to("kg").magnitude < 100_000
    # Roughly 1%/day compounding over 10 days at 0.1%/day.
    assert loss.to("kg").magnitude == pytest.approx(995.5, rel=0.01)


def test_regas_duty_matches_khi_figure():
    duty = regas.regas_duty(Q_(1.0, "kg"))
    assert duty.to("MJ").magnitude == pytest.approx(3.8)


def test_shipping_round_trip_uses_khi_speed_and_load_unload_window():
    days = shipping.round_trip_days(Q_(6000, "km"))
    transit = shipping.one_way_transit_days(Q_(6000, "km"))
    assert days == pytest.approx(2 * transit + 2.5)


def test_fleet_size_scales_with_volume():
    small = shipping.fleet_size(annual_volume_kg=1e8, round_trip_days_value=20)
    large = shipping.fleet_size(annual_volume_kg=1e9, round_trip_days_value=20)
    assert large >= small


def test_economics_lcoh_positive_and_sane():
    value = economics.lcoh(
        capex=1_000_000_000,
        opex_per_year=[50_000_000] * 20,
        h2_kg_per_year=[100_000_000] * 20,
        discount_rate=0.08,
    )
    assert value > 0


def test_economics_lcoh_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        economics.lcoh(1.0, [1.0, 2.0], [1.0], 0.08)


def test_interpolate_iae_cost_stack_reconciles_at_endpoints():
    base_stack, warnings = interpolate_iae_cost_stack(2.5e9)
    assert warnings == []
    assert base_stack["TOTAL"] == pytest.approx(37.6, abs=0.05)

    large_stack, warnings = interpolate_iae_cost_stack(10.0e9)
    assert warnings == []
    assert large_stack["TOTAL"] == pytest.approx(30.7, abs=0.05)


def test_interpolate_iae_cost_stack_flags_out_of_range():
    stack, warnings = interpolate_iae_cost_stack(20.0e9)
    assert warnings  # clipped + flagged, not silently extrapolated
    assert stack["TOTAL"] == pytest.approx(30.7, abs=0.05)


def test_scenario_without_cost_inputs_flags_gaps_not_fabricated_numbers():
    result = run_scenario(ProjectInputs(annual_liquefaction_tpa=300_000, distance_km=6000))
    assert result.lcoh_usd_per_kg is None
    assert result.cost_stack_usd_per_kg is None
    assert result.voyage_bog_kg_per_year is None
    assert any("LCOH not computed" in g for g in result.gaps)
    assert any("voyage_bor_pct_per_day not supplied" in g for g in result.gaps)
    assert any("fx_jpy_per_usd not supplied" in g for g in result.gaps)
    assert any("carbon_intensity" in g for g in result.gaps)


def test_scenario_with_full_inputs_computes_lcoh_and_usd_stack():
    result = run_scenario(
        ProjectInputs(
            annual_liquefaction_tpa=300_000,
            distance_km=6000,
            voyage_bor_pct_per_day=0.2,
            discount_rate=0.08,
            capex_musd=1200,
            opex_musd_per_year=60,
            fx_jpy_per_usd=150,
        )
    )
    assert result.lcoh_usd_per_kg is not None
    assert result.lcoh_usd_per_kg > 0
    assert result.cost_stack_usd_per_kg is not None
    assert result.voyage_bog_kg_per_year is not None
    assert result.delivered_mass_tpa < 300_000  # voyage BOG draws down delivered mass
    assert result.liquefaction_trains == math.ceil(result.liquefaction_trains)


def test_scenario_never_fabricates_carbon_intensity():
    result = run_scenario(ProjectInputs(annual_liquefaction_tpa=300_000, distance_km=6000))
    assert not hasattr(result, "carbon_intensity_kgco2e_per_kg")
