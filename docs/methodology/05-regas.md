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

## Open questions / TODO
- Delivery pressure/temperature spec at the import gate — project-specific.
