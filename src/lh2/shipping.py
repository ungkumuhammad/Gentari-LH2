"""[4] Shipping — LH2 marine transport + voyage boil-off.

Boundary: LH2 loaded -> LH2 discharged. See docs/methodology/04-shipping.md.
Vessel specs live in data/vessels/ (each referencing a references.csv id).

Every default below carries a data/references.csv id in a comment, per
CLAUDE.md §4. KHI did NOT disclose a standalone voyage boil-off rate (its
reply to reply Q23/Q26 states only that BOG-as-fuel consumption equals the
BOR, and that MGO-only sailing holds tank pressure within MARVS "for several
days" without giving a %/day figure) — callers must supply
``voyage_bor_pct_per_day`` explicitly as a tagged [ASSUMPTION] or [ESTIMATE];
there is no KHI-sourced default here.
"""

from __future__ import annotations

import math

from .units import Q_

#: Commercial-scale target vessel cargo capacity.
#: ref: kawasaki-2026-supplemental ("160,000 m3/ship").
KHI_COMMERCIAL_CARGO_CAPACITY = Q_(160_000.0, "m^3")

#: Commercial-scale target vessel service speed (~16 knots).
#: ref: kawasaki-2026-supplemental ("Velocity 29.6 km/h").
KHI_COMMERCIAL_SPEED = Q_(29.6, "km/hour")

#: Loading/unloading duration per vessel call, KHI-disclosed range.
#: ref: kawasaki-2026-questionnaire (reply Q27: "about 1 to 1.5 days").
KHI_LOAD_UNLOAD_DAYS_LOW = 1.0
KHI_LOAD_UNLOAD_DAYS_HIGH = 1.5
#: [ASSUMPTION] midpoint of KHI's disclosed load/unload duration range.
KHI_LOAD_UNLOAD_DAYS_MID = (KHI_LOAD_UNLOAD_DAYS_LOW + KHI_LOAD_UNLOAD_DAYS_HIGH) / 2


def one_way_transit_days(distance: object, speed: object = KHI_COMMERCIAL_SPEED) -> float:
    """One-way voyage transit time in days.

    Args:
        distance: Route (one-way) distance, as a ``pint`` quantity or bare km.
        speed: Vessel service speed (default: KHI's commercial-scale target,
            ``KHI_COMMERCIAL_SPEED``, ~16 knots).

    Returns:
        Transit time in days (float).
    """
    if not hasattr(distance, "units"):
        distance = Q_(distance, "km")
    if not hasattr(speed, "units"):
        speed = Q_(speed, "km/hour")
    return (distance / speed).to("day").magnitude


def round_trip_days(
    distance: object,
    speed: object = KHI_COMMERCIAL_SPEED,
    load_days: float = KHI_LOAD_UNLOAD_DAYS_MID,
    unload_days: float = KHI_LOAD_UNLOAD_DAYS_MID,
) -> float:
    """Total round-trip cycle time: laden + ballast transit + port calls.

    No separate ballast-leg BOR/speed is disclosed by KHI; ballast transit is
    assumed at the same speed as the laden leg ([ASSUMPTION]).

    Args:
        distance: One-way route distance.
        speed: Vessel service speed (default: KHI commercial target).
        load_days: Loading duration (default: midpoint of KHI's 1-1.5 day
            range).
        unload_days: Unloading duration (default: same).

    Returns:
        Round-trip cycle time in days (float).
    """
    transit = one_way_transit_days(distance, speed)
    return 2 * transit + load_days + unload_days


def voyage_boil_off(cargo_kg: object, voyage_days: float, voyage_bor_pct_per_day: float):
    """In-transit boil-off over a voyage.

    KHI states the ship's fuel-gas (H2) consumption rate equals the BOR, and
    that BOG is normally consumed as dual-fuel engine fuel rather than vented
    or lost (reply Q23/Q32) — so this is *inventory drawn down as propulsion
    fuel*, not necessarily a "loss" in the LCOH sense, but it does reduce the
    cargo delivered. Modeled as compounding daily loss of the remaining cargo.

    Args:
        cargo_kg: Loaded LH2 mass, as a ``pint`` quantity or bare kg.
        voyage_days: One-way (laden-leg) voyage duration, days.
        voyage_bor_pct_per_day: Voyage BOR, %/day. KHI did not disclose a
            standalone figure for this — pass an explicit [ASSUMPTION] or
            [ESTIMATE]-tagged value at the call site.

    Returns:
        Mass consumed as BOG over the voyage, as a ``pint`` Quantity in kg.
    """
    if not hasattr(cargo_kg, "units"):
        cargo_kg = Q_(cargo_kg, "kg")
    retained_fraction = (1.0 - voyage_bor_pct_per_day / 100.0) ** voyage_days
    return cargo_kg * (1.0 - retained_fraction)


def cargo_mass_per_voyage(
    cargo_capacity: object,
    cargo_density: object,
    fill_fraction: float = 1.0,
) -> float:
    """Liquid cargo mass carried per voyage, in kg.

    Generic across carrier/commodity — the caller supplies the vessel's own
    capacity, liquid density, and usable fill fraction. Used identically for
    LH2 and NH3 carriers; only the inputs differ.

    Args:
        cargo_capacity: Tank capacity, as a ``pint`` quantity or bare m3.
        cargo_density: Liquid density at carriage conditions, as a ``pint``
            quantity or bare kg/m3.
        fill_fraction: Usable fill vs full tank volume (0-1). Default 1.0
            (no ullage limit applied) — pass an explicit tagged value at the
            call site for a realistic figure.

    Returns:
        Cargo mass per voyage, kg (float).
    """
    if not hasattr(cargo_capacity, "units"):
        cargo_capacity = Q_(cargo_capacity, "m^3")
    if not hasattr(cargo_density, "units"):
        cargo_density = Q_(cargo_density, "kg/m^3")
    return (cargo_capacity * cargo_density * fill_fraction).to("kg").magnitude


def annual_capacity_per_vessel(
    round_trip_days_value: float,
    cargo_capacity: object,
    cargo_density: object,
    fill_fraction: float = 1.0,
    availability: float = 0.90,
) -> float:
    """Annual cargo throughput a single vessel can deliver on a route, in kg/y.

    Generic across carrier/commodity (see ``cargo_mass_per_voyage``). Shared
    by ``fleet_size`` and by cross-carrier shipping comparisons so the two
    never silently diverge.

    Args:
        round_trip_days_value: Round-trip cycle time, days (see
            ``round_trip_days``).
        cargo_capacity: Per-vessel tank capacity.
        cargo_density: Liquid density at carriage conditions.
        fill_fraction: Usable fill vs full tank volume (0-1). Default 1.0.
        availability: [ASSUMPTION] fleet-wide operational availability
            (default 0.90 — dry-docking/maintenance/weather margin; not
            carrier-specific).

    Returns:
        Annual cargo mass delivered per vessel, kg/y (float). This is
        *cargo* mass as loaded, before any voyage boil-off loss.
    """
    mass_per_voyage = cargo_mass_per_voyage(cargo_capacity, cargo_density, fill_fraction)
    trips_per_year = (365.0 / round_trip_days_value) * availability
    return mass_per_voyage * trips_per_year


def fleet_size(
    annual_volume_kg: float,
    round_trip_days_value: float,
    cargo_capacity: object = KHI_COMMERCIAL_CARGO_CAPACITY,
    lh2_density: object = Q_(70.8, "kg/m^3"),
    availability: float = 0.90,
    fill_fraction: float = 1.0,
) -> int:
    """Number of carriers needed to deliver an annual LH2 volume on a route.

    Args:
        annual_volume_kg: Annual LH2 delivery volume, kg/y.
        round_trip_days_value: Round-trip cycle time, days (see
            ``round_trip_days``).
        cargo_capacity: Per-vessel cargo capacity (default: KHI's
            commercial-scale target, 160,000 m3).
        lh2_density: LH2 density at NBP (default: 70.8 kg/m3, per
            data/properties/lh2-properties.csv — tagged needs-source pending
            a formal NIST/CODATA citation; see docs/memory.md open item).
        availability: [ASSUMPTION] fleet-wide operational availability
            (default 0.90 — dry-docking/maintenance/weather margin; KHI does
            not disclose a fleet availability figure).
        fill_fraction: Usable fill vs full tank volume (0-1). Default 1.0
            (matches this function's pre-existing behavior).

    Returns:
        Number of vessels (rounded up).
    """
    annual_capacity_per_ship = annual_capacity_per_vessel(
        round_trip_days_value, cargo_capacity, lh2_density, fill_fraction, availability
    )
    return math.ceil(annual_volume_kg / annual_capacity_per_ship)


__all__ = [
    "KHI_COMMERCIAL_CARGO_CAPACITY",
    "KHI_COMMERCIAL_SPEED",
    "KHI_LOAD_UNLOAD_DAYS_LOW",
    "KHI_LOAD_UNLOAD_DAYS_HIGH",
    "KHI_LOAD_UNLOAD_DAYS_MID",
    "one_way_transit_days",
    "round_trip_days",
    "voyage_boil_off",
    "cargo_mass_per_voyage",
    "annual_capacity_per_vessel",
    "fleet_size",
]
