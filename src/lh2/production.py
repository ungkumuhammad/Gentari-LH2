"""[1] Production — upstream gaseous H2 (electrolysis or SMR+CCS).

Boundary: energy/feedstock in -> gaseous H2 at battery limit.
See docs/methodology/01-production.md.

STUB. No numeric defaults yet — when added, each carries a
data/references.csv id or a [ASSUMPTION]/[ESTIMATE] tag (CLAUDE.md §4).
"""

from __future__ import annotations


def production_cost(*args, **kwargs):
    """H2 production cost (USD/kg). TODO: needs source for all inputs."""
    raise NotImplementedError("TODO: implement; inputs must be sourced/tagged")
