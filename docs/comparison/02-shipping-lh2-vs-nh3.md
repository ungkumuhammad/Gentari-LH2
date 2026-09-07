# LH2 (160,000 m³) vs Ammonia (24,000 m³) — Shipping Segment Comparison

> **Status:** first pass, 2026-09-07. **Boundary:** shipping only (nodes D1/D2
> of the six-node chain — see [`01-energy-penalty-method.md`](01-energy-penalty-method.md)
> for the full LH2-vs-NH3 chain model). This does **not** net out
> upstream production/liquefaction/Haber-Bosch losses — "annual H2-equivalent
> demand" here is the quantity handed to the ships at the export terminal, not
> the quantity leaving the electrolyser.
>
> **Units/currency:** SI/metric, no cost figures in this pass (shipping-only,
> economics not yet joined — see open items).
> **Corridor:** Kakinada, India → Hamburg, Germany.
> **Model:** [`scripts/run_shipping_comparison.py`](../../scripts/run_shipping_comparison.py),
> reusing [`src/lh2/shipping.py`](../../src/lh2/shipping.py).
> **Data:** [`data/vessels/lh2-carriers.csv`](../../data/vessels/lh2-carriers.csv),
> [`data/vessels/nh3-carriers.csv`](../../data/vessels/nh3-carriers.csv),
> [`data/routes/kakinada-hamburg.csv`](../../data/routes/kakinada-hamburg.csv).

## 1. Vessels compared

| | LH2 carrier | NH3 carrier |
|---|---|---|
| Capacity | 40,000 m³ | 24,000 m³ |
| Cargo condition | Cryogenic, ~20.3 K, ~1 bar(a) | Fully refrigerated, ~-33 °C, ~1 atm |
| Cargo density | 70.8 kg/m³ `[needs-source: NIST pending]` | 682 kg/m³ `[ESTIMATE]` |
| Fill fraction | 98% `[ASSUMPTION]` | 98% `[ASSUMPTION]` |
| Service speed | 29.6 km/h ≈ 16 kn `(kawasaki-2026-supplemental, cited)` | 24.076 km/h = 13 kn `[ASSUMPTION — user-specified]` |
| Port time/call | 1.25 d `(kawasaki-2026-questionnaire, cited, midpoint)` | 1.5 d `[ASSUMPTION — user-specified]` |
| Voyage boil-off | 0.2%/day `[ESTIMATE]` | 0.15%/day (range 0.1–0.2%) `[ASSUMPTION — user-selected]` |
| BOG handling | Burned as dual-fuel engine fuel → **cargo mass loss** (KHI reply Q23/Q33, cited) | Reliquefied on board → **energy cost, no mass loss** `[ASSUMPTION — user-specified]`, SEC not supplied — carried as a gap |

Note the fill-fraction, port-time, and 98% figures on the LH2 side are the
same placeholders already used in `src/lh2/chain_energy.py`; nothing here
reruns or contradicts that model, it isolates the shipping segment with the
user's specific 40k/24k vessel pairing.

## 2. Corridor distance

Kakinada→Hamburg is not in any distance table this environment could reach
(searoutes.com and similar calculators are blocked by the egress policy).
Both figures below are **first-principles great-circle waypoint sums** (not
a primary AIS/route-planning-tool figure) — `[ESTIMATE, needs source: primary
distance table]` if precision matters for a final economics run:

| Route | One-way distance | Basis |
|---|---|---|
| Via Suez Canal (classic route) | ≈10,260 km (≈5,540 NM) | reference only |
| **Via Cape of Good Hope** | **≈21,200 km (≈11,450 NM)** | **PRIMARY — user-selected, 2026-09-07** |

The Cape route was chosen deliberately: many carriers are currently avoiding
the Red Sea/Suez corridor given the security situation as of 2026, so this
reflects present operating reality rather than the historic shortest route.
The waypoint method was cross-checked against a public Karachi→Hamburg figure
surfaced by search (11,076 NM) — it matches a Cape routing of that pair to
within 2%, which independently confirms that public number is itself a Cape
figure, not Suez.

## 3. Headline result

| | Via Suez (10,260 km) | Via Cape (21,200 km, **primary**) |
|---|---|---|
| LH2 annual H2-eq./vessel | 28.2 M kg/y | **13.8 M kg/y** |
| NH3 annual H2-eq./vessel | 24.3 M kg/y | **12.2 M kg/y** |
| Fleet for 100 ktpa H2-eq. demand | 4 LH2 vs 5 NH3 | **8 LH2 vs 9 NH3** |
| Winner (per-vessel throughput) | LH2, by 1.16× | **LH2, by 1.13×** |

**At the stated vessel/route specs, LH2 wins on shipping throughput at every
distance tested (1,000–40,000 km)** — see the sensitivity table in §4. This
is *not* because LH2 carries more mass per voyage: at short distance the NH3
carrier's superior liquid density (682 vs 70.8 kg/m³) very nearly offsets its
smaller hull (16.0 M kg NH3 ÷ 5.632 stoichiometric ratio ≈ 2.85 M kg H2-eq.
per voyage vs LH2's 2.78 M kg H2/voyage before boil-off — NH3 is *slightly
ahead* on this metric alone). LH2 wins because of **turnaround speed**: its
faster service speed (16 vs 13 kn) and shorter port time (1.25 vs 1.5 d)
together give it more round trips per year, and that trip-frequency edge is
larger than NH3's small per-trip cargo edge.

The LH2 margin **narrows with distance** (1.16× at 10,260 km → 1.07× at
40,000 km) because LH2's voyage boil-off loss compounds over the longer laden
leg (2.85% lost at Suez distance, 5.80% at Cape distance) while NH3's
reliquefaction loses no cargo mass at all (its BOG becomes an energy cost
instead — not quantified here, see gaps). This is the mechanism behind the
sweet spot below.

## 4. Sensitivity sweep (annual H2-equivalent delivered per vessel, kg/y)

| Distance (km) | LH2 | NH3 | Winner |
|---:|---:|---:|:---:|
| 1,000 | 171.0 M | 144.8 M | LH2 |
| 2,500 | 94.9 M | 80.3 M | LH2 |
| 5,000 | 54.2 M | 46.1 M | LH2 |
| 7,500 | 37.8 M | 32.3 M | LH2 |
| 10,260 (Suez) | 28.2 M | 24.3 M | LH2 |
| 15,000 | 19.5 M | 17.0 M | LH2 |
| 21,200 (Cape) | 13.8 M | 12.2 M | LH2 |
| 25,000 | 11.7 M | 10.5 M | LH2 |
| 30,000 | 9.6 M | 8.8 M | LH2 |
| 40,000 | 7.1 M | 6.6 M | LH2 |

No crossover distance exists in the realistic 0–40,000 km range for these
vessel specs — **distance alone does not create a sweet spot for NH3 here.**
The real sweet-spot levers are the three parameters below, all of which are
currently unverified placeholders (D4).

## 5. Sweet spot — what would flip the result

| Lever | Current value | Breakeven (flips to NH3) | Read |
|---|---:|---:|---|
| LH2 voyage boil-off rate | 0.2%/day `[ESTIMATE]` | **0.60%/day** (Cape) / **1.23%/day** (Suez) | The single biggest swing factor. KHI never disclosed a voyage figure (only "fuel-gas rate = BOR"); the unpromoted RSER-2026 literature figure for a comparable vessel class is **~3.44%/day** — nearly 6× the Cape breakeven. If that literature figure is closer to reality than the placeholder, **NH3 wins decisively** (12.2 M vs LH2's 5.2 M kg H2-eq./vessel/y at Cape distance). This is the top-priority number to pin down (see open items). |
| NH3 service speed | 13 kn `[ASSUMPTION]` | **14.73 kn** (+1.7 kn) at Cape distance, LH2 at its default BOR | A realistic uplift — many refrigerated LPG/NH3 carriers this size run 15–17 kn. If the user's 13 kn figure is a conservative placeholder rather than a real charter-party speed, NH3 likely already wins in practice. |
| NH3 vessel capacity | 24,000 m³ `[ASSUMPTION]` | **≈27,060 m³** (+13%) at 13 kn, Cape distance | A modestly larger hull at the same speed closes the gap — cargo density means NH3 needs much less extra volume than LH2 would to gain the same throughput. |

**Reading the three together:** NH3's structural disadvantage in this
comparison is *not* volumetric — its density advantage already nearly
neutralizes the 40k-vs-24k hull-size gap. It loses on **speed and turnaround
cadence**, and LH2's advantage itself rests on an unverified 0.2%/day voyage
BOR assumption that could easily be too optimistic. **The comparison is far
more sensitive to the LH2 voyage boil-off rate than to anything about the
ammonia vessel** — that is where a real number would move this conclusion
the most.


## 5a. Boil-off as bunker fuel — the fuel balance (added 2026-09-07, 2nd pass)

User direction: the ammonia carrier burns **25 t/day VLSFO**; the LH2 carrier
burns its cargo boil-off instead. Test whether the boil-off actually covers
that duty — if it falls short, the LH2 carrier still buys VLSFO; if it
overshoots, the surplus leaves the ship having done no work. Then compare
**hydrogen given up as fuel** against **ammonia's re-liquefaction energy**,
pricing hydrogen as the premium fuel it is.

**Basis.** Both carriers are charged the same 25 t/day propulsion duty
`[ASSUMPTION — user-specified]`, over the **laden leg only** (ballast excluded
symmetrically, since that is where boil-off is generated). VLSFO LHV
40.2 MJ/kg `[ESTIMATE]`; H2 LHV 120 MJ/kg; BOG-vs-oil engine efficiency ratio
1.0 `[ASSUMPTION]`; NH3 re-liquefaction electricity converted to fuel at a 45 %
genset efficiency `[ASSUMPTION]`.

**Result at the Cape route, 0.2 %/day boil-off:**

| | LH2 carrier | NH3 carrier |
|---|---|---|
| Laden leg | 29.84 d | 36.69 d |
| Propulsion demand | 746 t VLSFO-eq | 917 t VLSFO-eq |
| Boil-off generated | 161.0 t H₂ (5.80 % of cargo) | 860 t NH₃ (re-liquefied, cargo kept) |
| Covered by boil-off | **64 %** (480 t VLSFO displaced) | 0 % |
| VLSFO still purchased | **266 t** | 917 t + 42.8 t re-liq = 960 t |
| Surplus vented | **none** | — |

**Finding 1 — at the working assumption, the boil-off does not cover the fuel
bill.** It covers 64 %, and the carrier still buys 266 t of VLSFO per leg.
Kawasaki's "fuel-gas consumption rate equals the BOR" does not close on its own
at 0.2 %/day.

**Finding 2 — the two regimes meet at 0.316 %/day** (Cape) / **0.308 %/day**
(Suez). Below it the ship buys fuel; above it the engine cannot absorb the
boil-off and the excess is disposed of. At the published RSER figure of
**3.44 %/day** the carrier generates **720 %** of what it can burn — 1,549 t of
hydrogen per leg, **86 % of the boil-off, doing no work at all**.

**Finding 3 — the premium-fuel penalty decides the economics.** Cost of one
laden leg per kg H₂ delivered, at VLSFO USD 600/t:

| H₂ valued at | LH2 carrier | NH3 carrier | Cheaper |
|---|---:|---:|---|
| $1.00/kg | $0.123 | $0.202 | LH2 |
| **$2.29/kg** | **$0.202** | **$0.202** | **parity** |
| $5.00/kg | $0.369 | $0.202 | NH3 |

**Breakeven hydrogen value ≈ USD 2.29/kg** (Cape) / **2.39/kg** (Suez) at
VLSFO USD 600/t, rising to ~$3.06/kg if bunker fuel reaches USD 800/t. Above
the breakeven the ammonia carrier is the cheaper way to move hydrogen: at
$5/kg, **83 % of the LH2 carrier's shipping cost is the hydrogen it burns**,
not the fuel it buys. The LH2 carrier runs on the most expensive thing it is
carrying.

**Prices are not sourced.** Neither the hydrogen value nor the bunker price is
logged in `data/references.csv`; both are live inputs in the artifact and the
study reports the breakeven rather than asserting a price.

**Surplus disposal — a discrepancy worth noting.** The user's framing is that
surplus boil-off is released to atmosphere. Kawasaki's reply Q26 instead
describes a **gas combustion unit** burning excess BOG above MARVS, which
oxidises it to water. The hydrogen is lost from the cargo either way and has no
fuel value beyond the propulsion cap — only the environmental line changes
(vented H₂ carries an indirect warming effect, ~11.6 kg CO₂e/kg on a 100-year
basis `[ESTIMATE]`; combusted H₂ does not). The artifact carries a toggle.

## 6. Explicit gaps (per CLAUDE.md §4 — nothing here is fabricated)

1. **LH2 voyage BOR (0.2%/day)** — KHI never disclosed a standalone figure.
   Placeholder only; the sweet-spot analysis above shows the whole result
   flips on this number. Highest-priority gap.
2. **NH3 onboard-reliquefaction SEC (kWh/kg)** — user confirmed the BOG
   disposition (reliquefied, not burned) but no energy figure was given.
   Carried as an unquantified energy cost, not zero — a real number would
   likely narrow NH3's per-vessel-throughput lead slightly further in an
   energy-inclusive comparison (it's currently absent from the mass-only
   metric used here).
3. **NH3 vessel speed, capacity, port time, BOR** — all `[ASSUMPTION]`
   pending the internal Gentari NH3 dataset (decision D4). Everything in §5
   changes if these are corrected.
4. **Corridor distance** — first-principles estimate, not a primary
   AIS/route-planning-tool figure (§2).
5. **No cost/CapEx in this pass** — this is a physical-throughput comparison
   only. LCOH-style shipping cost per kg H2 needs vessel day-rates/CapEx for
   both carrier types (none logged yet for either).
6. **Route choice (Cape vs Suez) is itself a live operational uncertainty**,
   not a fixed geographic fact, given the Red Sea security situation — both
   are carried in the data table for exactly this reason.
7. **The 25 t/day propulsion duty** is a user figure for the ammonia carrier,
   charged to the LH2 carrier as well so the two share one basis. The LH2
   vessel is a larger hull at ~23 % higher speed, so its real demand is
   probably higher — which would absorb more boil-off usefully *and* raise its
   top-up fuel bill. No power curve is held for either vessel.
8. **VLSFO LHV, genset efficiency, BOG-vs-oil engine efficiency, and the
   vented-H₂ warming potential** are all estimates or assumptions with no
   primary citation logged.
9. **Ballast leg excluded** from the propulsion-fuel charge for both vessels.

## 7. Open items for the user

1. Any real voyage BOR figure for a fully-refrigerated NH3 carrier and/or a
   confirmed LH2 voyage BOR would resolve the single biggest open question
   in this segment (§5, §6.1).
2. NH3 onboard-reliquefaction SEC (kWh/kg boil-off) — closes gap §6.2.
3. Confirm or correct NH3 speed (13 kn), capacity (24,000 m³), port time
   (1.5 d) against the internal dataset (D4) — small, quantified sensitivity
   already computed for each (§5).
4. Say when to join this to cost (CapEx/day-rate/OpEx) for an LCOH-style
   shipping cost per kg H2 comparison, and whether to fold this vessel
   pairing back into the full six-node `chain_energy.py` model (currently
   that model still uses a generic 40k/40k pairing, not this 40k/24k one).
5. Confirm the Kakinada→Hamburg distance with a primary source if this
   corridor becomes decision-relevant (§2, §6.4).


---

## 7. Third pass (2026-09-07): 160,000 m³ vessel and the boil-off cost basis

Four changes on user direction.

**7.1 The LH2 vessel is now the 160,000 m³ commercial-scale ship** (cited,
`kawasaki-2026-supplemental`), replacing the 40,000 m³ vessel under
construction. This is also more internally consistent: KHI's disclosed
29.6 km/h service speed was given for *this* ship.

| | LH2 160,000 m³ | NH3 24,000 m³ |
|---|---:|---:|
| Cargo loaded per voyage | 11,101 t LH2 | 16,041 t NH3 |
| Delivered per voyage, H2-eq | 10.46 M kg | 2.85 M kg |
| Annual per vessel, H2-eq | **55.2 M kg/y** | **12.2 M kg/y** |
| Fleet for 100 ktpa H2-eq | **2 vessels** | **9 vessels** |

One LH2 carrier does the work of **4.5** of the specified ammonia ships.
Matching it with a *single* ammonia vessel would take ~108,000 m³ at 13 kn or
~84,000 m³ at 17 kn — at or beyond the largest gas carriers in service
(~87,000 m³ for ammonia, ~93,000 m³ for any gas carrier)
`[ESTIMATE — vessel-class figures, not in this repository]`. The real choice
is between **a fleet of ordinary mid-size gas carriers and a pair of
purpose-built giants**, not between two ships.

Throughput parity now needs a boil-off rate **above 4.9 %/day** — higher even
than the RSER literature figure. On throughput the 160k ship wins decisively;
on cost it does not. The two criteria now point in opposite directions, which
is why both sets of studies are kept.

**7.2 The propulsion duty is now per carrier, and it is the weakest number in
the study.** 25 t/day is the ammonia vessel's figure. Carried across to a
160,000 m³ hull it produces a dramatic result — boil-off covers **258 %** of
demand, and 394 t of hydrogen per leg (61 % of the boil-off) has nowhere to
go. But that overshoot is substantially an artifact of the duty: at ~100 t/day,
roughly proportionate to the 4× cargo, coverage falls to **64 %** and the
surplus disappears entirely. **A design fuel rate for the 160k vessel is now
the highest-value missing input**, alongside the voyage BOR.

**7.3 Cost basis corrected to boil-off management only.** The previous pass
charged each carrier its whole leg fuel bill, which made the ammonia figure
(USD 0.202/kg) 96 % propulsion fuel — not a boil-off comparison at all. The
user's framing is right: with both ships on a common propulsion duty, the
comparison is **hydrogen given up as fuel vs the VLSFO burned to re-liquefy
ammonia BOG**. The default is now:

- **LH2** = hydrogen burned × H2 price, **credited** with the VLSFO that
  hydrogen displaced (746 t, USD 448k at USD 600/t). Without that credit the
  LH2 carrier would be charged for its boil-off while being given no recognition
  for the fuel it did not buy.
- **NH3** = re-liquefaction fuel only (42.8 t VLSFO, via a 45 % genset
  efficiency `[ASSUMPTION]`) = **USD 0.009/kg H2**.

| Basis | LH2 | NH3 | Breakeven H2 value |
|---|---:|---:|---:|
| Boil-off only (default) | USD 0.265/kg | USD 0.009/kg | **USD 0.84/kg** |
| Full leg fuel bill | USD 0.308/kg | USD 0.202/kg | USD 3.28/kg |

Both framings are kept as a toggle, because the two laden legs differ in
length (29.8 vs 36.7 d) so the propulsion term is **not** a clean common factor
that simply cancels. Under the boil-off-only basis the ammonia carrier is
cheaper at essentially any hydrogen value a project would book.

**7.4 Presentation.** Every chart legend now names its x and y parameters;
the boil-off fate chart states its basis explicitly and carries a per-leg /
per-day toggle (it was previously per laden leg, unlabelled); and the
throughput study is reframed from "what would make the ammonia ship win" —
which was unreadable against a 4.5× gap — to "how many ammonia ships equal one
LH2 carrier", sweeping ammonia capacity at three service speeds.


## 8. Fourth pass (2026-09-07): vessel scenario and H2-landed basis

**8.1 Both LH2 hulls are now selectable.** The 40,000 m³ vessel under
construction and the 160,000 m³ commercial-scale target are both KHI-cited,
and they tell materially different stories, so the choice is a first-class
control in the artifact (`--vessel 40k` on the CLI) rather than a buried input:

| At Cape, 0.2 %/day, 25 t/day duty | LH2 40,000 m³ | LH2 160,000 m³ |
|---|---:|---:|
| Boil-off vs propulsion demand | **64 %** — buys 266 t VLSFO | **258 %** — 394 t H₂/leg wasted |
| Fuel cover point | 0.316 %/day | 0.076 %/day |
| Boil-off cost per kg H₂ | USD 0.198 | USD 0.265 |
| Breakeven H₂ value | **USD 1.94/kg** | **USD 0.84/kg** |
| Annual per vessel | 13.8 ktpa | 55.2 ktpa |
| Ammonia ships per LH2 ship | 1.1 | 4.5 |

**8.2 Units.** Per-voyage masses are now kt, annual rates ktpa (1 M kg = 1 kt),
replacing "M kg" throughout — matching how the OKR's 100 ktpa basis is stated.

**8.3 What "H₂ landed" assumes — asked directly, so stated directly.**
For LH2 it is the cargo loaded less the laden-leg boil-off (that hydrogen is
burned as fuel and does not arrive). For ammonia it is the delivered ammonia
divided by the **pure stoichiometric ratio 5.632** — the hydrogen *chemically
contained* in the cargo landed, **assuming a cracker that recovers all of it**.
No cracking is modelled in this study, which stops at the discharge arm. A real
cracker returns less: the repository's whole-chain model
(`src/lh2/chain_energy.py`, node F2) carries a 3 % purification slip plus a
natural-gas-fired reaction duty of 4.22 kWh per kg H₂. **The ammonia figures in
this study are therefore an upper bound on hydrogen actually available at the
far end**, and joining this study to the cracker node is the obvious next step.
