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

### M0 — Foundations  *(Week 1 — in progress)*
- [x] Register Kawasaki source files in [`data/references.csv`](../references.csv).
- [x] Lock reference basis, platform, scope, NH3 policy (D1–D4 above).
- [ ] Define the KR1.1 database schema (`data/costs/`, `data/vessels/`, `data/properties/`).
- **Done when:** sources registered, schema agreed, this plan approved.

### M1 — KR1.1: LH2 techno-economic database v1  *(Weeks 2–4)*
- [ ] Component cost stack (liquefaction, loading terminal, shipping, receiving
      terminal, regas) extracted from `kawasaki-2026-supplemental` into `data/costs/`.
- [ ] Vessel specs (160 000 m³ @ 29.6 km/h, 40 000 m³, Suiso Frontier 1 250 m³,
      BOR) into `data/vessels/`.
- [ ] Energy & loss parameters (SEC 8–9 kWh/kg, regas 3.8 MJ/kg, BOR 0.1 %/d,
      "no H2 loss" claim) into `data/properties/` / `data/costs/`.
- [ ] Every row carries a `references.csv` id; no untagged numbers.
- **Done when:** an analyst can pull every LH2 component cost/energy figure from
      `data/` with a traceable source, and a smoke test loads the tables.

### M2 — KR1.2: LH2 shipping functional-requirements spec  *(Weeks 3–5)*
- [ ] Spec doc (`docs/comparison/lh2-shipping-functional-requirements.md`)
      defining inputs, outputs, parameters, and formulas for an LH2 shipping
      module mirroring the existing ammonia spreadsheet model.
- [ ] Cover: cargo capacity, voyage BOR, BOG-as-fuel logic (fuel rate = BOR),
      fleet sizing, speed/voyage time, port/turnaround, boil-off management
      (no onboard reliquefaction per KHI), vessel CapEx premium vs LNG.
- [ ] Flag LH2-vs-NH3 modelling differences the spreadsheet team must add.
- **Done when:** the model team can implement LH2 in their spreadsheet from the
      spec without further clarification; reviewed against Kawasaki answers.

### M3 — KR1.3: LH2-vs-NH3 comparison  *(Weeks 5–8)*
- [ ] Chain cost stack per carrier on the generic basis (LCOH $/kg delivered).
- [ ] Comparison dimensions: **economics, BOG/losses, speed (existing vessels),
      end-to-end energy, project complexity/TRL, safety/permitting**.
- [ ] Sensitivities on dominant drivers (scale, distance, energy price).
- [ ] Re-run on a named corridor once D1's corridor inputs are provided.
- **Depends on:** M1 (LH2 data) + NH3 dataset (D4).
- **Done when:** a memo presents a sourced, range-aware go/no-go read with the
      assumptions, units, cost-year, and boundary stated up front.

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
