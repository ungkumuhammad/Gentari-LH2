"""Cross-cutting project economics helpers (LCOH, NPV, IRR, payback).

No fabricated numbers: callers must pass sourced/tagged inputs; nothing here
invents a discount rate, lifetime, or cost (``CLAUDE.md`` §4).
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy_financial as npf


def npv(rate: float, cashflows: Sequence[float]) -> float:
    """Net Present Value of ``cashflows`` (period 0 first) at ``rate``.

    Args:
        rate: Discount rate per period (e.g. 0.08). Source/tag at the call site.
        cashflows: Cashflows by period, index 0 = now.

    Returns:
        NPV in the same currency/cost-year as the inputs.
    """
    return float(npf.npv(rate, cashflows))


def irr(cashflows: Sequence[float]) -> float:
    """Internal Rate of Return of ``cashflows`` (period 0 first)."""
    return float(npf.irr(cashflows))


def payback_period(cashflows: Sequence[float]) -> float | None:
    """Simple (undiscounted) payback period in periods, or ``None`` if never.

    Linearly interpolates within the period where cumulative cashflow turns
    non-negative.
    """
    cumulative = 0.0
    for i, cf in enumerate(cashflows):
        prev_cumulative = cumulative
        cumulative += cf
        if cumulative >= 0 and i > 0 and prev_cumulative < 0:
            return (i - 1) + (-prev_cumulative / cf) if cf else float(i)
        if cumulative >= 0 and i == 0:
            return 0.0
    return None


def lcoh(
    capex: float,
    opex_per_year: Sequence[float],
    h2_kg_per_year: Sequence[float],
    discount_rate: float,
) -> float:
    """Levelized Cost of Hydrogen, in USD/kg (cost-year per inputs).

    LCOH = (capex + sum(discounted annual opex)) / sum(discounted annual H2
    delivered). All inputs must be sourced or tagged; ``h2_kg_per_year`` must
    already be net of losses (boil-off / process losses), i.e. *delivered*,
    not produced.

    Args:
        capex: Total capital cost at period 0 (USD, cost-year noted by caller).
        opex_per_year: Annual operating cost incl. energy (USD/yr), one entry
            per year of project life (period 1 first).
        h2_kg_per_year: H2 *delivered* per year (kg/yr), net of losses, same
            length/period alignment as ``opex_per_year``.
        discount_rate: Per ``CLAUDE.md`` §4 — sourced or ``[ASSUMPTION]``.

    Returns:
        LCOH in USD/kg H2.
    """
    if len(opex_per_year) != len(h2_kg_per_year):
        raise ValueError("opex_per_year and h2_kg_per_year must be the same length")

    discounted_costs = capex
    discounted_h2 = 0.0
    for year, (opex, h2_kg) in enumerate(zip(opex_per_year, h2_kg_per_year), start=1):
        discount_factor = 1.0 / (1.0 + discount_rate) ** year
        discounted_costs += opex * discount_factor
        discounted_h2 += h2_kg * discount_factor

    if discounted_h2 <= 0:
        raise ValueError("discounted H2 delivered must be positive")

    return discounted_costs / discounted_h2
