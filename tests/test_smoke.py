"""Smoke tests: package imports and the shared unit registry behaves."""

from __future__ import annotations

from math import isclose


def test_package_imports():
    import lh2  # noqa: F401
    from lh2 import units  # noqa: F401


def test_unit_registry_and_quantities():
    from lh2.units import Q_, ureg

    # SEC (kWh/kg) times a mass (kg) yields energy in kWh, units carried.
    sec = Q_(9.0, "kWh/kg")
    energy = sec * Q_(1000, "kg")
    assert isclose(energy.to("kWh").magnitude, 9000.0)

    # kWh <-> MJ conversion is wired up (1 kWh = 3.6 MJ).
    assert isclose(Q_(1.0, "kWh").to("MJ").magnitude, 3.6)

    # Currency unit is registered for monetary quantities.
    cost = Q_(5.0, "USD/kg")
    assert isclose((cost * Q_(2.0, "kg")).to("USD").magnitude, 10.0)

    # Same registry instance is reused (no cross-registry quantities).
    assert sec._REGISTRY is ureg
