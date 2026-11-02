# LH2 vs ammonia chain summary dashboard (one input: ktpa)

**File:** [`docs/reports/lh2-vs-ammonia-chain-summary.html`](../reports/lh2-vs-ammonia-chain-summary.html), a single self-contained page (Verdana, Gentari header with the logo as an embedded raster).
**Built:** 2026-10-27 to 2026-11-02 in the `taurusgentari` working session; formulas copied from the earlier artifact
[`lh2-vs-ammonia-energy-value-chain.html`](../reports/lh2-vs-ammonia-energy-value-chain.html) (Upstream, Shipping, Downstream, Full Chain, Case Study, Economics sheets) and checked against it at 100 ktpa with electrolysis on.

**System boundary:** electrolysis, upstream plant (liquefier or Haber-Bosch plus 60,000 m³ export tank), shipping (40,000 m³ carriers), downstream (ORV regas or ammonia cracker plus import tank). **Units:** GWh/y, USD M/y, kWh/kg H2 delivered. **Currency:** USD, no cost year stated (prices are inputs). **Scope:** energy and energy cost only; no charter, CapEx, OpEx, carbon or financing.

## What the page does

- One input: H2 delivered, ktpa (default 100).
- Sections: 1 Upstream (no electrolysis; energy and cost charts, assumptions dropdown, NG-fired vs clean-fuel explanation, chart 7B liquefier SEC sweep), 2 Shipping (assumptions dropdown, kWh/kg per vessel chart, cost chart, per-vessel table, chart 1 boil-off vs fuel demand), 3 Downstream (energy chart, zoomed LH2 regas card), 4 Summary (five comparisons by stage, tables, cost-assumptions dropdown), 5 Liquefier maturity outlook (timeline and chart sorted lowest to highest), then a closing caveat.
- Five comparisons: LH2 (boil-off as fuel); NH3 NG-fired and NH3 clean fuel, each with a dual-fuel ship (95 % NH3 + 5 % VLSFO pilot) and with a VLSFO-only ship.

## Fixed basis (page defaults)

| Item | Value | Tag |
|------|-------|-----|
| Vessel, both carriers | 40,000 m³; LH2 70.8 kg/m³ (2,832 t H2); NH3 682 kg/m³ (27,280 t) | user input (2026-09-24); densities from `chain-energy-defaults.csv` |
| Liquefier SEC, today | 9 kWh/kg H2 | user input; KHI discloses 8-9 (kawasaki-2026-questionnaire) |
| Haber-Bosch | 1 kWh/kg H2; stoichiometry 5.6 kg NH3/kg H2 | user input (ASU inclusion open) |
| Electrolyser | 60 kWh/kg H2 | [ASSUMPTION: user placeholder, needs source] |
| Sea days laden | 20; port days 1.25; availability 90 % | [ASSUMPTION], KHI port-day midpoint 1-1.5 |
| LH2 ship | boil-off 0.40 %/d burned; demand 39 t/d VLSFO-eq | user input |
| NH3 ship | boil-off 0.15 %/d reliquefied; demand 30 t/d VLSFO-eq; 95 % NH3 | user input |
| Cracker | feed 6.5 (NG-fired) / 7.2 (clean fuel) kg NH3 per kg H2; 0.29 kWh/kg H2 | user input |
| Prices | power 140 USD/MWh (import terminal set equal, placeholder); VLSFO 553 USD/t; NH3 700 USD/t; gas 13 USD/MMBtu on LHV; **H2 6 USD/kg (boil-off only, changed from 4 on 2026-10-29)** | user input / [ASSUMPTION] |
| Maturity milestones | 9 kWh/kg 2026 (current); 7.5 kWh/kg 2030 (Air Liquide); 6 kWh/kg 2035-2040 (KHI) | user-provided, not independently sourced |

## Results at 100 ktpa (CALCULATED by the page, electrolysis included)

| Chain | Energy, GWh/y | kWh/kg H2 | Cost, USD M/y | USD/kg H2 |
|-------|---------------|-----------|---------------|-----------|
| LH2, 6 kWh/kg (high maturity) | 7,523 | 75.2 | 1,060.2 | 10.60 |
| LH2, 7.5 kWh/kg (2030) | 7,686 | 76.9 | 1,083 | 10.83 |
| LH2, 9 kWh/kg (today) | 7,849 | 78.5 | 1,105.8 | 11.06 |
| NH3 NG-fired, dual-fuel ship | 8,100 | 81.0 | 1,095.8 | 10.96 |
| NH3 clean fuel, dual-fuel ship | 8,880 | 88.8 | 1,237.9 | 12.38 |
| NH3 NG-fired, VLSFO-only ship | 8,100 | 81.0 | 1,082.4 | 10.82 |
| NH3 clean fuel, VLSFO-only ship | 8,880 | 88.8 | 1,223.0 | 12.23 |

- H2 that must be produced for 100 ktpa delivered: 108.7 kt (LH2, 8.7 kt boil-off burned as ship fuel), 116.1 kt (NH3 NG-fired), 128.6 kt (NH3 clean fuel). Electrolysis is 83-87 % of energy.
- NG-fired uses less than clean fuel because the cracker feed is 6.5 vs 7.2 kg NH3/kg H2 (stoichiometric minimum 5.6): clean fuel burns more of the cargo, so each cargo delivers 3,789 t H2 instead of 4,197 t.
- VLSFO-only ammonia ships have identical energy to the dual-fuel ones and lower cost, because VLSFO is 13.5 USD/GJ and ammonia fuel 37.6 USD/GJ at these prices.
- Cost parity of LH2 with the cheapest ammonia pathway (NG-fired, VLSFO-only ship) is at a liquefier SEC of 7.46 kWh/kg; 7.5 kWh/kg is USD 0.6 M/y above it, 6 kWh/kg is USD 22.2 M/y (2.1 %) below. On energy LH2 already wins up to 11.3 kWh/kg. Each 1 kWh/kg of liquefier SEC is worth 109 GWh/y and USD 15.2 M/y.
- Liquefier parity with Haber-Bosch (chart 7B): 1.04 kWh/kg H2, below the 3.9 kWh/kg para-H2 minimum work (doe-2009-h2-liquefaction-energy), so unreachable.

## Open items and cautions

1. **Burned-cargo convention.** The page counts the boil-off H2 burned on the LH2 ship as 290 GWh/y of shipping energy (LHV) on top of the electrolysis and liquefaction already spent making it. `docs/memory.md` (2026-10-11 entry) records that the repo's Section 13.7 corrected this double count (78.49 / 81.00 / 88.80 to 75.59 / 76.35 / 80.53 kWh/kg). The page follows the original artifact's uncorrected convention, so its energy gaps between LH2 and NH3 are not on the corrected basis. Cost is not affected (boil-off is charged at the H2 price, not as LHV energy).
2. **Thin cost margin.** The LH2 vs cheapest-ammonia cost gap is about 2 % at maturity and depends on three placeholders: H2 6 USD/kg, the power price, and the VLSFO-only ammonia ship.
3. Placeholders still unsourced: electrolyser 60 kWh/kg, import-terminal power price, 20 sea days (no corridor fixed, distance and speed are not inputs), Haber-Bosch 1 kWh/kg (ASU inclusion), maturity milestones.
4. Energy view only. The LH2 carrier is nascent; a true comparison waits for proper pre-FEED deliverables (stated on the page).

## Sources

kawasaki-2026-questionnaire (liquefier SEC 8-9 kWh/kg, regas duty, port days); doe-2009-h2-liquefaction-energy (minimum liquefaction work 3.3 normal-H2, 3.9 para-H2 kWh/kg); `data/carriers/chain-energy-defaults.csv` (densities, LHVs, reliquefaction placeholders); user inputs 2026-09-24 and 2026-10-27 to 2026-11-02 as tagged above.
