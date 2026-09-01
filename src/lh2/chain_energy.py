"""Node-by-node energy-penalty cascade for the LH2 and NH3 carrier chains.

**System boundary:** electrolyser battery limit (node A) -> hydrogen delivered
as gas at the import-terminal send-out flange (node F1 for LH2, node F2 for
NH3). Well-to-gate; distribution and end-use (segment 6) are excluded.

**Basis:** 1 kg of H2 leaving node A. Mass is tracked in *H2-equivalent* kg all
the way through, so the ammonia leg is directly comparable to the LH2 leg
(NH3 mass = H2-equivalent x 5.632, see ``NH3_PER_H2_MASS_RATIO``).

**Units:** energy kWh (MJ shown alongside in the UI layer), mass kg,
BOR %/day, distance km, speed km/h. Cost is out of scope for this module.

**The two efficiency views.** Both are computed from the same per-node energy
and mass figures; they answer different questions and are reported side by side:

1. *Input basis* -- ``eta = LHV of H2 delivered / total energy consumed``.
   At node A alone this reproduces the user's worked example:
   33.33 / 60 = 55.6 %.
2. *Carrier-penalty (deduction) basis* -- start with the 33.33 kWh of chemical
   energy in the 1 kg of H2 produced, then deduct each downstream node's
   parasitic energy and the LHV of any H2 lost. What remains is the energy
   still available at the gate net of everything the carrier chain cost.

Per ``CLAUDE.md`` §4 every default here is either cited to a
``data/references.csv`` id or tagged ``[ASSUMPTION]`` / ``[ESTIMATE]``. The
values live in ``data/carriers/chain-energy-defaults.csv``; this module mirrors
them as module constants so it can run without pandas, and
``tests/test_chain_energy.py`` asserts the two stay in sync.

**Standing caveat (decision D4):** *no* ammonia figure in the defaults below is
sourced. Every NH3 number is a placeholder awaiting the internal Gentari NH3
dataset, and every result carries that in its ``gaps`` list.
"""

from __future__ import annotations

from dataclasses import dataclass, field

MJ_PER_KWH = 3.6

# --------------------------------------------------------------------------
# Shared constants
# --------------------------------------------------------------------------

#: H2 lower heating value, kWh/kg (120 MJ/kg / 3.6).
#: ref: data/properties/lh2-properties.csv [needs-source: NIST/ISO pending].
H2_LHV_KWH_PER_KG = 120.0 / 3.6

#: NH3 lower heating value, kWh/kg (18.6 MJ/kg / 3.6).
#: [ESTIMATE - needs source] standard published value, no citation logged.
NH3_LHV_KWH_PER_KG = 18.6 / 3.6

#: kg NH3 per kg H2 from N2 + 3 H2 -> 2 NH3, using M(NH3) = 17.031 g/mol and
#: M(H2) = 2.016 g/mol. First-principles; the molar masses themselves are
#: standard values with no citation logged [needs-source: IUPAC/CODATA].
NH3_PER_H2_MASS_RATIO = (2 * 17.031) / (3 * 2.016)

#: Endothermic enthalpy of 2 NH3 -> N2 + 3 H2 at 298 K, kJ per mol NH3.
#: [needs-source] standard formation-enthalpy magnitude.
NH3_CRACKING_ENTHALPY_KJ_PER_MOL = 45.9

#: Moles of H2 per kg (1000 / 2.016).
H2_MOL_PER_KG = 1000.0 / 2.016


def cracking_reaction_duty_kwh_per_kg_h2() -> float:
    """Thermodynamic floor for cracker heat, kWh per kg H2 produced.

    Derivation: 2 NH3 -> N2 + 3 H2 needs 2/3 mol NH3 per mol H2, so the duty
    per kg H2 is ``(2/3) x 45.9 kJ/mol x 496.03 mol/kg`` = 15.2 MJ/kg =
    4.22 kWh/kg. [ASSUMPTION: derived] -- reported for reference only; the heat
    is actually supplied by the cracker's self-consumption term, so this is
    never added again to the energy total.
    """
    kj_per_kg_h2 = (2.0 / 3.0) * NH3_CRACKING_ENTHALPY_KJ_PER_MOL * H2_MOL_PER_KG
    return kj_per_kg_h2 / 1000.0 / MJ_PER_KWH


# --------------------------------------------------------------------------
# Inputs
# --------------------------------------------------------------------------


@dataclass
class ChainInputs:
    """Every user-editable input, with its tag documented per field.

    Defaults mirror ``data/carriers/chain-energy-defaults.csv``.
    """

    # -- shared ------------------------------------------------------------
    #: [ASSUMPTION] user-specified worked-example default; production is
    #: outside KHI's scope so no in-repo sourced figure exists.
    electrolyser_sec_kwh_per_kg: float = 60.0
    #: [ASSUMPTION] placeholder; no named corridor fixed yet (decision D1).
    voyage_distance_km: float = 6000.0

    # -- LH2 chain (nodes B1-F1) -------------------------------------------
    #: cited: kawasaki-2026-questionnaire (reply Q1, 8-9 kWh/kg range).
    liquefaction_sec_kwh_per_kg: float = 9.0
    #: cited: kawasaki-2026-questionnaire (reply Q15, no H2 losses claimed).
    liquefaction_h2_loss_pct: float = 0.0
    #: cited: kawasaki-2026-supplemental (0.1 %/d at rest).
    lh2_export_bor_pct_per_day: float = 0.1
    #: [ASSUMPTION] placeholder hold time.
    lh2_export_storage_days: float = 5.0
    #: cited: kawasaki-2026-supplemental (0.1 %/d at rest).
    lh2_import_bor_pct_per_day: float = 0.1
    #: [ASSUMPTION] placeholder hold time.
    lh2_import_storage_days: float = 5.0
    #: [ASSUMPTION: derived] 0.438 x liquefaction SEC -- see module docstring
    #: and data/properties/liquefaction.csv.
    lh2_bog_reliquefaction_sec_kwh_per_kg: float = 3.94
    #: cited: kawasaki-2026-supplemental (29.6 km/h ~ 16 kn).
    lh2_carrier_speed_km_per_h: float = 29.6
    #: [ESTIMATE - needs source] KHI discloses no standalone voyage BOR.
    lh2_voyage_bor_pct_per_day: float = 0.2
    #: cited: kawasaki-2026-questionnaire (reply Q18, 3.8 MJ/kg ORV duty).
    lh2_regas_heat_duty_mj_per_kg: float = 3.8
    #: [ASSUMPTION: derived] cryo pump to send-out + ORV seawater pump.
    lh2_regas_electrical_kwh_per_kg: float = 0.031

    # -- NH3 chain (nodes B2-F2) -- every one a placeholder (decision D4) ---
    #: [ESTIMATE - needs source] per kg NH3: ASU + compression + loop + refrig.
    hb_sec_kwh_per_kg_nh3: float = 0.60
    #: [ESTIMATE - needs source] purge/inerts, net of purge recovery.
    hb_h2_loss_pct: float = 2.0
    #: [ESTIMATE - needs source] refrigerated NH3 at ~ -33 C.
    nh3_export_bor_pct_per_day: float = 0.04
    #: [ASSUMPTION] matched to the LH2 side for a like-for-like hold time.
    nh3_export_storage_days: float = 5.0
    #: [ESTIMATE - needs source]
    nh3_import_bor_pct_per_day: float = 0.04
    #: [ASSUMPTION] matched to the LH2 side.
    nh3_import_storage_days: float = 5.0
    #: [ESTIMATE - needs source] per kg NH3 BOG re-liquefied.
    nh3_bog_reliquefaction_sec_kwh_per_kg: float = 0.25
    #: [ESTIMATE - needs source] set close to the LH2 carrier speed.
    nh3_carrier_speed_km_per_h: float = 30.0
    #: [ESTIMATE - needs source]
    nh3_voyage_bor_pct_per_day: float = 0.04
    #: [ESTIMATE] disposition switch: True re-liquefies voyage BOG (energy
    #: penalty), False burns it as fuel (mass loss), as the LH2 carrier does.
    nh3_voyage_bog_reliquefied: bool = True
    #: [ESTIMATE - needs source] H2-equivalent burned for reaction + sensible
    #: heat and lost in PSA tail gas. Floor is 12.7 % (reaction enthalpy only).
    cracker_self_consumption_pct: float = 20.0
    #: [ESTIMATE - needs source] PSA/compression/BOP, per kg H2-equiv entering.
    cracker_electrical_kwh_per_kg: float = 0.5


# --------------------------------------------------------------------------
# Results
# --------------------------------------------------------------------------


@dataclass
class NodeResult:
    """One node of the cascade, on a 1 kg-H2-at-node-A basis."""

    node_id: str
    name: str
    carrier: str  # 'GH2' | 'LH2' | 'NH3'
    mass_in_kg_h2e: float
    mass_out_kg_h2e: float
    energy_kwh: float  # purchased/parasitic energy charged at this node
    ambient_heat_kwh: float  # free ambient/seawater duty, reported not charged
    cumulative_energy_kwh: float
    lhv_carried_kwh: float  # LHV of the H2-equivalent still in the stream
    net_energy_kwh: float  # deduction view: LHV carried - cumulative penalties
    efficiency_pct: float  # input basis: LHV carried / cumulative energy
    tag: str
    note: str = ""

    @property
    def mass_loss_kg_h2e(self) -> float:
        return self.mass_in_kg_h2e - self.mass_out_kg_h2e

    @property
    def mass_loss_lhv_kwh(self) -> float:
        return self.mass_loss_kg_h2e * H2_LHV_KWH_PER_KG


@dataclass
class ChainResult:
    """Whole-chain roll-up for one carrier."""

    chain: str
    nodes: list[NodeResult]
    delivered_kg_h2: float
    total_energy_kwh: float
    ambient_heat_kwh: float
    gaps: list[str] = field(default_factory=list)

    @property
    def lhv_delivered_kwh(self) -> float:
        return self.delivered_kg_h2 * H2_LHV_KWH_PER_KG

    @property
    def efficiency_pct(self) -> float:
        """Input basis: LHV delivered / total energy consumed."""
        if self.total_energy_kwh <= 0:
            return 0.0
        return 100.0 * self.lhv_delivered_kwh / self.total_energy_kwh

    @property
    def total_loss_kg_h2(self) -> float:
        return 1.0 - self.delivered_kg_h2

    @property
    def carrier_energy_kwh(self) -> float:
        """Energy charged downstream of node A (the carrier chain proper)."""
        return sum(n.energy_kwh for n in self.nodes if n.node_id != "A")

    @property
    def net_energy_kwh(self) -> float:
        """Deduction view: 33.33 kWh minus carrier energy minus lost LHV."""
        return (
            H2_LHV_KWH_PER_KG
            - self.carrier_energy_kwh
            - self.total_loss_kg_h2 * H2_LHV_KWH_PER_KG
        )

    @property
    def retained_pct(self) -> float:
        """Net energy as a share of the 1 kg of H2's own LHV."""
        return 100.0 * self.net_energy_kwh / H2_LHV_KWH_PER_KG

    @property
    def energy_per_kg_delivered_kwh(self) -> float:
        if self.delivered_kg_h2 <= 0:
            return float("nan")
        return self.total_energy_kwh / self.delivered_kg_h2


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def boil_off_fraction(bor_pct_per_day: float, days: float) -> float:
    """Compounding boil-off over ``days``: ``1 - (1 - BOR)^days``.

    Compounding (not linear) because each day's boil-off leaves less inventory
    for the next day -- the same treatment used in ``src/lh2/storage.py``.
    """
    if bor_pct_per_day <= 0 or days <= 0:
        return 0.0
    return 1.0 - (1.0 - bor_pct_per_day / 100.0) ** days


def voyage_days(distance_km: float, speed_km_per_h: float) -> float:
    """One-way laden voyage duration, days."""
    if speed_km_per_h <= 0:
        return 0.0
    return distance_km / speed_km_per_h / 24.0


class _Cascade:
    """Accumulator that keeps the two efficiency views consistent."""

    def __init__(self) -> None:
        self.nodes: list[NodeResult] = []
        self.mass = 1.0  # kg H2-equivalent
        self.cumulative_energy = 0.0
        self.carrier_energy = 0.0  # energy charged after node A
        self.ambient_heat = 0.0

    def add(
        self,
        node_id: str,
        name: str,
        carrier: str,
        *,
        energy_kwh: float = 0.0,
        mass_loss_frac: float = 0.0,
        ambient_heat_kwh: float = 0.0,
        tag: str = "",
        note: str = "",
    ) -> NodeResult:
        mass_in = self.mass
        mass_out = mass_in * (1.0 - mass_loss_frac)
        self.mass = mass_out
        self.cumulative_energy += energy_kwh
        if node_id != "A":
            self.carrier_energy += energy_kwh
        self.ambient_heat += ambient_heat_kwh

        lhv_carried = mass_out * H2_LHV_KWH_PER_KG
        # Deduction view: the 1 kg of H2's own LHV, less every carrier-chain
        # penalty booked so far (parasitic energy + the LHV of H2 lost).
        net = (
            H2_LHV_KWH_PER_KG
            - self.carrier_energy
            - (1.0 - mass_out) * H2_LHV_KWH_PER_KG
        )
        efficiency = (
            100.0 * lhv_carried / self.cumulative_energy
            if self.cumulative_energy > 0
            else 0.0
        )
        node = NodeResult(
            node_id=node_id,
            name=name,
            carrier=carrier,
            mass_in_kg_h2e=mass_in,
            mass_out_kg_h2e=mass_out,
            energy_kwh=energy_kwh,
            ambient_heat_kwh=ambient_heat_kwh,
            cumulative_energy_kwh=self.cumulative_energy,
            lhv_carried_kwh=lhv_carried,
            net_energy_kwh=net,
            efficiency_pct=efficiency,
            tag=tag,
            note=note,
        )
        self.nodes.append(node)
        return node


def _production_node(cascade: _Cascade, inp: ChainInputs) -> None:
    """Node A -- shared by both chains."""
    cascade.add(
        "A",
        "H2 production (electrolysis)",
        "GH2",
        energy_kwh=inp.electrolyser_sec_kwh_per_kg,
        tag="ASSUMPTION",
        note=(
            f"{inp.electrolyser_sec_kwh_per_kg:g} kWh/kg in, {H2_LHV_KWH_PER_KG:.2f} "
            "kWh/kg out as LHV. Shared node -- identical for both chains."
        ),
    )


# --------------------------------------------------------------------------
# Chains
# --------------------------------------------------------------------------


def run_lh2_chain(inp: ChainInputs | None = None) -> ChainResult:
    """Nodes A -> B1 -> C1 -> D1 -> E1 -> F1."""
    inp = inp or ChainInputs()
    c = _Cascade()
    _production_node(c, inp)

    # B1 -- liquefaction.
    c.add(
        "B1",
        "Liquefaction",
        "LH2",
        energy_kwh=inp.liquefaction_sec_kwh_per_kg * c.mass,
        mass_loss_frac=inp.liquefaction_h2_loss_pct / 100.0,
        tag="cited",
        note="SEC cited kawasaki-2026-questionnaire (8-9 kWh/kg); zero-loss claim reply Q15.",
    )

    # C1 -- export terminal & storage. BOG is re-liquefied (KHI reply Q3), so
    # the penalty is energy, not mass.
    export_bog = boil_off_fraction(
        inp.lh2_export_bor_pct_per_day, inp.lh2_export_storage_days
    )
    c.add(
        "C1",
        "Export terminal & storage",
        "LH2",
        energy_kwh=export_bog * c.mass * inp.lh2_bog_reliquefaction_sec_kwh_per_kg,
        tag="cited+ASSUMPTION",
        note=(
            f"BOG {export_bog * 100:.3f}% of inventory over "
            f"{inp.lh2_export_storage_days:g} d at {inp.lh2_export_bor_pct_per_day:g} %/d "
            "(cited), re-liquefied at a derived SEC [ASSUMPTION]."
        ),
    )

    # D1 -- shipping. BOG is burned as propulsion fuel (reply Q23/Q33): it
    # leaves the chain as H2 mass, not as an electrical draw.
    days = voyage_days(inp.voyage_distance_km, inp.lh2_carrier_speed_km_per_h)
    voyage_bog = boil_off_fraction(inp.lh2_voyage_bor_pct_per_day, days)
    c.add(
        "D1",
        "LH2 shipping",
        "LH2",
        mass_loss_frac=voyage_bog,
        tag="ESTIMATE",
        note=(
            f"{days:.2f} d laden at {inp.lh2_carrier_speed_km_per_h:g} km/h (cited); "
            f"voyage BOR {inp.lh2_voyage_bor_pct_per_day:g} %/d [ESTIMATE - needs source] "
            "burned as propulsion fuel (cited) -> mass loss, no electrical penalty. "
            "MGO top-up fuel is outside this boundary."
        ),
    )

    # E1 -- import terminal & storage.
    import_bog = boil_off_fraction(
        inp.lh2_import_bor_pct_per_day, inp.lh2_import_storage_days
    )
    c.add(
        "E1",
        "Import terminal & storage",
        "LH2",
        energy_kwh=import_bog * c.mass * inp.lh2_bog_reliquefaction_sec_kwh_per_kg,
        tag="cited+ASSUMPTION",
        note=(
            f"BOG {import_bog * 100:.3f}% over {inp.lh2_import_storage_days:g} d at "
            f"{inp.lh2_import_bor_pct_per_day:g} %/d (cited), re-liquefied [ASSUMPTION]."
        ),
    )

    # F1 -- regasification. The 3.8 MJ/kg is ambient seawater heat: reported,
    # not charged. Only the pump work is a purchased-energy penalty.
    c.add(
        "F1",
        "Regasification (ORV)",
        "GH2",
        energy_kwh=inp.lh2_regas_electrical_kwh_per_kg * c.mass,
        ambient_heat_kwh=(inp.lh2_regas_heat_duty_mj_per_kg / MJ_PER_KWH) * c.mass,
        tag="cited+ASSUMPTION",
        note=(
            f"Heat duty {inp.lh2_regas_heat_duty_mj_per_kg:g} MJ/kg (cited) is free "
            "ambient seawater heat, so it is reported but not charged; the charged "
            "term is derived cryo-pump + seawater-pump work [ASSUMPTION: derived]."
        ),
    )

    gaps = [
        "Voyage BOR is a placeholder: KHI discloses no standalone shipping "
        "boil-off rate (reply Q23 only ties fuel-gas rate to BOR). "
        "[ESTIMATE - needs source]",
        "BOG re-liquefaction SEC is derived by scaling the liquefaction SEC "
        "with the ideal-work ratio (0.438), not a KHI figure. [ASSUMPTION: derived]",
        "Regas electrical energy is a first-principles pump-work estimate at the "
        "assumed send-out spec; no ORV electrical figure is disclosed anywhere. "
        "[ASSUMPTION: derived]",
        "Electrolyser SEC (node A) is a user-supplied placeholder -- production "
        "sits outside KHI's scope. [ASSUMPTION]",
        "MGO/auxiliary marine fuel, terminal utilities, and jetty/loading energy "
        "are outside this boundary and are not counted for either chain.",
    ]
    return ChainResult(
        chain="LH2",
        nodes=c.nodes,
        delivered_kg_h2=c.mass,
        total_energy_kwh=c.cumulative_energy,
        ambient_heat_kwh=c.ambient_heat,
        gaps=gaps,
    )


def run_nh3_chain(inp: ChainInputs | None = None) -> ChainResult:
    """Nodes A -> B2 -> C2 -> D2 -> E2 -> F2.

    Mass is carried as H2-equivalent throughout; multiply by
    ``NH3_PER_H2_MASS_RATIO`` for the physical ammonia tonnage.
    """
    inp = inp or ChainInputs()
    c = _Cascade()
    _production_node(c, inp)

    # B2 -- Haber-Bosch. Energy is quoted per kg NH3, so convert on the NH3
    # actually made from the H2 entering the node.
    hb_loss = inp.hb_h2_loss_pct / 100.0
    nh3_made_per_h2e = (1.0 - hb_loss) * NH3_PER_H2_MASS_RATIO
    c.add(
        "B2",
        "Ammonia synthesis (Haber-Bosch)",
        "NH3",
        energy_kwh=inp.hb_sec_kwh_per_kg_nh3 * nh3_made_per_h2e * c.mass,
        mass_loss_frac=hb_loss,
        tag="ESTIMATE",
        note=(
            f"1 kg H2 -> {NH3_PER_H2_MASS_RATIO:.3f} kg NH3 (stoichiometric, "
            f"first-principles). SEC {inp.hb_sec_kwh_per_kg_nh3:g} kWh/kg-NH3 and "
            f"{inp.hb_h2_loss_pct:g}% purge loss are both [ESTIMATE - needs source]. "
            "Exothermic heat export credit not modelled."
        ),
    )

    # C2 -- NH3 export terminal & storage; BOG re-liquefied.
    export_bog = boil_off_fraction(
        inp.nh3_export_bor_pct_per_day, inp.nh3_export_storage_days
    )
    c.add(
        "C2",
        "Export terminal & storage",
        "NH3",
        energy_kwh=(
            export_bog
            * c.mass
            * NH3_PER_H2_MASS_RATIO
            * inp.nh3_bog_reliquefaction_sec_kwh_per_kg
        ),
        tag="ESTIMATE",
        note=(
            f"BOG {export_bog * 100:.3f}% over {inp.nh3_export_storage_days:g} d at "
            f"{inp.nh3_export_bor_pct_per_day:g} %/d, re-liquefied. Every figure "
            "[ESTIMATE - needs source]."
        ),
    )

    # D2 -- NH3 shipping. Default disposition is onboard re-liquefaction
    # (energy); flipping the switch burns BOG as fuel (mass loss) instead.
    days = voyage_days(inp.voyage_distance_km, inp.nh3_carrier_speed_km_per_h)
    voyage_bog = boil_off_fraction(inp.nh3_voyage_bor_pct_per_day, days)
    if inp.nh3_voyage_bog_reliquefied:
        ship_energy = (
            voyage_bog
            * c.mass
            * NH3_PER_H2_MASS_RATIO
            * inp.nh3_bog_reliquefaction_sec_kwh_per_kg
        )
        ship_loss = 0.0
        disposition = "re-liquefied on board"
    else:
        ship_energy = 0.0
        ship_loss = voyage_bog
        disposition = "burned as fuel"
    c.add(
        "D2",
        "NH3 shipping",
        "NH3",
        energy_kwh=ship_energy,
        mass_loss_frac=ship_loss,
        tag="ESTIMATE",
        note=(
            f"{days:.2f} d laden at {inp.nh3_carrier_speed_km_per_h:g} km/h; voyage BOR "
            f"{inp.nh3_voyage_bor_pct_per_day:g} %/d, {disposition}. Every figure "
            "[ESTIMATE - needs source]."
        ),
    )

    # E2 -- NH3 import terminal & storage.
    import_bog = boil_off_fraction(
        inp.nh3_import_bor_pct_per_day, inp.nh3_import_storage_days
    )
    c.add(
        "E2",
        "Import terminal & storage",
        "NH3",
        energy_kwh=(
            import_bog
            * c.mass
            * NH3_PER_H2_MASS_RATIO
            * inp.nh3_bog_reliquefaction_sec_kwh_per_kg
        ),
        tag="ESTIMATE",
        note=(
            f"BOG {import_bog * 100:.3f}% over {inp.nh3_import_storage_days:g} d at "
            f"{inp.nh3_import_bor_pct_per_day:g} %/d, re-liquefied. Every figure "
            "[ESTIMATE - needs source]."
        ),
    )

    # F2 -- cracking. Self-consumption is booked as mass loss (H2-equivalent
    # burned for heat or lost in PSA tail gas); the reaction duty is therefore
    # NOT added again as an energy term.
    c.add(
        "F2",
        "NH3 cracking + purification",
        "GH2",
        energy_kwh=inp.cracker_electrical_kwh_per_kg * c.mass,
        mass_loss_frac=inp.cracker_self_consumption_pct / 100.0,
        tag="ESTIMATE",
        note=(
            f"{inp.cracker_self_consumption_pct:g}% of the H2-equivalent entering is "
            "burned for reaction + sensible heat or lost in PSA tail gas "
            "[ESTIMATE - needs source]; floor is "
            f"{100 * cracking_reaction_duty_kwh_per_kg_h2() / H2_LHV_KWH_PER_KG:.1f}% "
            "from the reaction enthalpy alone. Electrical term is a separate "
            "[ESTIMATE]."
        ),
    )

    gaps = [
        "DECISION D4: no ammonia figure in this run is sourced. Every NH3 node "
        "value is a placeholder pending the internal Gentari NH3 dataset. "
        "[ESTIMATE - needs source]",
        "Haber-Bosch exothermic heat is not credited; recovering it as steam "
        "would lower the NH3 chain's net penalty. [needs source]",
        "Cracker self-consumption is booked as H2 mass loss. If a real cracker "
        "is fired on ammonia rather than product H2, the split between mass "
        "loss and NH3 consumption changes. [ESTIMATE]",
        "Electrolyser SEC (node A) is a user-supplied placeholder. [ASSUMPTION]",
        "Marine fuel, terminal utilities, and NH3 abatement/safety systems are "
        "outside this boundary and are not counted for either chain.",
    ]
    return ChainResult(
        chain="NH3",
        nodes=c.nodes,
        delivered_kg_h2=c.mass,
        total_energy_kwh=c.cumulative_energy,
        ambient_heat_kwh=c.ambient_heat,
        gaps=gaps,
    )


def compare(inp: ChainInputs | None = None) -> dict[str, ChainResult]:
    """Run both chains on identical shared inputs."""
    inp = inp or ChainInputs()
    return {"LH2": run_lh2_chain(inp), "NH3": run_nh3_chain(inp)}


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


def format_report(inp: ChainInputs | None = None) -> str:
    """Text report of both cascades, for the CLI."""
    inp = inp or ChainInputs()
    results = compare(inp)
    lines: list[str] = []
    lines.append("LH2 vs NH3 value chain -- energy-penalty cascade")
    lines.append("=" * 72)
    lines.append("Boundary: electrolyser battery limit -> GH2 at import send-out flange")
    lines.append(f"Basis:    1 kg H2 produced at node A; H2 LHV {H2_LHV_KWH_PER_KG:.2f} kWh/kg")
    lines.append(f"Corridor: {inp.voyage_distance_km:g} km one-way [ASSUMPTION]")
    lines.append("")

    for key in ("LH2", "NH3"):
        r = results[key]
        lines.append(f"--- {r.chain} chain " + "-" * (66 - len(r.chain)))
        header = (
            f"{'Node':<4} {'Name':<32} {'E kWh':>8} {'Cum kWh':>9} "
            f"{'kg H2e':>8} {'Net kWh':>9} {'Eff %':>7}"
        )
        lines.append(header)
        for n in r.nodes:
            lines.append(
                f"{n.node_id:<4} {n.name[:32]:<32} {n.energy_kwh:>8.3f} "
                f"{n.cumulative_energy_kwh:>9.3f} {n.mass_out_kg_h2e:>8.4f} "
                f"{n.net_energy_kwh:>9.3f} {n.efficiency_pct:>7.1f}"
            )
        lines.append("")
        lines.append(f"  Delivered H2            : {r.delivered_kg_h2:.4f} kg per kg produced")
        lines.append(f"  Total energy in         : {r.total_energy_kwh:.2f} kWh "
                     f"({r.total_energy_kwh * MJ_PER_KWH:.1f} MJ)")
        lines.append(f"  Energy per kg delivered : {r.energy_per_kg_delivered_kwh:.2f} kWh/kg")
        lines.append(f"  LHV delivered           : {r.lhv_delivered_kwh:.2f} kWh")
        lines.append(f"  Efficiency (input basis): {r.efficiency_pct:.1f} %")
        lines.append(f"  Net energy (deduction)  : {r.net_energy_kwh:.2f} kWh "
                     f"= {r.retained_pct:.1f} % of the H2's own LHV")
        if r.ambient_heat_kwh:
            lines.append(f"  Ambient heat (not charged): {r.ambient_heat_kwh:.2f} kWh")
        lines.append("")
        lines.append("  Gaps:")
        for g in r.gaps:
            lines.append(f"    - {g}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover
    print(format_report())
