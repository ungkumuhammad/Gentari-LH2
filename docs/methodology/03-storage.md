# Methodology — [3] Storage

> **Status: v1 implemented** in `src/lh2/storage.py` (2026-07-20), driven by
> KHI's disclosed figures. All numbers cited or tagged (`CLAUDE.md` §4).

## System boundary
LH2 into tank ↔ LH2 out (at-rest storage, terminal or onboard pre-loading).

## Physics
- Heat ingress → boil-off (BOR, %/day) as a function of tank size, insulation,
  and surface-to-volume ratio. Modeled as compounding daily loss of the
  *remaining* inventory in `boil_off_at_rest()` (standard boil-off convention).
- KHI states this BOG is re-liquefied at both terminals (reply Q3/Q14), so it
  is a recycle-energy cost, not necessarily a net mass loss.

## Key parameters (sourced from KHI, see `src/lh2/storage.py`)
- BOR at rest: **0.1 %/day**, both export and import terminals
  (`KHI_BOR_AT_REST_PCT_PER_DAY`, kawasaki-2026-supplemental).
- Export tank size: **64,000 m³/tank**; import: **65,000 m³/tank**.
- CapEx ($/m³ or $/kg capacity): `[needs source]` — not separately disclosed
  by KHI; only the aggregate IAE cost stack exists.

## Outputs
Boil-off losses (`boil_off_at_rest()`). Storage cost ($/kg-throughput) is
**not** computable from KHI data alone — see the disclosure-gap register in
`docs/reports/khi-lh2-solution-database.md` §9.

## Open questions / TODO
- Terminal storage sizing basis (days of cover) is project-specific — no KHI
  default; supply `export_hold_days`/`import_hold_days` at the call site.
