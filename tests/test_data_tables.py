"""Validation tests for the KR1.1 LH2 techno-economic database (`data/`).

Enforces the cardinal rule (``CLAUDE.md`` §4): every row is either cited to a
``references.csv`` id or tagged. Also checks units parse, source ids resolve,
and the IAE cost stack reconciles to its per-scenario totals.
"""

from __future__ import annotations

from math import isclose
from pathlib import Path

import pandas as pd
import pytest

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

SCHEMA = [
    "segment", "component", "parameter", "value", "unit",
    "low", "high", "basis", "source_id", "tag", "notes",
]

TABLES = [
    "properties/liquefaction.csv",
    "properties/terminals.csv",
    "properties/regas.csv",
    "properties/lh2-properties.csv",
    "vessels/lh2-carriers.csv",
    "costs/lh2-cost-stack.csv",
]

NON_CITED_TAGS = {"ASSUMPTION", "ESTIMATE", "needs-source"}
VALID_TAGS = {"cited"} | NON_CITED_TAGS

# Controlled unit vocabulary for the database. Catalog units are human-readable
# (and include counts like ``ship``/``unit`` and notations like ``m3``/``Nm3``
# that the pint registry does not parse natively), so we validate against this
# vocabulary to catch typos rather than forcing every label through pint.
# pint enforcement lives in the modelling code (src/lh2), not the data catalog.
KNOWN_UNITS = {
    "kWh/kg", "kWh/Nm3", "t/d", "unit", "tpa", "%", "year",
    "USD/kg", "USD/ship", "kgCO2e/kg", "%/day", "m3", "inch", "TRL",
    "MJ/kg", "K", "kg/m3", "kg/Nm3", "km/h", "ship", "day", "JPY/Nm3",
}


def _load(rel: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / rel, dtype=str, keep_default_na=False)


def _reference_ids() -> set[str]:
    refs = pd.read_csv(DATA_DIR / "references.csv", dtype=str, keep_default_na=False)
    return set(refs["id"])


@pytest.mark.parametrize("rel", TABLES)
def test_schema_columns(rel: str):
    df = _load(rel)
    assert list(df.columns) == SCHEMA, f"{rel} has unexpected columns"


@pytest.mark.parametrize("rel", TABLES)
def test_every_row_cited_or_tagged(rel: str):
    df = _load(rel)
    ref_ids = _reference_ids()
    for i, row in df.iterrows():
        tag = row["tag"].strip()
        assert tag in VALID_TAGS, f"{rel} row {i}: bad tag {tag!r}"
        has_source = row["source_id"].strip() in ref_ids
        # Invariant: a resolving source_id OR a non-cited tag.
        assert has_source or tag in NON_CITED_TAGS, (
            f"{rel} row {i}: neither a resolving source_id nor a non-cited tag"
        )
        if tag == "cited":
            assert has_source, f"{rel} row {i}: tag=cited but source_id missing/unknown"


@pytest.mark.parametrize("rel", TABLES)
def test_source_ids_resolve(rel: str):
    df = _load(rel)
    ref_ids = _reference_ids()
    for i, row in df.iterrows():
        sid = row["source_id"].strip()
        if sid:
            assert sid in ref_ids, f"{rel} row {i}: unknown source_id {sid!r}"


@pytest.mark.parametrize("rel", TABLES)
def test_units_in_vocabulary(rel: str):
    df = _load(rel)
    for i, row in df.iterrows():
        unit = row["unit"].strip()
        if not unit:
            continue  # qualitative row, no unit
        assert unit in KNOWN_UNITS, f"{rel} row {i}: unknown unit {unit!r}"


def test_cost_stack_reconciles():
    """Per-scenario component costs sum to the documented TOTAL row."""
    df = _load("costs/lh2-cost-stack.csv")
    stack = df[(df["parameter"] == "supply_cost") & (df["value"] != "")].copy()
    stack["value"] = stack["value"].astype(float)
    for scenario, group in stack.groupby("basis"):
        components = group[group["component"] != "TOTAL"]["value"].sum()
        total_rows = group[group["component"] == "TOTAL"]["value"]
        assert len(total_rows) == 1, f"{scenario}: expected one TOTAL row"
        total = total_rows.iloc[0]
        assert isclose(components, total, abs_tol=0.05), (
            f"{scenario}: components {components} != TOTAL {total}"
        )
