#!/usr/bin/env python3
"""Upstream comparison: liquefaction (LH2) vs Haber-Bosch (NH3) at 100 ktpa H2.

Boundary
--------
Starts at **hydrogen at the battery limit** (gaseous H2 already produced) and
ends with the carrier **in the export-terminal tank, ready to load**. Hydrogen
production itself is common to both chains and is therefore OUTSIDE this
boundary; it is reported only as scale context.

    H2 at battery limit --> [conversion] --> [export terminal storage] --> ship

Two conversion routes:

  LH2 route  : liquefier, KHI SEC 8-9 kWh/kg-H2 (ref kawasaki-2026-questionnaire
               reply Q1, cited). No H2 mass loss (KHI reply Q15).
  NH3 route  : Haber-Bosch synthesis, electrical SEC per kg NH3
               [ESTIMATE 0.60 kWh/kg-NH3, data/carriers/chain-energy-defaults.csv]
               LESS a steam-turbine credit recovered from the exothermic
               synthesis reaction (this script's new term; see steam_credit()).

Both terminals hold the SAME tank volume (60 000 m3 default, user direction
2026-09-08) so the comparison is per unit of installed storage. Boil-off is
re-liquefied on both sides: an energy penalty, not a mass loss.

Units: mass kg, energy kWh, power MW, volume m3, time h/day/year. USD only
where an electricity price is supplied. Every default carries a
data/references.csv id or an explicit [ASSUMPTION]/[ESTIMATE] tag per
CLAUDE.md section 4.

Mirrored by docs/reports/lh2-vs-nh3-shipping-studies.html (sheet 2, "Upstream")
and tested by tests/test_upstream_comparison.py.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from lh2 import liquefaction  # noqa: E402
from lh2.units import Q_  # noqa: E402

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

#: kg NH3 per kg H2. First-principles: N2 + 3 H2 -> 2 NH3, using standard molar
#: masses M(NH3)=17.031, M(H2)=2.016 g/mol.
#: ref: data/carriers/chain-energy-defaults.csv common/stoichiometry
NH3_PER_H2 = 5.632

#: Molar mass of H2, kg/mol. Standard value [needs-source: IUPAC/CODATA].
M_H2 = 0.002016

#: H2 lower heating value, kWh/kg (120 MJ/kg / 3.6).
#: ref: data/properties/lh2-properties.csv [needs-source: NIST citation pending]
H2_LHV_KWH = 33.333

#: Theoretical minimum liquefaction work, para-H2 basis, kWh/kg-H2.
#: ref: doe-2009-h2-liquefaction-energy (cited); the normal-H2 figure is 3.3.
THEORETICAL_MIN_PARA = 3.9
THEORETICAL_MIN_NORMAL = 3.3


# --------------------------------------------------------------------------
# Inputs
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Inputs:
    """Every field carries its source tag in the comment beside it."""

    # --- scale ---
    h2_ktpa: float = 100.0            # [USER] study basis, 2026-09-08
    operating_hours: float = 8000.0   # [ASSUMPTION] plant stream hours per year

    # --- LH2 route ---
    lh2_sec: float = 9.0              # kWh/kg-H2, top of KHI's 8-9 range (cited)

    # --- NH3 route ---
    hb_sec: float = 0.60              # kWh/kg-NH3 [ESTIMATE] chain-energy-defaults
    hb_h2_loss_pct: float = 2.0       # % purge/inerts [ESTIMATE]
    rxn_enthalpy_kj_per_mol_nh3: float = 45.9   # kJ/mol-NH3 [needs-source]
    heat_recovery_pct: float = 75.0   # % of reaction heat raised as usable steam [ASSUMPTION]
    turbine_eff_pct: float = 30.0     # % steam heat -> electricity [ASSUMPTION]
    steam_credit_on: bool = True      # toggle, to show the credit's weight

    # --- export terminal (same tank volume for both, user direction) ---
    tank_m3: float = 60000.0          # [USER] 2026-09-08; KHI's own LH2 export tank is 64 000 m3 (cited)
    tank_fill_pct: float = 98.0       # [ASSUMPTION] usable fill
    hold_days: float = 5.0            # [ASSUMPTION] only used on the equal-days basis
    tank_basis: str = "fixed"         # "fixed" (60 000 m3 each) or "days" (equal cover)

    lh2_rho: float = 70.8             # kg/m3 [needs-source: NIST pending]
    nh3_rho: float = 682.0            # kg/m3 [ESTIMATE]
    lh2_bor: float = 0.1              # %/day at rest (cited, kawasaki-2026-supplemental)
    nh3_bor: float = 0.04             # %/day at rest [ESTIMATE]
    lh2_reliq_sec: float = 3.94       # kWh/kg-H2 BOG [ASSUMPTION, derived]
    nh3_reliq_sec: float = 0.25       # kWh/kg-NH3 BOG [ESTIMATE]

    # --- optional economics ---
    power_usd_per_mwh: float = 50.0   # [SET IT] no default asserted as correct


# --------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------

def reaction_heat_per_kg_h2(inp: Inputs) -> float:
    """Exothermic Haber-Bosch heat released, kWh per kg of H2 reacted.

    N2 + 3 H2 -> 2 NH3 releases ``dH`` per mol NH3, i.e. 2/3 dH per mol H2.
    Same enthalpy magnitude the repository already carries for the reverse
    (cracking) reaction: data/carriers/chain-energy-defaults.csv
    common/nh3/cracking_reaction_enthalpy = 45.9 kJ/mol-NH3.
    """
    kj_per_mol_h2 = inp.rxn_enthalpy_kj_per_mol_nh3 * 2.0 / 3.0
    return kj_per_mol_h2 / M_H2 / 3600.0


def steam_credit_per_kg_h2(inp: Inputs) -> float:
    """Electrical credit from the synthesis heat, kWh per kg of H2 reacted.

    [ASSUMPTION] reaction heat -> recoverable HP steam -> shaft/electric power.
    The two efficiencies are separate live inputs because neither is sourced:
    ``heat_recovery_pct`` is the share of reaction heat raised as usable steam
    (the rest goes to loop recuperation and ambient losses) and
    ``turbine_eff_pct`` is the steam cycle's heat-to-electricity efficiency.
    Their product can never approach 1, so the credit can never exceed the
    plant's own electrical demand at any plausible setting.
    """
    if not inp.steam_credit_on:
        return 0.0
    return (
        reaction_heat_per_kg_h2(inp)
        * inp.heat_recovery_pct / 100.0
        * inp.turbine_eff_pct / 100.0
    )


@dataclass(frozen=True)
class RouteResult:
    name: str
    h2_fed_kg: float
    h2_delivered_kg: float       # H2, or H2 chemically contained in the NH3
    carrier_kg: float            # LH2 kg, or NH3 kg
    conversion_kwh: float        # positive: electricity drawn
    credit_kwh: float            # positive: electricity returned (NH3 only)
    tank_m3: float
    inventory_kg: float          # carrier mass held in the tank
    bog_kg_per_day: float
    terminal_kwh: float          # annual BOG re-liquefaction electricity
    days_of_cover: float

    # --- power (MW) ---
    conversion_mw: float
    credit_mw: float
    terminal_mw: float

    @property
    def net_mw(self) -> float:
        return self.conversion_mw - self.credit_mw + self.terminal_mw

    @property
    def net_kwh_per_kg_h2(self) -> float:
        """Per kg of H2 delivered into the export tank."""
        return (self.conversion_kwh - self.credit_kwh + self.terminal_kwh) / self.h2_delivered_kg

    @property
    def share_of_h2_lhv_pct(self) -> float:
        return self.net_kwh_per_kg_h2 / H2_LHV_KWH * 100.0


def _terminal(inp: Inputs, carrier_annual_kg: float, rho: float, bor: float,
              reliq_sec: float) -> tuple[float, float, float, float]:
    """Export-terminal inventory, BOG rate and re-liquefaction energy.

    Steady-state, not a static hold: the tank is continuously replenished and
    drawn down, so boil-off is ``inventory * BOR`` each day and does NOT
    compound the way ``lh2.storage.boil_off_at_rest`` does for a fixed parcel
    left standing. Boil-off is re-liquefied (KHI reply Q3), so it is an energy
    penalty and not a mass loss.

    Returns: (tank_volume_m3, inventory_kg, bog_kg_per_day, annual_reliq_kwh)
    """
    fill = inp.tank_fill_pct / 100.0
    if inp.tank_basis == "days":
        inventory = carrier_annual_kg / 365.0 * inp.hold_days
        volume = inventory / rho / fill
    else:
        volume = inp.tank_m3
        inventory = volume * rho * fill
    bog_per_day = inventory * bor / 100.0
    # the tank boils off every calendar day, whether or not the plant runs
    annual_kwh = bog_per_day * 365.0 * reliq_sec
    return volume, inventory, bog_per_day, annual_kwh


def evaluate_lh2(inp: Inputs) -> RouteResult:
    fed = inp.h2_ktpa * 1e6
    delivered = fed                       # KHI reply Q15: no H2 loss in the plant
    conv_kwh = liquefaction.liquefaction_energy(fed, Q_(inp.lh2_sec, "kWh/kg")).magnitude
    vol, inv, bog, term_kwh = _terminal(inp, delivered, inp.lh2_rho, inp.lh2_bor, inp.lh2_reliq_sec)
    return RouteResult(
        name="LH2 (liquefaction)",
        h2_fed_kg=fed, h2_delivered_kg=delivered, carrier_kg=delivered,
        conversion_kwh=conv_kwh, credit_kwh=0.0,
        tank_m3=vol, inventory_kg=inv, bog_kg_per_day=bog, terminal_kwh=term_kwh,
        days_of_cover=inv / (delivered / 365.0),
        conversion_mw=conv_kwh / inp.operating_hours / 1000.0,
        credit_mw=0.0,
        terminal_mw=term_kwh / 8760.0 / 1000.0,
    )


def evaluate_nh3(inp: Inputs) -> RouteResult:
    fed = inp.h2_ktpa * 1e6
    reacted = fed * (1.0 - inp.hb_h2_loss_pct / 100.0)
    nh3 = reacted * NH3_PER_H2
    conv_kwh = nh3 * inp.hb_sec
    credit_kwh = reacted * steam_credit_per_kg_h2(inp)
    vol, inv, bog, term_kwh = _terminal(inp, nh3, inp.nh3_rho, inp.nh3_bor, inp.nh3_reliq_sec)
    h2e_stored = inv / NH3_PER_H2
    return RouteResult(
        name="NH3 (Haber-Bosch)",
        h2_fed_kg=fed, h2_delivered_kg=reacted, carrier_kg=nh3,
        conversion_kwh=conv_kwh, credit_kwh=credit_kwh,
        tank_m3=vol, inventory_kg=inv, bog_kg_per_day=bog, terminal_kwh=term_kwh,
        days_of_cover=h2e_stored / (reacted / 365.0),
        conversion_mw=conv_kwh / inp.operating_hours / 1000.0,
        credit_mw=credit_kwh / inp.operating_hours / 1000.0,
        terminal_mw=term_kwh / 8760.0 / 1000.0,
    )


def parity_lh2_sec(inp: Inputs) -> float:
    """Liquefaction SEC at which the two routes draw the same POWER.

    Solved on MW, not on annual kWh: conversion is spread over the plant's
    operating hours while the terminal runs all 8 760 h, so the two are not
    interchangeable. Linear in the SEC, so solved directly.
    """
    n = evaluate_nh3(inp)
    l = evaluate_lh2(inp)
    return (n.net_mw - l.terminal_mw) * 1000.0 * inp.operating_hours / l.h2_fed_kg


def parity_hb_sec(inp: Inputs) -> float:
    """Haber-Bosch electrical SEC (kWh/kg-NH3) at which the two routes draw the
    same POWER. Same MW basis as parity_lh2_sec, and also linear: neither the
    steam credit nor the terminal moves with the synthesis SEC."""
    l = evaluate_lh2(inp)
    n = evaluate_nh3(inp)
    return ((l.net_mw - n.terminal_mw) * 1000.0 * inp.operating_hours
            + n.credit_kwh) / n.carrier_kg


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _fmt(v: float, d: int = 2) -> str:
    return f"{v:,.{d}f}"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--h2-ktpa", type=float, default=Inputs.h2_ktpa)
    p.add_argument("--lh2-sec", type=float, default=Inputs.lh2_sec)
    p.add_argument("--hb-sec", type=float, default=Inputs.hb_sec)
    p.add_argument("--tank-m3", type=float, default=Inputs.tank_m3)
    p.add_argument("--tank-basis", choices=["fixed", "days"], default=Inputs.tank_basis)
    p.add_argument("--no-steam-credit", action="store_true")
    a = p.parse_args(argv)

    inp = Inputs(h2_ktpa=a.h2_ktpa, lh2_sec=a.lh2_sec, hb_sec=a.hb_sec,
                 tank_m3=a.tank_m3, tank_basis=a.tank_basis,
                 steam_credit_on=not a.no_steam_credit)
    l, n = evaluate_lh2(inp), evaluate_nh3(inp)

    print(f"UPSTREAM COMPARISON — {inp.h2_ktpa:,.0f} ktpa H2 at the battery limit")
    print(f"Boundary: H2 in -> carrier in the export tank. Production excluded (common to both).")
    print(f"Basis: {inp.operating_hours:,.0f} plant operating h/y; tank basis '{inp.tank_basis}'")
    print()
    rows = [
        ("Carrier produced", f"{l.carrier_kg/1e6:,.1f} kt LH2", f"{n.carrier_kg/1e6:,.1f} kt NH3"),
        ("H2 delivered into the tank", f"{l.h2_delivered_kg/1e6:,.1f} kt", f"{n.h2_delivered_kg/1e6:,.1f} kt"),
        ("", "", ""),
        ("Conversion power", f"{l.conversion_mw:,.1f} MW", f"{n.conversion_mw:,.1f} MW"),
        ("Steam-turbine credit", "—", f"−{n.credit_mw:,.1f} MW"),
        ("Terminal BOG re-liquefaction", f"{l.terminal_mw:,.3f} MW", f"{n.terminal_mw:,.3f} MW"),
        ("NET POWER", f"{l.net_mw:,.1f} MW", f"{n.net_mw:,.1f} MW"),
        ("", "", ""),
        ("Energy per kg H2 delivered", f"{l.net_kwh_per_kg_h2:,.3f} kWh/kg", f"{n.net_kwh_per_kg_h2:,.3f} kWh/kg"),
        ("Share of the H2's own LHV", f"{l.share_of_h2_lhv_pct:,.1f} %", f"{n.share_of_h2_lhv_pct:,.1f} %"),
        ("", "", ""),
        ("Tank volume", f"{l.tank_m3:,.0f} m3", f"{n.tank_m3:,.0f} m3"),
        ("Tank holds", f"{l.inventory_kg/1e6:,.2f} kt LH2", f"{n.inventory_kg/1e6:,.2f} kt NH3"),
        ("  = H2-equivalent", f"{l.inventory_kg/1e6:,.2f} kt", f"{n.inventory_kg/NH3_PER_H2/1e6:,.2f} kt"),
        ("  = days of cover", f"{l.days_of_cover:,.1f} d", f"{n.days_of_cover:,.1f} d"),
        ("Boil-off", f"{l.bog_kg_per_day/1000:,.2f} t H2/day", f"{n.bog_kg_per_day/1000:,.2f} t NH3/day"),
        ("Re-liquefaction power", f"{l.terminal_mw*1000:,.0f} kW", f"{n.terminal_mw*1000:,.0f} kW"),
    ]
    for k, a_, b_ in rows:
        if not k:
            print()
            continue
        print(f"  {k:<32} {a_:>22} {b_:>22}")

    print()
    print(f"  Reaction heat released      {reaction_heat_per_kg_h2(inp):,.3f} kWh/kg-H2 reacted")
    print(f"  Steam credit realised       {steam_credit_per_kg_h2(inp):,.3f} kWh/kg-H2 reacted "
          f"({inp.heat_recovery_pct:.0f}% recovery x {inp.turbine_eff_pct:.0f}% turbine)")
    print(f"  Power ratio  LH2 / NH3      {l.net_mw/n.net_mw:,.2f} x")
    print(f"  Parity liquefaction SEC     {parity_lh2_sec(inp):,.3f} kWh/kg-H2 "
          f"(thermodynamic floor {THEORETICAL_MIN_PARA} para / {THEORETICAL_MIN_NORMAL} normal)")
    print(f"  Parity Haber-Bosch SEC      {parity_hb_sec(inp):,.3f} kWh/kg-NH3 "
          f"({parity_hb_sec(inp)/inp.hb_sec:,.1f}x the estimate in use)")
    gap_gwh = ((l.conversion_kwh + l.terminal_kwh)
               - (n.conversion_kwh - n.credit_kwh + n.terminal_kwh)) / 1e6
    print(f"  Annual energy gap           {gap_gwh:,.0f} GWh/y "
          f"= USD {gap_gwh*1000*inp.power_usd_per_mwh/1e6:,.1f} M/y at {inp.power_usd_per_mwh:,.0f} USD/MWh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
