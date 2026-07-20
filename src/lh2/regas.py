"""[5] Regasification — LH2 -> gaseous H2 at delivery pressure.

Boundary: LH2 in -> GH2 out. See docs/methodology/05-regas.md.

Every default below carries a data/references.csv id in a comment, per
CLAUDE.md §4.
"""

from __future__ import annotations

from .units import Q_

#: Regasification heat duty per kg of LH2 vaporised.
#: ref: kawasaki-2026-questionnaire (reply Q18: "approximately 3.8 MJ/kg-LH2").
KHI_REGAS_HEAT_DUTY = Q_(3.8, "MJ/kg")

#: Import-side boil-off rate at rest (same as export side).
#: ref: kawasaki-2026-supplemental ("BOR 0.1 %/d").
KHI_BOR_AT_REST_PCT_PER_DAY = 0.1


def regas_duty(mass: object, duty: object = KHI_REGAS_HEAT_DUTY):
    """Vaporization heat duty for a given LH2 mass.

    Args:
        mass: LH2 mass to regasify, as a ``pint`` quantity or bare kg.
        duty: Heat duty per kg (default: KHI's disclosed 3.8 MJ/kg,
            ``KHI_REGAS_HEAT_DUTY``).

    Returns:
        Total heat duty, as a ``pint`` Quantity in MJ.
    """
    if not hasattr(mass, "units"):
        mass = Q_(mass, "kg")
    return (mass * duty).to("MJ")


__all__ = ["KHI_REGAS_HEAT_DUTY", "KHI_BOR_AT_REST_PCT_PER_DAY", "regas_duty"]
