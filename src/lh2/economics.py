"""Cross-cutting project economics helpers (LCOH, NPV, IRR, payback).

STUB — signatures and contracts are defined; calculations are to be implemented
as the cost stack is built. NPV/IRR will use ``numpy_financial`` once wired in.

No fabricated numbers: callers must pass sourced/tagged inputs; nothing here
invents a discount rate, lifetime, or cost (``CLAUDE.md`` §4).
"""

from __future__ import annotations

from collections.abc import Sequence


def npv(rate: float, cashflows: Sequence[float]) -> float:
    """Net Present Value of ``cashflows`` (period 0 first) at ``rate``.

    Args:
        rate: Discount rate per period (e.g. 0.08). Source/tag at the call site.
        cashflows: Cashflows by period, index 0 = now.

    Returns:
        NPV in the same currency/cost-year as the inputs.
    """
    raise NotImplementedError("TODO: implement via numpy_financial.npv")


def irr(cashflows: Sequence[float]) -> float:
    """Internal Rate of Return of ``cashflows`` (period 0 first)."""
    raise NotImplementedError("TODO: implement via numpy_financial.irr")


def lcoh(
    capex: float,
    opex_per_year: Sequence[float],
    h2_kg_per_year: Sequence[float],
    discount_rate: float,
) -> float:
    """Levelized Cost of Hydrogen, in USD/kg (cost-year per inputs).

    LCOH = sum(discounted annual costs) / sum(discounted annual H2 delivered).
    All inputs must be sourced or tagged; carry boil-off/process losses into
    ``h2_kg_per_year`` (delivered, not produced).

    Args:
        capex: Total capital cost at period 0 (USD, cost-year noted by caller).
        opex_per_year: Annual operating cost incl. energy (USD/yr).
        h2_kg_per_year: H2 *delivered* per year (kg/yr), net of losses.
        discount_rate: Per ``CLAUDE.md`` §4 — sourced or ``[ASSUMPTION]``.

    Returns:
        LCOH in USD/kg H2.
    """
    raise NotImplementedError("TODO: implement levelized cost calculation")
