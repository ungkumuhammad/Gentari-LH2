# Methodology — [2] Liquefaction

> **Status: v1 implemented** in `src/lh2/liquefaction.py` (2026-07-20), driven
> by KHI's disclosed figures. All numbers cited or tagged (`CLAUDE.md` §4).

## System boundary
Gaseous H2 in → LH2 at ~20 K, ~1 bar, out.

## Physics
- Cooling from ambient to ~20.3 K (NBP); minimum (ideal) work and real SEC.
- Ortho→para conversion (exothermic) managed with catalyst to limit storage
  self-boil-off.
- Exergy efficiency benchmark vs ideal work.

## Key parameters (sourced from KHI, see `src/lh2/liquefaction.py`)
- SEC: **8–9 kWh/kg** (KHI questionnaire reply Q1); midpoint 8.5 used as
  `KHI_SEC_MID` `[ASSUMPTION]` when a single point is needed.
- Train capacity: **115 t/d** (`KHI_TRAIN_CAPACITY`); train count derived via
  `train_count()` using a utilization factor (`0.78`) `[ASSUMPTION: derived]`
  from KHI's own Base/Large train-count disclosures (see code comment).
- Exergy/2nd-law efficiency (%): `[needs source]` — not disclosed by KHI.
- CapEx vs capacity (tpd), OpEx, carbon intensity: `[GAP — not disclosed]`
  (KHI reply Q8/Q9/Q11: "Feasibility Study necessary").
- Plant availability / turndown: not separately disclosed; folded into the
  derived utilization factor above.

## Outputs
Liquefaction energy use (`liquefaction_energy()`), train sizing
(`train_count()`). Liquefaction cost ($/kg) is **not** computable from KHI
data alone — see the disclosure-gap register in
`docs/reports/khi-lh2-solution-database.md` §9.

## Open questions / TODO
- CapEx/OpEx per USD/kg — awaiting a Feasibility Study or permitted external
  benchmark.
