# Methodology — [4] Shipping

> **Status: STUB.** Fill as sources are uploaded. All numbers must be cited or
> tagged (`CLAUDE.md` §4).

## System boundary
LH2 loaded at export terminal → LH2 discharged at import terminal.

## Physics & operations
- Voyage boil-off (BOR, %/day) over laden + ballast days.
- Boil-off management: venting, use as fuel, or onboard reliquefaction.
- Fleet sizing from cargo size, voyage distance/speed, and turnaround.

## Key parameters (to be sourced)
- Carrier cargo capacity (m³ / t LH2). `[needs source]`
- Voyage BOR (%/day). `[needs source]`
- Vessel CapEx and charter rate. `[needs source]`
- Speed, fuel, port times. `[needs source]`

> Record vessel specifics in [`../../data/vessels/`](../../data/vessels/), each
> row referencing a `references.csv` id.

## Outputs
Shipping cost ($/kg delivered), in-transit boil-off losses, fleet count.

## Open questions / TODO
- Route(s) and distance(s) of interest; reliquefaction onboard yes/no.
