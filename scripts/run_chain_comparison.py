#!/usr/bin/env python3
"""CLI for the LH2-vs-NH3 node-by-node energy-penalty cascade.

Boundary: electrolyser battery limit (node A) -> GH2 at the import-terminal
send-out flange (node F1 / F2). Basis: 1 kg H2 produced at node A.

Every default is cited or tagged -- see ``data/carriers/chain-energy-defaults.csv``
and ``src/lh2/chain_energy.py``. No ammonia figure is sourced yet (decision D4).

Usage::

    python scripts/run_chain_comparison.py
    python scripts/run_chain_comparison.py --electrolyser-sec 55 --distance 5300
    python scripts/run_chain_comparison.py --cracker-self-consumption 25 --json
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from lh2.chain_energy import ChainInputs, compare, format_report  # noqa: E402


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--electrolyser-sec", type=float, help="kWh/kg H2, node A [ASSUMPTION]")
    p.add_argument("--distance", type=float, help="km, one-way laden voyage [ASSUMPTION]")
    p.add_argument("--liquefaction-sec", type=float, help="kWh/kg, node B1 (KHI 8-9, cited)")
    p.add_argument("--voyage-bor", type=float, help="%%/day, node D1 [ESTIMATE]")
    p.add_argument("--hb-sec", type=float, help="kWh/kg-NH3, node B2 [ESTIMATE]")
    p.add_argument(
        "--cracker-self-consumption", type=float, help="%% of H2-equivalent, node F2 [ESTIMATE]"
    )
    p.add_argument("--json", action="store_true", help="emit machine-readable results")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    overrides = {
        "electrolyser_sec_kwh_per_kg": args.electrolyser_sec,
        "voyage_distance_km": args.distance,
        "liquefaction_sec_kwh_per_kg": args.liquefaction_sec,
        "lh2_voyage_bor_pct_per_day": args.voyage_bor,
        "hb_sec_kwh_per_kg_nh3": args.hb_sec,
        "cracker_self_consumption_pct": args.cracker_self_consumption,
    }
    inputs = ChainInputs(**{k: v for k, v in overrides.items() if v is not None})

    if args.json:
        results = compare(inputs)
        payload = {
            "inputs": asdict(inputs),
            "chains": {
                key: {
                    "nodes": [asdict(n) for n in r.nodes],
                    "delivered_kg_h2": r.delivered_kg_h2,
                    "total_energy_kwh": r.total_energy_kwh,
                    "lhv_delivered_kwh": r.lhv_delivered_kwh,
                    "efficiency_pct": r.efficiency_pct,
                    "net_energy_kwh": r.net_energy_kwh,
                    "retained_pct": r.retained_pct,
                    "gaps": r.gaps,
                }
                for key, r in results.items()
            },
        }
        print(json.dumps(payload, indent=2))
    else:
        print(format_report(inputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
