# Agent Memory

> Running log of decisions, learned context, user preferences, and open items.
> Updated every session. `CLAUDE.md` points here — read this at the start of
> any session where the user references prior work or continuing a task.
>
> Last updated: 2026-07-20

---

## Project identity

- **Repo:** `ungkumuhammad/Gentari-LH2`
- **User:** ungkumuhammad.work@gmail.com (Gentari / PETRONAS group)
- **Working branch:** `claude/h2-ammonia-value-chain-nwh8ls`
- **Context:** Gentari is developing low-carbon H2/NH3 supply projects in Malaysia,
  India (Kakinada green NH3 FID COD 2028, Tamil Nadu FEED-ready COD 2030),
  and Canada (blue NH3, target COD 2031). LH2 offtake interest exists but
  volume is still uncertain. METI/JOGMEC support active for Terengganu, Malaysia.

---

## Active OKR

See [`okr.md`](okr.md) for the full objective + KRs.
Short version:

| KR | Description | Status |
|----|-------------|--------|
| KR1.1 | LH2 techno-economic database v1 | 🟢 v1 built (M1.1–M1.8 ✅); pending NIST citation for physical props |
| KR1.2 | LH2 shipping functional-requirements spec (for Excel model team) | 🟡 In progress (M2) |
| KR1.3 | LH2-vs-NH3 long-distance supply-chain comparison | ⬜ Not started (M3) |

Hard deadline: **Q4 2026**. Stretch: **mid/end Q3 2026**.

---

## Locked decisions (D1–D4)

| # | Decision | Chosen |
|---|----------|--------|
| D1 | KR1.3 reference basis | Generic Kawasaki/IAE basis now (Base 2.5B Nm³/y, Large 10B Nm³/y); re-run on a named corridor once user provides origin → destination, distance, volume |
| D2 | KR1.2 target platform | **Excel / spreadsheet** — existing ammonia model is spreadsheet-based; LH2 spec must mirror it |
| D3 | KR1.1 scope | **LH2 only first**; NH3 columns added later for KR1.3 |
| D4 | NH3 data source | **User-provided internal dataset** (to land in `sources/raw/`); until then only Kawasaki/IAE NH3 figures used; no external NH3 data without explicit permission |

**Data policy (standing):** develop from in-repo Kawasaki data first. Any external
public source needs the user's explicit permission before use.

---

## Key technical facts extracted from Kawasaki data

All sourced; ref ids trace to `data/references.csv`.

### Liquefaction (ref: kawasaki-2026-questionnaire)
- SEC ≈ **8–9 kWh/kg-H2** (varies with scale and boundary conditions)
- Power consumption in KHI fleet assumption: **0.55 kWh/Nm³** (supplemental)
- Cycle: **H2 Claude cycle + N₂ precooling** (proven); hydrocarbon MR precooling under study
- O–P conversion: **Fe-based catalyst** inside liquefier; Co-based under eval; no expected degradation, no replacement needed
- Min economical scale: **~10 000 tpa** (subject to offtake pricing)
- KHI claim: **no H2 losses** across the chain (no losses in plant concept under consideration)
- Significant SEC improvement expected **2035–2040** (scale-up + new subcomponents)
- BOG downstream of liquefier: **re-liquefied** (ejector in liquefier or compressor with cryo-rated suction)
- CapEx/OpEx in $/kg: **not disclosed** ("Feasibility Study necessary") — critical gap

### Loading/export terminal (ref: kawasaki-2026-supplemental)
- BOR at rest: **0.1 %/day**
- Tank size: **64 000 m³/tank**, 3–4 tanks (Base/Large)
- Dead volume: **similar to LNG** (NPSHr-driven); spherical tank + pressurised send-out eliminates pump heel

### Shipping / vessels (ref: kawasaki-2026-supplemental, -questionnaire)
- **Commercial target vessel:** 160 000 m³ @ 29.6 km/h (≈ 16 knots)
- **Under construction (40 000 m³):** same tank tech as Suiso Frontier, no major issues flagged
- **Demo vessel (Suiso Frontier):** 1 250 m³
- **BOG management:** BOG used as propulsion fuel via dual-fuel (DF) engine (KHI in development); fuel consumption rate = BOR; **no onboard reliquefaction** (too much energy + space)
- Sloshing: **no filling-ratio restrictions**; no impact on BOG from sloshing
- Max sailing distance: **limited only by MGO fuel tank** (not BOG)
- MGO-only regime: tank pressure manageable within MARVS for several days; GCU burns excess BOG if pressure exceeds MARVS
- Loading/unloading duration: **~1–1.5 days** per vessel call
- Shipyard: **KHI Sakaide Shipyard**; longer lead time than LNG carriers (complex double-wall tanks + piping)
- Scale-up challenge to 160 000 m³: **cargo tank manufacturability**
- CapEx vs LNG: **significantly higher** (double-wall tanks + piping, limited suppliers) — no $/vessel number disclosed
- Loading arm TRL: 6-inch arm TRL 6–7 (Frontier demo completed); 16-inch arm **not yet verified** (~3 years); both by TBG
- FuelEU compliance: needs higher H2 fuel proportion + green H2; SOx ✓ (H2/MGO); NOx Tier 3 needs SCR

### Receiving terminal + regas (ref: kawasaki-2026-questionnaire, -supplemental)
- BOR at rest: **0.1 %/day**
- Tank size: **65 000 m³/tank**, 3–11 tanks (Base/Large)
- Vaporiser: **ORV (open-rack, seawater)**; dedicated heat source if cold-seawater discharge constrained
- Regas heat duty: **~3.8 MJ/kg-LH2**
- FSU / ship-to-ship: not yet specifically considered (too few LH2 carriers); technology considered applicable in principle

### Cost stacks — IAE basis (ref: kawasaki-2026-supplemental → iae-2019-gigaton)
Source: IAE Gigaton WS, WHTC 2019. Values are component-level cost estimates,
cost-year **not explicitly stated** in KHI presentation (2019 vintage, likely
USD2019) — **tag any use with cost-year caveat and [needs source: primary]**.

| Component | LH2 Base | LH2 Large | NH3 Base | NH3 Large |
|-----------|----------|-----------|----------|-----------|
| Production (H2/NH3 synthesis equiv.) | 10.1 | 10.1 | 10.9 | 10.9 |
| Liquefaction / Synthesis | 10.3 | 10.0 | 10.3 | 9.6 |
| Loading terminal | 5.6 | 1.9 | 0.4 | 0.2 |
| Seaborne transport | 4.0 | 4.0 | 3.2 | 3.2 |
| Receiving terminal | 6.3 | 3.4 | 1.3 | 1.0 |
| Cracking / dehydrogenation | 0.0 | 0.0 | 8.9 | 8.6 |
| Other / distribution | 1.3 | 1.3 | 1.3 | 1.3 |

Units inferred as JPY/Nm³ or relative cost unit — **verify unit before using**.
Primary IAE source not held in repo; figures are second-hand via KHI.

### LH2-vs-NH3 qualitative (ref: kawasaki-2026-comparison, -questionnaire)
- LH2: no toxicity, no conversion steps at destination; requires extreme
  refrigeration + high electrical power; **larger safety exclusion zones** (flammable HP gas)
- NH3: toxic, needs hazard abatement (water spray, gas detectors, evacuation zones)
  at receiving terminal; additional cracking + purification steps
- KHI position: "LH2 is not as lacking in competitiveness nor as challenging
  as often assumed" — evaluates as viable for earlier introduction than commonly perceived

---

## Milestone status snapshot

Full detail in [`comparison/00-milestones.md`](comparison/00-milestones.md).

| WP | Description | Status |
|----|-------------|--------|
| M0.1–M0.3 | Sources registered, decisions locked, plan + OKR written | ✅ |
| M0.4 | DB schema / data dictionary | ✅ (`data/README.md`) |
| M0.5 | User approval of plan | ✅ (KR1.1 build plan approved) |
| M1.1–M1.8 | LH2 techno-economic database | ✅ (CSV tables + xlsx + tests, 27 passing) |
| M2.1 | Capture ammonia model I/O (need user to share) | 🔒 |
| M2.2–M2.7 | LH2 shipping spec | ⬜ |
| M3.2 | NH3 LCOH (need internal NH3 dataset) | 🔒 |
| M3.8 | Corridor re-run (need origin/destination/volume) | 🔒 |
| M3.1, M3.3–M3.9 | LH2-vs-NH3 comparison (LH2 side pre-buildable) | ⬜ |

---

## Open inputs still needed from user

1. **NH3 internal techno-economic dataset** → drop in `sources/raw/`. Unlocks M3.2 and the full KR1.3 comparison.
2. **Existing ammonia spreadsheet model** (or I/O tab structure). Unlocks M2.1 and the rest of the KR1.2 spec.
3. **Named corridor** for D1 re-run: origin → destination, distance (km), annual volume (tpa or Nm³/y). Unlocks M3.8.
4. **Physical-property citation approval (KR1.1):** OK to add NIST/CODATA/ISO as a
   reference so `data/properties/lh2-properties.csv` rows (NBP, density, LHV/HHV,
   gas density) become `cited` instead of `needs-source`? Currently tagged off
   `conventions.md` pending approval.
5. **IAE primary source (KR1.1):** the cost stack (`data/costs/lh2-cost-stack.csv`)
   is second-hand via KHI with an **unlabelled axis** — stored as `JPY/Nm³ ~2019`
   with `[needs source: primary]`. Verify unit/cost-year before any USD/kg LCOH use.

---

## User working preferences (learned this session)

- Prefers questions upfront before building (decision-first workflow).
- Wants milestones granularized to work-package level with status tracking.
- Wants deliverables in both Markdown (source of truth) and Excel (shareability).
- Stretch target is more important than the hard deadline — push for Q3.
- Data discipline: external data needs explicit permission; work from Kawasaki first.

---

## Files created / modified this session

| File | Action | Purpose |
|------|--------|---------|
| `data/references.csv` | Created (5 source rows + 1 IAE row) | Source registry for Kawasaki files |
| `docs/okr.md` | Created | Active OKR — pointer for alignment |
| `docs/comparison/00-milestones.md` | Created | Granular milestone plan (M0–M3, 28 WPs) |
| `docs/comparison/milestones.xlsx` | Created | One-sheet Excel export of all WPs |
| `docs/memory.md` | Created | This file |
| `CLAUDE.md` | Updated | Added OKR callout, repo map entries for okr.md / comparison/ / memory.md |

### KR1.1 build session (2026-06-29)

| File | Action | Purpose |
|------|--------|---------|
| `data/properties/liquefaction.csv` | Created | M1.1 liquefaction params (SEC, cycle, O–P catalyst, gaps) |
| `data/properties/terminals.csv` | Created | M1.2 loading/export terminal (BOR, tanks, loading arm) |
| `data/vessels/lh2-carriers.csv` | Created | M1.3 carrier specs (160k m³, BOG-as-fuel, fleet) |
| `data/properties/regas.csv` | Created | M1.4 receiving terminal + regas (ORV, 3.8 MJ/kg) |
| `data/properties/lh2-properties.csv` | Created | M1.6 physical constants (tagged needs-source) |
| `data/costs/lh2-cost-stack.csv` | Created | M1.5 IAE per-component stack (native JPY/Nm³) + gap rows |
| `data/README.md` | Created | M1.7/M0.4 data dictionary (tidy schema, tag rules) |
| `scripts/build_db_workbook.py` | Created | Re-runnable CSV→xlsx mirror builder |
| `data/lh2-database.xlsx` | Generated | One-workbook Excel mirror of all tables |
| `tests/test_data_tables.py` | Created | M1.8 validation (no untagged numbers, ids resolve, cost reconciles) |
| `pyproject.toml` | Updated | Added `openpyxl` dev dependency |
| `docs/comparison/00-milestones.md` | Updated | M0.4, M1.1–M1.8 → ✅ |

### KHI database report + project scenario calculator (2026-07-20)

User asked for (1) a database built *from* the KHI questionnaire/assessment
(not the raw Q&A) delivered as a PDF, and (2) a modeling tool to calculate
economics for any Gentari project using KHI's solution.

| File | Action | Purpose |
|------|--------|---------|
| `docs/reports/khi-lh2-solution-database.md` | Created | Narrative KHI database: per-segment tables, IAE cost stack, LH2-vs-NH3-vs-MCH position, disclosure-gap register (§9), KHI corporate snapshot, source register |
| `docs/reports/khi-lh2-solution-database.pdf` | Created | PDF render of the above (via markdown → styled HTML → Playwright/Chromium print-to-PDF; no pandoc/weasyprint available in this environment) — delivered to user |
| `src/lh2/liquefaction.py` | Implemented (was stub) | SEC (KHI 8–9 kWh/kg), train sizing (115 t/d trains, utilization factor derived from KHI's own Base/Large train-count data points ≈0.78) |
| `src/lh2/storage.py` | Implemented (was stub) | At-rest boil-off (0.1%/day, compounding), KHI tank sizes |
| `src/lh2/shipping.py` | Implemented (was stub) | Transit/round-trip time, fleet sizing, voyage BOG — **note: KHI never disclosed a standalone voyage BOR figure**, so `voyage_boil_off` has no default and callers must supply a tagged value |
| `src/lh2/regas.py` | Implemented (was stub) | Regas duty (KHI 3.8 MJ/kg) |
| `src/lh2/economics.py` | Implemented (was stub) | NPV/IRR (`numpy_financial`), LCOH |
| `src/lh2/scenario.py` | Created | `ProjectInputs`/`ScenarioResult`/`run_scenario`: full chain calculator for any project (annual tpa + distance → energy/losses/fleet/cost); IAE Base/Large cost stack linearly interpolated to project volume; produces an explicit `gaps` list (CapEx, OpEx, discount rate, voyage BOR, FX rate, carbon intensity) instead of fabricating missing KHI figures |
| `scripts/run_project_model.py` | Created | CLI wrapper around `scenario.run_scenario` |
| `tests/test_scenario.py` | Created | 15 tests: unit consistency, reconciles to KHI's own Base/Large points, "no fabricated numbers" invariant |
| `pyproject.toml` deps | Installed (`pip install -e ".[dev]"`) | `numpy-financial` etc. now actually present in the environment (were declared but not installed) |
| `docs/comparison/00-milestones.md` | Updated | M2.3/M3.1 status notes + new "Additional artifacts" section |

**Known modeling limitation carried forward:** KHI disclosed no standalone
shipping/voyage boil-off rate (only that fuel-gas consumption = BOR, and that
MGO-only sailing holds MARVS "for several days"). The scenario tool treats
voyage BOR as a required user-supplied `[ASSUMPTION]`/`[ESTIMATE]` — it will
not silently assume 0.1%/day (that figure is specifically the *at-rest*
terminal BOR). Likewise CapEx/OpEx/carbon-intensity remain gaps until a
Feasibility Study or a permitted external benchmark supplies them.

### Reliquefaction → shipping → regas block flow diagram (2026-07-20, same session)

User asked for a Block Flow Diagram (HTML) of the reliquefaction process,
starting from electrolyzer GH2 at 30 barg/30°C, through shipping (as its own
detailed block including BOG handling) to regasification.

| File | Action | Purpose |
|------|--------|---------|
| `docs/reports/khi-lh2-reliq-shipping-regas-bfd.html` | Created | Self-contained HTML/SVG block flow diagram: Electrolyzer GH₂ feed (30 barg/30°C, user-specified) → Reliquefaction Plant (N₂ precool → O–P conversion → cryo liquefaction, SEC 8–9 kWh/kg) → Export/Loading Terminal (BOR 0.1%/day, BOG re-liquefied, recycle loop drawn back to the liquefaction inlet) → **Shipping block with its own expanded sub-flow** (cargo tanks → BOG generation [flagged gap — KHI never disclosed a standalone voyage BOR] → split to dual-fuel engine / GCU, explicit "onboard reliquefaction NOT ADOPTED" callout) → Import/Receiving Terminal → Regasification Plant (ORV, 3.8 MJ/kg-LH2) → end-use (out of scope). 22 numbered footnotes tie every label to a KHI reply/source or an explicit `[ASSUMPTION]`/`[GAP]` tag; light/dark theme supported. Published as a Claude Artifact. |

**Layout bug caught and fixed during build:** the first draft used narrow
gaps between blocks for the stream-condition labels (e.g. "LH₂ ~1 bar(a)/
~20.3 K"), so the labels overflowed into the neighboring block and were
partially painted over by that block's fill (SVG paints in document order).
Fixed by widening every inter-block gap (~140px) and moving all stream-label
`<text>` elements to render last in the SVG so they're never occluded.
Verified visually via Playwright screenshots (both themes, full horizontal
scroll) before publishing.
