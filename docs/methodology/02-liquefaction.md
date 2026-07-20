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
- CapEx vs capacity (tpd), OpEx, carbon intensity: `[GAP — not disclosed]`
  (KHI reply Q8/Q9/Q11: "Feasibility Study necessary").
- Plant availability / turndown: not separately disclosed; folded into the
  derived utilization factor above.

## Theoretical minimum work vs KHI's disclosed SEC (2026-07-20)

Ideal (reversible) specific work to liquefy H2, ambient (~300 K/1 atm) gas →
liquid at NBP (~doe-2009-h2-liquefaction-energy):

| Basis | Ideal work | Notes |
|---|---|---|
| Normal-H2 → normal-H2 liquid (no O–P conversion) | **≈3.3 kWh/kg** (11.9 MJ/kg) | textbook minimum-work/exergy baseline |
| Normal-H2 → (near-)para-H2 liquid | **≈3.9 kWh/kg** (14.2 MJ/kg) | fairer basis — KHI's process does O–P conversion (reply Q6/Q7); cross-checked via `hull-2024-orthopara-exergy` (LH2 exergy ≈11.5% of LHV → 33.33 × 0.115 = 3.83 kWh/kg) |

KHI's disclosed **8–9 kWh/kg** (reply Q1) implies a second-law (exergetic)
efficiency of **≈37–41%** against the normal-H2 basis, or **≈43–49%** against
the para-H2 basis — `data/properties/liquefaction.csv` rows
`khi_second_law_efficiency_normal_basis` / `_para_basis`, tagged
`[ASSUMPTION: derived]`. Literature places today's state-of-the-art plants at
roughly 30–40% exergetic efficiency, so KHI's figure sits at or above the top
of that range.

**Caveat (important):** KHI never confirmed the feed **pressure** basis for
its 8–9 kWh/kg figure (Gentari's question specified only "20°C gaseous
hydrogen"). Ideal work is pressure-sensitive — a feed already at elevated
pressure (e.g. this project's 30 barg assumption, §BFD feed condition) carries
more exergy than an atmospheric feed, which *lowers* the correctly-matched
ideal-work baseline and therefore *lowers* KHI's true second-law efficiency
below the figures above. Treat the 37–49% range as an **upper bound**, not a
confirmed value, until KHI's feed-pressure basis is clarified.

## Outputs
Liquefaction energy use (`liquefaction_energy()`), train sizing
(`train_count()`). Liquefaction cost ($/kg) is **not** computable from KHI
data alone — see the disclosure-gap register in
`docs/reports/khi-lh2-solution-database.md` §9.

## Open questions / TODO
- CapEx/OpEx per USD/kg — awaiting a Feasibility Study or permitted external
  benchmark.
