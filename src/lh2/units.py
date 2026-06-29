"""Shared unit registry for the LH2 value-chain models.

Single source of truth for units across the whole package. Import ``ureg`` and
``Q_`` from here — never instantiate a separate :class:`pint.UnitRegistry`,
otherwise quantities from different registries cannot be combined.

Conventions (see ``docs/conventions.md``):
    - Mass of H2 in kg; energy in kWh / MJ; power in MW; pressure in bar;
      temperature in K.
    - Currency in USD with cost-year tagged in the *value*, not the unit
      (e.g. label a result ``USD2024``); ``USD`` is registered as a bare unit
      so monetary quantities can carry units without year arithmetic.

Usage::

    from lh2.units import ureg, Q_
    sec = Q_(9.0, "kWh/kg")          # ref: <references.csv id>
    energy = sec * Q_(1000, "kg")    # -> 9000.0 kWh
"""

from __future__ import annotations

import pint

#: The one registry every module shares.
ureg: pint.UnitRegistry = pint.UnitRegistry()

#: Quantity constructor bound to the shared registry.
Q_ = ureg.Quantity

# Currency as a bare unit. Cost-year (e.g. USD2024) is tracked in labels/data,
# not via unit math — we never auto-convert between cost years.
ureg.define("USD = [currency]")
ureg.define("MMBtu = 1.05505585262e9 * joule")  # exact, by definition

__all__ = ["ureg", "Q_"]
