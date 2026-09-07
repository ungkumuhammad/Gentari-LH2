"""Tests for scripts/run_shipping_comparison.py (LH2 40k vs NH3 24k shipping
segment comparison, Kakinada-Hamburg corridor).

Covers: reuse of src/lh2/shipping.py primitives, the mass-loss-vs-energy-cost
BOG treatment split (LH2 burns BOG as fuel = mass loss; NH3 reliquefies on
board = no mass loss), fleet-sizing consistency, and the breakeven/sweet-spot
solvers stay self-consistent (their roots actually zero the underlying
difference function).
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import run_shipping_comparison as m  # noqa: E402
from lh2 import shipping  # noqa: E402


def test_lh2_voyage_loss_reduces_delivered_cargo():
    r = m.evaluate(m.LH2_40K, m.DISTANCE_CAPE_KM, is_nh3=False)
    assert 0.0 < r.voyage_loss_frac < 0.2
    assert r.delivered_cargo_per_voyage_kg < r.cargo_per_voyage_kg


def test_nh3_reliquefaction_has_no_mass_loss():
    r = m.evaluate(m.NH3_24K, m.DISTANCE_CAPE_KM, is_nh3=True)
    assert r.voyage_loss_frac == 0.0
    assert r.delivered_cargo_per_voyage_kg == r.cargo_per_voyage_kg


def test_cargo_per_voyage_matches_shipping_module():
    expected = shipping.cargo_mass_per_voyage(
        m.LH2_40K.capacity_m3, m.LH2_40K.density_kg_per_m3, m.LH2_40K.fill_fraction
    )
    r = m.evaluate(m.LH2_40K, m.DISTANCE_CAPE_KM, is_nh3=False)
    assert math.isclose(r.cargo_per_voyage_kg, expected)


def test_round_trip_matches_shipping_module():
    expected = shipping.round_trip_days(
        m.DISTANCE_SUEZ_KM, m.NH3_24K.speed_km_per_h,
        m.NH3_24K.port_days_per_call, m.NH3_24K.port_days_per_call,
    )
    r = m.evaluate(m.NH3_24K, m.DISTANCE_SUEZ_KM, is_nh3=True)
    assert math.isclose(r.round_trip_days, expected)


def test_annual_capacity_per_vessel_helper_matches_manual_calc():
    rtd = shipping.round_trip_days(5000, 20.0, 1.0, 1.0)
    manual_trips = (365.0 / rtd) * 0.9
    manual_cargo = shipping.cargo_mass_per_voyage(50_000, 100.0, 0.95)
    expected = manual_cargo * manual_trips
    got = shipping.annual_capacity_per_vessel(rtd, 50_000, 100.0, 0.95, 0.9)
    assert math.isclose(got, expected)


def test_fleet_size_unchanged_for_default_fill_fraction():
    """fleet_size's new fill_fraction kwarg defaults to 1.0, so pre-existing
    callers (chain_energy.py passes an already-fill-adjusted capacity) are
    unaffected."""
    rtd = 30.0
    a = shipping.fleet_size(1e8, rtd)
    b = shipping.fleet_size(1e8, rtd, fill_fraction=1.0)
    assert a == b


def test_cape_route_longer_than_suez():
    assert m.DISTANCE_CAPE_KM > m.DISTANCE_SUEZ_KM


def test_lh2_wins_at_default_parameters_both_routes():
    """At the stated defaults (2026-09-07 user inputs), LH2 delivers more
    annual H2-equivalent per vessel than the 24k NH3 carrier on both route
    options -- documents the headline result so a future default change is
    caught by the test suite."""
    for distance in (m.DISTANCE_SUEZ_KM, m.DISTANCE_CAPE_KM):
        lh2 = m.evaluate(m.LH2_40K, distance, is_nh3=False).annual_delivered_h2_equivalent_kg
        nh3 = m.evaluate(m.NH3_24K, distance, is_nh3=True).annual_delivered_h2_equivalent_kg
        assert lh2 > nh3


def test_breakeven_lh2_voyage_bor_actually_equalizes():
    distance = m.DISTANCE_CAPE_KM
    bor = m.breakeven_lh2_voyage_bor(distance)
    v = m.VesselCase(**{**m.LH2_40K.__dict__, "voyage_bor_pct_per_day": bor})
    lh2 = m.evaluate(v, distance, is_nh3=False).annual_delivered_h2_equivalent_kg
    nh3 = m.evaluate(m.NH3_24K, distance, is_nh3=True).annual_delivered_h2_equivalent_kg
    assert math.isclose(lh2, nh3, rel_tol=1e-3)


def test_breakeven_lh2_voyage_bor_within_plausible_range():
    """Both routes' breakeven BOR should sit strictly between the current
    0.2%/day placeholder and the unpromoted RSER literature figure of
    ~3.44%/day -- i.e. the outcome genuinely depends on which one turns out
    to be closer to reality (docs/comparison/khi-vs-literature-lh2-comparison.md)."""
    for distance in (m.DISTANCE_SUEZ_KM, m.DISTANCE_CAPE_KM):
        bor = m.breakeven_lh2_voyage_bor(distance)
        assert 0.2 < bor < 3.44


def test_breakeven_nh3_speed_actually_equalizes():
    distance = m.DISTANCE_CAPE_KM
    speed = m.breakeven_nh3_speed_km_per_h(distance)
    v = m.VesselCase(**{**m.NH3_24K.__dict__, "speed_km_per_h": speed})
    lh2 = m.evaluate(m.LH2_40K, distance, is_nh3=False).annual_delivered_h2_equivalent_kg
    nh3 = m.evaluate(v, distance, is_nh3=True).annual_delivered_h2_equivalent_kg
    assert math.isclose(lh2, nh3, rel_tol=1e-3)


def test_breakeven_nh3_speed_faster_than_current():
    """NH3 needs to sail faster than its current 13 kn default to match LH2
    -- documents the direction of the finding."""
    speed = m.breakeven_nh3_speed_km_per_h(m.DISTANCE_CAPE_KM)
    assert speed > m.NH3_24K.speed_km_per_h


def test_breakeven_nh3_capacity_actually_equalizes():
    distance = m.DISTANCE_CAPE_KM
    capacity = m.breakeven_nh3_capacity_m3(distance)
    v = m.VesselCase(**{**m.NH3_24K.__dict__, "capacity_m3": capacity})
    lh2 = m.evaluate(m.LH2_40K, distance, is_nh3=False).annual_delivered_h2_equivalent_kg
    nh3 = m.evaluate(v, distance, is_nh3=True).annual_delivered_h2_equivalent_kg
    assert math.isclose(lh2, nh3, rel_tol=1e-3)


def test_breakeven_nh3_capacity_larger_than_current():
    capacity = m.breakeven_nh3_capacity_m3(m.DISTANCE_CAPE_KM)
    assert capacity > m.NH3_24K.capacity_m3


def test_fleet_size_grows_with_distance():
    near = m.evaluate(m.LH2_40K, 1000, is_nh3=False).fleet_size_for_demand
    far = m.evaluate(m.LH2_40K, m.DISTANCE_CAPE_KM, is_nh3=False).fleet_size_for_demand
    assert far >= near


# --- bunker fuel / boil-off-as-fuel balance -------------------------------

def test_bog_fuel_balance_conserves_energy():
    b = shipping.bog_fuel_balance(bog_kg=100_000, demand_mj=5_000_000)
    assert math.isclose(b["useful_mj"] + b["surplus_mj"], b["bog_energy_mj"], rel_tol=1e-9)
    assert b["useful_mj"] <= b["bog_energy_mj"]


def test_bog_fuel_balance_shortfall_and_surplus_are_exclusive():
    """A voyage is either short of fuel or in surplus, never both."""
    for bog in (10_000, 100_000, 1_000_000):
        b = shipping.bog_fuel_balance(bog_kg=bog, demand_mj=5_000_000)
        assert b["surplus_mj"] == 0 or b["shortfall_mj"] == 0


def test_bog_fuel_balance_engine_ratio_scales_delivered_energy():
    lo = shipping.bog_fuel_balance(50_000, 1e12, engine_efficiency_ratio=0.8)
    hi = shipping.bog_fuel_balance(50_000, 1e12, engine_efficiency_ratio=1.0)
    assert lo["bog_energy_mj"] < hi["bog_energy_mj"]


def test_lh2_boil_off_does_not_cover_fuel_at_default_bor():
    """At the 0.2 %/day placeholder the boil-off is NOT enough to run the ship
    -- the carrier still buys bunker fuel and vents nothing. Documents the
    headline finding of the fuel-balance study."""
    fb = m.fuel_balance(m.LH2_40K, m.DISTANCE_CAPE_KM, False)
    assert fb.covered_fraction < 1.0
    assert fb.topup_fuel_t > 0
    assert fb.bog_surplus_kg == 0


def test_high_bor_produces_unusable_surplus():
    """Above the cover point the extra boil-off cannot be burned for
    propulsion -- it leaves the ship doing no useful work."""
    v = m.VesselCase(**{**m.LH2_40K.__dict__, "voyage_bor_pct_per_day": 3.44})
    fb = m.fuel_balance(v, m.DISTANCE_CAPE_KM, False)
    assert fb.bog_surplus_kg > 0
    assert fb.topup_fuel_t == 0
    assert math.isclose(fb.bog_useful_kg + fb.bog_surplus_kg, fb.bog_kg, rel_tol=1e-9)


def test_breakeven_bor_fuel_cover_actually_covers():
    for dist in (m.DISTANCE_SUEZ_KM, m.DISTANCE_CAPE_KM):
        bor = m.breakeven_bor_fuel_cover(dist)
        v = m.VesselCase(**{**m.LH2_40K.__dict__, "voyage_bor_pct_per_day": bor})
        fb = m.fuel_balance(v, dist, False)
        assert math.isclose(fb.covered_fraction, 1.0, rel_tol=1e-4)


def test_fuel_cover_bor_sits_above_the_working_assumption():
    """The cover point is above 0.2 %/day but far below the RSER literature
    figure -- i.e. the working assumption is in the 'buys fuel' regime and the
    literature figure is deep in the 'vents surplus' regime."""
    bor = m.breakeven_bor_fuel_cover(m.DISTANCE_CAPE_KM)
    assert 0.2 < bor < 3.44


def test_nh3_carrier_loses_no_cargo_but_burns_reliq_fuel():
    fb = m.fuel_balance(m.NH3_24K, m.DISTANCE_CAPE_KM, True)
    assert fb.cargo_lost_kg == 0
    assert fb.reliq_fuel_t > 0
    assert math.isclose(fb.total_fuel_t, fb.topup_fuel_t + fb.reliq_fuel_t, rel_tol=1e-9)


def test_breakeven_h2_price_equalizes_cost_per_kg():
    D, vlsfo = m.DISTANCE_CAPE_KM, 600.0
    p = m.breakeven_h2_price(D, vlsfo)
    lh2 = m.voyage_cost_per_kg(m.fuel_balance(m.LH2_40K, D, False), p, vlsfo)["per_kg"]
    nh3 = m.voyage_cost_per_kg(m.fuel_balance(m.NH3_24K, D, True), p, vlsfo)["per_kg"]
    assert math.isclose(lh2, nh3, rel_tol=1e-6)


def test_breakeven_h2_price_rises_with_bunker_price():
    """Dearer bunker fuel hurts the ammonia carrier more (it buys all of its
    propulsion energy), so LH2 tolerates a higher hydrogen value."""
    D = m.DISTANCE_CAPE_KM
    assert m.breakeven_h2_price(D, 400) < m.breakeven_h2_price(D, 800)


def test_cost_per_kg_splits_into_cargo_and_fuel():
    fb = m.fuel_balance(m.LH2_40K, m.DISTANCE_CAPE_KM, False)
    c = m.voyage_cost_per_kg(fb, 5.0, 600.0)
    assert math.isclose(c["cargo_per_kg"] + c["fuel_per_kg"], c["per_kg"], rel_tol=1e-9)
    assert c["cargo_per_kg"] > c["fuel_per_kg"]   # hydrogen is the premium term
