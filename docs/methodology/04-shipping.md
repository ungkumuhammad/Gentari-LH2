# Methodology — [4] Shipping

> **Status: v1 implemented** in `src/lh2/shipping.py` (2026-07-20), driven by
> KHI's disclosed figures. All numbers cited or tagged (`CLAUDE.md` §4).

## System boundary
LH2 loaded at export terminal → LH2 discharged at import terminal.

## Physics & operations
- Voyage boil-off (BOR, %/day) over laden + ballast days.
- Boil-off management: venting, use as fuel, or onboard reliquefaction.
- Fleet sizing from cargo size, voyage distance/speed, and turnaround.

## Key parameters (sourced from KHI, see `src/lh2/shipping.py`)
- Carrier cargo capacity: **160,000 m³** commercial target @ **29.6 km/h**
  (`KHI_COMMERCIAL_CARGO_CAPACITY`, `KHI_COMMERCIAL_SPEED`).
- Load/unload duration: **1–1.5 days** (`KHI_LOAD_UNLOAD_DAYS_LOW/HIGH`).
- **Voyage BOR (%/day): `[GAP — not disclosed]` by KHI as a standalone
  figure** — reply Q23 only states fuel-gas consumption equals the BOR, and
  reply Q26 that MGO-only sailing holds MARVS "for several days". No default
  is coded in `voyage_boil_off()`; callers must supply an `[ASSUMPTION]`/
  `[ESTIMATE]`-tagged value.
- Vessel CapEx and charter rate: `[GAP — not disclosed]` (reply Q31: only a
  qualitative "significantly higher than LNG" premium given).
- Onboard reliquefaction: **not adopted** by KHI's design (reply Q33) — BOG is
  consumed as dual-fuel engine propulsion fuel instead.

> Record vessel specifics in [`../../data/vessels/`](../../data/vessels/), each
> row referencing a `references.csv` id.

## Outputs
Round-trip cycle time, fleet sizing, and voyage BOG (`one_way_transit_days()`,
`round_trip_days()`, `fleet_size()`, `voyage_boil_off()`). Shipping cost
($/kg delivered) is **not** computable from KHI data alone — see the
disclosure-gap register in `docs/reports/khi-lh2-solution-database.md` §9.

## Open questions / TODO
- Route(s) and distance(s) of interest are project-specific — no KHI default;
  supply `distance_km` at the call site (`scripts/run_project_model.py`).
- A sourced voyage BOR figure would remove the largest remaining modeling gap.
