# Methodology — Overview

How analyses in this repo are structured. Each segment has its own methodology
file (01–06). All numbers follow the citation rule in `CLAUDE.md` §4 and the
conventions in [`../conventions.md`](../conventions.md).

## Value-chain map

```
[1] Production  →  [2] Liquefaction  →  [3] Storage  →  [4] Shipping
                                                            │
                                                            ▼
        [6] Distribution & End-use  ←  [5] Regasification
```

## System boundaries

State which boundary every analysis uses:

- **Gate-to-gate** — a single segment (e.g. liquefaction only).
- **Well-to-gate** — production through delivery at the import terminal gate.
- **Well-to-wheel** — through to end-use / reconversion.

## Cost stack approach (for LCOH / business cases)

Build cost up segment by segment. Each line item is CapEx-annualized + OpEx +
energy + losses (including boil-off), per kg H2 delivered, every figure cited or
tagged. Carry mass losses through the chain (production volume > delivered
volume because of boil-off and process losses).

## Status

All segment methodology files are **stubs** to be filled as source files are
uploaded and models are built. Replace `[ESTIMATE]`/`[ASSUMPTION]` tags with
cited values over time.
