#!/usr/bin/env python3
"""LH2 (40,000 m3) vs NH3 (24,000 m3) shipping-segment comparison.

Boundary: this is a SHIPPING-ONLY comparison (nodes D1/D2 in the wider
LH2-vs-NH3 chain — see docs/comparison/01-energy-penalty-method.md for the
full six-node model). It does not net out upstream production/liquefaction/
Haber-Bosch losses; the "annual H2-equivalent demand" here is the quantity
handed to the ships, not the quantity leaving the electrolyser. Use
src/lh2/chain_energy.py to join this to the rest of the chain.

Corridor: Kakinada, India -> Hamburg, Germany (data/routes/kakinada-hamburg.csv).
Vessel specs: data/vessels/lh2-carriers.csv (40k row) and
data/vessels/nh3-carriers.csv. Every figure is cited or tagged per CLAUDE.md S4.

Run: python scripts/run_shipping_comparison.py
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from lh2 import shipping  # noqa: E402

# --- Corridor (data/routes/kakinada-hamburg.csv) ---------------------------
DISTANCE_SUEZ_KM = 10_260.0    # [ESTIMATE] first-principles waypoint sum
DISTANCE_CAPE_KM = 21_200.0    # [ESTIMATE] first-principles waypoint sum; PRIMARY (user-selected 2026-09-07)

# --- Shared assumptions -----------------------------------------------------
FLEET_AVAILABILITY = 0.90                # [ASSUMPTION] src/lh2/shipping.py convention
ANNUAL_H2_EQUIVALENT_DEMAND_KG = 100e6    # 100 ktpa, [ASSUMPTION] study basis (docs/memory.md, 2026-09-02)
NH3_PER_H2_MASS_RATIO = 5.632             # [ASSUMPTION] first-principles stoichiometry (data/carriers/chain-energy-defaults.csv)

# --- Bunker fuel basis (data/vessels/nh3-carriers.csv) ----------------------
BUNKER_T_PER_DAY = 25.0            # [ASSUMPTION] user-specified NH3 carrier VLSFO burn; charged to BOTH carriers
VLSFO_LHV_MJ_PER_KG = shipping.VLSFO_LHV_MJ_PER_KG   # [ESTIMATE] 40.2 MJ/kg
H2_LHV_MJ_PER_KG = shipping.H2_LHV_MJ_PER_KG         # 120 MJ/kg, mirrors data/properties/lh2-properties.csv
BOG_ENGINE_EFFICIENCY_RATIO = 1.0  # [ASSUMPTION] BOG vs liquid-fuel thermal efficiency in the same engine
RELIQ_GENSET_EFFICIENCY = 0.45     # [ASSUMPTION] shipboard genset efficiency driving the NH3 reliquefaction plant
NH3_RELIQ_SEC_KWH_PER_KG = 0.25    # [ESTIMATE] placeholder, no NH3 dataset yet (decision D4)
H2_GWP100 = 11.6                   # [ESTIMATE] indirect GWP of VENTED H2 only; a GCU burns it to water instead


@dataclass
class VesselCase:
    name: str
    capacity_m3: float
    density_kg_per_m3: float
    fill_fraction: float
    speed_km_per_h: float
    port_days_per_call: float
    voyage_bor_pct_per_day: float
    bog_is_mass_loss: bool  # True: LH2 (burned as fuel, cargo consumed). False: NH3 (reliquefied, energy cost only)


LH2_40K = VesselCase(
    name="LH2 carrier (40,000 m3)",
    capacity_m3=40_000.0,                 # data/vessels/lh2-carriers.csv, cited, kawasaki-2026-questionnaire Q29
    density_kg_per_m3=70.8,               # data/properties/lh2-properties.csv, needs-source (NIST pending)
    fill_fraction=0.98,                   # [ASSUMPTION]
    speed_km_per_h=29.6,                  # cited, kawasaki-2026-supplemental (~16 kn)
    port_days_per_call=1.25,              # cited midpoint, kawasaki-2026-questionnaire Q27 (1-1.5 d)
    voyage_bor_pct_per_day=0.2,           # [ESTIMATE] KHI discloses no standalone voyage BOR
    bog_is_mass_loss=True,                # KHI reply Q23/Q33: burned as DF engine fuel, no onboard reliq
)

NH3_24K = VesselCase(
    name="NH3 carrier (24,000 m3)",
    capacity_m3=24_000.0,                 # [ASSUMPTION] user-specified, data/vessels/nh3-carriers.csv
    density_kg_per_m3=682.0,              # [ESTIMATE] standard published value, fully refrigerated
    fill_fraction=0.98,                   # [ASSUMPTION] matched to LH2 for comparability
    speed_km_per_h=24.076,                # [ASSUMPTION] user-specified, 13 knots
    port_days_per_call=1.5,               # [ASSUMPTION] user-specified, matched to LH2 range
    voyage_bor_pct_per_day=0.15,          # [ASSUMPTION] user-selected 0.1-0.2%/day range, midpoint
    bog_is_mass_loss=False,               # user-specified: onboard reliquefaction -> energy cost, not mass loss
)


@dataclass
class VoyageResult:
    vessel: VesselCase
    distance_km: float
    one_way_days: float
    round_trip_days: float
    cargo_per_voyage_kg: float
    bog_frac: float
    voyage_loss_frac: float
    delivered_cargo_per_voyage_kg: float
    trips_per_year: float
    annual_delivered_cargo_kg: float
    annual_delivered_h2_equivalent_kg: float
    fleet_size_for_demand: int


def evaluate(vessel: VesselCase, distance_km: float,
             annual_demand_kg: float = ANNUAL_H2_EQUIVALENT_DEMAND_KG,
             is_nh3: bool = False) -> VoyageResult:
    one_way = shipping.one_way_transit_days(distance_km, vessel.speed_km_per_h)
    rtd = shipping.round_trip_days(
        distance_km, vessel.speed_km_per_h,
        vessel.port_days_per_call, vessel.port_days_per_call,
    )
    cargo = shipping.cargo_mass_per_voyage(
        vessel.capacity_m3, vessel.density_kg_per_m3, vessel.fill_fraction
    )
    # Voyage boil-off is charged over the one-way LADEN leg only (matches
    # src/lh2/chain_energy.py's voyage_days() convention: BOG accrues while
    # carrying cargo, not on the ballast return leg).
    bog_frac = 1.0 - (1.0 - vessel.voyage_bor_pct_per_day / 100.0) ** one_way
    if vessel.bog_is_mass_loss:
        loss_kg = shipping.voyage_boil_off(cargo, one_way, vessel.voyage_bor_pct_per_day)
        loss_frac = loss_kg.to("kg").magnitude / cargo
    else:
        loss_frac = 0.0  # reliquefied on board -> no cargo mass loss (energy cost is a separate, un-quantified gap)
    delivered_per_voyage = cargo * (1.0 - loss_frac)

    trips_per_year = (365.0 / rtd) * FLEET_AVAILABILITY
    annual_delivered_cargo = delivered_per_voyage * trips_per_year

    if is_nh3:
        annual_delivered_h2e = annual_delivered_cargo / NH3_PER_H2_MASS_RATIO
    else:
        annual_delivered_h2e = annual_delivered_cargo

    # Fleet sizing: ships must LOAD enough cargo, net of voyage loss, to meet
    # the delivered H2-equivalent demand.
    if is_nh3:
        required_annual_delivered_cargo = annual_demand_kg * NH3_PER_H2_MASS_RATIO
    else:
        required_annual_delivered_cargo = annual_demand_kg
    import math
    fleet = math.ceil(required_annual_delivered_cargo / annual_delivered_cargo)

    return VoyageResult(
        vessel=vessel, distance_km=distance_km, one_way_days=one_way,
        round_trip_days=rtd, cargo_per_voyage_kg=cargo, bog_frac=bog_frac, voyage_loss_frac=loss_frac,
        delivered_cargo_per_voyage_kg=delivered_per_voyage, trips_per_year=trips_per_year,
        annual_delivered_cargo_kg=annual_delivered_cargo,
        annual_delivered_h2_equivalent_kg=annual_delivered_h2e,
        fleet_size_for_demand=fleet,
    )


def _bisect(f, lo: float, hi: float, want_low_when_true: bool, iters: int = 60) -> float:
    """Generic bisection: find x where f(x) crosses zero, assuming monotonic f."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == want_low_when_true:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def breakeven_lh2_voyage_bor(distance_km: float) -> float:
    """LH2 voyage BOR (%/day) at which LH2 and NH3 deliver equal annual
    H2-equivalent per vessel, holding every other input at its default. Above
    this BOR, NH3 wins; below it, LH2 wins."""
    nh3_annual = evaluate(NH3_24K, distance_km, is_nh3=True).annual_delivered_h2_equivalent_kg

    def diff(bor: float) -> float:
        v = VesselCase(**{**LH2_40K.__dict__, "voyage_bor_pct_per_day": bor})
        return evaluate(v, distance_km, is_nh3=False).annual_delivered_h2_equivalent_kg - nh3_annual

    return _bisect(diff, 0.0, 20.0, want_low_when_true=True)


def breakeven_nh3_speed_km_per_h(distance_km: float) -> float:
    """NH3 service speed (km/h) at which NH3 matches LH2's default annual
    per-vessel delivery, holding NH3 capacity/BOR at their defaults."""
    lh2_annual = evaluate(LH2_40K, distance_km, is_nh3=False).annual_delivered_h2_equivalent_kg

    def diff(speed: float) -> float:
        v = VesselCase(**{**NH3_24K.__dict__, "speed_km_per_h": speed})
        return lh2_annual - evaluate(v, distance_km, is_nh3=True).annual_delivered_h2_equivalent_kg

    return _bisect(diff, 10.0, 60.0, want_low_when_true=True)


def breakeven_nh3_capacity_m3(distance_km: float) -> float:
    """NH3 vessel capacity (m3, at 13 kn) at which NH3 matches LH2's default
    annual per-vessel delivery."""
    lh2_annual = evaluate(LH2_40K, distance_km, is_nh3=False).annual_delivered_h2_equivalent_kg

    def diff(capacity: float) -> float:
        v = VesselCase(**{**NH3_24K.__dict__, "capacity_m3": capacity})
        return lh2_annual - evaluate(v, distance_km, is_nh3=True).annual_delivered_h2_equivalent_kg

    return _bisect(diff, 10_000.0, 150_000.0, want_low_when_true=True)


def find_crossover_km(lo: float = 1.0, hi: float = 60_000.0, tol: float = 1.0) -> float | None:
    """Distance (km) where LH2 and NH3 deliver equal annual H2-equivalent per
    vessel. Returns None if no sign change in [lo, hi] (i.e. one carrier wins
    everywhere in range)."""
    def diff(d: float) -> float:
        lh2 = evaluate(LH2_40K, d, is_nh3=False).annual_delivered_h2_equivalent_kg
        nh3 = evaluate(NH3_24K, d, is_nh3=True).annual_delivered_h2_equivalent_kg
        return lh2 - nh3

    f_lo, f_hi = diff(lo), diff(hi)
    if f_lo == 0:
        return lo
    if f_lo * f_hi > 0:
        return None
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if diff(lo) * diff(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


@dataclass
class FuelBalance:
    """Bunker-fuel picture for one carrier over one laden leg.

    Both carriers are charged the same propulsion duty (``BUNKER_T_PER_DAY``),
    so the only difference is what covers it. The LH2 carrier burns cargo
    boil-off first and buys the shortfall; anything above the engine's demand
    cannot be used for propulsion and leaves the ship regardless. The NH3
    carrier buys all of its propulsion fuel and additionally burns fuel in a
    genset to drive the reliquefaction plant.
    """
    carrier: str
    laden_days: float
    demand_mj: float
    bog_kg: float                 # cargo boiled off over the laden leg
    bog_useful_kg: float          # of that, burned usefully for propulsion
    bog_surplus_kg: float         # of that, not usable for propulsion (vented or GCU-burned)
    covered_fraction: float       # BOG energy / propulsion demand
    topup_fuel_t: float           # bunker fuel still required for propulsion
    reliq_fuel_t: float           # bunker fuel burned in the genset for reliquefaction
    total_fuel_t: float
    cargo_lost_kg: float          # cargo mass that leaves the chain (H2 for LH2, 0 for NH3)
    delivered_h2e_kg: float


def fuel_balance(vessel: VesselCase, distance_km: float, is_nh3: bool,
                 bunker_t_per_day: float = BUNKER_T_PER_DAY,
                 reliq_sec: float = NH3_RELIQ_SEC_KWH_PER_KG,
                 genset_eff: float = RELIQ_GENSET_EFFICIENCY,
                 engine_ratio: float = BOG_ENGINE_EFFICIENCY_RATIO) -> FuelBalance:
    r = evaluate(vessel, distance_km, is_nh3=is_nh3)
    days = r.one_way_days
    demand = shipping.propulsion_demand_mj(bunker_t_per_day, days, VLSFO_LHV_MJ_PER_KG)
    bog_kg = r.cargo_per_voyage_kg * r.bog_frac

    if is_nh3:
        # BOG is re-liquefied: no cargo leaves, but the genset burns fuel for it.
        reliq_kwh = bog_kg * reliq_sec
        reliq_fuel_t = reliq_kwh * 3.6 / (VLSFO_LHV_MJ_PER_KG * genset_eff) / 1000.0
        return FuelBalance(
            carrier=vessel.name, laden_days=days, demand_mj=demand, bog_kg=bog_kg,
            bog_useful_kg=0.0, bog_surplus_kg=0.0, covered_fraction=0.0,
            topup_fuel_t=bunker_t_per_day * days, reliq_fuel_t=reliq_fuel_t,
            total_fuel_t=bunker_t_per_day * days + reliq_fuel_t,
            cargo_lost_kg=0.0,
            delivered_h2e_kg=r.delivered_cargo_per_voyage_kg / NH3_PER_H2_MASS_RATIO,
        )

    bal = shipping.bog_fuel_balance(bog_kg, demand, H2_LHV_MJ_PER_KG, engine_ratio,
                                    VLSFO_LHV_MJ_PER_KG)
    return FuelBalance(
        carrier=vessel.name, laden_days=days, demand_mj=demand, bog_kg=bog_kg,
        bog_useful_kg=bal["useful_kg"], bog_surplus_kg=bal["surplus_kg"],
        covered_fraction=bal["covered_fraction"], topup_fuel_t=bal["topup_fuel_t"],
        reliq_fuel_t=0.0, total_fuel_t=bal["topup_fuel_t"],
        cargo_lost_kg=bog_kg,
        delivered_h2e_kg=r.delivered_cargo_per_voyage_kg,
    )


def voyage_cost_per_kg(fb: FuelBalance, h2_price_usd_per_kg: float,
                       vlsfo_price_usd_per_t: float) -> dict:
    """Boil-off + bunker cost of one laden leg, per kg H2-equivalent delivered.

    Prices are caller-supplied: neither is logged in references.csv, and the
    study reports a breakeven price rather than asserting one.
    """
    cargo_cost = fb.cargo_lost_kg * h2_price_usd_per_kg
    fuel_cost = fb.total_fuel_t * vlsfo_price_usd_per_t
    return {
        "cargo_usd": cargo_cost, "fuel_usd": fuel_cost,
        "total_usd": cargo_cost + fuel_cost,
        "per_kg": (cargo_cost + fuel_cost) / fb.delivered_h2e_kg,
        "cargo_per_kg": cargo_cost / fb.delivered_h2e_kg,
        "fuel_per_kg": fuel_cost / fb.delivered_h2e_kg,
    }


def breakeven_bor_fuel_cover(distance_km: float,
                             bunker_t_per_day: float = BUNKER_T_PER_DAY) -> float:
    """LH2 voyage BOR (%/day) at which cargo boil-off exactly meets the engine's
    propulsion demand. Below it the ship buys top-up bunker fuel; above it the
    surplus boil-off cannot be used for propulsion."""
    def diff(bor: float) -> float:
        v = VesselCase(**{**LH2_40K.__dict__, "voyage_bor_pct_per_day": bor})
        fb = fuel_balance(v, distance_km, False, bunker_t_per_day)
        return fb.covered_fraction - 1.0
    return _bisect(diff, 0.0, 20.0, want_low_when_true=False)


def breakeven_h2_price(distance_km: float, vlsfo_price_usd_per_t: float,
                       bunker_t_per_day: float = BUNKER_T_PER_DAY) -> float | None:
    """Delivered-H2 value at which the two carriers' boil-off + bunker cost per
    kg H2 delivered is equal. Below it the LH2 carrier is cheaper on this
    metric; above it the ammonia carrier is."""
    nh3_fb = fuel_balance(NH3_24K, distance_km, True, bunker_t_per_day)
    nh3_pk = voyage_cost_per_kg(nh3_fb, 0.0, vlsfo_price_usd_per_t)["per_kg"]
    lh2_fb = fuel_balance(LH2_40K, distance_km, False, bunker_t_per_day)
    base = voyage_cost_per_kg(lh2_fb, 0.0, vlsfo_price_usd_per_t)["per_kg"]
    slope = lh2_fb.cargo_lost_kg / lh2_fb.delivered_h2e_kg
    if slope <= 0:
        return None
    return (nh3_pk - base) / slope


def format_result(r: VoyageResult) -> str:
    return (
        f"  {r.vessel.name}\n"
        f"    One-way transit         : {r.one_way_days:.2f} d\n"
        f"    Round-trip cycle        : {r.round_trip_days:.2f} d "
        f"({r.trips_per_year:.2f} trips/y at {FLEET_AVAILABILITY:.0%} availability)\n"
        f"    Cargo loaded/voyage     : {r.cargo_per_voyage_kg:,.0f} kg\n"
        f"    Voyage boil-off loss    : {r.voyage_loss_frac * 100:.3f}% "
        f"({'burned as fuel, cargo mass loss' if r.vessel.bog_is_mass_loss else 'reliquefied on board, no mass loss -- energy cost NOT quantified [GAP]'})\n"
        f"    Delivered cargo/voyage  : {r.delivered_cargo_per_voyage_kg:,.0f} kg\n"
        f"    Annual delivered H2-eq. : {r.annual_delivered_h2_equivalent_kg:,.0f} kg/y per vessel\n"
        f"    Fleet for {ANNUAL_H2_EQUIVALENT_DEMAND_KG/1e6:.0f} ktpa H2-eq.: {r.fleet_size_for_demand} vessel(s)\n"
    )


def main() -> None:
    print("=" * 78)
    print("LH2 (40,000 m3) vs NH3 (24,000 m3) -- SHIPPING SEGMENT COMPARISON")
    print("Corridor: Kakinada, India -> Hamburg, Germany")
    print("=" * 78)

    for label, distance in [("SUEZ route (reference)", DISTANCE_SUEZ_KM),
                             ("CAPE OF GOOD HOPE route (PRIMARY)", DISTANCE_CAPE_KM)]:
        print(f"\n--- {label}: {distance:,.0f} km one-way [ESTIMATE, first-principles] ---\n")
        lh2 = evaluate(LH2_40K, distance, is_nh3=False)
        nh3 = evaluate(NH3_24K, distance, is_nh3=True)
        print(format_result(lh2))
        print(format_result(nh3))
        winner = "LH2" if lh2.annual_delivered_h2_equivalent_kg > nh3.annual_delivered_h2_equivalent_kg else "NH3"
        ratio = max(lh2.annual_delivered_h2_equivalent_kg, nh3.annual_delivered_h2_equivalent_kg) / \
            min(lh2.annual_delivered_h2_equivalent_kg, nh3.annual_delivered_h2_equivalent_kg)
        print(f"  --> At this distance, {winner} delivers {ratio:.2f}x more annual "
              f"H2-equivalent per vessel; needs {'fewer' if winner=='LH2' else 'fewer'} vessels "
              f"for the same demand ({lh2.fleet_size_for_demand} LH2 vs {nh3.fleet_size_for_demand} NH3 ships).")

    crossover = find_crossover_km()
    print("\n" + "=" * 78)
    print("SWEET SPOT (crossover distance, per-vessel annual H2-equivalent basis)")
    print("=" * 78)
    if crossover is None:
        print("No crossover in 1-60,000 km range -- one carrier dominates at every distance tested.")
    else:
        print(f"Crossover at ~{crossover:,.0f} km one-way.")
        below = evaluate(NH3_24K, crossover - 500, is_nh3=True)
        below_lh2 = evaluate(LH2_40K, crossover - 500, is_nh3=False)
        print(f"  Below ~{crossover:,.0f} km: {'NH3' if below.annual_delivered_h2_equivalent_kg > below_lh2.annual_delivered_h2_equivalent_kg else 'LH2'} wins on per-vessel annual throughput.")
        print(f"  Above ~{crossover:,.0f} km: {'LH2' if below.annual_delivered_h2_equivalent_kg > below_lh2.annual_delivered_h2_equivalent_kg else 'NH3'} wins on per-vessel annual throughput.")

    print("\n" + "=" * 78)
    print("SWEET SPOT (parameter breakevens, at LH2's default 0.2%/day voyage BOR")
    print("unless the parameter itself IS the one being varied)")
    print("=" * 78)
    for label, distance in [("Suez", DISTANCE_SUEZ_KM), ("Cape (PRIMARY)", DISTANCE_CAPE_KM)]:
        bor_be = breakeven_lh2_voyage_bor(distance)
        print(f"  [{label}] LH2 voyage BOR breakeven: {bor_be:.3f} %/day "
              f"(current default 0.2%/day; NH3 wins above this)")
    speed_be = breakeven_nh3_speed_km_per_h(DISTANCE_CAPE_KM)
    print(f"  [Cape] NH3 speed breakeven (vs LH2 default): {speed_be:.2f} km/h "
          f"= {speed_be/1.852:.2f} kn (current 13 kn; NH3 wins above this)")
    cap_be = breakeven_nh3_capacity_m3(DISTANCE_CAPE_KM)
    print(f"  [Cape] NH3 capacity breakeven at 13 kn (vs LH2 default): {cap_be:,.0f} m3 "
          f"(current 24,000 m3; NH3 wins above this)")

    print("\nSensitivity sweep (annual delivered H2-equivalent per vessel, kg/y):")
    print(f"{'Distance (km)':>14} | {'LH2 (kg/y)':>16} | {'NH3 (kg/y)':>16} | {'Winner':>7}")
    for d in [1_000, 2_500, 5_000, 7_500, 10_260, 15_000, 21_200, 25_000, 30_000, 40_000]:
        lh2_val = evaluate(LH2_40K, d, is_nh3=False).annual_delivered_h2_equivalent_kg
        nh3_val = evaluate(NH3_24K, d, is_nh3=True).annual_delivered_h2_equivalent_kg
        w = "LH2" if lh2_val > nh3_val else "NH3"
        print(f"{d:>14,.0f} | {lh2_val:>16,.0f} | {nh3_val:>16,.0f} | {w:>7}")


if __name__ == "__main__":
    main()
