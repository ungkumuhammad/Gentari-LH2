"""Project-level LH2 scenario calculator built on KHI's disclosed data.

Ties together ``liquefaction``, ``storage``, ``shipping``, ``regas``, and
``economics`` to answer: *given an annual liquefaction throughput and a
shipping distance, what does KHI's solution imply for energy use, boil-off,
fleet size, and (if the user supplies CapEx/OpEx) LCOH?*

This is a project sizing/screening tool, not a substitute for a Feasibility
Study. Per CLAUDE.md §4, figures KHI declined to disclose (CapEx, OpEx,
carbon intensity, newbuild cost, a standalone shipping BOR) are never
invented: when the caller does not supply them, the result carries an
explicit ``gaps`` list instead of a fabricated number.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from . import liquefaction, regas, shipping, storage
from .economics import lcoh as _lcoh
from .units import Q_

#: Gaseous H2 density at normal conditions (0C, 1.013 bar(a)).
#: ref: data/properties/lh2-properties.csv, tagged needs-source (pending a
#: formal NIST/CODATA citation — see docs/memory.md open item #4).
GAS_DENSITY_KG_PER_NM3 = 0.0899

#: LH2 density at NBP.
#: ref: data/properties/lh2-properties.csv, tagged needs-source (same item).
LH2_DENSITY_KG_PER_M3 = 70.8

#: IAE per-component cost stack, JPY/Nm3, ~2019 vintage (unverified unit and
#: cost-year — see data/costs/lh2-cost-stack.csv and docs/reports/
#: khi-lh2-solution-database.md §7). Reproduced second-hand via KHI.
#: ref: kawasaki-2026-supplemental -> iae-2019-gigaton
#: [needs source: primary].
IAE_COST_STACK = {
    "Base": {
        "volume_nm3_per_year": 2.5e9,
        "production": 10.1,
        "liquefaction": 10.3,
        "loading_terminal": 5.6,
        "seaborne_transport": 4.0,
        "receiving_terminal": 6.3,
        "dehydrogenation": 0.0,
        "other": 1.3,
    },
    "Large": {
        "volume_nm3_per_year": 10.0e9,
        "production": 10.1,
        "liquefaction": 10.0,
        "loading_terminal": 1.9,
        "seaborne_transport": 4.0,
        "receiving_terminal": 3.4,
        "dehydrogenation": 0.0,
        "other": 1.3,
    },
    "Tech": {
        # Same 10B Nm3/y deal volume as Large, but with KHI's disclosed
        # "Tech" step-up (115->150 tpd trains, 16->25 knot vessel, storage
        # tank up to 200,000 m3). Not a further scale point for interpolation.
        "volume_nm3_per_year": 10.0e9,
        "production": 9.3,
        "liquefaction": 8.6,
        "loading_terminal": 1.8,
        "seaborne_transport": 2.3,
        "receiving_terminal": 2.8,
        "dehydrogenation": 0.0,
        "other": 1.3,
    },
}

_COST_COMPONENTS = (
    "production",
    "liquefaction",
    "loading_terminal",
    "seaborne_transport",
    "receiving_terminal",
    "dehydrogenation",
    "other",
)


def interpolate_iae_cost_stack(nm3_per_year: float) -> tuple[dict[str, float], list[str]]:
    """Linearly interpolate KHI/IAE's Base/Large cost stack to a project volume.

    KHI discloses only two scale points (Base 2.5B Nm3/y, Large 10B Nm3/y).
    This is a [ASSUMPTION: linear interpolation] between those two disclosed
    points — not a KHI-provided curve. Values outside [Base, Large] are
    clipped to the nearest endpoint and flagged, since KHI gives no basis for
    extrapolation.

    Returns:
        A tuple of (component -> JPY/Nm3 dict including "TOTAL", warnings).
    """
    base = IAE_COST_STACK["Base"]
    large = IAE_COST_STACK["Large"]
    v_lo, v_hi = base["volume_nm3_per_year"], large["volume_nm3_per_year"]

    warnings: list[str] = []
    v = nm3_per_year
    if v < v_lo or v > v_hi:
        warnings.append(
            f"Project volume {v:.3g} Nm3/y is outside KHI's disclosed "
            f"Base-Large range [{v_lo:.3g}, {v_hi:.3g}] Nm3/y; cost stack "
            "clipped to the nearest endpoint rather than extrapolated."
        )
        v = min(max(v, v_lo), v_hi)

    t = (v - v_lo) / (v_hi - v_lo)
    stack = {c: base[c] + t * (large[c] - base[c]) for c in _COST_COMPONENTS}
    stack["TOTAL"] = sum(stack.values())
    return stack, warnings


@dataclass
class ProjectInputs:
    """Inputs for a single project scenario.

    Args:
        annual_liquefaction_tpa: Required annual H2 throughput at the
            liquefaction plant (gate-to-gate production side), t/y.
        distance_km: One-way shipping distance, export -> import terminal.
        sec_kwh_per_kg: Liquefaction SEC (default: KHI's disclosed range
            midpoint, 8.5 kWh/kg — [ASSUMPTION], see liquefaction.KHI_SEC_MID).
        speed_kmh: Vessel service speed (default: KHI's commercial-scale
            target, 29.6 km/h / ~16 knots).
        cargo_capacity_m3: Vessel cargo capacity (default: KHI's
            commercial-scale target, 160,000 m3).
        export_hold_days: Dwell time in export storage before loading, days.
            Project-specific; no KHI default (0 = not modeled).
        import_hold_days: Dwell time in import storage after discharge, days.
            Project-specific; no KHI default (0 = not modeled).
        voyage_bor_pct_per_day: Voyage boil-off rate, %/day. KHI did not
            disclose a standalone figure for this (see shipping.py module
            docstring) — leave ``None`` to skip voyage-loss modeling (flagged
            as a gap) or supply an explicit [ASSUMPTION]/[ESTIMATE] value.
        discount_rate: Real discount rate for LCOH, per period. No KHI/
            corporate default — required only if CapEx/OpEx are also supplied.
        capex_musd: Total CapEx, million USD, cost-year as supplied by the
            caller. KHI did not disclose this (Feasibility Study required);
            leave ``None`` to skip LCOH (flagged as a gap).
        opex_musd_per_year: Annual OpEx, million USD/y, one value applied
            across ``project_years`` unless a full list is given. Same
            disclosure caveat as CapEx.
        project_years: Economic project life for LCOH (default 20 years —
            [ASSUMPTION: typical energy-infrastructure asset life; not
            KHI-sourced]).
        fx_jpy_per_usd: JPY-per-USD rate to convert the IAE cost stack
            (JPY/Nm3) to USD. No KHI-sourced rate exists; leave ``None`` to
            keep the cost stack in JPY/Nm3 (flagged as a gap).
    """

    annual_liquefaction_tpa: float
    distance_km: float
    sec_kwh_per_kg: float = liquefaction.KHI_SEC_MID.magnitude
    speed_kmh: float = shipping.KHI_COMMERCIAL_SPEED.magnitude
    cargo_capacity_m3: float = shipping.KHI_COMMERCIAL_CARGO_CAPACITY.magnitude
    export_hold_days: float = 0.0
    import_hold_days: float = 0.0
    voyage_bor_pct_per_day: float | None = None
    discount_rate: float | None = None
    capex_musd: float | None = None
    opex_musd_per_year: float | list[float] | None = None
    project_years: int = 20
    fx_jpy_per_usd: float | None = None


@dataclass
class ScenarioResult:
    """Output of ``run_scenario``. Every field traces to §sources in the
    KHI database report (docs/reports/khi-lh2-solution-database.md) or to an
    explicit assumption named in ``ProjectInputs``."""

    inputs: ProjectInputs
    liquefaction_trains: int
    liquefaction_energy_kwh_per_year: float
    export_terminal_bog_kg_per_year: float
    voyage_bog_kg_per_year: float | None
    delivered_mass_tpa: float
    fleet_size: int
    round_trip_days: float
    import_terminal_bog_kg_per_year: float
    regas_duty_mj_per_year: float
    cost_stack_jpy_per_nm3: dict[str, float]
    cost_stack_usd_per_kg: dict[str, float] | None
    cost_stack_warnings: list[str]
    lcoh_usd_per_kg: float | None
    gaps: list[str] = field(default_factory=list)


def run_scenario(inputs: ProjectInputs) -> ScenarioResult:
    """Run the full value-chain calculation for one project scenario."""
    gaps: list[str] = []
    annual_kg = inputs.annual_liquefaction_tpa * 1000.0

    trains = liquefaction.train_count(inputs.annual_liquefaction_tpa)
    energy = liquefaction.liquefaction_energy(
        Q_(annual_kg, "kg"), Q_(inputs.sec_kwh_per_kg, "kWh/kg")
    )

    # Export-terminal BOG: KHI states this is re-liquefied (reply Q3/Q14), so
    # it is reported for visibility but not subtracted from shipped mass.
    export_bog = storage.boil_off_at_rest(
        Q_(annual_kg, "kg"), inputs.export_hold_days
    )
    shipped_mass_kg = annual_kg

    transit_days = shipping.one_way_transit_days(inputs.distance_km, inputs.speed_kmh)
    round_trip = shipping.round_trip_days(inputs.distance_km, inputs.speed_kmh)
    fleet = shipping.fleet_size(
        shipped_mass_kg,
        round_trip,
        cargo_capacity=inputs.cargo_capacity_m3,
        lh2_density=LH2_DENSITY_KG_PER_M3,
    )

    if inputs.voyage_bor_pct_per_day is None:
        voyage_bog = None
        delivered_mass_kg = shipped_mass_kg
        gaps.append(
            "voyage_bor_pct_per_day not supplied — KHI disclosed no "
            "standalone shipping boil-off figure (only that fuel-gas "
            "consumption equals the BOR, reply Q23). Delivered mass assumes "
            "zero in-transit loss, which is optimistic; supply a tagged "
            "[ASSUMPTION]/[ESTIMATE] value to model it."
        )
    else:
        voyage_bog = shipping.voyage_boil_off(
            shipped_mass_kg, transit_days, inputs.voyage_bor_pct_per_day
        ).to("kg").magnitude
        delivered_mass_kg = shipped_mass_kg - voyage_bog

    import_bog = storage.boil_off_at_rest(
        Q_(delivered_mass_kg, "kg"), inputs.import_hold_days
    )

    duty = regas.regas_duty(Q_(delivered_mass_kg, "kg"))

    nm3_per_year = annual_kg / GAS_DENSITY_KG_PER_NM3
    cost_stack, cost_warnings = interpolate_iae_cost_stack(nm3_per_year)

    lcoh_value: float | None = None
    if inputs.capex_musd is None or inputs.opex_musd_per_year is None or inputs.discount_rate is None:
        missing = [
            name
            for name, val in (
                ("capex_musd", inputs.capex_musd),
                ("opex_musd_per_year", inputs.opex_musd_per_year),
                ("discount_rate", inputs.discount_rate),
            )
            if val is None
        ]
        gaps.append(
            f"LCOH not computed — missing {', '.join(missing)}. KHI did not "
            "disclose CapEx/OpEx for liquefaction, terminals, or the carrier "
            "newbuild (a Feasibility Study is required per KHI's reply); "
            "supply project-specific figures to unlock LCOH."
        )
    else:
        opex_list = inputs.opex_musd_per_year
        if isinstance(opex_list, (int, float)):
            opex_list = [float(opex_list)] * inputs.project_years
        h2_per_year = [delivered_mass_kg] * inputs.project_years
        lcoh_value = _lcoh(
            capex=inputs.capex_musd * 1e6,
            opex_per_year=[o * 1e6 for o in opex_list],
            h2_kg_per_year=h2_per_year,
            discount_rate=inputs.discount_rate,
        )

    cost_stack_usd: dict[str, float] | None = None
    if inputs.fx_jpy_per_usd is None:
        gaps.append(
            "fx_jpy_per_usd not supplied — the IAE/KHI cost stack is kept in "
            "its native JPY/Nm3 (~2019, unverified per docs/reports/"
            "khi-lh2-solution-database.md §7); supply a rate to see it in USD."
        )
    else:
        usd_per_nm3 = {k: v / inputs.fx_jpy_per_usd for k, v in cost_stack.items()}
        cost_stack_usd = {k: v / GAS_DENSITY_KG_PER_NM3 for k, v in usd_per_nm3.items()}
        gaps.append(
            "cost_stack_usd_per_kg uses a user-supplied FX rate and the "
            "unverified JPY/Nm3 IAE cost stack (§7 caveat) — treat as "
            "indicative only, not a sourced USD/kg LCOH."
        )

    gaps.extend(cost_warnings)
    gaps.append(
        "carbon_intensity_kgco2e_per_kg not modeled — KHI declined to "
        "disclose this (reply Q11: 'Feasibility Study is necessary')."
    )

    return ScenarioResult(
        inputs=inputs,
        liquefaction_trains=trains,
        liquefaction_energy_kwh_per_year=energy.to("kWh").magnitude,
        export_terminal_bog_kg_per_year=export_bog.to("kg").magnitude,
        voyage_bog_kg_per_year=voyage_bog,
        delivered_mass_tpa=delivered_mass_kg / 1000.0,
        fleet_size=fleet,
        round_trip_days=round_trip,
        import_terminal_bog_kg_per_year=import_bog.to("kg").magnitude,
        regas_duty_mj_per_year=duty.to("MJ").magnitude,
        cost_stack_jpy_per_nm3=cost_stack,
        cost_stack_usd_per_kg=cost_stack_usd,
        cost_stack_warnings=cost_warnings,
        lcoh_usd_per_kg=lcoh_value,
        gaps=gaps,
    )


def format_report(result: ScenarioResult) -> str:
    """Render a ``ScenarioResult`` as a human-readable text report."""
    i = result.inputs
    lines = [
        "LH2 PROJECT SCENARIO — built on KHI's disclosed value-chain data",
        "=" * 68,
        f"Annual liquefaction throughput : {i.annual_liquefaction_tpa:,.0f} t/y",
        f"Shipping distance (one-way)     : {i.distance_km:,.0f} km",
        f"SEC assumed                     : {i.sec_kwh_per_kg:.2f} kWh/kg",
        "",
        "-- Liquefaction --",
        f"Trains required (115 t/d each)  : {result.liquefaction_trains}",
        f"Annual liquefaction energy      : {result.liquefaction_energy_kwh_per_year:,.0f} kWh/y",
        "",
        "-- Terminals & storage (BOR 0.1%/day, re-liquefied per KHI) --",
        f"Export-terminal BOG (informational): {result.export_terminal_bog_kg_per_year:,.1f} kg/y",
        f"Import-terminal BOG (informational): {result.import_terminal_bog_kg_per_year:,.1f} kg/y",
        "",
        "-- Shipping --",
        f"Round-trip cycle time           : {result.round_trip_days:.2f} days",
        f"Fleet size required              : {result.fleet_size} vessel(s)",
        "Voyage BOG (fuel draw)          : "
        + (
            f"{result.voyage_bog_kg_per_year:,.1f} kg/y"
            if result.voyage_bog_kg_per_year is not None
            else "not modeled (see gaps)"
        ),
        f"Delivered mass at import        : {result.delivered_mass_tpa:,.1f} t/y",
        "",
        "-- Regasification --",
        f"Annual regas heat duty          : {result.regas_duty_mj_per_year:,.0f} MJ/y",
        "",
        "-- Indicative cost stack (JPY/Nm3, ~2019, IAE via KHI, unverified) --",
    ]
    for component, value in result.cost_stack_jpy_per_nm3.items():
        lines.append(f"  {component:<20s}: {value:6.2f}")
    if result.cost_stack_usd_per_kg is not None:
        lines.append("")
        lines.append("-- Same stack converted to USD/kg (user-supplied FX rate; indicative) --")
        for component, value in result.cost_stack_usd_per_kg.items():
            lines.append(f"  {component:<20s}: {value:6.3f}")
    lines += [
        "",
        "-- Economics --",
        "LCOH: "
        + (
            f"{result.lcoh_usd_per_kg:.2f} USD/kg"
            if result.lcoh_usd_per_kg is not None
            else "not computed (see gaps)"
        ),
        "",
        "-- Gaps / caveats (CLAUDE.md §4: nothing here is fabricated) --",
    ]
    lines += [f"  * {g}" for g in result.gaps]
    return "\n".join(lines)


__all__ = [
    "IAE_COST_STACK",
    "GAS_DENSITY_KG_PER_NM3",
    "LH2_DENSITY_KG_PER_M3",
    "interpolate_iae_cost_stack",
    "ProjectInputs",
    "ScenarioResult",
    "run_scenario",
    "format_report",
]
