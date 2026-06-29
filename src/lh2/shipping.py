"""[4] Shipping — LH2 marine transport + voyage boil-off.

Boundary: LH2 loaded -> LH2 discharged. See docs/methodology/04-shipping.md.
Vessel specs live in data/vessels/ (each referencing a references.csv id).

STUB. No numeric defaults yet — when added, each carries a
data/references.csv id or a [ASSUMPTION]/[ESTIMATE] tag (CLAUDE.md §4).
"""

from __future__ import annotations


def voyage_boil_off(*args, **kwargs):
    """In-transit boil-off losses over a voyage. TODO: needs source."""
    raise NotImplementedError("TODO: implement; inputs must be sourced/tagged")


def fleet_size(*args, **kwargs):
    """Number of carriers for a given trade. TODO: needs source."""
    raise NotImplementedError("TODO: implement; inputs must be sourced/tagged")
