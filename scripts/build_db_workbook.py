#!/usr/bin/env python3
"""Build the one-workbook Excel mirror of the LH2 techno-economic database.

The CSV tables under ``data/`` are the source of truth; this script reads them
plus ``data/references.csv`` and writes ``data/lh2-database.xlsx`` with one
sheet per table. Re-run after editing any CSV so the workbook never drifts.

Usage::

    python scripts/build_db_workbook.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT = DATA_DIR / "lh2-database.xlsx"

# (sheet name, csv path relative to data/). Sheet names kept <=31 chars (Excel).
TABLES: list[tuple[str, str]] = [
    ("references", "references.csv"),
    ("liquefaction", "properties/liquefaction.csv"),
    ("terminals", "properties/terminals.csv"),
    ("regas", "properties/regas.csv"),
    ("lh2_properties", "properties/lh2-properties.csv"),
    ("lh2_carriers", "vessels/lh2-carriers.csv"),
    ("cost_stack", "costs/lh2-cost-stack.csv"),
]


def build() -> Path:
    with pd.ExcelWriter(OUTPUT, engine="openpyxl") as writer:
        for sheet, rel in TABLES:
            df = pd.read_csv(DATA_DIR / rel, dtype=str, keep_default_na=False)
            df.to_excel(writer, sheet_name=sheet, index=False)
    return OUTPUT


if __name__ == "__main__":
    path = build()
    print(f"Wrote {path}")
