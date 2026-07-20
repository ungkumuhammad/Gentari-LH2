# KHI / Kawasaki Heavy Industries — LH2 Solution Assessment Database

**Prepared for:** Gentari (PETRONAS group) — LH2 value chain workstream
**Derived from:** Gentari ⇄ KHI technical questionnaire (Feb–Apr 2026) and KHI
technical/commercial decks (Apr–May 2026), plus KHI corporate materials.
**Scope:** Gate-to-gate KHI-offered technology across liquefaction, loading
terminal, seaborne transport, and receiving/regasification. Production
(upstream H2) and end-use/reconversion are out of KHI's offer and out of
scope here.
**Units & currency:** SI/metric; H2 mass in kg; costs in the source's native
unit with cost-year caveats stated per **CLAUDE.md §5**.
**Status:** This is a structured **database derived from KHI's assessment
responses**, not a reproduction of the questionnaire itself. Every figure
below is traceable to the source register in §10. Values KHI declined to
disclose are recorded as explicit gaps (§9), never estimated.

---

## 1. How to read this document

| Marker | Meaning |
|---|---|
| **(cited)** | Backed by a specific KHI or IAE document, listed in §10 |
| **[ASSUMPTION]** | A value we chose deliberately to make the database usable; rationale given |
| **[GAP — not disclosed]** | KHI was asked and declined, pending a Feasibility Study |

All figures are KHI's own representations of their technology and are
**not independently verified** by Gentari. Where KHI gave a range instead of
a point value, the range is carried, not collapsed.

---

## 2. Executive summary

- KHI positions **LH2 as commercially and technically viable for earlier
  introduction than commonly assumed**, relative to NH3 and MCH carriers —
  this is KHI's stated view, not an independent finding *(cited, KHI2604 R1)*.
- The **core technology is proven at pilot scale** (Suiso Frontier, 1,250 m³,
  2021–2022 Australia–Japan voyage) and is **scaling through a 40,000 m³
  vessel under construction** toward a **160,000 m³ commercial-scale target**
  *(cited, kawasaki-hydrogen-activities, kawasaki-2026-questionnaire)*.
- **Liquefaction SEC is 8–9 kWh/kg-H2** *(cited)*, with material efficiency
  gains expected only in the **2035–2040** window, not near-term.
- KHI reports **no hydrogen loss** across its plant concept and **no filling
  restrictions or sloshing-driven BOG penalty** on the carrier — both are
  KHI's stated design targets rather than operating-data-backed guarantees
  *(cited, reply Q15/Q20)*.
- **The single largest gap for investment screening is cost**: KHI has
  **not disclosed CapEx or OpEx** in USD/kg for liquefaction, terminals, or
  the carrier newbuild — in each case KHI's answer was "a Feasibility Study
  is necessary" (§9). The only cost data available is a **second-hand,
  unlabelled-axis IAE cost stack** reproduced in a KHI slide (§7), which is
  unit- and cost-year-unverified.
- **Regulatory/permitting detail for LH2 import terminals outside Japan is
  not yet available from KHI**; only a qualitative LH2-vs-NH3 hazard
  comparison was given (§8).

---

## 3. Liquefaction

*Boundary: gaseous H2 in → LH2 at ≈20 K, ≈1 bar, out.*

| Parameter | Value | Basis | Source |
|---|---|---|---|
| Specific energy consumption (SEC) | **8–9 kWh/kg-H2** | varies with liquefier scale & boundary conditions | (cited, kawasaki-2026-questionnaire) |
| Plant-level power consumption | **0.55 kWh/Nm³** | KHI fleet/plant assumption used in cost-basis slides | (cited, kawasaki-2026-supplemental) |
| Unit train capacity | **115 t/day** per train | scales toward ~150 tpd in KHI's "Tech" (large-scale/high-speed) case | (cited, kawasaki-2026-supplemental) |
| Train count — Base scale | **7 trains** | Base = 2.5 billion Nm³/y | (cited, kawasaki-2026-supplemental) |
| Train count — Large scale | **27 trains** | Large = 10 billion Nm³/y | (cited, kawasaki-2026-supplemental) |
| Minimum economical scale | **≈10,000 tpa** | depends on target-market offtake pricing | (cited, kawasaki-2026-questionnaire) |
| Liquefaction cycle | **H2 Claude cycle + N₂ precooling** | proven track record | (cited, kawasaki-2026-questionnaire) |
| Precooling alternative | Hydrocarbon mixed refrigerant | under consideration; **not yet proven** | (cited, kawasaki-2026-questionnaire) |
| Ortho–para (O–P) conversion | Performed **inside the liquefier**, catalytic, to planned para-H₂ fraction | — | (cited, reply Q6) |
| O–P catalyst | **Fe-based** (in service); Co-based **under evaluation** | no expected degradation → **no replacement planned** | (cited, reply Q7) |
| Liquefier performance degradation | **None expected** over operating life | — | (cited, reply Q16) |
| Downstream BOG handling (pre-loading) | **Re-liquefied** — via ejector in the liquefier, or compressor with cryo-rated suction | — | (cited, reply Q3/Q14) |
| Hydrogen loss, chain-wide | **0%** — KHI's plant concept assumes no H2 losses | KHI design claim, not measured field data | (cited, reply Q15) |
| SEC improvement outlook | Significant improvement expected **2035–2040** | driven by subcomponents currently under development, not near-term | (cited, reply Q1) |
| CapEx, USD/kg | **[GAP — not disclosed]** | KHI: "Feasibility Study necessary… varies with plant size" | reply Q8 |
| OpEx, USD/kg | **[GAP — not disclosed]** | same caveat | reply Q9 |
| Carbon intensity, kgCO₂e/kg-H2 (with RE supply) | **[GAP — not disclosed]** | same caveat | reply Q11 |
| PFD / heat & mass balance | **[GAP — not disclosed]** | KHI: shareable "at Feasibility Study timing" | reply Q10 |
| Permitting (Japan & abroad) | Approved case-by-case via a **special evaluation committee** in Japan for matters outside existing law; similar country-specific approach expected elsewhere | qualitative only | (cited, reply Q12) |

---

## 4. Loading / export terminal

*Boundary: LH2 from liquefier → LH2 loaded onto carrier.*

| Parameter | Value | Basis | Source |
|---|---|---|---|
| Boil-off rate (BOR) at rest | **0.1 %/day** | at-rest storage | (cited, kawasaki-2026-supplemental) |
| Storage tank size | **64,000 m³/tank** | export side | (cited, kawasaki-2026-supplemental) |
| Tank count — Base / Large | **3 tanks / 4 tanks** | Base 2.5B Nm³/y, Large 10B Nm³/y | (cited, kawasaki-2026-supplemental) |
| Dead volume | Broadly **similar to LNG tanks** — driven by pump NPSHr, not by in-tank pump presence | — | (cited, reply Q4) |
| Dead-volume minimization option | **Spherical tank + pressurised send-out** (no pumps) | a small "keep-cool" heel may remain | (cited, reply Q4) |
| Loading arm — demonstrated size | **6-inch**, TRL **6–7** | pilot demonstration completed on Suiso Frontier | (cited, reply Q19) |
| Loading arm — commercial size | **16-inch**, **not yet verified** | verification expected in **~3 years** from Apr 2026; both arm types by TBG | (cited, reply Q19 supplemental) |
| Export-terminal CapEx, USD/kg | **[GAP — not disclosed]** | only the aggregate IAE cost stack (§7) is available | — |

---

## 5. Shipping / carrier

*Boundary: LH2 loaded → LH2 discharged at import terminal.*

| Parameter | Value | Basis | Source |
|---|---|---|---|
| Demonstration vessel (Suiso Frontier) | **1,250 m³**, 116 m LOA, 13 knots, diesel-electric, 25 crew | world's first LH2 carrier; Dec 2021–Feb 2022 Australia→Japan voyage | (cited, kawasaki-hydrogen-activities) |
| Vessel under construction | **40,000 m³** | same cargo-tank technology as Suiso Frontier; **no major issues flagged** | (cited, reply Q29) |
| Commercial-scale target vessel | **160,000 m³** at **29.6 km/h (≈16 knots)** | KHI cost-basis slide | (cited, kawasaki-2026-supplemental) |
| Fleet count — Base / Large | **2 ships / 8 ships** | Base 2.5B Nm³/y, Large 10B Nm³/y | (cited, kawasaki-2026-supplemental) |
| BOG management (propulsion) | **BOG used as fuel** via a **dual-fuel (DF) engine** KHI is developing | fuel-gas consumption rate = BOR | (cited, reply Q23/Q32) |
| Onboard reliquefaction | **Not adopted** — too much electrical energy and space required | — | (cited, reply Q33) |
| Filling-ratio / sloshing restriction | **None** — no filling-ratio limit, no sloshing impact on BOG | — | (cited, reply Q20) |
| Max sailing distance | Limited **only by the MGO fuel tank**, not by BOG | — | (cited, reply Q21) |
| 100% MGO (no BOG-as-fuel) regime | Tank pressure holds within **MARVS for several days**; GCU burns excess BOG if MARVS is exceeded | — | (cited, reply Q26) |
| Loading/unloading duration | **≈1–1.5 days** per vessel call | varies with terminal facilities | (cited, reply Q27) |
| Preferred shipyard | **KHI Sakaide Shipyard** | lead time **longer than LNG carriers** — more complex double-wall tanks/piping | (cited, reply Q28) |
| Scale-up challenge to 160,000 m³ | **Cargo-tank manufacturability** flagged as the key issue | — | (cited, reply Q29) |
| Cost premium vs. LNG carrier | **Significantly higher** — double-wall tanks *and* piping increase material/welding; **limited supplier base** for H2 cargo equipment | qualitative only, **no $/vessel figure disclosed** | (cited, reply Q30/Q31) |
| Newbuild cost, USD/vessel (160,000 m³) | **[GAP — not disclosed]** | same as above | reply Q31 |
| Power Take-Off (PTO) | **Optional**, per shipowner's operational policy | — | (cited, reply Q24) |
| FuelEU / ECA compliance | Needs **higher H2 fuel fraction + green H2** to meet FuelEU; SOx met via H2/MGO; **NOx Tier 3 needs SCR** | — | (cited, reply Q22) |
| Floating Storage Unit (FSU) / ship-to-ship | **Not yet specifically considered** — too few LH2 carriers in service today; KHI believes the technology is **applicable in principle** (similar to other liquefied-gas carriers) | — | (cited, reply Q25) |
| Minimum heel (temperature hold) | **No general figure** — varies with voyage length | — | (cited, reply Q34) |

---

## 6. Receiving terminal & regasification

*Boundary: LH2 in → gaseous H2 at delivery pressure, out.*

| Parameter | Value | Basis | Source |
|---|---|---|---|
| Boil-off rate (BOR) at rest | **0.1 %/day** | at-rest storage, same as export side | (cited, kawasaki-2026-supplemental) |
| Storage tank size | **65,000 m³/tank** | receiving side | (cited, kawasaki-2026-supplemental) |
| Tank count — Base / Large | **3 tanks / 11 tanks** | Base 2.5B Nm³/y, Large 10B Nm³/y | (cited, kawasaki-2026-supplemental) |
| Vaporiser type | **Open-Rack Vaporiser (ORV)**, seawater heat source | large heat source required to vaporize LH2 | (cited, reply Q17) |
| Alternative heat source | **Dedicated heat-source system** | if nearby aquaculture constrains cold-seawater discharge | (cited, reply Q17) |
| Regas heat duty | **≈3.8 MJ/kg-LH2** | — | (cited, reply Q18) |
| FSU / ship-to-ship | Same as §5 — not yet specifically considered | — | (cited, reply Q25) |
| Receiving-terminal CapEx, USD/kg | **[GAP — not disclosed]** | only aggregate IAE cost stack available | — |

---

## 7. Chain-wide cost stack (IAE basis, via KHI)

**Source & caveats (read before using):** KHI reproduces a per-component
carrier-cost comparison attributed to *IAE (Institute of Applied Energy),
Gigaton Workshop, WHTC 2019 (6 May 2019)* — this is **second-hand**; the
primary IAE publication is not held in this repo, and the **axis on KHI's
slide is unlabelled**. Magnitudes are consistent with the METI/IAE
¥/Nm³ hydrogen supply-cost framing used elsewhere in Japanese hydrogen
policy work, so the unit is carried as **JPY/Nm³, ~2019 vintage**, but this
is **[needs source: primary — unit/cost-year unverified]**. **Do not use
these figures for a USD/kg LCOH without verifying the unit and cost-year
against the primary IAE source.**

Three scale/technology scenarios, deal volumes per KHI:

- **Base** = 2.5 billion Nm³/y
- **Large scale** = 10 billion Nm³/y
- **Tech** = 10 billion Nm³/y **with** a technology step-up: larger liquefier
  trains (115→150 tpd), higher-speed vessel (16→25 knot), larger storage
  tank (up to 200,000 m³)

| Component (JPY/Nm³, ~2019) | LH2 Base | LH2 Large | LH2 Tech |
|---|---|---|---|
| Production (H2 supply) | 10.1 | 10.1 | 9.3 |
| Liquefaction | 10.3 | 10.0 | 8.6 |
| Loading terminal | 5.6 | 1.9 | 1.8 |
| Seaborne transport | 4.0 | 4.0 | 2.3 |
| Receiving terminal | 6.3 | 3.4 | 2.8 |
| Cracking / dehydrogenation | 0.0 | 0.0 | 0.0 |
| Other / distribution | 1.3 | 1.3 | 1.3 |
| **TOTAL** | **37.6** | **30.7** | **26.1** |

For reference, KHI's slide also carries the equivalent **MCH** and **NH3**
stacks at Base/Large scale (same source and unit caveats) — reproduced here
because they frame KHI's own LH2-vs-alternatives argument in §8:

| Component (JPY/Nm³, ~2019) | MCH Base | MCH Large | NH3 Base | NH3 Large |
|---|---|---|---|---|
| Production/Synthesis feed | 10.3 | 10.3 | 10.9 | 10.9 |
| Conversion (hydrogenation/synthesis) | 5.5 | 5.4 | 10.3 | 9.6 |
| Loading terminal | 0.4 | 0.2 | 0.4 | 0.2 |
| Seaborne transport | 4.0 | 3.9 | 3.2 | 3.2 |
| Receiving terminal | 1.0 | 0.7 | 1.3 | 1.0 |
| Cracking / dehydrogenation | 12.7 | 12.7 | 8.9 | 8.6 |
| Other / distribution | 1.3 | 1.3 | 1.3 | 1.3 |

**Reading, per KHI's own framing:** LH2 has **no reconversion-step cost**
(cracking/dehydrogenation = 0), unlike NH3 and MCH, and its total cost
**falls faster with scale** (Base 37.6 → Large 30.7 → Tech 26.1) than the
other carriers shown. This is KHI's argument for LH2 competitiveness — carry
it as KHI's position, not as an independently verified LCOH comparison,
given the unit/cost-year caveat above.

---

## 8. LH2 vs. NH3 vs. MCH — qualitative position (KHI's view)

| Dimension | LH2 | NH3 | MCH |
|---|---|---|---|
| Toxicity | None | **Toxic** — needs hazard abatement (water-spray, gas detectors, evacuation zones) at receiving terminal | Toluene toxicity at carrier stage |
| Reconversion step at destination | **None** | Cracking + purification required | Dehydrogenation + purification required |
| Energy/process penalty | Extreme refrigeration (~20 K) + high electrical power for liquefaction | Ammonia synthesis + cracking energy | Hydrogenation + dehydrogenation energy |
| Safety footprint | **Non-toxic but flammable high-pressure gas** → larger safety exclusion/separation zones | Toxic-gas evacuation zones | Toluene flammability/toxicity |
| Energy efficiency (well-to-x) | Reported **5–35% lower** than comparator pathways depending on stage (see note) | — | — |
| CO₂ during marine transport | Can approach **zero during navigation** by using BOG as carrier propulsion fuel | — | — |
| KHI's overall position | *"LH2 is not as lacking in competitiveness nor as challenging as often assumed"* — advocated for **earlier introduction**, not a rejection of NH3 | KHI: not dismissing ammonia as a future fuel | — |

**Note on the energy-efficiency deltas (5–35% figures):** these are
attributed by KHI to *IEA Global Hydrogen Review 2022*; the CO₂ comparison is
attributed to *IEA, April 2023, "Towards hydrogen definitions based on their
emissions intensity."* Both are **cited by KHI, second-hand**; primary IEA
documents are not yet held in this repo *(cited, kawasaki-2026-comparison)*.

**Ammonia-as-fuel technical constraints** (KHI's supporting context, not
LH2-specific): ammonia combustion needs larger combustors for stable, complete
combustion; large gas turbines with >10 closely-spaced combustors cannot
simply swap to ammonia-compatible combustors without redesign — cited from a
Feb 2025 Hanwha/Baker Hughes ammonia gas-turbine JDA example
*(cited, kawasaki-2026-comparison)*.

---

## 9. Disclosure-gap register (critical for investment screening)

These are figures Gentari asked for and KHI **explicitly declined to
provide** pending a Feasibility Study. They are **not zero, not estimated —
they are open**:

| # | Gap | Segment | KHI's stated reason |
|---|---|---|---|
| 1 | CapEx, USD/kg | Liquefaction | "cost varies depending on the plant size" |
| 2 | OpEx, USD/kg | Liquefaction | same |
| 3 | Carbon intensity, kgCO₂e/kg (with RE) | Liquefaction | same |
| 4 | PFD / heat & mass balance | Liquefaction | shareable only "at Feasibility Study timing" |
| 5 | Newbuild cost, USD/vessel (160,000 m³) | Shipping | premium over LNG only qualified qualitatively |
| 6 | Export/receiving terminal CapEx, USD/kg | Terminals | not separately broken out; only the aggregate, unit-unverified IAE stack exists |
| 7 | LH2 import-terminal permitting detail outside Japan | Cross-cutting | "does not yet have detailed regulatory/permit information for LH₂ import terminals" |
| 8 | Malaysia government subsidy/support specifics for NH3/LH2 | Commercial (Gentari↔KHI mutual Q&A) | left unanswered in both questionnaire rounds |

**Implication for any techno-economic model built on this database:** technical
KPIs (energy, losses, fleet sizing, BOR) can be modeled today directly from
KHI's disclosed figures. A full **USD/kg LCOH cannot be produced from KHI
data alone** — CapEx/OpEx must come from a Feasibility Study, a comparable
OEM benchmark (with the user's explicit permission per **CLAUDE.md §4** source
hierarchy), or be supplied as a tagged `[ASSUMPTION]` at the point of use.

---

## 10. KHI corporate / track-record snapshot

- Kawasaki Heavy Industries, Ltd. — FY ended 31 Mar 2023: revenue **¥1,725.6
  billion (≈USD 11,920.7 million)**; **38,254 employees**; 103 consolidated
  subsidiaries *(cited, kawasaki-hydrogen-activities)*.
- LH2 track record: **Suiso Frontier** (world's first LH2 carrier, 1,250 m³)
  completed a demonstration voyage Hastings, Australia → Kobe, Japan,
  Dec 2021–Feb 2022, under the CO₂-free Hydrogen Energy Supply-chain
  Technology Research Association (**HySTRA**) pilot project
  *(cited, kawasaki-hydrogen-activities)*.
- KHI's own scale-up roadmap: pilot (1,250 m³ × ~1) → commercialization
  demonstration (~2025, 2,500 m³-class) → commercial chain (~2030,
  160,000 m³ × 2 carriers) → further scale-up toward 2050, with **indicative
  CIF cost figures of ¥170/Nm³ (pilot) → ¥30/Nm³ (2030 commercial) → ¥20/Nm³
  (~2050)** *(cited, kawasaki-hydrogen-activities)* — **note: this CIF figure
  is a different KHI-internal roadmap estimate from the IAE stack in §7; do
  not mix the two without reconciling basis/vintage.*
- Full supply-chain scope KHI markets: production (electrolysis/fertiliser-
  plant hydrogen) → liquefaction → LH2 carrier/tank/container → loading arm →
  end-use (hydrogen gas turbines, gas engines, fuel-cell trains, hydrogen
  boilers) *(cited, kawasaki-hydrogen-activities)*.

---

## 11. Source register

| ID | Document | Date | Tier |
|---|---|---|---|
| `kawasaki-2026-questionnaire` | Gentari→KHI Liquid H2 Questionnaire, KHI reply (Rev.1) | 31 Mar / 6 Apr 2026 | Proprietary |
| `kawasaki-2026-questionnaire-r0` | Same questionnaire, earlier reply (superseded) | 4 Mar 2026 | Proprietary |
| `kawasaki-2026-supplemental` | Supplemental Information — Comparison between LH2 and other Carriers of Hydrogen (KHI2605 R0) | May 2026 | Proprietary |
| `kawasaki-2026-comparison` | Comparison between LH2 and other Carriers of Hydrogen (KHI2604 R1) | Apr 2026 | Proprietary |
| `kawasaki-hydrogen-activities` | Kawasaki's Hydrogen Activities (corporate overview) | May 2024 | Proprietary |
| `iae-2019-gigaton` | Institute of Applied Energy, Gigaton Workshop, WHTC 2019 | 6 May 2019 | Institutional (second-hand via KHI) |

Full machine-readable register with file paths: `data/references.csv`.
Full per-parameter database (CSV, tidy schema): `data/properties/`,
`data/vessels/`, `data/costs/` — see `data/README.md` for the schema and tag
rules. This PDF is a synthesized, narrative rendering of those same tables
for reading and sharing; the CSVs remain the source of truth for modeling.

---

*Generated from the Gentari-LH2 repository. Every figure above traces to
§11. No figure in this document is estimated or fabricated — gaps are
recorded as such in §9.*
