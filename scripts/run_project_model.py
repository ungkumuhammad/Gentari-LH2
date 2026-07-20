#!/usr/bin/env python3
"""CLI: run the KHI-based LH2 project scenario calculator (``lh2.scenario``).

Given a project's annual liquefaction throughput and shipping distance, this
prints the resulting energy use, boil-off, fleet sizing, indicative cost
stack, and (if CapEx/OpEx/discount rate are supplied) LCOH — all built on
KHI's disclosed value-chain data (see docs/reports/khi-lh2-solution-database.md).

Examples::

    # Technical KPIs only (no cost inputs supplied -> LCOH flagged as a gap)
    python scripts/run_project_model.py --tpa 300000 --distance-km 6000

    # With cost inputs, to get an LCOH
    python scripts/run_project_model.py --tpa 300000 --distance-km 6000 \\
        --capex-musd 1200 --opex-musd-per-year 60 --discount-rate 0.08 \\
        --voyage-bor-pct-per-day 0.2 --fx-jpy-per-usd 150
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from lh2.scenario import ProjectInputs, format_report, run_scenario  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tpa", type=float, required=True, help="Annual liquefaction throughput, t/y")
    parser.add_argument("--distance-km", type=float, required=True, help="One-way shipping distance, km")
    parser.add_argument("--sec-kwh-per-kg", type=float, default=None, help="Liquefaction SEC override, kWh/kg (default: KHI 8-9 range midpoint)")
    parser.add_argument("--speed-kmh", type=float, default=None, help="Vessel speed override, km/h (default: KHI commercial target 29.6 km/h)")
    parser.add_argument("--cargo-capacity-m3", type=float, default=None, help="Vessel cargo capacity override, m3 (default: KHI commercial target 160,000 m3)")
    parser.add_argument("--export-hold-days", type=float, default=0.0, help="Export-terminal dwell time, days")
    parser.add_argument("--import-hold-days", type=float, default=0.0, help="Import-terminal dwell time, days")
    parser.add_argument("--voyage-bor-pct-per-day", type=float, default=None, help="Voyage BOR, %%/day (KHI does not disclose this; supply your own [ASSUMPTION]/[ESTIMATE])")
    parser.add_argument("--discount-rate", type=float, default=None, help="Real discount rate per year, for LCOH")
    parser.add_argument("--capex-musd", type=float, default=None, help="Total CapEx, million USD")
    parser.add_argument("--opex-musd-per-year", type=float, default=None, help="Annual OpEx, million USD/y")
    parser.add_argument("--project-years", type=int, default=20, help="Project life for LCOH (default 20 — [ASSUMPTION])")
    parser.add_argument("--fx-jpy-per-usd", type=float, default=None, help="JPY-per-USD rate, to convert the IAE cost stack to USD")
    args = parser.parse_args()

    kwargs = dict(
        annual_liquefaction_tpa=args.tpa,
        distance_km=args.distance_km,
        export_hold_days=args.export_hold_days,
        import_hold_days=args.import_hold_days,
        voyage_bor_pct_per_day=args.voyage_bor_pct_per_day,
        discount_rate=args.discount_rate,
        capex_musd=args.capex_musd,
        opex_musd_per_year=args.opex_musd_per_year,
        project_years=args.project_years,
        fx_jpy_per_usd=args.fx_jpy_per_usd,
    )
    if args.sec_kwh_per_kg is not None:
        kwargs["sec_kwh_per_kg"] = args.sec_kwh_per_kg
    if args.speed_kmh is not None:
        kwargs["speed_kmh"] = args.speed_kmh
    if args.cargo_capacity_m3 is not None:
        kwargs["cargo_capacity_m3"] = args.cargo_capacity_m3

    inputs = ProjectInputs(**kwargs)
    result = run_scenario(inputs)
    print(format_report(result))


if __name__ == "__main__":
    main()
