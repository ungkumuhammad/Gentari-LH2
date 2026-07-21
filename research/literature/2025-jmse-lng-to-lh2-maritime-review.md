# Source dossier — *From LNG to LH2 in Maritime Transport: A Review of Technology, Materials, and Safety Challenges*

> **Prepared by:** Zane (LH2 research sub-agent) · **Date:** 2026-07-21
> **Source type:** peer-reviewed review article (open access) · **Tier:** journal
> **Scope of this dossier:** LH2 maritime transport — cryogenic handling,
> containment **materials**, hydrogen **embrittlement**, and **safety**, framed
> against established **LNG** practice. Covers value-chain segments **3 (storage),
> 4 (shipping), 5 (regas/handling)**.
> **Units:** SI per [`../../docs/conventions.md`](../../docs/conventions.md).
> **Rule:** every figure is cited or tagged — no fabricated numbers (`../AGENT.md` §3).

---

## ⚠️ Access note (read first)

The full text could **not be retrieved in this environment**: the network egress
policy blocked MDPI, doi.org, and the scholarly metadata APIs (Crossref /
OpenAlex) with HTTP 403, and per the proxy policy those blocks must be reported,
not routed around. **This dossier is therefore built from the article's
metadata, abstract, and indexed excerpts** (verified across MDPI's own listing,
the DOI record, and ResearchGate). Every claim below that is attributed to the
paper was found in those excerpts. **Quantitative property/BOG numbers that could
not be confirmed as this paper's own are listed separately under
"Full-text extraction pending" and are NOT attributed to it.**

➡️ **To complete this dossier:** drop the PDF into
[`../../sources/raw/`](../../sources/raw/) (it becomes proprietary-tier precedence
per `CLAUDE.md` §7e) and Zane will do a full, correctly-attributed
section-by-section extraction and propose promotions into `../../data/`.

---

## 1. Citation

- **Title:** From LNG to LH2 in Maritime Transport: A Review of Technology,
  Materials, and Safety Challenges
- **Authors:** Matteo Passalacqua; Alberto Traverso
  *(affiliations not captured from excerpts — confirm from full text)*
- **Venue:** *Journal of Marine Science and Engineering* (JMSE), MDPI —
  **Vol. 13, Issue 9, Article 1748**
- **Published:** **10 September 2025**
- **DOI:** `10.3390/jmse13091748` · **Open access:** yes
- **Link:** https://doi.org/10.3390/jmse13091748
- **staging.csv id:** `jmse-2025-lng-to-lh2-review`

---

## 2. What the paper is (scope & approach)

- A **review** of the operational requirements and challenges of **LH2 cryogenic
  handling systems**, deliberately using mature **LNG practice as the reference
  baseline** — i.e. what transfers from LNG to LH2 and what does not
  (Passalacqua & Traverso, 2025).
- Central comparison axes: **cryogenic materials**, **hydrogen embrittlement**,
  and **structural integrity under maritime conditions** (Passalacqua & Traverso,
  2025).
- Motivating context cited by the paper: LNG is already used to cut GHG/NOx/SOx
  emissions, while LH2 is new to the maritime sector and leans on **aerospace**
  experience; e.g. a 2018 proposal (Jeong et al.) for an **LNG–LH2 hybrid
  propulsion** system on an LNG tanker to cut CO₂ and meet future GHG rules
  (as cited in Passalacqua & Traverso, 2025).

---

## 3. Key findings (attributable to this paper)

### 3.1 Containment materials
- **Most maritime-approved materials are suitable for cryogenic use**
  (Passalacqua & Traverso, 2025).
- **Recommended baseline:** **austenitic stainless steels**, particularly
  **AISI 316** (EU designation **X5CrNiMo17-12-2**) and its low-carbon variant
  **316L** (**X2CrNiMo17-12-2**) — already well known to the maritime industry
  (Passalacqua & Traverso, 2025).
- **Titanium and nickel alloys** are also suitable at cryogenic temperature **but
  suffer enhanced hydrogen embrittlement** (attributed to their crystal-lattice
  configuration) **and carry significantly higher cost** (Passalacqua & Traverso,
  2025).

### 3.2 Hydrogen embrittlement
- **Hydrogen embrittlement is *less* critical at cryogenic temperatures**, because
  **reduced atomic mobility** limits hydrogen diffusion into the lattice
  (Passalacqua & Traverso, 2025). → Practically: the embrittlement worry for LH2
  containment is smaller at ~20 K than intuition (from ambient-temperature H2
  service) suggests, shifting the materials question toward cost and code
  acceptance rather than embrittlement per se.

### 3.3 Safety / risk posture
- **LH2's favourable safety record reflects limited operational data, not
  inherently superior safety** — risk assessments should not over-read the
  scarce incident history as proof of safety (Passalacqua & Traverso, 2025).
  → A conservative, evidence-honest framing that aligns with this repo's own
  data-discipline stance.

---

## 4. Relevance to this repo / OKR

| Where it plugs in | Use |
|-------------------|-----|
| **KR1.2 — LH2 shipping functional-requirements spec** | Materials baseline (316/316L austenitic SS) and the "LNG-practice-as-reference" framing are directly useful for the spec's containment & handling requirements. |
| **KR1.3 — LH2-vs-NH3 comparison, safety/permitting dimension** | The "safety record ≠ inherent safety / limited data" point is a citable, balanced input for the safety read (counterweight to over-optimistic LH2 safety claims). |
| **Segment 3–5 methodology** (`../../docs/methodology/`) | Embrittlement-vs-temperature nuance and material selection rationale. |
| **Cross-check vs KHI data** | KHI (in-repo, proprietary) uses double-wall vacuum-insulated tanks; this paper's LNG-reference materials/insulation discussion is an independent public cross-reference (do not merge numbers without full-text confirmation). |

---

## 5. Full-text extraction pending (NOT yet attributed to this paper)

These items appeared in the broader search around this paper's topic but could
**not be confirmed as this paper's own values** without the blocked full text.
They are recorded here as **extraction targets only** — deliberately *not* cited
to Passalacqua & Traverso (2025), and *not* to be used as numbers until confirmed:

- [ ] LH2 vs LNG **boil-off rate** (%/day) comparison and any stated **insulation
  thickness multiplier** to bring LH2 BOR to LNG-carrier standard.
- [ ] LH2 vs LNG **physical-property table** (NBP, density, volumetric heat of
  vaporisation, volumetric energy density) as stated *by this paper*.
- [ ] **Tank-type** taxonomy (Type A/B/C, membrane) applicability to LH2 and the
  role of **vacuum insulation / MLI**.
- [ ] Any **BOG-management / reliquefaction / regasification** and **bunkering**
  specifics.
- [ ] The paper's **reference project** set (Suiso Frontier, Kawasaki designs) and
  **standards** references.

_(For established LH2 physical constants the repo already holds sourced/tagged
values in [`../../data/properties/lh2-properties.csv`](../../data/properties/lh2-properties.csv)
and `conventions.md` — use those, not unconfirmed numbers, in the interim.)_

---

## 6. Promotion candidates

- **None promoted.** No figure from this dossier is proposed for `../../data/`
  yet — the strongest content (materials recommendation, embrittlement-vs-temperature,
  safety framing) is **qualitative**. Once the PDF is available, the materials
  guidance (316/316L baseline) is a good candidate for a `data/`-level
  containment-materials note for the KR1.2 spec, and any confirmed BOR/property
  numbers can be assessed against the repo's existing rows.

---

## Sources

| id | citation | tier | url/doi | accessed |
|----|----------|------|---------|----------|
| jmse-2025-lng-to-lh2-review | Passalacqua, M.; Traverso, A. *From LNG to LH2 in Maritime Transport: A Review of Technology, Materials, and Safety Challenges.* J. Mar. Sci. Eng. 2025, 13(9), 1748. | journal | https://doi.org/10.3390/jmse13091748 | 2026-07-21 |
