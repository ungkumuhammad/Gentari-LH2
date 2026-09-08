# Agent Memory

> Running log of decisions, learned context, user preferences, and open items.
> Updated every session. `CLAUDE.md` points here — read this at the start of
> any session where the user references prior work or continuing a task.
>
> Last updated: 2026-09-07

---

## Project identity

- **Repo:** `ungkumuhammad/Gentari-LH2`
- **User:** ungkumuhammad.work@gmail.com (Gentari / PETRONAS group)
- **Working branch:** `claude/lh2-ammonia-value-chain-4a1525`
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
| KR1.3 | LH2-vs-NH3 long-distance supply-chain comparison | 🟡 Energy dimension (M3.5) built end-to-end; economics/BOG/speed still open; NH3 values all placeholders (D4) |

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

### Interactive viability calculator added to the BFD (2026-07-20, same session)

User asked for an input tab where they enter total demand volume (KTPA-H2)
and get total energy/etc required for each block, to gauge viability.

| Change | Detail |
|--------|--------|
| Added a 2-tab UI to `docs/reports/khi-lh2-reliq-shipping-regas-bfd.html` | Tab 1 "Inputs" (KTPA-H2 demand + shipping distance as primary fields; an advanced/collapsible section for SEC, vessel speed/capacity, hold times, voyage BOR, CapEx/OpEx/discount rate/project years/FX rate). Tab 2 "Diagram & Results": KPI bar (delivered H2, liquefaction energy, fleet, LCOH), the same static diagram, a 7-card results grid (one per block + an economics card), and a dynamic gaps/caveats list. |
| Client-side JS re-implements `src/lh2/scenario.py`'s math | Train count (115 t/d, 0.78 utilization), liquefaction energy, at-rest BOG (compounding), transit/round-trip days, fleet sizing, voyage BOG (only if a BOR is supplied), regas duty, IAE Base/Large cost-stack interpolation, and LCOH — same constants and formulas as the Python module, so results should stay consistent with the CLI tool. |
| Verified against `scripts/run_project_model.py` | Ran both with identical inputs (300 KTPA, 6000 km, capex 1200/opex 60/discount 8%/voyage BOR 0.2%/fx 150/hold 5+5 days) via Playwright — every number matched the Python output exactly (trains, GWh/y, BOG masses, fleet, LCOH $0.62/kg, cost stack). |
| Bug caught and fixed during build | The regas annual-duty tile was labeled "PJ/y" but the JS divided MJ by 1e6, which is TJ, not PJ (1 PJ = 1e9 MJ). Fixed the label to "TJ/y" to match the actual computed value. |
| Gaps list is now dynamic | Only shows the caveats that actually apply to the current inputs (e.g. the voyage-BOR gap disappears once the user supplies one; the LCOH gap disappears once CapEx/OpEx/discount rate are all filled in). |

### Electrolyzer efficiency + LHV well-to-LH2 energy accounting (2026-07-20, same session)

User asked to add electrolyzer plant efficiency (kWh/kg H2) as an input, and
at the end reference H2's LHV to compute overall energy efficiency/loss —
worked example given: electrolyzer 60 kWh/kg vs LHV 33.33 kWh/kg = 55.55%
efficient/44.45% loss; + reliq 9 kWh/kg = 69 kWh/kg total; final efficiency
vs LHV = 33.33/69 = 48.3%/51.7% loss.

| Change | Detail |
|--------|--------|
| New primary input: "Electrolyzer plant efficiency" (kWh/kg H₂) | Left blank by default (no sourced default exists — production is segment [1], outside KHI's LH2 offer/this diagram's boundary); if blank, the efficiency card and KPI tile show a gap instead of guessing. |
| `H2_LHV_KWH_PER_KG = 120/3.6 = 33.33` | Same LHV figure already in `data/properties/lh2-properties.csv` (120 MJ/kg, tagged needs-source); added as footnote (25) alongside the existing NBP citation (20). |
| Feed card (①) now shows | Electrolyzer input, efficiency vs LHV, loss vs LHV (stage-level). |
| New final results card "⚡ Well-to-LH2 energy efficiency (LHV basis)" | Walks through electrolyzer input + reliq SEC = total input energy, then overall efficiency/loss vs LHV, plus annual GWh figures (total input energy vs. the LHV energy content of the H2 actually delivered). |
| New 5th KPI tile "Well-to-LH2 efficiency" | Headline %, with loss% and total kWh/kg in the subtext; turns to the warn (red-top) state when the electrolyzer input is missing, same pattern as the LCOH tile. |
| Verified against the user's worked example | 60 + 9 = 69 kWh/kg; 55.56%/44.44% (electrolyzer stage) and 48.31%/51.69% (overall) — confirmed via Playwright, matches exactly. |

### Theoretical minimum liquefaction work vs KHI's SEC (2026-07-20, same session)

User asked for the theoretical (first-principles) kWh/kg to liquefy H2 and a
comparison against KHI's disclosed 8-9 kWh/kg. First use of `WebSearch` in
this repo — added two new institutional-tier references since this is a
knowledge question, not project-specific data (`CLAUDE.md` workflow (c)).

| File | Action | Purpose |
|------|--------|---------|
| `data/references.csv` | Added 2 rows | `doe-2009-h2-liquefaction-energy` (DOE H2 Program Record #9013, Gardiner 2009 — ideal work 3.3/3.9 kWh/kg normal/para basis) and `hull-2024-orthopara-exergy` (Int. J. Hydrogen Energy 2024 — cross-check via LH2 exergy ≈11.5% of LHV). Both direct-PDF-fetch attempts returned HTTP 403; figures corroborated across multiple independent search results before citing. |
| `data/properties/liquefaction.csv` | Added 4 rows | `theoretical_min_specific_work_normal` (3.3 kWh/kg, cited), `_para` (3.9 kWh/kg, cited), `khi_second_law_efficiency_normal_basis` (37-41%, ASSUMPTION: derived), `_para_basis` (43-49%, ASSUMPTION: derived) |
| `docs/methodology/02-liquefaction.md` | Added section | "Theoretical minimum work vs KHI's disclosed SEC" — table + the important caveat that KHI never confirmed its feed-pressure basis, so the 37-49% efficiency range is an **upper bound**, not confirmed (a pressurised feed, like this project's 30 barg BFD assumption, would lower the true ideal-work baseline and thus the true efficiency below this range) |
| `data/lh2-database.xlsx` | Regenerated | via `scripts/build_db_workbook.py` after the CSV edits |

**Answer given to user:** ideal/reversible liquefaction work ≈3.3 kWh/kg
(normal-H2) to ≈3.9 kWh/kg (para-H2, the fairer comparison since KHI's
process does O-P conversion) — KHI's 8-9 kWh/kg therefore implies ~37-49%
second-law efficiency, at or above the ~30-40% literature benchmark for
today's state-of-the-art plants, but flagged as an upper bound pending
KHI's feed-pressure confirmation.

### Layman exergy explanation + worked derivation, then BOG comparison (2026-07-20, same session)

Follow-up questions: (1) explain exergy in plain language and show the actual
calculation behind the 3.3 kWh/kg figure; (2) is the BOG re-liquefaction
calculation the same as fresh-feed liquefaction?

- Answered (1) with the coffee-cooling-to-room-temperature analogy, the
  formula `w_ideal = Δh - T0*Δs`, and a full worked two-step calculation
  (sensible cooling, Cp≈11.5 kWh/kg·K illustrative average + condensation,
  L≈445.6 kJ/kg) that reproduces ≈3.39 kWh/kg — added to
  `docs/methodology/02-liquefaction.md` as an explicitly-flagged illustrative
  appendix (not a replacement for the cited DOE figure).
- Answered (2): **no**, BOG is a smaller problem — it's already at ~20.3 K and
  already near-equilibrium para fraction (it boiled off the liquid), so only
  the condensation step applies (no sensible-cooling, no O-P conversion).
  Same formula, condensation-only Δh/Δs → **≈1.71 kWh/kg**, about half of
  fresh-feed liquefaction. Flagged two real-world gaps this excludes: (a) real
  compression work to route low-pressure BOG into the cycle (KHI's
  ejector/compressor, no SEC disclosed), (b) BOG-reliquefaction's real
  exergetic efficiency is unknown (if it matched the main train's ~40-46%,
  real energy would be ≈3.7-4.3 kWh/kg — an extrapolation, not a KHI figure).
- `data/properties/liquefaction.csv`: added
  `theoretical_min_specific_work_bog_reliquefaction` (1.71 kWh/kg, tag
  ASSUMPTION: derived, source_id doe-2009-h2-liquefaction-energy).
  `data/lh2-database.xlsx` regenerated.

### MJ units + storage-days-driven BOG energy in the calculator, then merge to main (2026-07-20, same session)

User asked for three things: (1) show MJ alongside kWh throughout the HTML
calculator (H2 LHV = 120 MJ/kg); (2) let storage days (export/import
terminal hold time) drive BOG mass *and* the energy needed to manage that
BOG, using the fresh-feed-vs-BOG ideal-work ratio derived earlier, added to
the total energy requirement — same treatment for shipping's voyage BOG;
(3) merge everything to `main`.

| Change | Detail |
|--------|--------|
| `docs/reports/khi-lh2-reliq-shipping-regas-bfd.html` | Every kWh/kg value now shows its MJ/kg equivalent (`fmtKwhMj()`); every annual GWh/y total now shows TJ/y (`fmtAnnualEnergy()`), incl. regas duty (previously TJ-only). Export/import terminal "storage days" promoted from the collapsed advanced section to primary inputs, since they now drive a headline output. New `BOG_SEC_RATIO` (≈0.438) scales the user's own reliq SEC by the ratio of BOG's ideal condensation-only work (1.71 kWh/kg) to fresh-feed ideal work (3.9 kWh/kg) — applied to export BOG, import BOG, *and* shipping voyage BOG for a consistent "energy cost of managing boil-off" figure, with an explicit caveat (both inline and in the dynamic gaps list) that KHI's ships actually burn voyage BOG as engine fuel rather than electrically re-liquefying it. New rows: per-block "BOG re-liq energy (derived)" in the Export/Import/Shipping cards, "+ BOG management (all locations)" / "= Total incl. BOG" in the Reliquefaction card, and a "+ BOG management (per kg delivered)" row folded into the Well-to-LH2 efficiency card's total (now `electrolyzer + reliq + BOG`, all expressed per kg *delivered* rather than per kg produced, for full consistency). Added footnote (26). |
| `src/lh2/scenario.py` | Mirrored the same BOG-management-energy math in Python (`BOG_IDEAL_KWH_PER_KG`, `FRESH_IDEAL_PARA_KWH_PER_KG`, `BOG_SEC_RATIO`, new `ScenarioResult` fields `bog_management_sec_kwh_per_kg`, `*_bog_energy_kwh_per_year`, `total_energy_incl_bog_kwh_per_year`), since the tool's own UI text claims to mirror this module — kept the claim true rather than letting it drift. `format_report()` updated to print the new BOG energy lines. |
| Verified | Ran identical inputs (300 KTPA, 6000 km, export/import hold 5 d each, voyage BOR 0.2%) through both the CLI and the HTML calculator via Playwright — BOG energies matched to rounding (export 5.58 GWh/y, import 5.49 GWh/y, shipping 18.75 GWh/y, total 29.81 GWh/y, grand total 2,580 GWh/y in both). Also checked the default (0 hold days) state shows 0 BOG energy cleanly, no spurious gap text, no console errors; checked layout in light/dark and at narrow (420px) width. |
| `git merge` | Branch `claude/khi-kawasaki-questionnaire-db-xj1wnw` merged into `main` and pushed, per explicit user instruction — see git log for the merge commit. |

**Running list of what's now in this repo from this multi-turn session:**
KHI LH2 solution database (report + PDF), a Python project-scenario
calculator (`src/lh2/scenario.py` + CLI), an interactive HTML block-flow
diagram with a full viability calculator (demand volume → per-block energy/
BOG/fleet/cost/LCOH, electrolyzer efficiency → LHV well-to-LH2 efficiency,
storage-days → BOG management energy), and two thermodynamics deep-dives
(theoretical liquefaction work vs KHI's SEC, and BOG re-liquefaction's
smaller ideal-work requirement) folded into `docs/methodology/02-liquefaction.md`
and `data/properties/liquefaction.csv` as cited/tagged database rows.

### "Zane" LH2 research sub-agent + weekly news loop (2026-07-21)

User asked to build a dedicated research sub-agent — a specific folder — to
research LH2 technology from public sources (papers, licensors, news) with a
strict no-fabrication rule, acting as a senior principal H2/NH3 engineer expert
in H2 carriers/derivatives, and with a weekly loop scanning new LH2 news every
Monday 07:00 Malaysia Time. Clarifying questions asked upfront (decision-first,
per user preference).

**Decisions from the user (this session):**

| # | Decision | Chosen |
|---|----------|--------|
| Z1 | Agent name | **"Zane"** |
| Z2 | Research-consent model | Invoking Zane **by name** = standing consent to autonomously use WebSearch/WebFetch on public sources (no per-source approval); the **weekly loop** also has standing consent to run + commit. The no-fabrication cardinal rule is **unchanged** — consent governs *fetching*, never *whether a number needs a source*. Outside Zane, the repo's "ask-first" external-data policy still holds. |
| Z3 | Agent form | **Folder + dispatchable sub-agent + scheduled loop** |
| Z4 | Weekly loop | **LH2-only**, commit a dated digest & push, notify |
| Z5 | Standing research scope | **LH2 only** (Zane's broad carrier expertise — NH3, e-methane, SAF, e-methanol, LOHC — is on-demand only when the user names the carrier) |

**Isolation policy:** Zane's findings stage in `research/sources/staging.csv`
and live in `research/`; promotion into the repo-wide `data/references.csv` /
`data/` tables is a **separate explicit user approval** (keeps the proprietary
Kawasaki DB clean).

| File | Action | Purpose |
|------|--------|---------|
| `research/AGENT.md` | Created | Zane's full charter: persona, research-consent model (§4), inherited no-fabrication rule (§3), workflows (§5), weekly-digest spec (§6), guardrails |
| `research/README.md` | Created | Human-facing overview + how to invoke Zane |
| `research/digests/README.md` | Created | Weekly digest folder index |
| `research/profiles/README.md` | Created | Licensor/technology profile folder index |
| `research/templates/weekly-digest-template.md` | Created | Standard weekly LH2 digest layout |
| `research/sources/staging.csv` | Created | Isolated source registry (header only) |
| `.claude/agents/zane.md` | Created | Dispatchable Claude Code sub-agent definition (tools: Read/Write/Edit/Glob/Grep/Bash/WebSearch/WebFetch) |
| `CLAUDE.md` | Updated | Repo map: added `research/` + `.claude/agents/` and a "dispatch Zane for external LH2 research" pointer |
| `docs/memory.md` | Updated | This entry |

**Scheduled trigger (loop):** created via the claude-code-remote routines API —
id `trig_015meLYXKh1RoNoEswWW94rh`, name "Zane — Weekly LH2 News Digest (Mon
07:00 MYT)", cron `0 23 * * 0` (UTC) = **Monday 07:00 Malaysia Time**,
fresh-session-per-fire, push + email notification on. First run:
2026-07-27 ~07:00 MYT. The fired session reads `research/AGENT.md`, does the LH2
scan, writes `research/digests/YYYY-MM-DD-lh2-weekly.md`, commits to **`main`**
(durable default branch, so digests survive after feature branches merge) and
pushes, listing new figures as "promotion candidates" rather than auto-promoting.

**Open follow-ups / offered:** (1) can run a first seed digest on request to
validate the end-to-end pipeline; (2) can build the first licensor profile
(e.g. `research/profiles/kawasaki.md`, cross-linked to existing repo data) when
the user wants; (3) digest commit-target is `main` — tell Zane if a dedicated
`zane/lh2-weekly-digests` branch is preferred instead.

### Zane in action: first digest, source dossiers, PDF ingestion (2026-07-21, same session)

After building Zane, the user exercised it:

1. **First weekly LH2 digest** (`research/digests/2026-07-21-lh2-weekly.md`) — user
   said "Zane, run this week digest." Quiet week; two firm in-window items (LH2
   Shipping NOK 344.3 M Enova award for two 7,700 dwt LH2-fuelled bulkers; DNV
   July-2026 class-rules edition with gas-fuelled-hydrogen rules, in force
   2027-01-01) + date-tagged adjacent items. **Web-research limitation observed:**
   most news domains (marinelink, Ship&Bunker, DNV, MDPI, etc.) return HTTP 403 to
   WebFetch, and the scholarly APIs (Crossref/OpenAlex) + doi.org are blocked by
   the environment **egress policy** — so Zane worked from corroborated WebSearch
   snippets and flagged it. WebSearch works; WebFetch/curl to non-allowlisted
   hosts do not.

2. **RSER voyage-BOR source dated** — user asked when the ~3.44%/day BOG figure was
   published. Pinned: RSER Vol. 233 (Jun 2026), art. 116850, DOI
   10.1016/j.rser.2026.116850, **online 28 Feb 2026** (i.e. NOT this-week; adjacent
   literature). Corrected the digest + staging.csv.

3. **JMSE dossier** — user asked to build a DB markdown from the open-access JMSE
   review. Created `research/literature/` (new source-dossier folder) +
   `2025-jmse-lng-to-lh2-maritime-review.md`. Full text was egress-blocked at the
   time, so quantitative numbers were deliberately left **unattributed** under a
   "full-text extraction pending" section (no misattribution, no fabrication).

4. **Both PDFs ingested via markitdown** — user uploaded the two paper PDFs and
   asked to convert them with Microsoft `markitdown` and store them in Zane's
   environment. Done:
   - Installed `markitdown[pdf]` 0.1.6 (had to `pip install --force-reinstall cffi`
     first — its C backend `_cffi_backend` was missing, breaking `cryptography`/
     pdfminer).
   - Originals: `research/sources/raw/jmse-2025-lng-to-lh2-maritime-review.pdf`,
     `research/sources/raw/rser-2026-lh2-maritime-transportation.pdf`.
   - Full-text Markdown (with provenance headers):
     `research/literature/jmse-2025-lng-to-lh2-maritime-review.fulltext.md`,
     `research/literature/rser-2026-lh2-maritime-transportation.fulltext.md`.
   - **Authors now confirmed from PDFs:** JMSE = Passalacqua & Traverso (TPG, DIME,
     University of Genova, Italy); RSER = MD. Shajratul Alam Towhid & Sumaiya Binte
     Hossain (BUET / North South University, Dhaka, Bangladesh).
   - Updated the JMSE dossier access note (full text now in-repo) and staging.csv
     rows for both papers (raw + fulltext paths, confirmed authors, verified
     abstract figures for RSER: BOG ~3.44%/day, ~3.74 $/GJ, larger tank diameter
     ~1.8%→~0.2%/day, ballast-warming heat cut 41.6–54.3%, single-node under-
     predicts wall energy up to 60% at ≤5% fill).

5. **Merged all to `main`** per explicit user instruction (see git log merge
   commit) and pushed. The Zane weekly trigger already commits to `main`, so this
   consolidates everything (agent + digests + dossiers + PDFs) onto the trunk.

**➡️ NEXT SESSION (user's stated goal):** build a **comparison table of KHI vs the
two papers** — i.e. KHI's LH2 solution (in-repo proprietary data, esp. shipping/
BOG/tank/materials/economics) vs. Towhid & Hossain (RSER 2026) and Passalacqua &
Traverso (JMSE 2025). Both papers' full text is now in `research/literature/*.fulltext.md`
and `research/sources/raw/`. Key axes to compare (from OKR KR1.3 + these papers):
voyage/at-rest **BOR** (KHI 0.1%/day at-rest, no voyage figure disclosed vs RSER
~3.44%/day and the tank-diameter BOR scaling), **tank design/insulation** (KHI
double-wall vacuum spherical 64–65k m³ vs paper tank-architecture taxonomy),
**materials** (JMSE 316/316L austenitic SS baseline, embrittlement-vs-temperature),
**BOG management** (KHI burns voyage BOG as fuel, no onboard reliq vs paper reliq/
management strategies), **techno-economics** (KHI IAE stack vs RSER ~3.74 $/GJ),
and **safety** (JMSE "record reflects limited data, not inherent safety"). Verify
every paper number against the PDF before putting it in the table; keep KHI
(proprietary) vs public-paper sources clearly separated.

### LH2 vs NH3 node-by-node energy-penalty ledger (2026-09-01)

User asked to start the LH2-vs-ammonia whole-value-chain comparison as a set of
lettered nodes — LH2: A production → B1 liquefaction → C1 export terminal &
storage → D1 shipping → E1 import terminal & storage → F1 regasification; NH3:
A → B2 Haber-Bosch → C2 → D2 → E2 → F2 cracker — with an **energy penalty**
tracked through the chain, and an artifact built for both. The worked example
they gave defines the accounting: 60 kWh/kg electrolyser vs H2's 33.33 kWh/kg
LHV = 26.67 kWh/kg penalty = 55.6 % efficient; then each downstream node's
consumption is deducted from the 33.33 kWh the stream carries. They said to use
default numbers first and they will change what needs changing.

**Modelling decisions taken this session:**

| # | Decision | Choice |
|---|----------|--------|
| E1 | Basis | 1 kg H2 produced at node A; mass tracked as **H2-equivalent** so the NH3 leg is directly comparable (NH3 = H2e x 5.632) |
| E2 | Both efficiency views reported | *Input basis* (LHV delivered / total energy consumed — reproduces the user's 55.6 % at node A) **and** *deduction basis* (33.33 kWh less carrier energy less lost LHV — the user's "deduct from 33.33" framing). Both from the same per-node numbers |
| E3 | Two penalty currencies | Each node takes either **energy drawn** (external power) or **H2 mass lost** — never conflated. LH2 voyage BOG is mass (KHI burns it as fuel, Q23/Q33); terminal BOG is energy (re-liquefied, Q3) |
| E4 | Regas heat not charged | KHI's 3.8 MJ/kg is free ambient seawater heat through an ORV — reported as thermal duty, never added to input energy. Only derived pump work is charged |
| E5 | Cracker self-consumption booked as mass loss | With a first-principles floor: reaction enthalpy alone = 4.22 kWh/kg-H2 = **12.7 % of LHV**, so any self-consumption below that is flagged as physically unreachable |
| E6 | NH3 column stays unsourced | Per D4, **every** NH3 default is an `[ESTIMATE]` placeholder. No external NH3 data was pulled; the artifact says so in its masthead, its register, and its gap list |

**Result at the defaults** (60 kWh/kg, 6,000 km, 5 d holds each end):
LH2 delivers 0.9832 kg H2 for 69.07 kWh → **47.5 %** chain efficiency, 70.25 kWh
per kg delivered. NH3 delivers 0.7840 kg for 63.81 kWh → **41.0 %**, 81.39 kWh
per kg delivered. The shape of the answer: LH2 pays in *energy*, once, at the
liquefier (9 of its 9.63 kWh carrier penalty is node B1); NH3 pays in *hydrogen*,
at the far end (19.6 % of the arriving H2e is consumed in the cracker) — which is
why NH3 draws less total energy yet delivers 20 % less hydrogen.

| File | Action | Purpose |
|------|--------|---------|
| `data/carriers/chain-energy-defaults.csv` | Created | Every default for both chains in the repo's tidy schema, cited or tagged. New units added to the test vocabulary: `km`, `kg/kg`, `kJ/mol` |
| `src/lh2/chain_energy.py` | Created | The model: `ChainInputs`/`NodeResult`/`ChainResult`, `run_lh2_chain`, `run_nh3_chain`, `compare`, `format_report`. Compounding boil-off, stoichiometry, cracker duty derivation, per-chain `gaps` |
| `scripts/run_chain_comparison.py` | Created | CLI wrapper, `--json` for machine-readable output |
| `tests/test_chain_energy.py` | Created | 55 tests incl. the user's worked example, mass balance, both efficiency definitions, the 12.7 % cracker floor, and a **drift test** that fails if any Python default diverges from the CSV |
| `tests/test_data_tables.py` | Updated | New table added to `TABLES`; `km`/`kg/kg`/`kJ/mol` added to `KNOWN_UNITS` |
| `scripts/build_db_workbook.py` + `data/lh2-database.xlsx` | Updated / regenerated | New `chain_energy_defaults` sheet |
| `docs/reports/lh2-vs-nh3-energy-penalty.html` | Created | **"LH2 vs Ammonia Energy Ledger"** artifact: masthead with boundary/basis/units/tag policy, two verdict cards, shared node A panel, two node rails with inputs *on* each node card, two waterfall cascade charts (solid = energy drawn, 45° hatch = H2 lost), node ledger table, live gap list, assumption register, sources. Mirrors `chain_energy.py` exactly |
| `docs/comparison/01-energy-penalty-method.md` | Created | Method write-up |
| `docs/comparison/00-milestones.md` | Updated | M3.5 → 🟡; new artifacts listed |

**Build notes worth keeping:** the two series hues were validated with the
dataviz palette checker (light `#0C7C9E`/`#A9660B`, dark `#2E97B9`/`#BA8930` —
all six checks pass on both surfaces); a third hue for "H2 lost" failed the
normal-vision separation floor against the amber, so mass loss is encoded by
**hatch texture** in the chain's own hue instead. Verified against the Python CLI
via Playwright: every headline figure matched exactly (47.5 %, 41.0 %, 69.07,
63.81, 0.9832, 0.7840, 23.70, 22.32, 55.6 %, 26.67). Playwright's pip build
expects browser rev 1234 but the image ships 1194 — launch with
`executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"`.

**➡️ Open items for the user on this workstream:**
1. Replace the NH3 placeholders with the internal dataset (D4) — the single
   biggest thing standing between this and a decision-grade answer.
2. Confirm or replace the LH2 voyage BOR (0.2 %/day placeholder). It is the
   largest LH2 mass loss in the chain and rests on nothing.
3. Give a named corridor (origin → destination, distance) to replace the generic
   6,000 km (D1).
4. Say whether Haber-Bosch steam export should be credited — it is currently not
   modelled, which is conservative *against* ammonia.
5. Cost is deliberately absent from this build. Say when the energy ledger should
   be joined to the LCOH model (`src/lh2/scenario.py`) for KR1.3's economics.


### Annual scale, fleet sizing, and the NG-fired cracker reframe (2026-09-02)

Follow-up to the energy-penalty ledger. User asked to (1) replace the 1 kg
normalized basis with **100 ktpa H2 supply** as the study's headline scale,
"deriving from this" — i.e. sizing the shipping fleet, not just re-scaling
energy; (2) set **both** carriers to **40,000 m³** vessels (previously the
model didn't size vessels at all, only used a disclosed speed); (3) assume the
**cracker is natural-gas-fired**, giving an ammonia-to-H2 supply ratio of
**~6.5:1**, above the pure mass-balance ratio (~5.63:1, i.e. this repo's
existing `NH3_PER_H2_MASS_RATIO` = 5.632) — the user framed the gap as
"ammonia used as a fuel."

**Modelling decisions taken this session:**

| # | Decision | Choice |
|---|----------|--------|
| E7 | Annual supply basis | Anchored at **node A** (H2 produced), matching the per-kg cascade's own basis — not the delivered/import-side quantity. Stated prominently in the artifact masthead so the user can flag if they meant delivered demand instead |
| E8 | Fleet sizing | Reused `src/lh2/shipping.py`'s existing `round_trip_days()`/`fleet_size()` rather than duplicating the formula — new `annual_scale()` in `chain_energy.py` passes an *effective capacity* (nameplate × fill fraction) since that helper takes no fill-fraction argument itself |
| E9 | LH2 vessel = 40,000 m³ | **Cited**, not invented — this figure already existed in-repo (`data/vessels/lh2-carriers.csv`, KHI reply Q29: vessel under construction, same tank tech as Suiso Frontier). The 160,000 m³ commercial-scale figure is no longer this build's default; its disclosed 29.6 km/h speed is reused (no separate speed exists for the 40k ship) |
| E10 | NH3 vessel = 40,000 m³, density 682 kg/m³ | Both `[ESTIMATE]` — mid-size ammonia/LPG-type carrier and standard refrigerated-NH3 density, neither KHI-specific nor externally sourced (D4 still stands) |
| E11 | Cracker reframe | Reaction heat (4.22 kWh/kg-H2 floor) now **charged** as purchased natural gas at an 85% fired efficiency `[ASSUMPTION]`, not paid for by burning product H2/NH3. Mass loss at F2 drops from the old 20% self-consumption default to a 3% PSA/purification slip `[ESTIMATE]` only |
| E12 | Where the extra ammonia goes | The gap between the mass-balance floor (5.632:1) and the user's target (~6.5:1) is modelled as **ammonia burned as the carrier's own bunker fuel during shipping** (new node-D2 mechanic, linear in voyage days, always lost — never re-liquefied), calibrated (1.3 %/day default) to land near 6.5:1 at the default voyage length. Chosen over alternatives (cracker-side combustion, an unplaced aggregate factor) because it's the one mechanism with a real-world analog (ammonia-fuelled marine engines) and mirrors the LH2 chain's own D1 BOG-as-fuel treatment structurally. Flagged as a placeholder *device*, not a validated shipping-fuel model — real ammonia engines aren't commercial at scale yet |
| E13 | `nh3_supply_ratio()` reported, not hard-coded | The ~6.5:1 figure is a **derived, live-recomputing output** (physical NH3 made at B2 ÷ H2 delivered at F2), not a fixed input — so every atomic assumption behind it (HB loss, bunker rate, process loss) stays independently editable and the ratio updates with them, per the user's "editable, autocalculate" requirement from the prior turn |

**Result at the new defaults** (100 ktpa, 60 kWh/kg electrolyser, 6,000 km,
40,000 m³ both vessels): LH2 delivers 0.9832 kg/kg (unchanged — LH2-side
mechanics didn't change) at 47.5% chain efficiency; **3 vessels**. NH3 now
delivers 0.8476 kg/kg (up from 0.7840 pre-reframe, since the old 20%
self-consumption mass loss dropped to 3%) at **41.5%** chain efficiency, total
energy 68.09 kWh (close to LH2's 69.07, vs clearly lower before — the NG
purchase now shows up as a real charged cost instead of a "free" internal
burn); ammonia supply ratio **6.51:1**; **2 vessels** (fewer than LH2 despite
shipping 5.5× the physical tonnage, because liquid ammonia is ~10× denser than
LH2 — 682 vs 70.8 kg/m³ — in the same 40,000 m³ hull).

| File | Action | Purpose |
|------|--------|---------|
| `src/lh2/chain_energy.py` | Updated | New `ChainInputs` fields (annual supply, fleet availability, vessel capacity/fill/density/port-days both carriers, bunker fuel rate, NG-fired efficiency, renamed `cracker_self_consumption_pct` → `cracker_process_loss_pct`); new `AnnualScaleResult` dataclass + `annual_scale()` (reuses `src/lh2/shipping.py`); new `nh3_supply_ratio()`; D2 now models ordinary BOG *and* bunker fuel as independent mass-loss mechanisms; F2 now charges NG thermal + electrical energy instead of self-consumption; `format_report()` prints the annual/fleet block and the supply ratio |
| `data/carriers/chain-energy-defaults.csv` | Updated | 13 new/changed rows (annual supply, fleet availability, both vessels' capacity/fill/density/port-days, bunker fuel rate, NG-fired efficiency, process loss replacing self-consumption); new unit `ktpa` added to the test vocabulary |
| `tests/test_chain_energy.py` | Updated | 80 tests (was 55): NG-fired energy accounting, process-loss-vs-old-floor sanity, bunker-fuel voyage scaling, `nh3_supply_ratio()` ≈6.5 at defaults and → mass-balance floor at zero bunker fuel, annual-scale linearity, LH2 cargo needs no stoichiometric conversion vs NH3 does, fleet-size cross-check directly against `src/lh2/shipping.py` (so the two can never silently diverge), format_report includes the new sections |
| `scripts/run_chain_comparison.py` | Updated | New CLI flags `--annual-supply`, `--lh2-vessel-capacity`, `--nh3-vessel-capacity`, `--cracker-process-loss` (renamed from `--cracker-self-consumption`); JSON output now includes `annual_scale` and `nh3_supply_ratio` per chain |
| `docs/reports/lh2-vs-nh3-energy-penalty.html` | Updated | New "Annual H2 supply" + "Fleet availability" inputs on the shared Node A panel; D1/D2 node cards gained vessel capacity/fill/density/port-time inputs (D2 also gained the bunker-fuel-rate input); F2 rewired to NG-fired efficiency + process-loss inputs; new **"Annual scale & fleet"** section (two cards: annual energy/delivered/cargo, cargo-per-voyage, round-trip days, trips/year, headline fleet-size number, ammonia supply ratio); calc trail extended for D2 (ordinary BOG + bunker fuel lines) and F2 (NG thermal + electrical breakdown); gap list and assumption register rewritten for the new mechanics |
| `docs/comparison/01-energy-penalty-method.md` | Updated | New §6a "Annual scale & fleet"; §4 formulas/choices extended (NG-fired cracker as "choice 3"); §5/§6/§7/§9 numbers, defaults tables, and sources updated |
| `docs/comparison/00-milestones.md`, `docs/memory.md` | Updated | This entry; M3.5 status note |

**Verified:** every headline HTML figure matched the Python CLI exactly
(41.5%, 68.09, 0.8476, 20.16, 6.51:1, fleet 3/2, 6.907/6.809 TWh/y) via
Playwright; zeroing bunker-fuel-rate and process-loss in the browser collapsed
the live ratio to 5.63:1 (the pure mass-balance floor), confirming the
derived-not-hardcoded requirement; reset-to-defaults round-trips correctly;
no new console errors; both themes and the 420px narrow layout still hold.
Full suite: 124 passing (was 99).

**➡️ Open items for the user on this workstream (carried forward + new):**
1. Replace the NH3 placeholders with the internal dataset (D4) — including,
   now, the vessel spec, NG-fired efficiency, and bunker-fuel mechanism.
2. Confirm whether "100 ktpa H2 supply" should be anchored at node A
   (production, current assumption) or at the delivered/import side instead —
   the two differ by the chain's own loss fraction.
3. Confirm or replace the LH2 voyage BOR (0.2 %/day placeholder).
4. Give a named corridor (origin → destination, distance) to replace 6,000 km.
5. Confirm the ammonia bunker-fuel mechanism is the right *place* to put the
   6.5:1 gap (vs. e.g. attributing it to the cracker itself) — it's currently
   a modelling choice (E12 above), not something the user explicitly located.
6. Cost is deliberately absent from this build. Say when the energy ledger
   should be joined to the LCOH model (`src/lh2/scenario.py`).

### KHI-vs-literature comparison table built (2026-07-21, same session)

Built the artifact flagged above as "NEXT SESSION." Re-read all four KHI
proprietary source files and both paper `.fulltext.md` files directly (not
just `staging.csv` summaries) to verify every figure before citing it.

| File | Action | Purpose |
|------|--------|---------|
| `docs/comparison/khi-vs-literature-lh2-comparison.md` | Created | Sourced comparison of KHI's proprietary LH2 solution vs. RSER 2026 (Towhid & Hossain) and JMSE 2025 (Passalacqua & Traverso), across 6 axes: (1) BOR at-rest vs voyage, (2) tank design/insulation, (3) materials, (4) BOG management strategy, (5) techno-economics, (6) safety. Every cell tagged `[KHI]`/`[RSER]`/`[JMSE]` — no blended/unattributed numbers. Closes with a "Gaps & promotion candidates" section (KHI disclosure gaps + 6 paper-figure promotion candidates, none actually promoted — that stays a separate explicit user approval per `research/AGENT.md`). Does **not** touch `research/sources/staging.csv` promotion status, per task instruction — this lives in `docs/comparison/`, cross-referencing already-ingested sources rather than doing new Zane research. |
| `docs/comparison/00-milestones.md` | Updated | Added the new artifact under "Additional artifacts"; bumped M3.3 (BOG) and M3.6 (complexity/TRL/safety) to 🟡 with a pointer to the new file — full LH2-vs-NH3 memo (M3.9) still blocked on the NH3 dataset (D4) |

**Key findings/citation issues surfaced while building it:**
- **KHI's biggest confirmed gap:** no standalone voyage/laden BOR for the
  160,000 m³ commercial vessel — KHI only says fuel consumption = BOR, never
  a %/day figure. RSER's ~3.44%/day is at a comparable ship scale but is
  itself RSER's synthesis of a *third-party* cited study (not RSER's own new
  experiment) — flagged so it isn't mistaken for a KHI-validated benchmark.
- **RSER's tank-diameter BOR scaling (~1.8%→~0.2%/day)** covers 2–1,200 m³
  tanks — 2–3 orders of magnitude smaller than KHI's 64,000–160,000 m³ tanks;
  flagged that extrapolating the curve to KHI's scale isn't supported by
  either source.
- **New data point found in JMSE, not previously in any repo file:** on the
  Suiso Frontier's actual Australia→Japan demo voyage, "roughly 10% of the
  loaded LH2 is dispersed through the vent mast" (JMSE fulltext, lines
  405–409) — a rare *real operational* number, distinct from any
  commercial-scale (160,000 m³) claim. Flagged as a promotion candidate for
  `data/vessels/lh2-carriers.csv`.
- **Strongest cross-source corroboration:** KHI's "burn BOG as DF engine
  fuel, no onboard reliquefaction" choice is independently reached by JMSE
  from a first-principles energy-balance argument (reliquefaction SEC
  6–8 kWh/kg vs cryocooler power draw ~0.45 kW/W), with no contradiction
  from either paper.
- **Techno-economics apples-to-oranges flag:** KHI's IAE cost stack (native
  unlabelled-axis JPY/Nm³~2019, whole-chain) and RSER's ~3.74 $/GJ (USD/GJ,
  transportation-phase only, from a 2020 secondary source with its own
  Qatar→Japan/160,000 m³/20 kn baseline) are **not directly comparable**
  without resolving the IAE axis/cost-year gap first — did not force a false
  conversion; left as an explicit gap.
- **Materials:** KHI discloses no tank alloy at all in any of the 4 files
  reviewed; JMSE's AISI 316/316L baseline (confirmed via the real Suiso
  Frontier vessel) is the strongest materials evidence across all three
  sources — used as context, not attributed to KHI.
- **Safety:** kept KHI's vendor-positioning framing ("not as challenging as
  often assumed," qualitative separation-distance comparison to NH3)
  clearly separate from JMSE's independent, incident-data-based caution that
  LH2's safety record reflects *limited operational data*, not proven
  inherent safety — presented as two different kinds of claims, not
  reconciled into one.

### Branch cleanup, regulatory-compliance table, and KHI parameter/challenges
deliverables (2026-09-07)

1. **Merged all outstanding branches to `main`** per explicit user instruction.
   Found 9 non-main branches; 7 were already fully merged (no-op), 2 had real
   unmerged work and were merged: `claude/lh2-ammonia-value-chain-4a1525`
   (fast-forward — the energy-penalty ledger work above) and
   `claude/zane-research-comparison-table-4ybs3d` (2-way conflict in
   `docs/comparison/00-milestones.md` and `docs/memory.md`, resolved by
   keeping both sessions' entries since they were independent parallel
   additions, not real edits to the same content). 124 tests passed after
   the merge; pushed to `origin/main`. **As of this entry, `main` is the only
   branch with unmerged work relative to itself — i.e. everything is
   consolidated.** The user's designated per-session branch
   (`claude/merge-unmerged-branches-0mkmwc`) was never used for real commits;
   all work this session landed directly on `main` per the user's explicit
   "merge to main" instructions.

2. **Built KHI technical-parameter tables** (liquefaction, shipping,
   regasification terminal) as a reviewable chat table first, then as a
   formatted `.docx` (`docx` npm library, US Letter, navy header tables).
   Every disclosed figure traces to a KHI reply ID; undisclosed figures
   (CapEx/OpEx, newbuild cost, voyage BOR) shaded amber and tagged rather
   than invented.

3. **Added `data/properties/regulatory-compliance.csv` to the database** —
   this segment had **zero** prior coverage anywhere in the repo. 9 rows: 2
   cited to KHI (Q12 permitting approach, Q36 safety separation distance),
   7 explicit `needs-source` gaps (IMO tank-type classification, IGC/IGF
   Code or equivalent, classification-society approval, liquefaction/
   terminal design codes, carbon-border exposure). Wired into
   `scripts/build_db_workbook.py` (new `regulatory_compliance` sheet),
   `tests/test_data_tables.py` (33 tests passing), and `data/README.md`
   with a new Known-caveats entry. Committed and pushed as `5bf5f6d`.
   **Open item for the user:** this table needs a real research pass
   (dispatch Zane, or a Gentari-legal input) before it supports any
   permitting-timeline or go/no-go claim — right now it's mostly a
   documented gap, not an answer.

4. **Wrote a "Key Challenges in the LH2 Value Chain" report** (chat +
   iterated `.docx` deliverables, not committed to the repo — these are
   user-facing documents, not database content). Covers: (a) energy
   intensity at a 100 ktpa H2 study scale — liquefaction alone ≈103 MW
   continuous average, using KHI's 8–9 kWh/kg SEC; production energy
   explicitly **excluded** at the user's request since it's managed outside
   this report; (b) vessel boil-off gas — KHI's 0.1%/day at-rest figure is
   solid, but the voyage/laden BOR is a confirmed KHI disclosure gap (only
   "fuel-gas rate = BOR" was given); the repo's own 0.2%/day placeholder and
   the unpromoted RSER-2026 literature figure (~3.4%/day, different vessel
   scale) are both named as unvalidated, not used as fact; (c) other risks
   (vessel scale-up/CapEx, undisclosed plant costs, regulatory uncertainty,
   materials/safety, the still-placeholder NH3 comparison) as a simplified
   two-column table per the user's final revision request.
   **User's stated formatting preferences for this deliverable type** (worth
   reusing without being asked again): Arial font throughout; **no dashes
   ("-", "–", "—") anywhere in sentence text** — rephrase instead of using
   them, including in compound words; plain/simple language over technical
   phrasing; no visible source/tag/gap markup in the prose (attribution
   folded into plain sentences like "has not been confirmed" instead of
   `[needs-source]`); tabular content (case-study numbers, multi-item lists)
   presented as a proper table rather than prose or bullet pull-quotes.
   These files were sent directly to the user via SendUserFile, not saved
   under `docs/` or `sources/` — if the user wants a persistent copy in the
   repo, ask where it should live (`docs/reports/` seems the natural home,
   matching `docs/reports/khi-lh2-solution-database.md` etc.).

### Shipping-only LH2 vs NH3 comparison: 40,000 m³ vs 24,000 m³, Kakinada→Hamburg (2026-09-07)

User asked to start the LH2-vs-ammonia comparison from the **shipping side
only**, comparing the existing 40,000 m³ LH2 carrier to a **24,000 m³ (24
kcbm)** liquid ammonia carrier, and asked (via AskUserQuestion, decision-first
per user preference) what NH3 shipping data was needed before building.

**Decisions/inputs from the user this session:**

| # | Decision | Chosen |
|---|----------|--------|
| S1 | NH3 data source | User answers questions directly (no Zane dispatch this round); every NH3 shipping figure is either user-specified `[ASSUMPTION]` or a flagged placeholder |
| S2 | NH3 cargo condition | Fully refrigerated, ~-33°C, 682 kg/m³ (standard published value, `[ESTIMATE]`, no primary citation) |
| S3 | NH3 service speed | **13 knots** (24.076 km/h) |
| S4 | NH3 voyage BOR | 0.1-0.2%/day range selected; **0.15%/day midpoint** used as point default |
| S5 | NH3 BOG handling | **Onboard reliquefaction** (energy cost, no cargo mass loss) — contrasts with LH2's KHI-disclosed "burned as fuel" (cargo mass loss) |
| S6 | NH3 port time | 1.5 days/call, matched to LH2's KHI range for comparability |
| S7 | Corridor | **Kakinada, India → Hamburg, Germany** |
| S8 | Priority framing | User wants the analysis framed as a **"sweet spot" / breakeven search** — under what conditions does each carrier win — not just a static table |
| S9 | Route basis | **Cape of Good Hope** (~21,200 km one-way) chosen as primary over Suez (~10,260 km) to reflect current Red Sea/Suez security-driven rerouting reality, not the classic shortest route |

**Distance-sourcing limitation discovered:** WebFetch to searoutes.com and
similar sea-distance calculators is blocked by this environment's egress
policy, and WebSearch could not surface the exact published Kakinada-Hamburg
figure either. Computed both route distances **first-principles** via
great-circle waypoint summation (Kakinada → S. tip Sri Lanka → [Bab-el-Mandeb
→ Suez → Port Said, or → Cape of Good Hope] → Gibraltar → Hamburg, +8% margin)
and cross-checked the method against a public Karachi→Hamburg figure (11,076
NM) surfaced by search — it matched a Cape-route computation of that same
pair to within 2%, which also revealed that public figure is itself a
Cape-route number, not Suez. Both figures tagged `[ESTIMATE, needs source:
primary distance table]`.

**Headline finding:** at these specific vessel/route specs, **LH2 wins
per-vessel annual H2-equivalent shipping throughput at every distance tested
(1,000-40,000 km)**, by 1.07-1.18× depending on distance. This is *not* a
volumetric story — NH3's density (682 vs 70.8 kg/m³) nearly offsets its
smaller hull (24k vs 40k m³) on a per-voyage cargo basis (NH3 is actually
*slightly* ahead before boil-off). LH2 wins on **turnaround cadence**: faster
speed (16 vs 13 kn) + shorter port time (1.25 vs 1.5 d) yields more trips/y,
outweighing NH3's small per-trip cargo edge. LH2's margin *narrows* with
distance because its voyage boil-off (burned as fuel, cargo lost) compounds
over the longer laden leg, while NH3's reliquefaction loses no cargo mass.

**Sweet-spot / breakeven analysis (the actual deliverable the user asked
for):**
- LH2 voyage BOR breakeven: **0.60%/day (Cape) / 1.23%/day (Suez)** — above
  this, NH3 wins. Current default is 0.2%/day (KHI never disclosed a voyage
  figure); the unpromoted RSER-2026 literature figure is ~3.44%/day — nearly
  6× the Cape breakeven. **This is the single highest-leverage open number**
  in the whole comparison, more than anything about the NH3 vessel itself.
- NH3 speed breakeven: **14.73 kn** (vs current 13 kn) at Cape distance,
  holding LH2 at its default BOR.
- NH3 capacity breakeven: **≈27,060 m³** (vs current 24,000 m³) at 13 kn,
  Cape distance.

| File | Action | Purpose |
|------|--------|---------|
| `data/vessels/nh3-carriers.csv` | Created | 24,000 m³ NH3 vessel spec table (capacity, density, speed, voyage BOR range, BOG disposition, port days, fill fraction), every row tagged ASSUMPTION/ESTIMATE with rationale — distinct from the generic 40,000 m³ NH3 placeholder already in `chain-energy-defaults.csv` (that one stays untouched, serves the full six-node energy ledger) |
| `data/routes/kakinada-hamburg.csv` | Created | Suez (~10,260 km) and Cape (~21,200 km, primary) one-way distances, both `[ESTIMATE]` with full derivation in notes |
| `src/lh2/shipping.py` | Extended | New generic `cargo_mass_per_voyage()` and `annual_capacity_per_vessel()` helpers (factored out of `fleet_size()`'s internals so LH2/NH3/any future carrier share one implementation); `fleet_size()` gained an optional `fill_fraction` kwarg (default 1.0 — no behavior change for existing callers) |
| `scripts/run_shipping_comparison.py` | Created | The full comparison + breakeven solvers (`breakeven_lh2_voyage_bor`, `breakeven_nh3_speed_km_per_h`, `breakeven_nh3_capacity_m3`, generic bisection `find_crossover_km`); prints headline results at both distances, a distance-sensitivity sweep, and the sweet-spot breakeven table |
| `tests/test_shipping_comparison.py` | Created | 15 tests: mass-loss-vs-energy-cost BOG split, cross-checks against `shipping.py` primitives, "LH2 wins at defaults" regression, and each breakeven solver verified to actually zero its underlying difference function |
| `tests/test_data_tables.py` | Updated | Registered the two new CSV tables in `TABLES` |
| `scripts/build_db_workbook.py`, `data/lh2-database.xlsx` | Updated / regenerated | New `nh3_carriers` and `kakinada_hamburg_route` sheets |
| `docs/comparison/02-shipping-lh2-vs-nh3.md` | Created | Full write-up: vessels compared, corridor distance derivation, headline result, sensitivity sweep, sweet-spot breakeven table with interpretation, explicit gap register, open items |
| `docs/comparison/00-milestones.md` | Updated | M3.4 → 🟡 with pointer; new artifact row |

**Verified:** full test suite 151 passing (was 124); script output numbers
cross-checked by hand against the breakeven solvers (each confirmed to
equalize the two carriers' annual H2-equivalent to within 0.1%).

**➡️ Open items for the user on this workstream:**
1. Any real voyage BOR for a fully-refrigerated NH3 carrier and/or a
   confirmed LH2 voyage BOR — resolves the single biggest lever in the
   entire comparison (§5/§6.1 of the new doc).
2. NH3 onboard-reliquefaction SEC (kWh/kg) — currently an unquantified energy
   cost, not zero.
3. Confirm/correct NH3 speed (13 kn), capacity (24,000 m³), port time (1.5 d)
   against the internal dataset (D4) — sensitivity for each already computed.
4. When to join this to cost (CapEx/day-rate/OpEx) for a shipping-cost-per-kg
   comparison, and whether to fold this specific 40k/24k pairing back into
   the full six-node `chain_energy.py` model (which still defaults to a
   generic 40k/40k pairing).
5. Confirm the Kakinada→Hamburg distance with a primary source if this
   corridor becomes decision-relevant — current figures are first-principles
   estimates, not AIS/route-planning-tool output.

### Boil-off as bunker fuel: the fuel-balance reframe (2026-09-07, same session)

User rejected the first artifact's energy study and supplied the real physics:
the LH2 carrier's boil-off is **used as fuel**, the ammonia carrier burns
**25 MT/day of VLSFO**. Check whether the LH2 boil-off covers that duty; if
not, extra VLSFO is needed; if it exceeds the duty, the balance is **released
to atmosphere**. Their point: since both ships then sit on the same propulsion
baseline, the comparison reduces to **H2-lost-as-fuel vs ammonia
re-liquefaction** — and H2 is a premium fuel, so burning it is a real cost.

**Decisions taken:**

| # | Decision | Choice |
|---|----------|--------|
| S10 | Propulsion duty | Both carriers charged the same 25 t/day VLSFO duty `[ASSUMPTION - user]`, so the LH2 boil-off is tested against a like-for-like demand. Flagged: the LH2 vessel is a larger hull at ~23% higher speed, so its real demand is probably higher — no power curve held for either vessel, so it is flagged rather than scaled |
| S11 | Fuel-charging boundary | **Laden leg only**, both vessels symmetrically — that is where boil-off is generated. Ballast excluded, stated explicitly |
| S12 | Surplus disposition | User says vented; **KHI reply Q26 says a GCU burns excess BOG above MARVS**. Both carried as a toggle — the H2 is lost from cargo either way, only the environmental line changes |
| S13 | NH3 reliq energy booked as fuel | Re-liquefaction electricity converted to physical bunker fuel via a 45% genset efficiency `[ASSUMPTION]`, so both carriers' costs land in the same currency |
| S14 | Prices | H2 value and VLSFO price are **live user inputs with no default asserted as correct**; the study reports the breakeven price instead. Logged in the data table as `needs-source` with value deliberately blank |

**Findings (Cape route, 21,200 km, 0.2 %/day):**
1. **Boil-off covers only 64 % of the fuel bill.** The carrier still buys 266 t
   of VLSFO per laden leg and vents nothing. KHI's "fuel-gas consumption rate
   equals the BOR" does not close on its own at this rate.
2. **The regimes meet at 0.316 %/day** (Cape) / 0.308 %/day (Suez). Below it
   the ship buys fuel; above it the engine cannot absorb the boil-off. At the
   RSER 3.44 %/day figure the carrier makes **720 %** of what it can burn —
   1,549 t H2 per leg, **86 % of the boil-off doing no work** (~17,969 t CO2e
   if vented at GWP100 11.6).
3. **Breakeven hydrogen value ≈ USD 2.29/kg** (Cape) / 2.39/kg (Suez) at VLSFO
   USD 600/t; ~3.06/kg at USD 800/t bunker. Above it ammonia is the cheaper
   carrier. At USD 5/kg H2, **83 % of the LH2 carrier's shipping cost is the
   hydrogen it burns**, not the fuel it buys — the premium-fuel penalty.

| File | Action | Purpose |
|------|--------|---------|
| `src/lh2/shipping.py` | Extended | `VLSFO_LHV_MJ_PER_KG` (40.2, ESTIMATE), `H2_LHV_MJ_PER_KG`, `propulsion_demand_mj()`, `bog_fuel_balance()` — splits boil-off into propulsion-useful vs unusable surplus and reports the top-up fuel tonnage |
| `data/vessels/nh3-carriers.csv` | 8 rows added | Bunker rate/type, VLSFO LHV, BOG-vs-oil engine efficiency ratio, reliq genset efficiency, vented-H2 GWP100, and two deliberately-blank `needs-source` price rows |
| `scripts/run_shipping_comparison.py` | Extended | `FuelBalance`, `fuel_balance()`, `voyage_cost_per_kg()`, `breakeven_bor_fuel_cover()`, `breakeven_h2_price()`; `VoyageResult` gained `bog_frac` |
| `tests/test_shipping_comparison.py` | +11 tests (162 total) | Energy conservation in the split, shortfall/surplus exclusivity, "does not cover at 0.2 %/day" as a regression, the cover-BOR sits between 0.2 and 3.44, breakeven price actually equalizes and rises with bunker price, cargo term dominates the fuel term |
| `docs/reports/lh2-vs-nh3-shipping-studies.html` | **Rebuilt** | Reordered to lead with the fuel balance: (1) does boil-off cover the fuel bill (% of demand, two shaded regimes), (2) where the hydrogen goes (stacked useful vs hatched surplus + VLSFO top-up line), (3) cost vs hydrogen value with the parity price, (4) sweet-spot map over H2 price × boil-off with both the cost-parity contour and the fuel-cover line, then the throughput studies. New inputs: bunker rate, H2 price, VLSFO price, VLSFO LHV, engine ratio, genset efficiency, vent/GCU toggle |
| `docs/comparison/02-shipping-lh2-vs-nh3.md` | New §5a + gaps 7-9 | The fuel-balance method, results and breakevens |

**Verified** against the Python CLI at the defaults: covers 64 %, 266 t top-up,
cover point 0.32 %/day, breakeven H2 price $2.29/kg, cost $0.369 vs $0.202 per
kg — all exact matches. No console errors, both themes checked.

**Artifact watch could not be registered this session** (the artifact service
refuses wake subscriptions here), so comments on the page will not wake this
session — the user has to relay them.

**➡️ Open items added by this pass:**
1. A real LH2 voyage BOR remains the top gap — it now decides three separate
   things (throughput, whether the ship buys or wastes fuel, and cost).
2. The LH2 carrier's own propulsion demand — 25 t/day is the ammonia vessel's
   figure borrowed for symmetry. A power curve or a design fuel rate for the
   40k LH2 carrier would sharpen every fuel-balance number.
3. Hydrogen and bunker price assumptions for the corridor, if the economics
   are to be quoted rather than parameterised.
4. Whether the ballast leg should be charged — currently excluded for both.

### 160,000 m³ vessel + boil-off cost basis corrected (2026-09-07, same session)

Four user corrections to the shipping studies.

| # | Change | Detail |
|---|--------|--------|
| S15 | **LH2 vessel → 160,000 m³** | The KHI commercial-scale target (cited, `kawasaki-2026-supplemental`), replacing the 40,000 m³ ship. More internally consistent too: the disclosed 29.6 km/h speed was given for this vessel. `LH2_160K` added; `LH2_40K` kept for the legacy tests |
| S16 | **Per-carrier propulsion duty** | `LH2_BUNKER_T_PER_DAY` split from the ammonia vessel's. Defaults to 25 t/day per the user's stated basis but flagged hard — see below |
| S17 | **Cost basis → boil-off management only** | User was right: the previous NH3 figure (USD 0.202/kg) was 96 % propulsion fuel, not a boil-off comparison. `voyage_cost_per_kg(mode=...)`: `"boiloff"` (default) charges LH2 for hydrogen burned **credited with displaced VLSFO**, and NH3 for reliq fuel only; `"full"` kept as a toggle because the laden legs differ in length so propulsion does not cleanly cancel |
| S18 | **Presentation** | Axis parameters named in every legend; boil-off fate chart got an explicit per-leg/per-day toggle (the user asked which it was — it was per laden leg, unlabelled); throughput study reframed to "how many ammonia ships equal one LH2 carrier" |

**Results at the new default (Cape, 160k, 0.2 %/day, 25 t/day duty):**
- Throughput: **55.2 vs 12.2 M kg H2-eq/vessel-y**, fleet **2 vs 9** — one LH2
  carrier ≈ **4.5** ammonia ships. Single-ship match needs ~108k m³ at 13 kn
  (~84k m³ at 17 kn), at/beyond the largest gas carriers afloat.
- Fuel balance: boil-off covers **258 %** of demand; 394 t H2/leg (61 %) has
  nowhere to go; cover point falls to **0.076 %/day**.
- Cost (boil-off only): LH2 **USD 0.265/kg** vs NH3 **USD 0.009/kg**;
  breakeven H2 value **USD 0.84/kg**. Full-leg basis: 0.308 vs 0.202,
  breakeven USD 3.28/kg.
- Throughput parity BOR now **>4.9 %/day** — above the RSER figure. Throughput
  and cost point in opposite directions; both study sets kept for that reason.

**⚠️ The single most important caveat now:** 25 t/day is the *ammonia* vessel's
burn rate. Applied to a 160,000 m³ hull it manufactures the 258 % overshoot.
At ~100 t/day (proportionate to the 4× cargo) coverage falls to 64 % and the
surplus vanishes. A design fuel rate for the 160k vessel is now the
highest-value missing input alongside the voyage BOR. Both the artifact
readout and the gap list say this explicitly, and the duty is a live input.

Tests: 167 passing (was 162). New coverage for hull-size scaling of the cover
point, the surplus-is-an-artifact-of-the-duty caveat, the displacement credit
making boil-off a net saving at zero H2 value, mode separation, and that speed
alone cannot close a 4.5× gap.

### Vessel scenario selector + ktpa units + H2-landed basis stated (2026-09-07, same session)

| # | Change | Detail |
|---|--------|--------|
| S19 | **LH2 vessel is a scenario, not a fixed input** | Segmented control in the artifact's primary panel for 40,000 m³ (under construction) vs 160,000 m³ (commercial target) — both KHI-cited. `scripts/run_shipping_comparison.py --vessel 40k` mirrors it. All copy that hardcoded "160,000 m³" now reads from the input |
| S20 | **Units: kt / ktpa** | Per-voyage masses in kt, annual rates in ktpa (1 M kg = 1 kt), replacing "M kg" — matches the OKR's 100 ktpa basis |
| S21 | **"H₂ landed" assumption stated on the page** | User asked what the number assumes. LH2: cargo less laden-leg boil-off. NH3: delivered ammonia ÷ 5.632 stoichiometric — i.e. hydrogen *chemically contained*, **assuming a cracker that recovers all of it**. No cracking is modelled (study stops at the discharge arm), so the ammonia figures are an **upper bound**; the whole-chain model's F2 node carries a 3 % slip + 4.22 kWh/kg NG reaction duty. Study 6 retitled "How much hydrogen does each hull actually land?" since "why is the smaller ship competitive" only made sense against the 40k hull |

**The scenario genuinely changes the story** (Cape, 0.2 %/day, 25 t/day):

| | 40,000 m³ | 160,000 m³ |
|---|---:|---:|
| Boil-off vs fuel demand | 64 % (buys 266 t) | 258 % (394 t H₂ wasted) |
| Fuel cover point | 0.316 %/day | 0.076 %/day |
| Breakeven H₂ value | USD 1.94/kg | USD 0.84/kg |
| Annual per vessel | 13.8 ktpa | 55.2 ktpa |
| Ammonia ships per LH₂ ship | 1.1 | 4.5 |

Tests: 169 passing (was 167). Verified both scenarios render correctly and all
scenario-dependent copy updates; no console errors.

**➡️ Obvious next step surfaced by S21:** join this shipping study to the
cracker node (F2) so the ammonia side reports hydrogen actually recovered
rather than hydrogen contained.

### Decision map (H2 price × hull size), then merged to main (2026-09-07, session close)

Final study of the shipping workstream, answering the question the whole
sequence was heading towards: **at what hydrogen price and vessel size does
LH2 beat ammonia?** Mapped on the boil-off cost basis, Cape route, VLSFO
USD 600/t. New `scaled_duty()` in the script + a three-way duty-scaling control
on the study (`0` fixed / `2/3` resistance, default / `1` ∝ cargo), anchored on
the selected scenario's own capacity–duty pair.

**Parity hydrogen value (USD/kg):**

| LH2 hull | Duty fixed | Duty ∝ size^⅔ | Duty ∝ cargo |
|---:|---:|---:|---:|
| 40,000 m³ | 1.94 | 1.25 | 0.84 |
| 160,000 m³ | 0.84 | 0.84 | 0.84 |
| 200,000 m³ | 0.70 | 0.79 | 0.84 |

**Counterintuitive finding: on boil-off cost, bigger is worse.** Boil-off
scales with cargo; the engine that can burn it does not. Past the cover point
the surplus is wasted and the fuel-displacement credit per kg delivered thins,
so the parity price *falls* as the hull grows. Under `∝ cargo` the effect
vanishes (coverage constant, parity line vertical) — which is itself the test
of whether the effect is real or an artifact of the duty assumption.

**Practical conclusion:** both KHI hulls sit under USD 2/kg parity, the 160k
under USD 1/kg. No green-H2 project books hydrogen that cheap, so **on shipping
boil-off cost the map is ammonia's**. LH2's case must be made on what this
study excludes — throughput per vessel (160k wins 4.5:1), terminal/conversion
CapEx, and not needing a cracker.

Tests: **173 passing**. Merged the whole shipping workstream to `main` and
pushed, per user instruction.

---

## ➡️ NEXT SESSION: liquefaction (upstream)

User is starting a new session on **liquefaction**. What is already in the repo
for that segment:

- `data/properties/liquefaction.csv` — KHI SEC 8–9 kWh/kg (cited), H2 Claude
  cycle + N₂ precooling, Fe-based O–P catalyst, ~10,000 tpa minimum economical
  scale, plus the derived theoretical-minimum rows (3.3 kWh/kg normal-H2,
  3.9 para, both cited to `doe-2009-h2-liquefaction-energy`) and the
  BOG-reliquefaction ideal work (1.71 kWh/kg).
- `docs/methodology/02-liquefaction.md` — theoretical minimum vs KHI's SEC
  (implies ~37–49 % second-law efficiency, flagged as an **upper bound** since
  KHI never confirmed its feed-pressure basis), plus the layman exergy
  explanation and worked derivation.
- `src/lh2/liquefaction.py` — SEC, train sizing (115 t/d trains, ~0.78
  utilization derived from KHI's own Base/Large train counts).
- Open gaps carried forward: **no CapEx/OpEx from KHI** ("Feasibility Study
  necessary"), the IAE cost stack's unlabelled axis (`JPY/Nm³ ~2019`,
  `[needs source: primary]`), and the NIST/CODATA citation approval still
  pending for the physical-property rows.
- Standing data policy unchanged: Kawasaki data first; external sources need
  explicit permission, except via Zane (who has standing consent but must cite
  everything).

### Ammonia vessel scenarios added (2026-09-08)

User asked for selectable ammonia hulls: **24k / 40k / 60k / 90k m³**, matching
the LH2 scenario control. 24k is the originally specified vessel; the rest are
mid-size / large / VLGC-scale gas carriers — general industry size bands,
**not** repository figures (largest ammonia carriers in service ~87k m³,
`[ESTIMATE]`).

| NH3 hull | Annual per vessel | NH3 ships per 160k LH2 ship |
|---|---:|---:|
| 24,000 m³ | 12.2 ktpa | 4.5 |
| 40,000 m³ | 20.4 ktpa | 2.7 |
| 60,000 m³ | 30.6 ktpa | 1.8 |
| 90,000 m³ | 45.9 ktpa | 1.2 |

**Two things worth remembering about this control:**
1. **The cost studies do not move with it.** The ammonia carrier's boil-off
   cost per kg H2 is *invariant to hull size* — reliq fuel and delivered cargo
   both scale with cargo, so the ratio cancels. Only the throughput studies and
   the full-leg cost basis respond. There is a test pinning this.
2. **Propulsion duty does not transfer between hulls.** The stated 25 t/day is
   the 24k vessel's. Each duty input now shows a size^⅔ suggestion scaled from
   that pair with a one-click "use" — deliberately NOT applied silently, since
   it is a rule of thumb and no power curve is held for any vessel. 90k → ≈60
   t/day; the 160k LH2 hull → ≈89 t/day (which, if applied, largely dissolves
   the venting finding — see the S16 caveat).

Even at VLGC scale one ammonia carrier does not match one 160,000 m³ LH2 ship:
parity needs ~108,000 m³, above both the scenario set and the fleet in service.

Tests: **177 passing**. Merged to `main`.
