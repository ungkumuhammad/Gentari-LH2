# Methodology — [5] Regasification

> **Status: v1 implemented** in `src/lh2/regas.py` (2026-07-20), driven by
> KHI's disclosed figures. All numbers cited or tagged (`CLAUDE.md` §4).

## System boundary
LH2 in → gaseous H2 at required delivery pressure, out.

## Physics
- Vaporization duty = sensible + latent heat to warm LH2 to delivery temp.
- Vaporizer types (ambient air, water bath, etc.).
- Cold-energy recovery potential (the refrigeration released on warming).

## Key parameters (sourced from KHI, see `src/lh2/regas.py`)
- Regas heat duty: **≈3.8 MJ/kg-LH2** (`KHI_REGAS_HEAT_DUTY`,
  kawasaki-2026-questionnaire reply Q18).
- Vaporiser type: **Open-Rack Vaporiser (ORV)**, seawater heat source (reply
  Q17); dedicated heat-source system as an alternative if seawater discharge
  is constrained.
- Delivery pressure requirement: `[ASSUMPTION until specified]` — not
  addressed by KHI or by a Gentari-specified gate spec yet.
- CapEx vs send-out capacity: `[GAP — not disclosed]` by KHI; only the
  aggregate IAE cost stack exists.

## Outputs
Vaporization heat duty (`regas_duty()`). Regas cost ($/kg) and any
cold-energy recovery credit are **not** computable from KHI data alone — see
the disclosure-gap register in `docs/reports/khi-lh2-solution-database.md` §9.

## ORV seawater pump electrical energy (calculator-only, not yet in `regas.py`)
The BFD calculator (`docs/reports/khi-lh2-reliq-shipping-regas-bfd.html`)
derives an electrical energy figure for the ORV's seawater circulation pump
— KHI's heat duty is thermal (free ambient seawater heat), not electrical,
and KHI discloses no electrical consumption for the vaporizer. Derivation
(first-principles, all four parameters user-editable, none KHI-sourced):
seawater mass flow = heat duty / (seawater Cp × ΔT) → volume via seawater
density → pump hydraulic energy = ρ·g·H·V → electrical = hydraulic / pump
efficiency. An optional supplemental-heater SEC input (default 0, i.e.
seawater-only per KHI's actual design) can add a second electrical term.
See calculator notes 30–31 for the full derivation and seawater property
citations (density/Cp are standard values, tagged `needs-source`).
**This logic has not been ported to `src/lh2/regas.py`/tested** — it lives
only in the calculator's JS for now. Port it here (with a matching test) if
the model needs to be driven from `scripts/run_project_model.py` too.

## Open questions / TODO
- Delivery pressure/temperature spec at the import gate — project-specific.
- Port the ORV seawater pump-power derivation (above) into `regas.py`.
- Log a formal citation for seawater density (~1,025 kg/m³) and specific
  heat (~3.93 kJ/kg·K) in `data/references.csv` — currently `needs-source`.
