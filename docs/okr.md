# OKR — Active Objectives & Key Results

> **Read this when the task relates to current priorities.** This file records
> the team's standing OKR so work stays aligned to it. `CLAUDE.md` points here.
> Execution detail (work packages, schedule, acceptance criteria) lives in
> [`comparison/00-milestones.md`](comparison/00-milestones.md).
>
> Last updated: 2026-06-29 · Status: **ACTIVE**

---

## Objective 1 — Compare the H2 liquefaction (LH2) value chain with the ammonia (NH3) value chain

Provide a sourced, decision-grade comparison of LH2 vs NH3 as carriers for
long-distance hydrogen supply, to support carrier selection and go/no-go.

### Key Results

**KR1.1 — Develop the first version of a techno-economic database for key
components of the LH2 value chain.**
- A populated, fully cited set of `data/` tables covering the key LH2 components
  (liquefaction, terminals, shipping, regas): cost, energy, and performance.
- LH2 first (NH3 columns added later for KR1.3). Every figure traceable to a
  `references.csv` id or tagged per `CLAUDE.md` §4.

**KR1.2 — Expand the shipping model to include LH2 as a transport vector.**
- An ammonia shipping model already exists (spreadsheet-based, model team owns it).
- Deliverable is a **functional-requirements specification** the model team can
  implement: inputs, outputs, parameters, and formulas for LH2 shipping, plus
  the LH2-vs-NH3 modelling differences.

**KR1.3 — Conduct a high-level comparison of long-distance LH2 vs NH3 supply chains.**
- Dimensions: **economics (LCOH $/kg delivered), BOG/boil-off, speed based on
  existing vessels, project complexity/TRL, end-to-end energy consumption,**
  and safety/permitting. Range-aware, with sensitivities and a go/no-go read.

---

## Timeline

- **Hard deadline:** end of **Q4 2026**.
- **Stretch target:** mid-to-end **Q3 2026** (≈ Aug–Sep).

## Standing constraints (apply to all KRs)

1. **Develop from in-repo data first.** Primary source is the Kawasaki Heavy
   Industries material in `sources/raw/` (proprietary tier).
2. **External data needs explicit permission.** Do not pull public/external
   sources without the user approving it first (`CLAUDE.md` §4).
3. **NH3 techno-economics come from a user-provided internal dataset** (to be
   dropped into `sources/raw/`). Until then, only Kawasaki/IAE NH3 figures are
   used and gaps are tagged `[needs source]`.
4. **No fabricated numbers** — every quantitative claim cited or tagged.

## Kickoff decisions (D1–D4)

See [`comparison/00-milestones.md`](comparison/00-milestones.md#locked-decisions-from-kickoff)
for the locked decisions on reference basis, model platform, DB scope, and NH3
data, and for the full milestone breakdown (M0–M3).
