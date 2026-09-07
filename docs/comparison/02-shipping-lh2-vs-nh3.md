# LH2 (40,000 m³) vs Ammonia (24,000 m³) — Shipping Segment Comparison

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
