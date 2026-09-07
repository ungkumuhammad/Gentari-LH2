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
