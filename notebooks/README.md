# Notebooks

Scenario runs and ad-hoc analysis. Notebooks **consume** the library and data —
they should not redefine models or hardcode unsourced numbers.

## Setup

```bash
pip install -e ".[dev]"   # installs lh2 + jupyter
jupyter lab               # or: jupyter notebook
```

## Rules

- Import models from `lh2.*`; import units from `lh2.units` (never a new
  `pint` registry).
- Pull figures from `data/`; every number cited or tagged (`CLAUDE.md` §4).
- Name notebooks by purpose, e.g. `liquefaction-sec-sensitivity.ipynb`.
- Clear large outputs before committing (`.ipynb_checkpoints` is gitignored).
