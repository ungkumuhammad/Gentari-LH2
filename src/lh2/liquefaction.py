"""[2] Liquefaction — gaseous H2 -> LH2 at ~20 K, ~1 bar.

Boundary: GH2 in -> LH2 out. See docs/methodology/02-liquefaction.md.

Every default below carries a data/references.csv id in a comment, or an
explicit [ASSUMPTION] with its derivation, per CLAUDE.md §4. Values KHI
declined to disclose (CapEx, OpEx, carbon intensity) are NOT modeled here;
callers must supply those from a Feasibility Study or a permitted external
benchmark.
"""

from __future__ import annotations

import math

from .units import Q_

#: SEC range for KHI's liquefaction process, 20C gaseous feed.
#: ref: kawasaki-2026-questionnaire (reply Q1) — "approximately 8-9 kWh/kg,
#: though it varies with liquefier scale and boundary conditions".
KHI_SEC_LOW = Q_(8.0, "kWh/kg")
KHI_SEC_HIGH = Q_(9.0, "kWh/kg")
#: [ASSUMPTION] midpoint of the KHI-disclosed range, for single-point scenarios.
KHI_SEC_MID = (KHI_SEC_LOW + KHI_SEC_HIGH) / 2

#: Per-train nameplate capacity. ref: kawasaki-2026-supplemental (Base/Large
#: scale slide: "Capacity 115 t/(d unit)").
KHI_TRAIN_CAPACITY = Q_(115.0, "t/day")

#: Minimum economically-viable scale, subject to offtake pricing.
#: ref: kawasaki-2026-questionnaire (reply Q2).
KHI_MIN_ECONOMICAL_SCALE_TPA = 10_000.0

#: [ASSUMPTION: derived] Effective train utilization/availability factor.
#: KHI discloses two (deal-volume, train-count) points on its own cost-basis
#: slide (kawasaki-2026-supplemental): Base = 2.5e9 Nm3/y on 7 trains of
#: 115 t/d; Large = 10e9 Nm3/y on 27 trains of 115 t/d. Converting Nm3/y to
#: t/y via the normal gas density (0.0899 kg/Nm3, data/properties/
#: lh2-properties.csv, tagged needs-source) gives implied utilizations of
#: ~76.5% (Base) and ~79.3% (Large); we use the average as a single
#: representative factor. This is derived arithmetic on KHI's own disclosed
#: figures, not an invented default — replace if KHI provides a direct figure.
KHI_TRAIN_UTILIZATION_ASSUMPTION = 0.78

#: [ASSUMPTION] Plant stream days per year (on-stream time, i.e. calendar
#: days less planned turnaround/maintenance downtime). KHI's own Base/Large
#: data points used to derive KHI_TRAIN_UTILIZATION_ASSUMPTION above assumed
#: a 365-day (calendar) year, so 365 is the default here to reproduce that
#: derivation unchanged. Not a KHI-disclosed figure — override with a
#: project-specific turnaround/maintenance schedule if available (typical
#: cryogenic liquefaction trains run ~330-350 stream-days/y after planned
#: turnaround; no source for a KHI-specific value exists yet).
KHI_STREAM_DAYS_PER_YEAR_ASSUMPTION = 365.0


def liquefaction_energy(mass: object, sec: object = KHI_SEC_MID):
    """Liquefaction energy use for a given hydrogen mass.

    Args:
        mass: H2 mass to liquefy, as a ``pint`` quantity (e.g. ``Q_(1000,
            "kg")``) or a bare number of kg.
        sec: Specific energy consumption, a ``pint`` quantity (default:
            ``KHI_SEC_MID``, the midpoint of KHI's disclosed 8-9 kWh/kg
            range — an [ASSUMPTION], not a KHI point value).

    Returns:
        Energy required, as a ``pint`` Quantity in kWh.
    """
    if not hasattr(mass, "units"):
        mass = Q_(mass, "kg")
    return (mass * sec).to("kWh")


def train_count(
    annual_capacity_tpa: float,
    train_capacity: object = KHI_TRAIN_CAPACITY,
    utilization: float = KHI_TRAIN_UTILIZATION_ASSUMPTION,
    stream_days_per_year: float = KHI_STREAM_DAYS_PER_YEAR_ASSUMPTION,
) -> int:
    """Number of liquefaction trains needed for an annual throughput.

    Args:
        annual_capacity_tpa: Required annual liquefaction throughput, t/y.
        train_capacity: Per-train nameplate capacity (default: KHI's
            disclosed 115 t/d train, ``KHI_TRAIN_CAPACITY``).
        utilization: Effective rate-utilization factor while on-stream
            (default: ``KHI_TRAIN_UTILIZATION_ASSUMPTION``, derived from
            KHI's own Base/Large data points — see that constant's
            docstring/comment).
        stream_days_per_year: Plant on-stream days per year, i.e. calendar
            days less planned turnaround/maintenance downtime (default:
            ``KHI_STREAM_DAYS_PER_YEAR_ASSUMPTION`` = 365 d, matching the
            365-day basis KHI's own data points were back-solved against).
            Pass a project-specific value (e.g. 330-350 d) to model planned
            downtime explicitly instead of folding it into ``utilization``.

    Returns:
        Number of whole trains (rounded up) required.
    """
    if not hasattr(train_capacity, "units"):
        train_capacity = Q_(train_capacity, "t/day")
    annual_train_capacity = (
        train_capacity * Q_(stream_days_per_year, "day") * utilization
    ).to("t")
    n = annual_capacity_tpa / annual_train_capacity.magnitude
    return math.ceil(n)


__all__ = [
    "KHI_SEC_LOW",
    "KHI_SEC_HIGH",
    "KHI_SEC_MID",
    "KHI_TRAIN_CAPACITY",
    "KHI_MIN_ECONOMICAL_SCALE_TPA",
    "KHI_TRAIN_UTILIZATION_ASSUMPTION",
    "KHI_STREAM_DAYS_PER_YEAR_ASSUMPTION",
    "liquefaction_energy",
    "train_count",
]
