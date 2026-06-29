# Conventions

Authoritative reference for units, currency, naming, and citation format used
across this repository. `CLAUDE.md` links here; do not duplicate these rules
elsewhere — point to this file.

## Units (SI / metric)

| Quantity | Unit | Notes |
|----------|------|-------|
| Mass of H2 | kg | Primary basis for all H2 quantities; tonnes (t) for bulk |
| Energy | kWh, MJ | 1 kWh = 3.6 MJ; show both where helpful |
| Power | MW | kW for small equipment |
| Pressure | bar | bar(a) absolute unless noted bar(g) gauge |
| Temperature | K | LH2 normal boiling point ≈ 20.3 K |
| Volume | m³ | LH2 density ≈ 70.8 kg/m³ at NBP (cite when used) |
| Specific energy consumption (SEC) | kWh/kg | Liquefaction, etc. |
| Boil-off rate (BOR) | %/day | Of inventory, per day |
| Carbon intensity | kg CO₂e/kg H2 | State scope/boundary |

- **Never strip units.** In prose, attach units to every figure. In code, use
  the shared `pint` registry (`src/lh2/units.py`) — see below.
- Show conversions explicitly (e.g. `6 kWh/kg = 21.6 MJ/kg`).

## Currency

- Report costs in **USD**, always with the **cost year** tagged: `USD2024`.
- When escalating/deflating across years, state the index used (e.g. CEPCI for
  CapEx, CPI for OpEx) and cite it.
- Commercial outputs expressed **per kg H2**. For energy-market comparison,
  also give **per GJ** and/or **per MMBtu** delivered
  (H2 LHV ≈ 120 MJ/kg, HHV ≈ 142 MJ/kg — cite when used).

## Citation format

Every number is **cited** or **tagged** (see `CLAUDE.md` §4):

- **Inline citation:** `value unit (Source, Year)` →
  `SEC ≈ 6–12 kWh/kg (IEA, 2019)`. The `Source, Year` must resolve to a row in
  [`../data/references.csv`](../data/references.csv).
- **Assumption:** `[ASSUMPTION: 8% discount rate — corporate WACC placeholder]`
- **Estimate needing a source:** `[ESTIMATE – needs source: ~1.5 kWh/kg regas]`

### references.csv schema

| Column | Meaning |
|--------|---------|
| `id` | Short stable key, e.g. `iea-2019-foh` |
| `citation` | Human-readable citation |
| `year` | Publication year |
| `tier` | `proprietary` \| `oem` \| `institutional` \| `first-principles` |
| `url_or_file` | URL, or path under `sources/raw/` |
| `notes` | What it's used for |

In code, reference an id in a comment next to any default:
`SEC_DEFAULT = 9.0  # kWh/kg, ref: iea-2019-foh`.

## Naming

- Files: lowercase, hyphen-separated (`lh2-carrier-specs.csv`).
- Reference ids: `<source>-<year>-<slug>` (`kawasaki-2022-suiso`).
- Python: modules per value-chain segment; `snake_case` functions/vars.

## Code: units via `pint`

Import the shared registry — never instantiate your own:

```python
from lh2.units import ureg, Q_
sec = Q_(9.0, "kWh/kg")          # ref: <references.csv id>
energy = sec * Q_(1000, "kg")    # -> 9000 kWh, units carried automatically
```
