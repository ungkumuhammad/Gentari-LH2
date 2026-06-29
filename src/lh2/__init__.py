"""LH2 value-chain modeling library.

One module per value-chain segment (see ``CLAUDE.md`` §3):

    production   -> [1] upstream H2 production
    liquefaction -> [2] liquefaction
    storage      -> [3] cryogenic storage
    shipping     -> [4] marine transport + boil-off
    regas        -> [5] regasification
    enduse       -> [6] distribution & end-use
    economics    -> cross-cutting LCOH / NPV / IRR helpers

Shared infrastructure:
    units -> the single ``pint`` registry all models import.

Rule of the repo: no fabricated numbers. Every numeric default must carry a
``data/references.csv`` id in a comment, or a ``[ASSUMPTION]`` / ``[ESTIMATE]``
tag. See ``CLAUDE.md`` §4.
"""

from __future__ import annotations

from . import units

__all__ = ["units"]
