# LH2 vs NH3 — node-by-node energy-penalty method

> **System boundary:** electrolyser battery limit (node A) → hydrogen delivered as
> gas at the import-terminal send-out flange (node F1 for LH2, F2 for NH3).
> Well-to-gate. Distribution and end-use (segment 6) are excluded.
> **Basis:** every cascade is computed per 1 kg H₂ produced at node A, then
> scaled to the study's annual supply — **100 ktpa H₂ at node A** by default
> (§6a). **Units:** energy kWh (MJ alongside), mass kg, BOR %/day.
> **Cost:** out of scope in this build — energy only, so no currency and no
> cost-year.
> **Key assumption up front:** *no ammonia figure in this build is sourced* —
> every NH₃ value is a placeholder pending the internal Gentari dataset
> (decision D4). See [Defaults](#defaults-and-their-tags).
>
> Created 2026-09-01 · KR1.3 (milestone M3.5, end-to-end energy)
> Updated 2026-09-02 — annual scale & fleet sizing, 40,000 m³ vessels for both
> carriers, natural-gas-fired cracker (see §6a/§4).

---

## 1. What this answers

Both chains start from the same hydrogen. The question is what each *carrier*
costs to move that hydrogen to an import terminal — in energy drawn to run the
chain, and in hydrogen that never arrives.

| # | LH2 chain | NH3 chain |
|---|-----------|-----------|
| A | H₂ production (electrolysis) | *(same node — shared)* |
| B | **B1** Liquefaction | **B2** Ammonia synthesis (Haber–Bosch) |
| C | **C1** Export terminal & storage | **C2** Export terminal & storage |
| D | **D1** LH2 shipping | **D2** NH3 shipping |
| E | **E1** Import terminal & storage | **E2** Import terminal & storage |
| F | **F1** Regasification | **F2** Cracking + purification |

Node A is shared, so it cancels out of the comparison — but it sets the scale of
everything downstream, which is why the model still shows it.

## 2. Deliverables

| Artifact | What it is |
|----------|------------|
| [`docs/reports/lh2-vs-nh3-energy-penalty.html`](../reports/lh2-vs-nh3-energy-penalty.html) | Interactive ledger: editable inputs on every node card, two cascade charts, node ledger, live gap list, assumption register. Published as a Claude Artifact. |
| [`src/lh2/chain_energy.py`](../../src/lh2/chain_energy.py) | The model. Same math as the HTML, node for node. |
| [`scripts/run_chain_comparison.py`](../../scripts/run_chain_comparison.py) | CLI (`--json` for machine-readable output). |
| [`data/carriers/chain-energy-defaults.csv`](../../data/carriers/chain-energy-defaults.csv) | Every default, cited or tagged, in the repo's standard tidy schema. |
| [`tests/test_chain_energy.py`](../../tests/test_chain_energy.py) | 80 tests, including one that fails if a Python default ever drifts from the CSV. |

## 3. Two ways to read the same cascade

Both are computed from the same per-node energy and mass figures.

**(a) Input basis — chain efficiency.**

```
η = (H₂ delivered × LHV) ÷ (Σ energy consumed by every node)
```

At node A alone this is the user's worked example: 33.33 ÷ 60 = **55.6 %**, a
penalty of 26.67 kWh/kg. Carrying liquefaction in: 33.33 ÷ 69 = **48.3 %**.

**(b) Deduction basis — energy retained.**

Start with the 33.33 kWh of chemical energy in the 1 kg produced; subtract every
*downstream* node's energy draw and the heating value of every kg lost:

```
net = 33.33 − Σ(carrier-chain energy) − (kg H₂ lost × 33.33)
```

This is the "what does the carrier itself cost me" reading. It excludes node A's
own inefficiency, which both chains share.

## 4. Node mechanics

Each node takes a cut in one of two currencies, and the distinction matters:

- **Energy drawn** — external electricity or heat consumed to run the node. Adds
  to the input side.
- **Hydrogen lost** — H₂ that physically leaves the chain (boil-off burned as
  fuel, purge gas, cracker self-consumption). Removes mass *and* its heating value.

Mass is tracked as **H₂-equivalent** throughout, so the ammonia leg is directly
comparable. Physical ammonia tonnage = H₂-equivalent × 5.632.

### Formulas

| Quantity | Formula | Note |
|----------|---------|------|
| Boil-off over a hold | `1 − (1 − BOR)^days` | Compounding, not linear — each day's boil-off leaves less inventory. Same treatment as `src/lh2/storage.py`. |
| Voyage duration | `distance ÷ speed ÷ 24` | One-way laden leg. |
| NH₃ per H₂ (mass-balance floor) | `(2 × 17.031) ÷ (3 × 2.016) = 5.632 kg/kg` | N₂ + 3 H₂ → 2 NH₃. First-principles; molar masses are standard values with no citation logged. This is the *pure stoichiometric* floor — see `nh3_supply_ratio()` below for the operative, higher ratio. |
| Cracker reaction duty | `(2/3) × 45.9 kJ/mol × 496.03 mol/kg = 15.2 MJ/kg` | = 4.22 kWh per kg H₂ = 12.7 % of H₂'s LHV. Since 2026-09-02 this **is charged**, as purchased natural gas (see below) — it is no longer a self-consumption floor. |
| Round-trip cycle | `2 × (distance ÷ speed ÷ 24) + 2 × port days/call` | Reuses `src/lh2/shipping.py`'s `round_trip_days()`. |
| Fleet size | `ceil(annual cargo ÷ (cargo/voyage × trips/year))` | Reuses `src/lh2/shipping.py`'s `fleet_size()`; cargo/voyage = vessel capacity × fill fraction × density. |

### Three deliberate modelling choices

1. **Regas heat is not charged.** KHI's 3.8 MJ/kg-LH₂ (reply Q18) is ambient
   seawater heat through an ORV. It is reported as a thermal duty but never added
   to the input energy, because nobody buys it. Only the derived pump work
   (cryogenic pump to send-out pressure + seawater circulation) is charged.
2. **LH2 voyage BOG is mass, not energy.** KHI burns it in a dual-fuel engine and
   adopts no onboard re-liquefaction (replies Q23/Q33), so it leaves the chain as
   hydrogen. Ammonia's voyage BOG defaults the other way (re-liquefied → energy),
   with a switch in the tool because that disposition is itself a placeholder.
3. **The cracker is natural-gas-fired (2026-09-02), the opposite of choice 1.**
   The reaction floor above *is* charged as purchased NG energy (scaled by a
   fired-heater efficiency), because — unlike ambient seawater — natural gas is
   a real fuel someone buys and burns. Mass loss at node F2 drops to a small
   PSA/purification slip only; no product H₂/NH₃ is combusted for heat. The
   ammonia chain instead pays its extra mass penalty at **node D2**, where
   ammonia burned as the carrier's own marine fuel (`nh3_bunker_fuel_rate_pct_per_day`,
   linear in voyage days, always lost — never re-liquefied) is calibrated so the
   ratio of physical NH₃ produced to H₂ ultimately delivered lands near the
   user's target of **~6.5 : 1**, above the pure mass-balance floor of 5.632 : 1.
   `nh3_supply_ratio()` reports this ratio for verification on every run.

## 5. Defaults and their tags

Full table with provenance: [`data/carriers/chain-energy-defaults.csv`](../../data/carriers/chain-energy-defaults.csv).

**LH2 side — the cited spine:**

| Node | Parameter | Default | Tag |
|------|-----------|---------|-----|
| B1 | Liquefaction SEC | 9 kWh/kg (range 8–9) | cited — `kawasaki-2026-questionnaire` Q1 |
| B1 | H₂ loss | 0 % | cited — reply Q15 |
| C1/E1 | BOR at rest | 0.1 %/day | cited — `kawasaki-2026-supplemental` |
| D1 | Vessel capacity | 40,000 m³ | **cited** — reply Q29 (vessel under construction, same tank tech as Suiso Frontier) |
| D1 | Service speed | 29.6 km/h | cited — `kawasaki-2026-supplemental`, disclosed for the 160,000 m³ commercial vessel, reused as no separate figure exists for 40,000 m³ |
| D1 | BOG disposition | burned as propulsion fuel | cited — replies Q23/Q33 |
| D1 | Cargo fill / port time | 98 % / 1.25 d | fill **ASSUMPTION**; port time **cited** — reply Q27 midpoint |
| F1 | Regas heat duty | 3.8 MJ/kg | cited — reply Q18 |
| C1/E1 | BOG re-liquefaction SEC | 3.94 kWh/kg | **ASSUMPTION: derived** — 0.438 × liquefaction SEC, the ratio of condensation-only ideal work (1.71) to fresh-feed para-basis ideal work (3.9 kWh/kg, `doe-2009-h2-liquefaction-energy`) |
| F1 | Regas electrical draw | 0.031 kWh/kg | **ASSUMPTION: derived** — pump work at 30 barg/30 °C send-out |
| D1 | Voyage BOR | 0.2 %/day | **ESTIMATE – needs source** — KHI discloses none |
| A | Electrolyser SEC | 60 kWh/kg | **ASSUMPTION** — user-specified; production is outside KHI's scope |
| — | Shipping distance | 6,000 km | **ASSUMPTION** — no corridor fixed (D1) |
| — | Annual H₂ supply | 100 ktpa | **ASSUMPTION** — user-specified study basis (2026-09-02), anchored at node A |
| — | Fleet availability | 90 % | **ASSUMPTION** — shared by both fleets, same convention as `src/lh2/shipping.py` |

**NH3 side — every value a placeholder (decision D4):**

| Node | Parameter | Default | Tag |
|------|-----------|---------|-----|
| B2 | Synthesis SEC | 0.60 kWh/kg-NH₃ (range 0.5–0.7) | ESTIMATE – needs source |
| B2 | H₂ purge loss | 2 % | ESTIMATE – needs source |
| B2 | NH₃ per H₂ | 5.632 kg/kg | ASSUMPTION — first-principles stoichiometric floor |
| C2/E2 | BOR at rest | 0.04 %/day | ESTIMATE – needs source |
| C2/D2/E2 | BOG re-liquefaction SEC | 0.25 kWh/kg-NH₃ | ESTIMATE – needs source |
| D2 | Vessel capacity | 40,000 m³ | ESTIMATE — user-specified (2026-09-02) mid-size ammonia/LPG carrier, not KHI-specific |
| D2 | Service speed | 30 km/h | ESTIMATE – needs source |
| D2 | Ordinary voyage BOR | 0.04 %/day | ESTIMATE – needs source |
| D2 | **Bunker fuel rate** | 1.3 %/day | **ESTIMATE** — new (2026-09-02); ammonia burned as marine fuel, calibrated to the ~6.5:1 supply ratio (§4, choice 3) |
| D2 | Cargo fill / port time | 98 % / 1.25 d | ESTIMATE — placeholders, matched to the LH2 side |
| F2 | **NG-fired efficiency** | 85 % | **ASSUMPTION** — new (2026-09-02); typical industrial fired-heater efficiency |
| F2 | **Process loss (PSA slip)** | 3 % of H₂-equivalent | **ESTIMATE** — replaces the pre-2026-09-02 20 % self-consumption default |
| F2 | Cracker electrical draw | 0.5 kWh/kg | ESTIMATE – needs source |

## 6. Result at the defaults

Per 1 kg H₂ produced at node A, 60 kWh/kg electrolyser, 6,000 km:

| | LH2 | NH3 |
|---|-----|-----|
| H₂ delivered | 0.9832 kg | 0.8476 kg |
| Total energy in | 69.07 kWh (248.7 MJ) | 68.09 kWh (245.1 MJ) |
| Energy per kg **delivered** | 70.25 kWh/kg | 80.33 kWh/kg |
| Chain efficiency (input basis) | **47.5 %** | **41.5 %** |
| Energy retained (deduction basis) | 23.70 kWh — 71.1 % of LHV | 20.16 kWh — 60.5 % of LHV |
| Ammonia supply ratio (`nh3_supply_ratio()`) | — | **6.51 : 1** (mass-balance floor 5.63 : 1) |

**How to read it (updated 2026-09-02 for the NG-fired cracker).** LH2 still pays
almost entirely in *energy*, once, at the liquefier (9 of its 9.63 kWh carrier
penalty is node B1). Ammonia now pays in **two** currencies instead of one: a
modest synthesis energy (3.31 kWh at B2) plus a **charged NG-thermal energy at
the cracker** (4.86 kWh — the 4.22 kWh/kg reaction floor at 85 % fired
efficiency), *and* a mass penalty during shipping (node D2), where ammonia
burned as the carrier's own bunker fuel is the mechanism behind the ~6.5:1
ammonia-to-delivered-H₂ ratio. The net effect of moving the cracker onto
natural gas: NH3's total energy draw is now close to LH2's (68.09 vs 69.07 kWh)
rather than clearly lower as in the pre-2026-09-02 self-consumption framing,
because the reaction heat that used to be "free" (paid for in lost product H2)
is now an explicit, charged purchase.

**This is not a cost ranking.** Cheap electricity/gas at the export end and
expensive energy at the import end can invert the conclusion. Cost lives in
`src/lh2/scenario.py`; this model is energy only.

## 6a. Annual scale & fleet (new, 2026-09-02)

The per-kg cascade above is the normalized basis. `annual_scale()` (Python) /
`annualScale()` (HTML) multiply it by the study's `annual_h2_supply_ktpa`
(default 100 ktpa at node A) and size the shipping fleet, reusing
`src/lh2/shipping.py`'s `round_trip_days()`/`fleet_size()` so the fleet math
never diverges from the rest of the repo.

| | LH2 (40,000 m³) | NH3 (40,000 m³) |
|---|---|---|
| Annual energy | 6.907 TWh/y | 6.809 TWh/y |
| Annual H₂ delivered | 98.3 kt/y | 84.8 kt/y |
| Annual cargo shipped | 100.0 kt/y (LH2 mass) | 551.9 kt/y (physical NH3 mass) |
| Cargo per voyage | 2,775 t (40,000 m³ @ 98 % fill, 70.8 kg/m³) | 26,734 t (40,000 m³ @ 98 % fill, 682 kg/m³) |
| Round-trip cycle | 19.39 d | 19.17 d |
| Trips / year / vessel | 16.9 | 17.1 |
| **Fleet size required** | **3 vessels** | **2 vessels** |

Ammonia needs far fewer, far larger-tonnage voyages than LH2 for the same H₂
throughput, because liquid ammonia is ~10× denser than LH2 (682 vs 70.8 kg/m³)
even though both vessels share the same 40,000 m³ hull size — so despite
shipping 5.5× the physical tonnage (NH3 carries its own nitrogen), NH3 needs a
*smaller* fleet at this scale.

## 7. Known gaps

1. **The whole ammonia column is unsourced** (D4). Read the NH3 result as a
   structure to fill in, not as an answer.
2. **Voyage BOR (D1) is a placeholder** — the single largest LH2 mass loss in the
   chain rests on it. KHI ties fuel-gas consumption to the BOR but never
   discloses the rate. An unpromoted public figure (~3.44 %/day, RSER 2026) sits
   in `research/` and is deliberately not used here.
3. **BOG re-liquefaction SEC is derived**, assuming BOG handling matches the main
   liquefier's exergetic efficiency.
4. **Regas electricity is first-principles pump work** at an assumed send-out
   spec; validate against a real ORV pump curve.
5. **Haber–Bosch heat is not credited.** Synthesis is exothermic; recovering that
   heat as steam would lower the NH3 chain's net penalty below what is shown.
6. **The NG-fired cracker and ammonia bunker-fuel mechanism are both new
   placeholder mechanics (2026-09-02)**, not disclosed figures: the 85 % fired
   efficiency, the 3 % PSA/purification slip, and the 1.3 %/day bunker-fuel
   rate are all `[ASSUMPTION]`/`[ESTIMATE]`. Real ammonia-fuelled marine engines
   are not yet commercial at scale — the bunker-fuel mechanism is a *device* to
   reproduce the user's target ratio, not a validated shipping-fuel model.
7. **Natural gas combustion emissions** (CO2 from the cracker's own fuel) are
   outside this energy-only boundary and are not counted for either chain.
8. **Ammonia vessel capacity (40,000 m³) is not KHI-specific** — a user-specified
   mid-size placeholder; LH2's 40,000 m³ figure *is* cited (KHI reply Q29).
9. **Outside the boundary for both chains:** marine fuel beyond BOG/bunker,
   terminal utilities, jetty and loading energy, ammonia safety/abatement
   systems, and all distribution downstream of the send-out flange.
10. **H₂ LHV, molar masses, and the cracking reaction enthalpy** are standard
    values carried as `needs-source` pending a formal NIST/CODATA/ISO citation
    (`docs/memory.md` open item 4).

## 8. Running it

```bash
python scripts/run_chain_comparison.py
python scripts/run_chain_comparison.py --distance 5300 --electrolyser-sec 55
python scripts/run_chain_comparison.py --annual-supply 250 --lh2-vessel-capacity 160000
python scripts/run_chain_comparison.py --json | jq '.chains.NH3.efficiency_pct, .chains.NH3.annual_scale.fleet_size'
python -m pytest tests/test_chain_energy.py -q
```

Open `docs/reports/lh2-vs-nh3-energy-penalty.html` in a browser for the
interactive version. The HTML mirrors `chain_energy.py`; both read the same
defaults, and the test suite fails if they drift.

## 9. Sources

| Ref id | Used for |
|--------|----------|
| `kawasaki-2026-questionnaire` | Liquefaction SEC (Q1), no-loss claim (Q15), terminal BOG re-liquefaction (Q3), BOG-as-fuel and no onboard re-liquefaction (Q23/Q33), regas heat duty and ORV (Q17/Q18), 40,000 m³ vessel under construction (Q29), port time (Q27) |
| `kawasaki-2026-supplemental` | At-rest BOR 0.1 %/day both terminals; 160,000 m³ commercial-scale vessel speed 29.6 km/h (reused for the 40,000 m³ ship — no separate speed disclosed) |
| `doe-2009-h2-liquefaction-energy` | Ideal liquefaction work (3.3 / 3.9 kWh/kg) behind the derived BOG re-liquefaction SEC |
| `data/properties/lh2-properties.csv` | H₂ LHV 120 MJ/kg, LH2 density 70.8 kg/m³ (`needs-source`) |
| — | **No source exists for the ammonia column**, including the 40,000 m³ NH3 vessel, its 682 kg/m³ density, the NG-fired efficiency, or the bunker-fuel rate. Nothing external was pulled; D4 stands. |
