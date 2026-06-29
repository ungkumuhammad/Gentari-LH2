# Gentari-LH2 — Liquid Hydrogen Value Chain AI Agent

An AI agent and modeling toolkit for the **full liquid hydrogen (LH2) value
chain** — production → liquefaction → storage → shipping → regasification →
distribution & end-use — supporting techno-economic modeling, business-case
analysis, an engineering knowledge base, and report generation.

The agent's operating charter is [`CLAUDE.md`](CLAUDE.md). **Read it first.**

## The one rule that matters most

**No fabricated numbers.** Every quantitative claim is either cited
inline `(Source, Year)` — resolving to a row in
[`data/references.csv`](data/references.csv) — or explicitly tagged
`[ASSUMPTION]` / `[ESTIMATE – needs source]`. See `CLAUDE.md` §4.

## Conventions

SI / metric + USD (cost-year tagged); H2 by kg; units enforced in code via
`pint`. Details in [`docs/conventions.md`](docs/conventions.md).

## Layout

```
CLAUDE.md       Agent charter (read first)
docs/           Conventions, glossary, per-segment methodology (01–06)
data/           references.csv registry + properties / costs / vessels (cited)
sources/raw/    Drop zone for uploaded company/technology source files
src/lh2/        Python modeling library (one module per chain segment)
notebooks/      Scenario runs & analysis
tests/          Smoke + model tests
```

## Quick start

```bash
pip install -e ".[dev]"
pytest -q
python -c "from lh2.units import Q_; print(Q_(9,'kWh/kg')*Q_(1000,'kg'))"
```

## Status

Skeleton stage. CLAUDE.md, conventions, structure, and the shared unit registry
are in place; segment models and data files are stubs to be filled as source
material is uploaded.
