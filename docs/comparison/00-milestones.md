# OKR — LH2 vs Ammonia Value-Chain Comparison · Milestone Plan

> **Status: ACTIVE (M0 in progress)** · Owner: LH2 Value Chain team · Created 2026-06-29
> Source of truth for sequencing, scope, and acceptance criteria. All numbers
> cited or tagged per [`CLAUDE.md`](../../CLAUDE.md) §4.

---

## Objective

Compare the **H2 liquefaction (LH2) value chain** with the **ammonia (NH3)
value chain** for long-distance hydrogen supply, to support a go/no-go and
carrier-selection decision.

## Key Results

| KR | Description | Primary deliverable |
|----|-------------|---------------------|
| **1.1** | First version of a techno-economic database for key LH2 components | Populated, cited `data/` tables (LH2 first) |
| **1.2** | Expand the shipping model to include LH2 as a transport vector | Functional-requirements spec for the (Excel) model team |
| **1.3** | High-level long-distance LH2-vs-NH3 supply-chain comparison | Comparison memo: economics, BOG, speed, complexity, end-to-end energy |

## Timeline

- **Hard deadline:** end of Q4 2026.
- **Stretch target:** mid-to-end Q3 2026 (≈ Aug–Sep), i.e. ~6–10 weeks from now.
- Today: **2026-06-29** (end Q2).

---

## Locked decisions (from kickoff)

| # | Decision | Choice | Consequence |
|---|----------|--------|-------------|
| D1 | KR1.3 reference basis | **Generic now, corridor later** | Build on Kawasaki/IAE Base (2.5B Nm³/y) & Large (10B Nm³/y); re-run on a named Gentari corridor once distance + annual volume are given. |
| D2 | KR1.2 target platform | **Excel / spreadsheet** | Functional requirements written as input/output tables, parameter lists, and formulas an existing spreadsheet ammonia model can absorb. |
| D3 | KR1.1 scope | **LH2 only first** | Build the LH2 component database first; NH3 columns added in a later pass for KR1.3. |
| D4 | NH3 data source | **User-provided internal dataset** | NH3 techno-economics await an internal Gentari dataset (to land in `sources/raw/`). Until then, only Kawasaki/IAE NH3 figures are used, gaps tagged `[needs source]`. No external NH3 data pulled without explicit permission. |

**Data policy:** Develop from in-repo data first (Kawasaki, proprietary tier).
Any external/public source requires the user's explicit permission before use
(`CLAUDE.md` §4 / D4).

---

## Milestones

Work is broken into **work packages (WPs)**. Each WP has an ID, an output
artifact, its source/dependency, and a status. Status legend:
`✅ done` · `🟡 doing` · `⬜ todo` · `🔒 blocked` (waiting on a user input).

---

### M0 — Foundations  *(Week 1 — in progress)*

Goal: everything needed to start building is in place and agreed.

| ID | Task | Output artifact | Source · depends on | Status |
|----|------|-----------------|---------------------|--------|
| M0.1 | Register Kawasaki source files | rows in `data/references.csv` | sources/raw | ✅ |
| M0.2 | Lock kickoff decisions D1–D4 | "Locked decisions" table | kickoff | ✅ |
| M0.3 | This milestone plan + OKR file | `00-milestones.md`, `docs/okr.md` | — | ✅ |
| M0.4 | Define KR1.1 DB schema (columns, units, id-link rule) for `costs/`, `vessels/`, `properties/` | `data/README.md` (data dictionary) | conventions.md | ⬜ |
| M0.5 | User approval of plan | sign-off | **user** | 🔒 |

**Exit criteria:** sources registered, schema documented, plan approved.

---

### M1 — KR1.1: LH2 techno-economic database v1  *(Weeks 2–4)*

Goal: every key LH2 component cost/energy/performance figure is pullable from
`data/` with a traceable source. Built segment by segment from Kawasaki data.

| ID | Task | Output artifact | Source · depends on | Status |
|----|------|-----------------|---------------------|--------|
| M1.1 | **Liquefaction** params: SEC 8–9 kWh/kg & 0.55 kWh/Nm³, unit capacity 115 t/d, min economical scale ~10 000 tpa, H2 Claude + N₂ precool, Fe-based O–P catalyst, no degradation | `data/properties/liquefaction.csv` | `kawasaki-2026-questionnaire`, `-supplemental` · M0.4 | ⬜ |
| M1.2 | **Export/loading terminal**: BOR 0.1 %/d, 64 000 m³/tank ×3–4, dead-volume (≈ LNG, NPSHr-driven), downstream BOG reliquefaction | `data/properties/terminals.csv` | `kawasaki-2026-supplemental`, `-questionnaire` | ⬜ |
| M1.3 | **Shipping** specs: 160 000 m³ @ 29.6 km/h (16 kn), 40 000 m³ (building), Suiso Frontier 1 250 m³, BOG-as-fuel = BOR, no onboard reliquefaction, load/unload 1–1.5 d | `data/vessels/lh2-carriers.csv` | `kawasaki-2026-supplemental`, `-questionnaire` | ⬜ |
| M1.4 | **Receiving terminal + regas**: BOR 0.1 %/d, ORV/seawater, heat duty 3.8 MJ/kg-LH2 | `data/properties/regas.csv` | `kawasaki-2026-questionnaire` | ⬜ |
| M1.5 | **Cost stack table**: IAE per-component USD breakdown, LH2 Base / Large / Tech (liquefier, loading, transport, receiving, regas) | `data/costs/lh2-cost-stack.csv` | `kawasaki-2026-supplemental` → `iae-2019-gigaton` | ⬜ |
| M1.6 | **LH2 physical properties**: NBP ≈ 20.3 K, ρ ≈ 70.8 kg/m³, LHV/HHV — each cited | `data/properties/lh2-properties.csv` | conventions.md + cited refs | ⬜ |
| M1.7 | **Data dictionary**: column defs, units, cost-year, id-link rule | `data/README.md` | M0.4 | ⬜ |
| M1.8 | **Validation**: smoke test loads every table; assert no untagged numbers; cost-stack components reconcile to totals | `tests/test_data_tables.py` | M1.1–M1.6 | ⬜ |

**Exit criteria:** all tables populated and cited, data dictionary written, smoke
test green; an analyst can trace every figure to a `references.csv` id.
**⚠ Gaps flagged now:** liquefaction/regas CapEx & OpEx in USD/kg are
**not** disclosed by KHI ("Feasibility Study necessary") → carried as
`[needs source]`; the IAE cost stack (M1.5) is the only quantitative cost basis.

---

### M2 — KR1.2: LH2 shipping functional-requirements spec  *(Weeks 3–5)*

Goal: a spec the (Excel) model team can implement to add LH2 to the existing
ammonia shipping model — runs in parallel with M1.

| ID | Task | Output artifact | Source · depends on | Status |
|----|------|-----------------|---------------------|--------|
| M2.1 | Capture existing **ammonia model I/O structure** (tabs, inputs, outputs, formula style) to mirror | notes section in spec | **user** (model/structure) | 🔒 |
| M2.2 | Define **inputs**: cargo size, route distance, speed, BOR, fuel logic, port/turnaround times, fleet & availability params, vessel CapEx/charter | spec §Inputs | M1.3 | ⬜ |
| M2.3 | Define **calculation logic / formulas**: voyage time, laden+ballast BOG, BOG-as-fuel consumption (fuel = BOR), shortfall fuel (MGO), in-transit losses, fleet sizing, annual delivered kg | spec §Logic | `kawasaki-2026-questionnaire` | ⬜ |
| M2.4 | Define **outputs**: shipping $/kg delivered, fleet count, boil-off loss %, energy/voyage, CO₂ | spec §Outputs | M2.3 | ⬜ |
| M2.5 | **LH2-vs-NH3 modelling deltas** the spreadsheet must add: no onboard reliquefaction, cryogenic BOR regime, density/volumetric basis, dual-fuel BOG engine, KHI "no H2 loss" treatment | spec §LH2-vs-NH3 deltas | `kawasaki-2026-*` | ⬜ |
| M2.6 | **Worked example / validation case** with a sample voyage for the team to check against | spec §Worked example | M2.2–M2.4 | ⬜ |
| M2.7 | **Handover review** with model team; incorporate feedback | reviewed spec v1 | **user / model team** | ⬜ |

**Exit criteria:** model team can implement LH2 from
`docs/comparison/lh2-shipping-functional-requirements.md` without further
clarification; spec reviewed against Kawasaki answers and signed off.

---

### M3 — KR1.3: LH2-vs-NH3 comparison  *(Weeks 5–8)*

Goal: a sourced, range-aware comparison memo with a go/no-go read. LH2 side is
pre-built to de-risk; NH3 side unlocks when the internal dataset lands.

| ID | Task | Output artifact | Source · depends on | Status |
|----|------|-----------------|---------------------|--------|
| M3.1 | **LH2 chain cost stack → LCOH** ($/kg delivered) on generic basis | memo §Economics, `data/costs/` | M1.5, `economics.lcoh` | ⬜ |
| M3.2 | **NH3 chain cost stack → LCOH** (incl. cracking/reconversion) | memo §Economics | **user NH3 dataset (D4)** | 🔒 |
| M3.3 | **BOG / boil-off** comparison across chain (terminal + voyage) | memo §BOG | M1, NH3 data | ⬜ |
| M3.4 | **Speed / voyage time** on existing vessels (LH2 16 kn vs NH3 carrier) | memo §Speed | M1.3, NH3 data | ⬜ |
| M3.5 | **End-to-end energy** consumption (liquefaction vs synthesis+cracking, regas) | memo §Energy | M1.1/1.4, NH3 data | ⬜ |
| M3.6 | **Complexity / TRL + safety / permitting** (toxicity, separation distances, loading-arm TRL 6–7) | memo §Complexity | `kawasaki-2026-questionnaire`, `-comparison` | ⬜ |
| M3.7 | **Sensitivities** on dominant drivers (scale, distance, energy price) | memo §Sensitivity | M3.1–M3.2 | ⬜ |
| M3.8 | **Corridor re-run** (D1) once origin→destination, distance, volume given | memo addendum | **user corridor inputs (D1)** | 🔒 |
| M3.9 | **Memo write-up + go/no-go** (boundary, units, cost-year, assumptions up front; Sources list) | `docs/comparison/lh2-vs-nh3.md` | M3.1–M3.7 | ⬜ |

**Exit criteria:** memo presents a sourced, range-aware go/no-go read on the
generic basis; corridor addendum delivered once D1 inputs arrive.

---

## Critical path & dependencies

```
M0 ──> M1 (LH2 DB) ─────────────┐
   └─> M2 (KR1.2 spec) ─────────┤
                                 ├─> M3 (KR1.3 comparison)
   NH3 internal dataset (D4) ────┘
   corridor inputs (D1) ────────> M3 corridor re-run
```

- **M1 and M2 run in parallel** — neither blocks the other.
- **M3 is gated on the NH3 dataset (D4).** Earliest risk to the stretch target
  is late arrival of NH3 data; LH2-side of M3 can be pre-built to de-risk.

## Open inputs needed from user

1. **NH3 internal techno-economic dataset** → drop in `sources/raw/` (D4). Blocks M3 NH3 side.
2. **Named corridor** for D1 re-run: origin → destination, distance, annual volume.
3. **Existing ammonia spreadsheet model** (or its I/O structure) to mirror in the M2 spec.
4. Confirmation of this milestone plan.

---

## Source inventory (in-repo, proprietary tier)

| Ref id | What it gives us |
|--------|------------------|
| `kawasaki-2026-supplemental` | Per-component cost stacks + chain specs, LH2/MCH/NH3, Base & Large |
| `kawasaki-2026-questionnaire` | SEC, regas duty, BOG/fuel logic, vessel scale-up, no-loss claim |
| `kawasaki-2026-comparison` | Qualitative carrier comparison, energy/CO2 deltas, NH3-fuel constraints |
| `kawasaki-hydrogen-activities` | KHI value-chain overview (vessels, terminals) |
| `iae-2019-gigaton` | Origin of the LH2/MCH/NH3 cost comparison (second-hand via KHI) |
