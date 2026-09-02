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

**Annual scale & fleet (2026-09-02).** The per-kg cascade above is the
normalized basis; ``AnnualScaleResult`` (via ``annual_scale()``) multiplies it
by the study's annual H2 supply -- ``ChainInputs.annual_h2_supply_ktpa``,
[ASSUMPTION] anchored at node A, same basis as the per-kg cascade -- and sizes
the shipping fleet needed to move it, reusing ``src/lh2/shipping.py``'s
``round_trip_days``/``fleet_size`` for consistency with the rest of the repo.

**Cracker re-basis (2026-09-02).** Per user direction the cracker is now
natural-gas-fired: reaction heat is purchased NG (an external, charged energy
input, converted via ``ChainInputs.ng_fired_thermal_efficiency_pct``), not
combusted product H2/NH3. ``cracker_process_loss_pct`` replaces the old
``cracker_self_consumption_pct`` and covers only a small PSA/purification
slip. The resulting ammonia-per-delivered-H2 ratio (``nh3_supply_ratio()``,
computed from the physical NH3 made at B2 divided by the H2 delivered at F2)
comes out near the user's target of ~6.5:1 at the defaults -- above the pure
stoichiometric ~5.63:1 (``NH3_PER_H2_MASS_RATIO``) because
``nh3_bunker_fuel_rate_pct_per_day`` models ammonia consumed as the carrier's
own marine fuel during shipping (node D2), on top of ordinary cargo boil-off.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from . import shipping

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
    4.22 kWh/kg. [ASSUMPTION: derived] -- this is the minimum heat a
    natural-gas-fired heater must deliver (before its own firing losses) to
    crack 1 kg of H2 worth of ammonia; see ``ChainInputs.ng_fired_thermal_efficiency_pct``
    for how it becomes a purchased-NG energy figure at node F2.
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
    #: [ASSUMPTION] the study's annual H2 supply, anchored at node A -- same
    #: basis as the per-kg cascade. User-specified (2026-09-02), replacing the
    #: normalized 1 kg basis as the headline scale.
    annual_h2_supply_ktpa: float = 100.0
    #: [ASSUMPTION] fleet-wide operational availability (dry-docking,
    #: maintenance, weather margin), shared by both carriers. Same convention
    #: as ``src/lh2/shipping.py``'s ``fleet_size()`` default.
    fleet_availability_pct: float = 90.0

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
    #: cited: kawasaki-2026-questionnaire (reply Q29, vessel under
    #: construction, same tank tech as Suiso Frontier).
    lh2_vessel_capacity_m3: float = 40000.0
    #: [ASSUMPTION] usable fill vs full tank volume; not KHI-specific.
    lh2_vessel_fill_fraction_pct: float = 98.0
    #: [needs-source] LH2 density at NBP; mirrors
    #: data/properties/lh2-properties.csv (pending NIST/CODATA).
    lh2_density_kg_per_m3: float = 70.8
    #: cited: kawasaki-2026-questionnaire (reply Q27, ~1-1.5 d midpoint), same
    #: convention as ``src/lh2/shipping.py``'s ``KHI_LOAD_UNLOAD_DAYS_MID``.
    lh2_port_days_per_call: float = 1.25
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
    #: [ESTIMATE] user-specified (2026-09-02) mid-size ammonia/LPG-type
    #: carrier; not KHI-specific.
    nh3_vessel_capacity_m3: float = 40000.0
    #: [ASSUMPTION] matched to the LH2 side.
    nh3_vessel_fill_fraction_pct: float = 98.0
    #: [ESTIMATE - needs source] refrigerated liquid NH3 at ~ -33 C, 1 atm;
    #: standard published value, no citation logged.
    nh3_density_kg_per_m3: float = 682.0
    #: [ESTIMATE] placeholder, matched to the LH2 side pending an
    #: NH3-specific figure.
    nh3_port_days_per_call: float = 1.25
    #: [ESTIMATE] ammonia burned as the carrier's own propulsion fuel, on top
    #: of ordinary cargo boil-off -- linear in voyage days (fuel consumption
    #: tracks time at sea, not remaining inventory, so this is NOT compounded
    #: like boil-off). User direction (2026-09-02): the cracker is now
    #: NG-fired, so the ammonia-vs-delivered-H2 ratio (target ~6.5:1) exceeds
    #: the pure mass-balance ratio (~5.63:1, ``NH3_PER_H2_MASS_RATIO``); this
    #: is where that gap is modelled. Ammonia-fuelled marine engines are not
    #: yet commercial at scale -- this is a placeholder mechanism, not a
    #: disclosed figure.
    nh3_bunker_fuel_rate_pct_per_day: float = 1.3
    #: [ESTIMATE - needs source] PSA/purification tail-gas slip only -- the
    #: cracker's reaction heat now comes from natural gas (see
    #: ``ng_fired_thermal_efficiency_pct``), not from combusting product
    #: H2/NH3, so this replaces the old ``cracker_self_consumption_pct`` with
    #: a much smaller figure.
    cracker_process_loss_pct: float = 3.0
    #: [ASSUMPTION] typical industrial fired-heater efficiency converting NG
    #: HHV/LHV energy into delivered cracking reaction heat; not a disclosed
    #: figure.
    ng_fired_thermal_efficiency_pct: float = 85.0
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

    # D2 -- NH3 shipping. Two independent mass-loss mechanisms: ordinary cargo
    # BOG (compounding; reliquefied by default, or burned if the switch is
    # flipped) and bunker-fuel consumption (linear in voyage days; always
    # burned -- it is deliberately combusted as the ship's own propulsion
    # fuel, so it is never a candidate for re-liquefaction).
    days = voyage_days(inp.voyage_distance_km, inp.nh3_carrier_speed_km_per_h)
    voyage_bog = boil_off_fraction(inp.nh3_voyage_bor_pct_per_day, days)
    bunker_fuel_frac = min(inp.nh3_bunker_fuel_rate_pct_per_day * days / 100.0, 1.0)
    if inp.nh3_voyage_bog_reliquefied:
        ship_energy = (
            voyage_bog
            * c.mass
            * NH3_PER_H2_MASS_RATIO
            * inp.nh3_bog_reliquefaction_sec_kwh_per_kg
        )
        ship_loss = bunker_fuel_frac
        disposition = "ordinary BOG re-liquefied on board; bunker fuel burned"
    else:
        ship_energy = 0.0
        ship_loss = 1.0 - (1.0 - voyage_bog) * (1.0 - bunker_fuel_frac)
        disposition = "ordinary BOG and bunker fuel both burned"
    c.add(
        "D2",
        "NH3 shipping",
        "NH3",
        energy_kwh=ship_energy,
        mass_loss_frac=ship_loss,
        tag="ESTIMATE",
        note=(
            f"{days:.2f} d laden at {inp.nh3_carrier_speed_km_per_h:g} km/h; ordinary "
            f"voyage BOR {inp.nh3_voyage_bor_pct_per_day:g} %/d + bunker fuel "
            f"{inp.nh3_bunker_fuel_rate_pct_per_day:g} %/d ({disposition}). Every figure "
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

    # F2 -- cracking. Reaction heat is now natural-gas-fired (purchased,
    # charged energy), not combusted product H2/NH3, per user direction
    # (2026-09-02). Mass loss is a small PSA/purification slip only.
    ng_thermal_kwh = (
        cracking_reaction_duty_kwh_per_kg_h2()
        * c.mass
        / (inp.ng_fired_thermal_efficiency_pct / 100.0)
    )
    electrical_kwh = inp.cracker_electrical_kwh_per_kg * c.mass
    c.add(
        "F2",
        "NH3 cracking + purification",
        "GH2",
        energy_kwh=ng_thermal_kwh + electrical_kwh,
        mass_loss_frac=inp.cracker_process_loss_pct / 100.0,
        tag="ESTIMATE",
        note=(
            f"NG thermal {ng_thermal_kwh:.3f} kWh (reaction floor "
            f"{cracking_reaction_duty_kwh_per_kg_h2():.2f} kWh/kg-H2 @ "
            f"{inp.ng_fired_thermal_efficiency_pct:g}% fired efficiency) "
            "[ASSUMPTION] + electrical "
            f"{electrical_kwh:.3f} kWh (BOP/PSA/compression) [ESTIMATE]. "
            f"Mass loss is a {inp.cracker_process_loss_pct:g}% PSA/purification "
            "slip only [ESTIMATE - needs source] -- no product H2/NH3 is burned "
            "for reaction heat."
        ),
    )

    gaps = [
        "DECISION D4: no ammonia figure in this run is sourced. Every NH3 node "
        "value is a placeholder pending the internal Gentari NH3 dataset. "
        "[ESTIMATE - needs source]",
        "Haber-Bosch exothermic heat is not credited; recovering it as steam "
        "would lower the NH3 chain's net penalty. [needs source]",
        "Cracker is assumed natural-gas-fired (user direction 2026-09-02); "
        "the NG-fired thermal efficiency and the small process-loss slip left "
        "over are both placeholders. [ASSUMPTION / ESTIMATE]",
        "Ammonia bunker-fuel consumption during shipping (node D2) is a "
        "placeholder mechanism sized to reproduce the ~6.5:1 ammonia-to-"
        "delivered-H2 supply ratio at the default voyage length; real "
        "ammonia-fuelled marine engines are not yet commercial at scale. "
        "[ESTIMATE]",
        "Electrolyser SEC (node A) is a user-supplied placeholder. [ASSUMPTION]",
        "Natural gas combustion emissions (CO2 from the cracker's own fuel) "
        "are outside this energy-only boundary and are not counted.",
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


def nh3_supply_ratio(result: ChainResult) -> float:
    """Physical kg ammonia made (at B2/C2) per kg H2 ultimately delivered (F2).

    Reported for verification against the user's target ratio (~6.5:1,
    2026-09-02) -- it is a derived output, not a separate input. At the
    defaults this comes out near 6.5 because of the bunker-fuel loss modelled
    at node D2; it moves toward the pure stoichiometric ~5.63:1
    (``NH3_PER_H2_MASS_RATIO``) as that loss is reduced toward zero.
    """
    try:
        b2 = next(n for n in result.nodes if n.node_id == "B2")
    except StopIteration:
        return float("nan")
    nh3_produced_kg = b2.mass_out_kg_h2e * NH3_PER_H2_MASS_RATIO
    if result.delivered_kg_h2 <= 0:
        return float("nan")
    return nh3_produced_kg / result.delivered_kg_h2


# --------------------------------------------------------------------------
# Annual scale & fleet
# --------------------------------------------------------------------------


@dataclass
class AnnualScaleResult:
    """Scales the per-kg cascade to the study's annual H2 supply and sizes
    the shipping fleet needed to move it.

    [ASSUMPTION] ``annual_h2_supply_ktpa`` is anchored at node A (H2
    produced), matching the per-kg cascade's own basis -- not the delivered
    (import-side) quantity. See docs/comparison/01-energy-penalty-method.md.
    """

    chain: str
    annual_h2_supply_kg: float
    annual_delivered_kg: float
    annual_energy_kwh: float
    #: Physical cargo mass loaded onto vessels per year (kg) -- LH2 kg for the
    #: LH2 chain, physical NH3 kg (via ``NH3_PER_H2_MASS_RATIO``) for NH3.
    annual_cargo_kg: float
    vessel_capacity_m3: float
    fill_fraction_pct: float
    cargo_per_voyage_kg: float
    round_trip_days: float
    trips_per_year_per_vessel: float
    annual_capacity_per_vessel_kg: float
    fleet_size: int


def annual_scale(result: ChainResult, inp: ChainInputs) -> AnnualScaleResult:
    """Derive annual energy, cargo tonnage, and fleet size from a per-kg
    ``ChainResult`` and the study's ``annual_h2_supply_ktpa``.

    Reuses ``src/lh2/shipping.py``'s ``round_trip_days``/``fleet_size`` (an
    effective capacity = nameplate capacity x fill fraction is passed in,
    since that helper does not itself take a fill fraction) so the fleet math
    stays identical to the rest of the repo.
    """
    annual_h2_supply_kg = inp.annual_h2_supply_ktpa * 1.0e6  # 1 kt = 1e6 kg
    annual_delivered_kg = result.delivered_kg_h2 * annual_h2_supply_kg
    annual_energy_kwh = result.total_energy_kwh * annual_h2_supply_kg

    d_node = next(n for n in result.nodes if n.node_id in ("D1", "D2"))
    if result.chain == "NH3":
        physical_mass_frac = d_node.mass_in_kg_h2e * NH3_PER_H2_MASS_RATIO
        capacity_m3 = inp.nh3_vessel_capacity_m3
        fill_pct = inp.nh3_vessel_fill_fraction_pct
        density = inp.nh3_density_kg_per_m3
        port_days = inp.nh3_port_days_per_call
        speed = inp.nh3_carrier_speed_km_per_h
    else:
        physical_mass_frac = d_node.mass_in_kg_h2e
        capacity_m3 = inp.lh2_vessel_capacity_m3
        fill_pct = inp.lh2_vessel_fill_fraction_pct
        density = inp.lh2_density_kg_per_m3
        port_days = inp.lh2_port_days_per_call
        speed = inp.lh2_carrier_speed_km_per_h

    annual_cargo_kg = physical_mass_frac * annual_h2_supply_kg
    rtd = shipping.round_trip_days(inp.voyage_distance_km, speed, port_days, port_days)
    effective_capacity_m3 = capacity_m3 * (fill_pct / 100.0)
    availability = inp.fleet_availability_pct / 100.0
    n_vessels = shipping.fleet_size(
        annual_cargo_kg,
        rtd,
        cargo_capacity=effective_capacity_m3,
        lh2_density=density,
        availability=availability,
    )
    cargo_per_voyage_kg = effective_capacity_m3 * density
    trips_per_year = (365.0 / rtd) * availability if rtd > 0 else 0.0

    return AnnualScaleResult(
        chain=result.chain,
        annual_h2_supply_kg=annual_h2_supply_kg,
        annual_delivered_kg=annual_delivered_kg,
        annual_energy_kwh=annual_energy_kwh,
        annual_cargo_kg=annual_cargo_kg,
        vessel_capacity_m3=capacity_m3,
        fill_fraction_pct=fill_pct,
        cargo_per_voyage_kg=cargo_per_voyage_kg,
        round_trip_days=rtd,
        trips_per_year_per_vessel=trips_per_year,
        annual_capacity_per_vessel_kg=cargo_per_voyage_kg * trips_per_year,
        fleet_size=n_vessels,
    )


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
    lines.append(f"Scale:    {inp.annual_h2_supply_ktpa:g} ktpa H2 supply at node A [ASSUMPTION]")
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
        if key == "NH3":
            lines.append(f"  Ammonia supply ratio    : {nh3_supply_ratio(r):.2f} kg NH3 per kg H2 "
                         f"delivered (mass-balance floor {NH3_PER_H2_MASS_RATIO:.2f}:1)")
        lines.append("")

        a = annual_scale(r, inp)
        lines.append(f"  --- Annual scale & fleet ({inp.annual_h2_supply_ktpa:g} ktpa H2 supply) ---")
        lines.append(f"  Annual energy           : {a.annual_energy_kwh / 1e9:.3f} TWh/y")
        lines.append(f"  Annual H2 delivered     : {a.annual_delivered_kg / 1e6:.1f} kt/y")
        lines.append(f"  Annual cargo shipped    : {a.annual_cargo_kg / 1e6:.1f} kt/y "
                     f"({r.chain} mass)")
        lines.append(f"  Vessel                  : {a.vessel_capacity_m3:,.0f} m3 @ "
                     f"{a.fill_fraction_pct:g}% fill = {a.cargo_per_voyage_kg / 1e3:.0f} t/voyage")
        lines.append(f"  Round-trip cycle        : {a.round_trip_days:.2f} d, "
                     f"{a.trips_per_year_per_vessel:.1f} trips/y/vessel")
        lines.append(f"  Fleet size required     : {a.fleet_size} vessel(s)")
        lines.append("")
        lines.append("  Gaps:")
        for g in r.gaps:
            lines.append(f"    - {g}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":  # pragma: no cover
    print(format_report())
