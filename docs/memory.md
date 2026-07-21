# Agent Memory

> Running log of decisions, learned context, user preferences, and open items.
> Updated every session. `CLAUDE.md` points here — read this at the start of
> any session where the user references prior work or continuing a task.
>
> Last updated: 2026-07-21

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
