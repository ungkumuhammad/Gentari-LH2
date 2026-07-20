"""[3] Storage — at-rest cryogenic LH2 storage.

Boundary: LH2 in <-> LH2 out (at rest). See docs/methodology/03-storage.md.

Every default below carries a data/references.csv id in a comment, per
CLAUDE.md §4.
"""

from __future__ import annotations

from .units import Q_

#: Boil-off rate at rest, both export (loading) and import (receiving)
#: terminals per KHI's cost-basis slide.
#: ref: kawasaki-2026-supplemental ("BOR 0.1 %/d").
KHI_BOR_AT_REST_PCT_PER_DAY = 0.1

#: Export-side storage tank size.
#: ref: kawasaki-2026-supplemental ("64,000 m3/tank").
KHI_EXPORT_TANK_SIZE = Q_(64_000.0, "m^3")

#: Import-side storage tank size.
#: ref: kawasaki-2026-supplemental ("65,000 m3/tank").
KHI_IMPORT_TANK_SIZE = Q_(65_000.0, "m^3")


def boil_off_at_rest(inventory_kg: object, days: float, bor_pct_per_day: float = KHI_BOR_AT_REST_PCT_PER_DAY):
    """Boil-off loss from at-rest storage over a holding period.

    Modeled as compounding daily loss of the *remaining* inventory (the
    standard boil-off convention), not a flat percentage of the original
    inventory: ``loss = inventory * (1 - (1 - bor/100)^days)``.

    Args:
        inventory_kg: Stored LH2 mass, as a ``pint`` quantity or bare kg.
        days: Holding time at rest, in days.
        bor_pct_per_day: Boil-off rate, %/day (default: KHI's disclosed
            0.1 %/day, ``KHI_BOR_AT_REST_PCT_PER_DAY``).

    Returns:
        Mass lost to boil-off, as a ``pint`` Quantity in kg.
    """
    if not hasattr(inventory_kg, "units"):
        inventory_kg = Q_(inventory_kg, "kg")
    retained_fraction = (1.0 - bor_pct_per_day / 100.0) ** days
    return inventory_kg * (1.0 - retained_fraction)


__all__ = [
    "KHI_BOR_AT_REST_PCT_PER_DAY",
    "KHI_EXPORT_TANK_SIZE",
    "KHI_IMPORT_TANK_SIZE",
    "boil_off_at_rest",
]
