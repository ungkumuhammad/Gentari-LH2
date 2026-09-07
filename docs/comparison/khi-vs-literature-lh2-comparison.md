# KHI Proprietary LH2 Solution vs. Public Literature — Comparison

> Cross-reference of Kawasaki Heavy Industries' (KHI) proprietary LH2 offer
> (as disclosed to Gentari) against two peer-reviewed public papers already
> ingested by the research sub-agent ("Zane"). Built as a **repo-internal
> deliverable** in `docs/comparison/` — separate from Zane's isolated staging
> area (`research/sources/staging.csv`); no staging/promotion status is
> changed by this file, per `research/AGENT.md`'s isolation policy.

**Purpose.** Support KR1.3 (LH2-vs-alternative-carrier comparison) by
positioning KHI's disclosed engineering/commercial figures against the wider
academic literature on LH2 maritime transport — where they corroborate,
where they diverge, and where KHI simply has not disclosed a figure the
literature does address (and vice versa).

**Scope / system boundary.** Full LH2 chain as far as each source discloses:
production is out of scope for all three sources; liquefaction → export
terminal → shipping (laden voyage) → import terminal → regasification is
covered to varying depth. Where a source's boundary differs (e.g. "voyage"
vs "terminal at rest", or "transportation cost" vs "full chain LCOH"), this
is called out explicitly rather than merged.

**Units & cost-year.** SI units (kg, %/day, K, bar, m³, MJ/kg, kWh/kg) per
`docs/conventions.md`. Costs are shown in their **native, disclosed unit**
(the IAE stack is unlabelled-axis JPY/Nm³‑equivalent, ~2019 vintage; the RSER
figure is USD/GJ, cost-year not stated in the paper) — units are **not**
forced onto a common basis here because the underlying cost bases differ (see
§5).

**Provenance-separation rule.** Every cell is tagged with its source
provenance:
- **[KHI]** — Kawasaki Heavy Industries, proprietary, Gentari-confidential
  (do not redistribute outside Gentari/KHI engagement).
- **[RSER]** — Towhid & Hossain, *Renewable & Sustainable Energy Reviews*
  233 (2026) 116850 (public, open literature).
- **[JMSE]** — Passalacqua & Traverso, *J. Mar. Sci. Eng.* 2025, 13(9), 1748
  (public, open-access literature).

No cell blends KHI and paper figures into one unattributed number. Where KHI
discloses no figure, the cell says so explicitly rather than being left
blank or inferred from the papers.

**Sources used (citation ids):**
- `kawasaki-2026-comparison`, `kawasaki-2026-supplemental`,
  `kawasaki-2026-questionnaire`, `kawasaki-hydrogen-activities`,
  `iae-2019-gigaton` — all in `data/references.csv` (proprietary tier).
- `rser-2026-lh2-maritime-review` — in `research/sources/staging.csv`
  (journal tier); full text verified at
  `research/literature/rser-2026-lh2-maritime-transportation.fulltext.md`.
- `jmse-2025-lng-to-lh2-review` — in `research/sources/staging.csv`
  (journal tier); full text verified at
  `research/literature/jmse-2025-lng-to-lh2-maritime-review.fulltext.md`.

Every paper figure below was re-verified against the actual `.fulltext.md`
(not just the `staging.csv` summary/abstract) before being cited; page/line
context is noted in the notes column where it materially affects
interpretation (e.g. whether a figure is the paper's own result or a
secondary source the paper is reviewing).

---

## 1. Boil-off rate (BOR) — at-rest vs voyage

| Metric | [KHI] | [RSER] | [JMSE] |
|---|---|---|---|
| At-rest terminal BOR | **0.1 %/day**, both loading and receiving terminal tanks (KHI, 2026, `kawasaki-2026-supplemental`) | Not the paper's focus (paper is voyage-centric); no at-rest terminal figure independently modelled | Not quantified for a specific terminal; discusses BOR sensitivity qualitatively (see below) |
| Voyage/laden BOR (commercial-scale ship) | **Not disclosed** — KHI. KHI states only that "the consumption rate of fuel gas (H₂) is equal to BOR" and gives no standalone %/day figure for the 160,000 m³ commercial vessel (KHI, 2026, `kawasaki-2026-questionnaire`, Q23) | **~3.44 %/day**, for a 160,000 m³ LH2 carrier, 4 spherical tanks (radius 21.23 m), 30-day baseline voyage, passive insulation ~0.1 W/m²K (Towhid & Hossain, 2026, fulltext lines 638–668, 1370–1375). **Note:** this is RSER's synthesis of a cited technical-analysis study within the review (not the RSER authors' own new experiment) — RSER attributes the ~3.438%/day figure to that underlying study's sensitivity analysis across carriers | Not modelled as a standalone %/day figure for a commercial-scale ship; but reports an **observed real-world data point**: on the Suiso Frontier's demonstration voyage (Australia → Japan, 1,250 m³ pilot vessel), "roughly 10% of the loaded LH2 is dispersed through the vent mast" over the trip (Passalacqua & Traverso, 2025, fulltext lines 405–409) |
| Tank-diameter scaling of BOR | Not addressed — KHI's disclosed figures are point values for its own 64,000–65,000 m³/160,000 m³ scale, no scaling curve given | Larger tank diameter reduces relative BOG losses from **~1.8 %/day (small, ~2 m³) to ~0.2 %/day** for tanks up to ~1,200 m³, "due to thermal inertia," validated against NASA's MHTB experimental tank data (Wang et al. 2024, as reviewed in Towhid & Hossain 2026, fulltext lines 1082–1083, 1370–1372). **Note: this scaling study covers 2–1,200 m³ tanks — two to three orders of magnitude smaller than KHI's 64,000–160,000 m³ tanks; extrapolating the curve to KHI's scale is not something either source supports** | Not quantified as a diameter-scaling curve; states qualitatively that LH2 BOR (unlike LNG's) is "strongly affected" by ambient temperature and storage size (fulltext lines 359–362) |
| Single-node vs multi-zone modelling error | Not applicable — KHI does not publish a thermodynamic model | Single-node equilibrium models can **under-predict internal tank-wall energy by up to 60%** at low fill levels (≤5%), when max vapour temperature exceeds ~100 K (Wang et al. 2024, as reviewed, fulltext lines 1091–1100, 1108) | Not addressed at this level of modelling detail |
| BOG energy-recovery potential (bulk carrier) | Not addressed | Not this specific figure | BOG treatment/utilization can recover **~4–6% of the energy** otherwise lost through spontaneous evaporation, for large-volume LH2 bulk carriers (as opposed to fuel-tank scale) (fulltext lines 363–367) |

**Read:** KHI's only hard, disclosed BOR number is the 0.1%/day at-rest
terminal figure; it has never given a standalone voyage BOR for its
commercial 160,000 m³ ship concept. The literature's ~3.44%/day figure is at
a comparable ship scale (160,000 m³) but is itself a secondary citation
within RSER, not a first-principles KHI-validated number — it should be
treated as an independent modelling estimate, not a benchmark KHI has
endorsed. The one real *operational* data point available anywhere in these
three sources is JMSE's ~10% total voyage loss on the 1,250 m³ Suiso
Frontier demonstration run — but that is a small pilot vessel, not
representative of the 160,000 m³ target scale.

---

## 2. Tank design / insulation

| Metric | [KHI] | [RSER] | [JMSE] |
|---|---|---|---|
| Tank architecture (export/loading) | **64,000 m³/tank**, 3 tanks (Base, 2.5 Bn Nm³/y) or 4 tanks (Large, 10 Bn Nm³/y) (KHI, 2026, `kawasaki-2026-supplemental`) | N/A (not a design-taxonomy paper for terminal tanks) | N/A |
| Tank architecture (receiving) | **65,000 m³/tank**, 3 tanks (Base) or 11 tanks (Large) (KHI, 2026, `kawasaki-2026-supplemental`) | N/A | N/A |
| Onboard/vessel tank type | Commercial target vessel **160,000 m³**, 2 ships (Base)/8 ships (Large); construction underway for a **40,000 m³** vessel using "the same technology of cargo tanks proven by Suiso Frontier" (KHI, 2026, `kawasaki-2026-supplemental`, `-questionnaire` Q29). Design description: **"double-shelled/vacuum insulated tank"**, "high-performance insulation technology" (KHI, `kawasaki-hydrogen-activities`, company-level, 2024, not project-specific). One option raised for ground tanks — but not confirmed as the chosen design — is a **spherical tank with pressurized send-out** to minimize dead volume (KHI, 2026, `kawasaki-2026-questionnaire` Q4) | Reviews an IMO Type-taxonomy framework generically (Type A prismatic, Type B spherical/Moss or prismatic, Type C cylindrical pressurized) developed for **LNG**, and notes spherical tanks (Type B, Moss-type) "showed the lowest BOG rate" in a cited thermodynamic sensitivity study because of minimum surface-area-to-volume ratio (fulltext lines 638–650); does not assign an IMO type specifically to LH2 carriers | Same IMO Type A/B/C taxonomy (fulltext lines 171–182), explicitly for **LNG**; separately confirms the Suiso Frontier LH2 tanker "both the inner vessel and the outer containment are realized utilizing austenitic stainless steel" (fulltext lines 461–464) with **glass-fibre-reinforced plastic (GFRP)** used for the inner-vessel saddles (fulltext lines 473–475). LH2 tank & insulation **TRL: 6–7**, vs LNG's mature TRL 9 (fulltext Table 4, lines 346–351) |
| Ballast-voyage thermal management | Not addressed by KHI | Controlled ballast-voyage tank warming/venting strategy cuts heat accumulation by **41.6–54.3%** vs an uncontrolled baseline, per a 21-day ballast-voyage scenario studied by Wang et al. (2024) and reviewed in RSER (staging.csv note, corroborated in fulltext discussion of insulation-type comparisons, lines 1073–1081) | Not addressed at this level of detail |

**Read:** KHI's disclosed tank facts are firm point specs (volumes, tank
counts, "double-shelled/vacuum insulated") for its own concept, but KHI has
not confirmed the IMO tank-type classification (Type B spherical vs other)
for its 160,000 m³ commercial design — the "spherical + pressurized
send-out" language appears only as one *option* KHI raised for ground
storage dead-volume minimization, not a confirmed choice for the ship
tanks. The literature's spherical-tank BOG advantage (both papers) is
consistent with, but does not confirm, that KHI's ship design would behave
the same way — KHI's ship tank geometry itself is not confirmed as spherical
in the documents reviewed.

---

## 3. Materials

| Metric | [KHI] | [RSER] | [JMSE] |
|---|---|---|---|
| Tank/vessel material | Not specified by KHI beyond "double-shelled/vacuum insulated tank"; no alloy grade disclosed in any of the four KHI source files reviewed | Not addressed — RSER is a thermodynamics/techno-economics review, not a materials review | **Austenitic stainless steel** (AISI 316 / 316L, i.e. X5CrNiMo17-12-2 / X2CrNiMo17-12-2) identified as the baseline material for cryogenic H2 tanks, already used on the **Suiso Frontier** (inner vessel + outer containment) (fulltext lines 456–464, 527–529). Aluminum alloys and Ti/Ni alloys cited as viable alternatives but Ti/Ni are costlier and more embrittlement-prone (fulltext lines 439–441, 523–532) |
| Embrittlement vs temperature (JMSE finding) | N/A | N/A | Hydrogen-embrittlement severity is **not monotonic with decreasing temperature**: NASA data show the HEE (hydrogen-environmental-embrittlement) index for AISI 316 is worst near **−73 °C**, not at cryogenic (~20 K) temperatures — at true cryogenic temperatures hydrogen mobility is "too sluggish" to fill enough lattice vacancies, so embrittlement risk is *lower* there than at intermediate/near-ambient temperatures (fulltext lines 489–517). This directly supports the abstract's claim that "hydrogen embrittlement is less critical at cryogenic temperatures due to reduced atomic mobility" (fulltext lines 40–41) |
| Tensile strength at cryo | N/A | N/A | Korean Register data: AISI 316/316L tensile strength **more than doubles at 20 K** vs room temperature (fulltext lines 457–459) |
| Nitrogen-enriched alloys | N/A | N/A | Nitronic®-type nitrogen-enriched stainless steels offer improved corrosion resistance/tensile strength at both high and cryogenic temperatures — flagged as a possible alternative for harsher environments (fulltext lines 464–468) |

**Read:** KHI has not disclosed a material spec at all in the documents
reviewed — this is a clean, explicit KHI gap (not an omission on our part).
JMSE's 316/316L baseline (validated by the one operating reference vessel,
Suiso Frontier) is the strongest evidence-backed materials data point
available across all three sources, and is a reasonable working assumption
for KHI's own ships given KHI built Suiso Frontier — but that inference is
ours, not a KHI-confirmed fact, and is flagged as such.

---

## 4. BOG management strategy

| Metric | [KHI] | [RSER] | [JMSE] |
|---|---|---|---|
| Terminal-side (downstream of liquefaction) | BOG **re-liquefied** — via an ejector in the liquefier or a compressor with cryo-rated suction (KHI, 2026, `kawasaki-2026-questionnaire` Q3, Q14) | Not addressed at the terminal level | Not addressed at the terminal level |
| Voyage-side (onboard, laden) | BOG is **burned as dual-fuel (DF) engine propulsion fuel**; "the consumption rate of fuel gas (H₂) is equal to BOR" (KHI, 2026, `kawasaki-2026-questionnaire` Q23, Q32-33). **No onboard reliquefaction** — KHI states this explicitly is not adopted, citing the large energy (electricity) requirement and lack of onboard space (KHI, 2026, `kawasaki-2026-questionnaire` Q33) | Reviews multiple onboard strategies from third-party studies (Wang et al. 2025 et al.): COGAS-engine BOG combustion, fuel-cell auxiliary power from BOG, BOG-to-main-propulsion, and a gas-combustion-unit (GCU) as flexible modes depending on BOG generation rate (fulltext lines 743–789, 824–829). Notes that reliquefaction is one of the theoretical options considered in the broader techno-economic literature but that "in the reference case, no active BOG re-liquefaction" is typically modelled for the base comparative-cost case (fulltext line ~670) | Independently concludes **BOG reliquefaction is not economically viable onboard LH2-powered ships** today: process-simulation SEC estimates for large liquefaction plants are 6–8 kWh/kg-LH2 (with real SECs higher), one to two orders of magnitude worse than would be viable at ship scale; state-of-the-art cryocoolers need ~0.45 kW input per W of cooling power (NASA zero-boil-off study) (fulltext lines 398–418). Concludes **direct BOG utilization as fuel is the viable solution, "currently employed onboard dual-fuel ships"** (fulltext lines 419–429) |
| 100%-MGO / non-BOG-fuel regime | Tank pressure can be held within MARVS "for several days" on MGO alone; if pressure exceeds MARVS, excess BOG is burned via an onboard **gas combustion unit (GCU)** (KHI, 2026, `kawasaki-2026-questionnaire` Q26) | Not addressed at this operational-mode granularity | Not addressed at this operational-mode granularity |

**Read:** This is the strongest cross-source corroboration in the whole
comparison. KHI's real-world engineering choice (burn BOG as DF fuel, do
**not** reliquefy onboard) is independently reached by JMSE from a
first-principles energy-balance argument (reliquefaction SEC vs cryocooler
power draw), and is consistent with the range of onboard strategies RSER
surveys from the broader literature. No contradiction found between KHI and
either paper on this axis.

---

## 5. Techno-economics

| Metric | [KHI] | [RSER] | [JMSE] |
|---|---|---|---|
| Cost basis | IAE (Institute of Applied Energy) Gigaton Workshop, WHTC 2019, per-component cost stack for LH2 Base (2.5 Bn Nm³/y) and Large (10 Bn Nm³/y), reproduced second-hand via KHI, `kawasaki-2026-supplemental` → `iae-2019-gigaton`. **Units: unlabelled cost axis** (`data/costs/lh2-cost-stack.csv` stores it as `JPY/Nm³ ~2019`, `[needs source: primary]` — the primary IAE source is not held in this repo and the axis has not been independently verified) | Transportation cost of **~3.74 $/GJ** for LH2, vs 0.74 $/GJ (LNG) and 1.09 $/GJ (liquid ammonia) — this is RSER's synthesis of a **secondary source**, Al-Breiki & Bicer (2020) as reviewed by Towhid & Hossain (fulltext lines 700–725). Baseline assumptions given in RSER: 160,000 m³ ship, 20-knot cruising speed, 12,000 km representative long-haul distance (Qatar → Japan route), natural-gas feedstock price 2 $/GJ; costs broken into Capital, Operating, and BOG cost components, and explicitly account for BOG mass loss as an economic cost rather than an externality (fulltext lines 744–752) | Does not provide a $/GJ or $/kg cost figure; techno-economic content is limited to noting that reliquefaction is economically unattractive at ship scale (see §4) |
| Boundary of the cost figure | KHI's stack spans **production-adjacent through receiving terminal** (production/synthesis-equivalent, liquefaction, loading terminal, seaborne transport, receiving terminal, cracking [N/A for LH2], other/distribution) — i.e., closer to a full-chain LCOH-style breakdown | RSER's ~3.74 $/GJ is specifically the **transportation-cost** component (Fig. 4 in the paper), separate from the production/liquefaction "conversion" cost shown in the paper's upper cost-phase diagram (fulltext lines 695–702) — **narrower boundary than KHI's stack** | N/A |
| **Unit/boundary mismatch flag** | — | — | — |

**Flagging the mismatch explicitly (per task instructions — not forcing a
false apples-to-apples):** KHI's IAE-based figures are a native-unit,
whole-chain component cost stack (unlabelled JPY/Nm³-equivalent axis,
~2019), while RSER's 3.74 $/GJ is a USD/GJ figure for the *transportation
phase only*, drawn from a third-party 2020 study with its own route/ship/
fuel-price assumptions (Qatar→Japan, 12,000 km, 20 kn, 160,000 m³). **These
two numbers are not directly comparable** without (a) resolving the IAE
stack's cost-year and axis unit [gap — already flagged in `docs/memory.md`
as an open input], and (b) isolating the transport-only slice of KHI's
stack (its "Seaborne transport" line: 4.0 for both Base and Large — same
unlabelled unit) and converting both to a common currency/cost-year/energy
basis. Doing that conversion now would require inventing an FX rate and
JPY/Nm³-to-$/GJ conversion basis not given by any source — **flagged as a
gap, not attempted here.**

---

## 6. Safety

| Metric | [KHI] | [RSER] | [JMSE] |
|---|---|---|---|
| Qualitative safety position | LH2 is **non-toxic** but classified as a **flammable high-pressure gas**, requiring "significantly larger safety separation distances compared to liquid ammonia" (KHI, 2026, `kawasaki-2026-questionnaire`, additional Q36). No onboard filling-ratio restriction from sloshing; BOG unaffected by sloshing (KHI, 2026, `kawasaki-2026-questionnaire` Q20). KHI's overall framing: LH2 "is not as lacking in competitiveness nor as challenging as often assumed" (KHI, 2026, `kawasaki-2026-comparison`, closing notes) | Not a safety-focused paper; no incident/accident data presented | **Key finding:** LH2's apparently favorable safety record **"stems from limited operational data rather than superior inherent safety"** (fulltext abstract, lines 41–43) — i.e. the *absence* of major incidents to date should not be read as evidence of low hazard, given how little LH2 has actually been operated at scale |
| Incident data cited | Not addressed by KHI | N/A | Cites a study of 287 hydrogen-release occurrences: explosion occurred in ~96% of GH2 releases vs ~50% of LH2 releases; hot surfaces were the ignition source in 21% (GH2) / 11% (LH2) of cases; 199 injuries across 201 GH2 accidents vs 10 injuries across 86 LH2 accidents (fulltext lines 823–832). Separately cites the PRESHLY project's identification of 18 LH2 storage/containment incidents during transport and liquefaction/storage, with cause/outcome breakdowns (fulltext lines 833–864) |
| BLEVE risk | Not addressed | N/A | Notes BLEVE (boiling-liquid-expanding-vapor explosion) is **less common in the incident data than academic risk assessments often assume**, because a ruptured LH2 tank's evaporated fraction is cold/concentrated and unlikely to ignite all at once — a "small flash fire is a more realistic scenario" (fulltext lines 876–884) |

**Read:** KHI's qualitative safety claims (larger exclusion zones for LH2 vs
NH3, but otherwise "not as challenging as often assumed") are a commercial/
positioning framing from a technology vendor. JMSE's independent,
incident-data-based finding is more circumspect: it neither confirms nor
contradicts KHI's framing, but explicitly cautions that the *statistical*
safety record so far reflects low sample size (few LH2 operations to date),
not a demonstrated inherent safety advantage. These two views are not
contradictory but sit at different levels of rigor — KHI's is a vendor's
qualitative comparison to ammonia; JMSE's is a caveat about reading *any*
current LH2 safety statistics with confidence.

---

## 7. Gaps & promotion candidates

### KHI disclosure gaps (confirmed absent across all four KHI source files reviewed)

- **Voyage/laden BOR for the 160,000 m³ commercial vessel** — KHI states only
  that fuel consumption = BOR, no standalone %/day figure. (Carried forward
  from prior sessions; `src/lh2/shipping.py`'s `voyage_boil_off` already
  requires a user-supplied value rather than defaulting.)
- **Tank IMO-type classification** for the ship-mounted 160,000 m³ tanks
  (spherical/Type B vs other) — not confirmed, only raised as one *option*
  for ground-tank dead-volume minimization.
- **Tank/vessel material specification** (alloy grade) — not disclosed in
  any KHI file reviewed.
- **CapEx/OpEx in USD/kg** for liquefaction, terminals, or vessels — KHI
  states "Feasibility Study necessary" each time asked.
- **Carbon intensity (kgCO2e/kgH2)** — same "Feasibility Study necessary"
  response.
- **IAE cost-stack unit/cost-year** — native axis unlabelled, ~2019 vintage
  assumed; primary IAE source not held in this repo.

### Paper figures that are candidates for promotion into `data/references.csv` (NOT promoted here — separate, explicit user approval required per `research/AGENT.md` §4/§5d)

1. **RSER ~3.44%/day voyage BOG** (160,000 m³, 4 spherical tanks, 30-day
   voyage) — candidate benchmark for the repo's open voyage-BOR gap, *if*
   the user is comfortable using a third-party literature estimate (not
   KHI-endorsed) as a placeholder/sensitivity case in `src/lh2/scenario.py`.
2. **RSER tank-diameter BOR scaling (~1.8% → ~0.2%/day, 2–1,200 m³ tanks)**
   — useful for a qualitative sensitivity note, but scale mismatch vs KHI's
   64,000–160,000 m³ tanks should be flagged wherever it's used.
3. **JMSE Suiso Frontier ~10% voyage loss (Australia→Japan demo trip)** —
   a rare *real operational* data point; strong candidate for
   `data/vessels/lh2-carriers.csv` as a demo-vessel-specific figure (already
   distinct from any commercial-scale claim).
4. **JMSE materials baseline (AISI 316/316L, Suiso Frontier confirmed)** and
   the **cryo-embrittlement-minimum-near-−73°C finding** — good candidates
   for a new `data/properties/` materials table if the team wants a sourced
   materials reference for LH2 tank design.
5. **JMSE LH2 component TRL table** (Tank & Insulation 6–7, Pump 5–6, Heat
   Exchanger 7–8, Piping 7–8, Valves/Fittings 8, vs LNG's 9 across) —
   candidate cross-check against KHI's own TRL disclosures (loading arm
   TRL 6–7, already in `data/properties/terminals.csv`).
6. **RSER ~3.74 $/GJ LH2 transportation cost** (with its Qatar→Japan/
   160,000 m³/20 kn/12,000 km baseline) — flagged as a possible sensitivity
   comparator for KHI's IAE seaborne-transport line, but only after the IAE
   axis/cost-year gap (above) is resolved; promoting it without that
   resolution risks an apples-to-oranges comparison.

None of the above have been copied into `data/references.csv` or any
`data/` table as part of this task — this file is a read-only cross-
reference, per the task's explicit instruction not to touch promotion
status.

---

## Sources

- `kawasaki-2026-comparison` — Kawasaki Heavy Industries, Ltd. *Comparison
  between LH2 and other Carriers of Hydrogen.* April 2026.
  `sources/raw/Project/Kawasaki Heavy Industries/Comparison_btw_LH2_and_other_carriers_KHI2604_R1.md`
- `kawasaki-2026-supplemental` — Kawasaki Heavy Industries, Ltd.
  *Supplemental Information — Comparison between LH2 and other Carriers of
  Hydrogen.* May 2026.
  `sources/raw/Project/Kawasaki Heavy Industries/Supplemental_Information_Comparison_btw_LH2_and_other_carriers_KHI2605_R0.md`
- `kawasaki-2026-questionnaire` — Kawasaki Heavy Industries, Ltd. *Gentari
  Liquid H2 Questionnaire — KHI reply (Rev.1).* Mar 31 / Apr 6 2026.
  `sources/raw/Project/Kawasaki Heavy Industries/KHI_Gentari_Liquid_H2_Questionnaire_20260220_KHI_reply0331_GHSB20260406.md`
- `kawasaki-hydrogen-activities` — Kawasaki Heavy Industries, Ltd.
  *Kawasaki's Hydrogen Activities.* May 2024.
  `sources/raw/Project/Kawasaki Heavy Industries/Kawasakis_Hydrogen_Activities_2.md`
- `iae-2019-gigaton` — Institute of Applied Energy (IAE). Gigaton Workshop,
  WHTC 2019 (6 May 2019). Cited second-hand via `kawasaki-2026-supplemental`.
- `rser-2026-lh2-maritime-review` — Towhid, MD. Shajratul Alam; Hossain,
  Sumaiya Binte. *Advances and challenges in cryogenic liquefied hydrogen
  (LH2) maritime transportation: thermal performance, tank design, boil-off
  gas management, and techno-economic considerations.* Renewable &
  Sustainable Energy Reviews 233 (2026) 116850. DOI
  10.1016/j.rser.2026.116850. Full text:
  `research/literature/rser-2026-lh2-maritime-transportation.fulltext.md`.
- `jmse-2025-lng-to-lh2-review` — Passalacqua, M.; Traverso, A. *From LNG to
  LH2 in Maritime Transport: A Review of Technology, Materials, and Safety
  Challenges.* J. Mar. Sci. Eng. 2025, 13(9), 1748. DOI
  10.3390/jmse13091748. Full text:
  `research/literature/jmse-2025-lng-to-lh2-maritime-review.fulltext.md`.
