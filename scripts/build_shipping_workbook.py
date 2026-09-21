#!/usr/bin/env python3
"""Build the Excel translation of docs/reports/lh2-vs-nh3-shipping-studies.html.

Same model as scripts/run_shipping_comparison.py and src/lh2/shipping.py,
reimplemented as live Excel formulas so a reviewer can change an input cell
and watch every table and chart recompute -- no macros, no external add-ins.
All breakeven values that the HTML artifact finds by bisection are solved
here in closed form (the underlying relationships are invertible), so no
Goal Seek / iterative calculation is required.

Run:   python scripts/build_shipping_workbook.py
Then:  python <xlsx-skill-dir>/scripts/recalc.py docs/reports/lh2-vs-nh3-shipping-studies.xlsx
"""

from __future__ import annotations

from openpyxl import Workbook
from openpyxl.chart import LineChart, BarChart, Reference
from openpyxl.chart.marker import Marker
from openpyxl.comments import Comment
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = "docs/reports/lh2-vs-nh3-shipping-studies.xlsx"

# ---------------------------------------------------------------- styling --
ARIAL = "Arial"
BLUE, BLACK, GREEN = "0000FF", "000000", "196619"
INK, MUTED = "1F2937", "6B7280"
HDR_FILL = PatternFill("solid", fgColor="1F3864")
SEC_FILL = PatternFill("solid", fgColor="DDEBF7")
LH2_FILL = PatternFill("solid", fgColor="D9EEF5")
NH3_FILL = PatternFill("solid", fgColor="FBEACB")
INPUT_FILL = PatternFill("solid", fgColor="FFFFFF")
FLAG_FILL = PatternFill("solid", fgColor="FFF2CC")
CITED_FILL = PatternFill("solid", fgColor="E2EFDA")
KPI_FILL = PatternFill("solid", fgColor="F2F6FB")
THIN = Side(style="thin", color="B7C4D6")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

TITLE_F = Font(name=ARIAL, size=16, bold=True, color="FFFFFF")
SUBTITLE_F = Font(name=ARIAL, size=10, italic=True, color="FFFFFF")
SECTION_F = Font(name=ARIAL, size=11, bold=True, color="1F3864")
HEADER_F = Font(name=ARIAL, size=10, bold=True, color=INK)
LABEL_F = Font(name=ARIAL, size=10, color=INK)
NOTE_F = Font(name=ARIAL, size=9, italic=True, color=MUTED)
INPUT_F = Font(name=ARIAL, size=10, bold=True, color=BLUE)
FORMULA_F = Font(name=ARIAL, size=10, color=BLACK)
LINK_F = Font(name=ARIAL, size=10, color=GREEN)
TAG_F = Font(name=ARIAL, size=8, bold=True, color=MUTED)
KPI_LABEL_F = Font(name=ARIAL, size=9, color=MUTED)
KPI_VALUE_F = Font(name=ARIAL, size=18, bold=True, color="1F3864")


def cell(ws, row, col, value=None, font=None, fill=None, fmt=None, align=None,
         border=True, wrap=False, comment=None):
    c = ws.cell(row=row, column=col, value=value)
    c.font = font or FORMULA_F
    if fill:
        c.fill = fill
    if fmt:
        c.number_format = fmt
    if align:
        c.alignment = align
    elif wrap:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    if border:
        c.border = BORDER
    if comment:
        c.comment = Comment(comment, "Model")
    return c


def title_bar(ws, text, subtitle, ncols=6):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    for r in (1, 2):
        for c in range(1, ncols + 1):
            ws.cell(row=r, column=c).fill = HDR_FILL
    t = ws.cell(row=1, column=1, value=text)
    t.font = TITLE_F
    t.alignment = Alignment(vertical="center")
    s = ws.cell(row=2, column=1, value=subtitle)
    s.font = SUBTITLE_F
    s.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 26
    ws.row_dimensions[2].height = 28


def section(ws, row, text, ncols, fill=SEC_FILL):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row=row, column=1, value=text)
    c.font = SECTION_F
    c.fill = fill
    for col in range(1, ncols + 1):
        ws.cell(row=row, column=col).fill = fill
        ws.cell(row=row, column=col).border = BORDER
    return row + 1


def input_row(ws, row, label, value, unit, tag, note, fmt="0.00", col_val=2):
    cell(ws, row, 1, label, LABEL_F, border=True)
    v = cell(ws, row, col_val, value, INPUT_F, INPUT_FILL, fmt)
    cell(ws, row, col_val + 1, unit, NOTE_F, border=True)
    tagfill = CITED_FILL if tag == "CITED" else (FLAG_FILL if tag in ("ASSUMPTION", "ESTIMATE") else None)
    cell(ws, row, col_val + 2, tag, TAG_F, tagfill, align=Alignment(horizontal="center"))
    cell(ws, row, col_val + 3, note, NOTE_F, wrap=True)
    return f"${get_column_letter(col_val)}${row}"


def calc_row(ws, row, label, formula, unit, fmt="#,##0.00", note=None, col_val=2, link=False):
    cell(ws, row, 1, label, LABEL_F)
    v = cell(ws, row, col_val, formula, LINK_F if link else FORMULA_F, None, fmt)
    cell(ws, row, col_val + 1, unit, NOTE_F, border=True)
    if note:
        cell(ws, row, col_val + 3, note, NOTE_F, wrap=True)
    return f"${get_column_letter(col_val)}${row}"


def set_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def sheet_ref(sheet, coord):
    return f"'{sheet}'!{coord}"


# ============================================================================
wb = Workbook()
wb.remove(wb.active)

# ============================================================================
# SHEET 1: INPUTS
# ============================================================================
ws = wb.create_sheet("Inputs")
set_widths(ws, [34, 13, 10, 12, 46])
title_bar(ws, "LH₂ vs Ammonia — Shipping Inputs",
          "Edit any blue cell — every sheet, table and chart in this workbook recomputes live. "
          "Corridor: Kakinada, India → Hamburg, Germany. Font: Arial throughout.", ncols=5)

r = 4
for i, h in enumerate(["Parameter", "Value", "Unit", "Tag", "Note / source"], start=1):
    cell(ws, r, i, h, HEADER_F, SEC_FILL)
r += 1

r = section(ws, r, "CORRIDOR  —  Kakinada, India → Hamburg, Germany", 5)
DIST = input_row(ws, r, "One-way distance", 21200, "km", "ESTIMATE",
                  "First-principles great-circle waypoint sum (distance-calculator sites are "
                  "egress-blocked from this environment). Suez route ≈10,260 km; Cape of Good "
                  "Hope route (primary, current Red Sea rerouting reality) ≈21,200 km. "
                  "See data/routes/kakinada-hamburg.csv.", "#,##0"); r += 1

r += 1
r = section(ws, r, "LH₂ VESSEL", 5, LH2_FILL)
LH2_CAP = input_row(ws, r, "Capacity (choose 40,000 or 160,000)", 160000, "m³", "CITED",
                     "KHI-disclosed. 40,000 m³ = vessel under construction (reply Q29); "
                     "160,000 m³ = commercial-scale target (cost-basis slide).", "#,##0")
dv_lh2 = DataValidation(type="list", formula1='"40000,160000"', allow_blank=False)
ws.add_data_validation(dv_lh2); dv_lh2.add(ws[LH2_CAP.replace("$", "")]); r += 1
LH2_RHO = input_row(ws, r, "Cargo density", 70.8, "kg/m³", "needs-source",
                     "LH2 at NBP; data/properties/lh2-properties.csv, pending NIST/CODATA citation.",
                     "#,##0.0"); r += 1
LH2_FILLFRAC = input_row(ws, r, "Fill fraction", 0.98, "%", "ASSUMPTION",
                          "Ullage / ship-fill-limit placeholder, not KHI-specific.", "0.0%"); r += 1
LH2_SPEED = input_row(ws, r, "Service speed", 29.6, "km/h", "CITED",
                       "≈16 kn; kawasaki-2026-supplemental, given for the 160,000 m³ "
                       "commercial vessel and reused for the 40,000 m³ hull.", "#,##0.0"); r += 1
LH2_PORT = input_row(ws, r, "Port days per call", 1.25, "day", "CITED",
                      "Midpoint of KHI's disclosed 1–1.5 day range (reply Q27).", "0.00"); r += 1
LH2_BOR = input_row(ws, r, "Voyage boil-off rate", 0.002, "%/day", "ESTIMATE",
                     "KHI never disclosed a standalone voyage BOR. The single biggest lever in this "
                     "workbook. Literature (RSER 2026, unpromoted) suggests ~3.44%/day for a "
                     "comparable vessel class.", "0.000%"); r += 1
LH2_DUTY = input_row(ws, r, "Propulsion fuel duty (VLSFO)", 25, "t/day", "ASSUMPTION",
                      "Carried over from the ammonia vessel's stated duty so both ships share one "
                      "basis — NOT a disclosed figure for either LH2 hull. See suggested-duty "
                      "cell below.", "#,##0.0"); r += 1

r += 1
r = section(ws, r, "NH₃ VESSEL  (fully refrigerated, ~-33°C)", 5, NH3_FILL)
NH3_CAP = input_row(ws, r, "Capacity (choose 24k / 40k / 60k / 90k)", 24000, "m³", "ASSUMPTION",
                     "24,000 m³ = originally specified vessel; 40k/60k/90k = mid-size / large / "
                     "VLGC-scale gas-carrier size bands (general industry classes, not repository "
                     "figures). Largest ammonia carriers in service are ~87,000 m³.", "#,##0")
dv_nh3 = DataValidation(type="list", formula1='"24000,40000,60000,90000"', allow_blank=False)
ws.add_data_validation(dv_nh3); dv_nh3.add(ws[NH3_CAP.replace("$", "")]); r += 1
NH3_RHO = input_row(ws, r, "Cargo density", 682, "kg/m³", "ESTIMATE",
                     "Standard published value for refrigerated liquid ammonia; no primary "
                     "citation logged yet.", "#,##0"); r += 1
NH3_FILLFRAC = input_row(ws, r, "Fill fraction", 0.98, "%", "ASSUMPTION",
                          "Matched to the LH2 side for comparability.", "0.0%"); r += 1
NH3_SPEED_KN = input_row(ws, r, "Service speed", 13, "knot", "ASSUMPTION",
                          "User-specified. Converted to km/h below.", "0.0"); r += 1
NH3_SPEED = calc_row(ws, r, "  → converted speed", f"={NH3_SPEED_KN}*1.852", "km/h",
                      "#,##0.000", note="13 kn × 1.852 = 24.076 km/h"); r += 1
NH3_PORT = input_row(ws, r, "Port days per call", 1.5, "day", "ASSUMPTION",
                      "Matched to the LH2 carrier's disclosed range for comparability.", "0.00"); r += 1
NH3_BOR = input_row(ws, r, "Voyage boil-off rate", 0.0015, "%/day", "ASSUMPTION",
                     "User selected the 0.10–0.20%/day range; midpoint used as the point "
                     "default.", "0.000%"); r += 1
NH3_DUTY = input_row(ws, r, "Propulsion fuel duty (VLSFO)", 25, "t/day", "ASSUMPTION",
                      "User-specified.", "#,##0.0"); r += 1
NH3_RELIQ = input_row(ws, r, "Re-liquefaction energy", 0.25, "kWh/kg BOG", "ESTIMATE",
                       "Placeholder — no NH3 dataset yet (decision D4).", "0.00"); r += 1
NH3_GENSET = input_row(ws, r, "Reliquefaction genset efficiency", 0.45, "%", "ASSUMPTION",
                        "Typical medium-speed marine genset efficiency; not vessel-specific.",
                        "0.0%"); r += 1

r += 1
r = section(ws, r, "SHARED ASSUMPTIONS", 5)
AVAIL = input_row(ws, r, "Fleet availability", 0.90, "%", "ASSUMPTION",
                   "Dry-docking / maintenance / weather margin.", "0.0%"); r += 1
DEMAND = input_row(ws, r, "Annual H₂-equivalent demand", 100, "ktpa", "ASSUMPTION",
                    "Study basis — quantity handed to the ships, not upstream production.",
                    "#,##0"); r += 1
RATIO = input_row(ws, r, "NH₃ : H₂ stoichiometric ratio", 5.632, "kg/kg", "ASSUMPTION",
                   "First-principles: N₂ + 3H₂ → 2NH₃.", "0.000"); r += 1
VLSFO_LHV = input_row(ws, r, "VLSFO lower heating value", 40.2, "MJ/kg", "ESTIMATE",
                       "Marine convention for (very-low-sulphur) fuel oil.", "0.0"); r += 1
H2_LHV = input_row(ws, r, "H₂ lower heating value", 120, "MJ/kg", "needs-source",
                    "data/properties/lh2-properties.csv, pending NIST/ISO citation.", "0.0"); r += 1
ENGRATIO = input_row(ws, r, "BOG vs oil engine efficiency ratio", 1.00, "kg/kg", "ASSUMPTION",
                      "Thermal efficiency burning cargo boil-off vs burning liquid bunker fuel in "
                      "the same engine. 1.0 = identical.", "0.00"); r += 1
GWP = input_row(ws, r, "Vented H₂ warming potential (GWP100)", 11.6, "kgCO2e/kg", "ESTIMATE",
                 "Wide published uncertainty band, no primary citation logged. Applies only if "
                 "disposal below = Vented — a gas combustion unit burns it to water instead.",
                 "0.0"); r += 1

r += 1
r = section(ws, r, "PRICES  &  MODE  (set by you — nothing here is a repository default)", 5)
H2PRICE = input_row(ws, r, "Hydrogen value", 5.00, "USD/kg", "needs-source",
                     "Not logged anywhere in the repository. The model reports a breakeven price "
                     "rather than asserting one.", "$#,##0.00"); r += 1
VLSFOPRICE = input_row(ws, r, "VLSFO price", 600, "USD/t", "needs-source",
                        "Not logged in the repository.", "$#,##0"); r += 1

cell(ws, r, 1, "Cost basis mode", LABEL_F)
MODE = f"$B${r}"; cell(ws, r, 2, "Boil-off only", INPUT_F, INPUT_FILL)
cell(ws, r, 3, "choice", NOTE_F, border=True)
cell(ws, r, 4, "CHOICE", TAG_F, align=Alignment(horizontal="center"))
cell(ws, r, 5, "\"Boil-off only\" charges each carrier just what its boil-off costs. \"Full leg "
     "fuel bill\" adds the whole propulsion duty each ship buys — kept because the two laden "
     "legs differ in length, so that term does not cleanly cancel.", NOTE_F, wrap=True)
dv_mode = DataValidation(type="list", formula1='"Boil-off only,Full leg fuel bill"', allow_blank=False)
ws.add_data_validation(dv_mode); dv_mode.add(ws["B" + str(r)]); r += 1

cell(ws, r, 1, "Surplus boil-off disposal", LABEL_F)
DISPOSAL = f"$B${r}"; cell(ws, r, 2, "Vented", INPUT_F, INPUT_FILL)
cell(ws, r, 3, "choice", NOTE_F, border=True)
cell(ws, r, 4, "CHOICE", TAG_F, align=Alignment(horizontal="center"))
cell(ws, r, 5, "Boil-off above the engine's demand cannot be used for propulsion regardless. "
     "\"GCU burned\" oxidises it to water (KHI reply Q26) instead of releasing it — the "
     "hydrogen is lost from cargo either way; only the CO2e line changes.", NOTE_F, wrap=True)
dv_disp = DataValidation(type="list", formula1='"Vented,GCU burned"', allow_blank=False)
ws.add_data_validation(dv_disp); dv_disp.add(ws["B" + str(r)]); r += 1

cell(ws, r, 1, "Boil-off fate basis (Sens - Boiloff sheet)", LABEL_F)
BASIS = f"$B${r}"; cell(ws, r, 2, "Per laden leg", INPUT_F, INPUT_FILL)
cell(ws, r, 3, "choice", NOTE_F, border=True)
cell(ws, r, 4, "CHOICE", TAG_F, align=Alignment(horizontal="center"))
cell(ws, r, 5, "Switches the \"fate of the boil-off\" table/chart between totals for the whole "
     "one-way route and a daily rate.", NOTE_F, wrap=True)
dv_basis = DataValidation(type="list", formula1='"Per laden leg,Per day"', allow_blank=False)
ws.add_data_validation(dv_basis); dv_basis.add(ws["B" + str(r)]); r += 1

cell(ws, r, 1, "Duty scaling exponent (Decision Map sheet)", LABEL_F)
EXPO = f"$B${r}"; cell(ws, r, 2, 0.667, INPUT_F, INPUT_FILL); ws["B" + str(r)].number_format = "0.000"
cell(ws, r, 3, "exponent", NOTE_F, border=True)
cell(ws, r, 4, "ASSUMPTION", TAG_F, FLAG_FILL, align=Alignment(horizontal="center"))
cell(ws, r, 5, "How LH2 propulsion duty scales with hull size when the Decision Map sweeps "
     "capacity, anchored on the 24,000 m³ / 25 t/day pair. 0 = duty fixed; 0.667 = resistance "
     "≈ wetted area (default); 1 = duty ∝ cargo (coverage constant, size drops out). No "
     "power curve is held for any vessel.", NOTE_F, wrap=True); r += 2

r = section(ws, r, "SUGGESTED DUTY  (informational only — not applied automatically)", 5)
SUG_LH2 = calc_row(ws, r, "Suggested LH₂ duty at the selected capacity",
                    f"=25*({LH2_CAP}/24000)^0.667", "t/day", "#,##0.0",
                    note="size^⅔ (resistance) scaling from the 24,000 m³ / 25 t/day ammonia "
                         "basis; copy into the LH2 duty cell above if you want to use it."); r += 1
SUG_NH3 = calc_row(ws, r, "Suggested NH₃ duty at the selected capacity",
                    f"=25*({NH3_CAP}/24000)^0.667", "t/day", "#,##0.0",
                    note="Same scaling rule, evaluated at the NH3 capacity selected above."); r += 1

ws.freeze_panes = "A4"

IN = dict(DIST=DIST, LH2_CAP=LH2_CAP, LH2_RHO=LH2_RHO, LH2_FILLFRAC=LH2_FILLFRAC,
          LH2_SPEED=LH2_SPEED, LH2_PORT=LH2_PORT, LH2_BOR=LH2_BOR, LH2_DUTY=LH2_DUTY,
          NH3_CAP=NH3_CAP, NH3_RHO=NH3_RHO, NH3_FILLFRAC=NH3_FILLFRAC, NH3_SPEED_KN=NH3_SPEED_KN,
          NH3_SPEED=NH3_SPEED, NH3_PORT=NH3_PORT, NH3_BOR=NH3_BOR, NH3_DUTY=NH3_DUTY,
          NH3_RELIQ=NH3_RELIQ, NH3_GENSET=NH3_GENSET, AVAIL=AVAIL, DEMAND=DEMAND, RATIO=RATIO,
          VLSFO_LHV=VLSFO_LHV, H2_LHV=H2_LHV, ENGRATIO=ENGRATIO, GWP=GWP, H2PRICE=H2PRICE,
          VLSFOPRICE=VLSFOPRICE, MODE=MODE, DISPOSAL=DISPOSAL, BASIS=BASIS, EXPO=EXPO)
IX = {k: sheet_ref("Inputs", v) for k, v in IN.items()}
print("Inputs sheet OK, last row", r)

# ============================================================================
# SHEET 2: VOYAGE MODEL
# ============================================================================
ws = wb.create_sheet("Voyage Model")
set_widths(ws, [40, 12, 16, 16, 46])
title_bar(ws, "Voyage Model", "One voyage, both carriers, at the current Inputs. "
          "Every downstream sheet reads from here or recomputes the same formulas at swept values.",
          ncols=5)

r = 4
cell(ws, r, 1, "Metric", HEADER_F, SEC_FILL)
cell(ws, r, 2, "Unit", HEADER_F, SEC_FILL)
cell(ws, r, 3, "LH₂ carrier", HEADER_F, LH2_FILL)
cell(ws, r, 4, "NH₃ carrier", HEADER_F, NH3_FILL)
cell(ws, r, 5, "Note", HEADER_F, SEC_FILL)
r += 1
M = {}


def model_row(row, label, unit, f_lh2, f_nh3, fmt="#,##0.00", note=None):
    cell(ws, row, 1, label, LABEL_F)
    cell(ws, row, 2, unit, NOTE_F, border=True)
    cell(ws, row, 3, f_lh2, FORMULA_F, LH2_FILL, fmt)
    cell(ws, row, 4, f_nh3, FORMULA_F, NH3_FILL, fmt)
    if note:
        cell(ws, row, 5, note, NOTE_F, wrap=True)
    return f"$C${row}", f"$D${row}"


r = section(ws, r, "VOYAGE  &  THROUGHPUT", 5)
M["one_way"] = model_row(r, "One-way transit", "day",
                          f"={IX['DIST']}/{IX['LH2_SPEED']}/24", f"={IX['DIST']}/{IX['NH3_SPEED']}/24",
                          "0.00"); r += 1
M["rtd"] = model_row(r, "Round-trip cycle", "day",
                      f"=2*{M['one_way'][0]}+2*{IX['LH2_PORT']}", f"=2*{M['one_way'][1]}+2*{IX['NH3_PORT']}",
                      "0.00"); r += 1
M["cargo"] = model_row(r, "Cargo loaded per voyage", "kg",
                        f"={IX['LH2_CAP']}*{IX['LH2_RHO']}*{IX['LH2_FILLFRAC']}",
                        f"={IX['NH3_CAP']}*{IX['NH3_RHO']}*{IX['NH3_FILLFRAC']}",
                        "#,##0"); r += 1
M["bog_frac"] = model_row(r, "Boil-off fraction (compounding, laden leg)", "%",
                           f"=1-(1-{IX['LH2_BOR']})^{M['one_way'][0]}",
                           f"=1-(1-{IX['NH3_BOR']})^{M['one_way'][1]}",
                           "0.000%",
                           note="Compounding daily loss over the one-way laden leg only "
                                "(matches src/lh2/chain_energy.py's voyage_days() convention)."); r += 1
M["loss_frac"] = model_row(r, "Cargo mass-loss fraction", "%",
                            f"={M['bog_frac'][0]}", "=0", "0.000%",
                            note="LH2 burns boil-off as fuel → cargo mass lost = boil-off "
                                 "fraction. NH3 re-liquefies on board → no mass loss (energy "
                                 "cost instead, costed below)."); r += 1
M["delivered_voy"] = model_row(r, "Delivered cargo per voyage", "kg",
                                f"={M['cargo'][0]}*(1-{M['loss_frac'][0]})",
                                f"={M['cargo'][1]}*(1-{M['loss_frac'][1]})", "#,##0"); r += 1
M["trips"] = model_row(r, "Trips per vessel-year", "trips/y",
                        f"=365/{M['rtd'][0]}*{IX['AVAIL']}", f"=365/{M['rtd'][1]}*{IX['AVAIL']}",
                        "0.00"); r += 1
M["annual_cargo"] = model_row(r, "Annual delivered cargo per vessel", "kg/y",
                               f"={M['delivered_voy'][0]}*{M['trips'][0]}",
                               f"={M['delivered_voy'][1]}*{M['trips'][1]}", "#,##0"); r += 1
M["annual_h2e"] = model_row(r, "Annual delivered H₂-equivalent per vessel", "kg/y",
                             f"={M['annual_cargo'][0]}", f"={M['annual_cargo'][1]}/{IX['RATIO']}",
                             "#,##0"); r += 1
M["annual_ktpa"] = model_row(r, "Annual delivered H₂-equivalent per vessel", "ktpa",
                              f"={M['annual_h2e'][0]}/1000000", f"={M['annual_h2e'][1]}/1000000",
                              "#,##0.00"); r += 1
M["fleet"] = model_row(r, "Fleet size for the stated annual demand", "vessels",
                        f"=CEILING({IX['DEMAND']}*1000000/{M['annual_cargo'][0]},1)",
                        f"=CEILING({IX['DEMAND']}*1000000*{IX['RATIO']}/{M['annual_cargo'][1]},1)",
                        "0",
                        note="Ships must LOAD enough cargo, net of voyage loss, to meet the "
                             "delivered H2-equivalent demand."); r += 1

r += 1
r = section(ws, r, "BUNKER FUEL  &  BOIL-OFF BALANCE", 5)
M["demand_mj"] = model_row(r, "Propulsion energy demand (laden leg)", "MJ",
                            f"={IX['LH2_DUTY']}*1000*{M['one_way'][0]}*{IX['VLSFO_LHV']}",
                            f"={IX['NH3_DUTY']}*1000*{M['one_way'][1]}*{IX['VLSFO_LHV']}",
                            "#,##0"); r += 1
M["bog_kg"] = model_row(r, "Boil-off generated (laden leg)", "kg",
                         f"={M['cargo'][0]}*{M['bog_frac'][0]}", f"={M['cargo'][1]}*{M['bog_frac'][1]}",
                         "#,##0"); r += 1
M["bog_energy"] = model_row(r, "Boil-off energy available to burn", "MJ",
                             f"={M['bog_kg'][0]}*{IX['H2_LHV']}*{IX['ENGRATIO']}", "=0",
                             "#,##0",
                             note="NH3 does not burn its boil-off for propulsion — it "
                                  "re-liquefies it (see reliquefaction fuel row below)."); r += 1
M["useful_mj"] = model_row(r, "  — useful (displaces VLSFO)", "MJ",
                            f"=MIN({M['bog_energy'][0]},{M['demand_mj'][0]})", "=0", "#,##0"); r += 1
M["surplus_mj"] = model_row(r, "  — surplus (cannot be used for propulsion)", "MJ",
                             f"=MAX(0,{M['bog_energy'][0]}-{M['demand_mj'][0]})", "=0", "#,##0"); r += 1
M["coverage"] = model_row(r, "Boil-off covers this share of propulsion demand", "%",
                           f"=IF({M['demand_mj'][0]}=0,0,{M['bog_energy'][0]}/{M['demand_mj'][0]})",
                           "=0", "0%",
                           note="Above 100%, the surplus is wasted. Below 100%, top-up VLSFO is "
                                "still bought."); r += 1
M["useful_kg"] = model_row(r, "  — useful boil-off mass", "kg",
                            f"=IF({IX['H2_LHV']}*{IX['ENGRATIO']}=0,0,{M['useful_mj'][0]}/({IX['H2_LHV']}*{IX['ENGRATIO']}))",
                            "=0", "#,##0"); r += 1
M["surplus_kg"] = model_row(r, "  — surplus boil-off mass", "kg",
                             f"=IF({IX['H2_LHV']}*{IX['ENGRATIO']}=0,0,{M['surplus_mj'][0]}/({IX['H2_LHV']}*{IX['ENGRATIO']}))",
                             "=0", "#,##0"); r += 1
M["topup_t"] = model_row(r, "Top-up VLSFO bought", "t",
                          f"=MAX(0,{M['demand_mj'][0]}-{M['bog_energy'][0]})/{IX['VLSFO_LHV']}/1000",
                          f"={IX['NH3_DUTY']}*{M['one_way'][1]}", "#,##0.0",
                          note="NH3 always buys its full propulsion duty in bunker fuel — its "
                               "boil-off is re-liquefied, never burned for propulsion."); r += 1
M["displaced_t"] = model_row(r, "VLSFO displaced by boil-off", "t",
                              f"={M['useful_mj'][0]}/{IX['VLSFO_LHV']}/1000", "=0", "#,##0.0"); r += 1
M["reliq_kwh"] = model_row(r, "Reliquefaction electricity required", "kWh", "=0",
                            f"={M['bog_kg'][1]}*{IX['NH3_RELIQ']}", "#,##0"); r += 1
M["reliq_t"] = model_row(r, "Reliquefaction VLSFO (via genset)", "t", "=0",
                          f"={M['reliq_kwh'][1]}*3.6/({IX['VLSFO_LHV']}*{IX['NH3_GENSET']})/1000",
                          "#,##0.0"); r += 1
M["total_fuel_t"] = model_row(r, "Total VLSFO purchased", "t",
                               f"={M['topup_t'][0]}", f"={M['topup_t'][1]}+{M['reliq_t'][1]}",
                               "#,##0.0"); r += 1
M["cargo_lost"] = model_row(r, "Cargo mass lost to boil-off", "kg",
                             f"={M['bog_kg'][0]}", "=0", "#,##0",
                             note="0 for NH3: re-liquefaction conserves cargo mass."); r += 1
M["delivered_h2e_voy"] = model_row(r, "Delivered H₂-equivalent, this voyage", "kg",
                                    f"={M['delivered_voy'][0]}", f"={M['delivered_voy'][1]}/{IX['RATIO']}",
                                    "#,##0"); r += 1
co2e = model_row(r, "CO₂e if surplus is vented", "kg CO2e",
                  f"=IF({IX['DISPOSAL']}=\"Vented\",{M['surplus_kg'][0]}*{IX['GWP']},0)", "=0",
                  "#,##0",
                  note="0 whenever disposal = \"GCU burned\": the gas combustion unit oxidises "
                       "surplus H2 to water (KHI reply Q26); the hydrogen is still lost from "
                       "cargo either way."); r += 1
M["co2e"] = co2e

r += 1
r = section(ws, r, "COST PER KG H₂ DELIVERED", 5)
M["cargo_cost"] = model_row(r, "Hydrogen given up, priced as fuel", "USD",
                             f"={M['cargo_lost'][0]}*{IX['H2PRICE']}", "=0", "$#,##0"); r += 1
M["fuel_cost_boiloff"] = model_row(r, "Fuel cost — boil-off only basis", "USD",
                                    f"=({M['reliq_t'][0]}-{M['displaced_t'][0]})*{IX['VLSFOPRICE']}",
                                    f"=({M['reliq_t'][1]}-{M['displaced_t'][1]})*{IX['VLSFOPRICE']}",
                                    "$#,##0",
                                    note="LH2: negative (a credit) — the VLSFO its own boil-off "
                                         "displaced. NH3: the genset fuel to re-liquefy."); r += 1
M["fuel_cost_full"] = model_row(r, "Fuel cost — full leg fuel bill basis", "USD",
                                 f"={M['total_fuel_t'][0]}*{IX['VLSFOPRICE']}",
                                 f"={M['total_fuel_t'][1]}*{IX['VLSFOPRICE']}", "$#,##0"); r += 1
M["fuel_cost_active"] = model_row(r, "Fuel cost — ACTIVE (per Inputs mode)", "USD",
                                   f"=IF({IX['MODE']}=\"Boil-off only\",{M['fuel_cost_boiloff'][0]},{M['fuel_cost_full'][0]})",
                                   f"=IF({IX['MODE']}=\"Boil-off only\",{M['fuel_cost_boiloff'][1]},{M['fuel_cost_full'][1]})",
                                   "$#,##0"); r += 1
M["total_cost"] = model_row(r, "Total cost, active mode", "USD",
                             f"={M['cargo_cost'][0]}+{M['fuel_cost_active'][0]}",
                             f"={M['cargo_cost'][1]}+{M['fuel_cost_active'][1]}", "$#,##0"); r += 1
M["cost_per_kg"] = model_row(r, "Cost per kg H₂ delivered, active mode", "USD/kg",
                              f"={M['total_cost'][0]}/{M['delivered_h2e_voy'][0]}",
                              f"={M['total_cost'][1]}/{M['delivered_h2e_voy'][1]}",
                              "$#,##0.000"); r += 1

r += 1
r = section(ws, r, "BREAKEVENS  (closed-form; all relationships here invert algebraically)", 5)
cell(ws, r, 1, "Metric", HEADER_F, SEC_FILL); cell(ws, r, 2, "Value", HEADER_F, SEC_FILL)
cell(ws, r, 3, "Unit", HEADER_F, SEC_FILL)
cell(ws, r, 5, "Read", HEADER_F, SEC_FILL); r += 1

BE = {}
target_retained = (f"({M['annual_h2e'][1]})/({M['cargo'][0]}*{M['trips'][0]})")
BE["bor_throughput"] = calc_row(
    ws, r, "LH₂ boil-off rate at which annual throughput matches NH₃",
    f"=1-({target_retained})^(1/{M['one_way'][0]})", "%/day", "0.000%",
    note="Above this BOR, NH3 delivers more annual H2-eq per vessel than LH2; below it, LH2 "
         "does. Solved in closed form: bog_frac=1-(1-bor)^days is monotonic and invertible."); r += 1

bog_frac_at_cover = f"({M['demand_mj'][0]}/({M['cargo'][0]}*{IX['H2_LHV']}*{IX['ENGRATIO']}))"
BE["bor_cover"] = calc_row(
    ws, r, "LH₂ boil-off rate at which boil-off exactly meets fuel demand",
    f"=1-(1-{bog_frac_at_cover})^(1/{M['one_way'][0]})", "%/day", "0.000%",
    note="Below this BOR, the ship still buys top-up VLSFO. Above it, the surplus boil-off "
         "cannot be used for propulsion and is disposed of."); r += 1

trips_target = f"({M['annual_h2e'][0]}*{IX['RATIO']}/{IX['NH3_CAP']}/{IX['NH3_RHO']}/{IX['NH3_FILLFRAC']})"
rtd_target = f"(365*{IX['AVAIL']}/{trips_target})"
BE["speed_throughput"] = calc_row(
    ws, r, "NH₃ speed at which annual throughput matches LH₂",
    f"={IX['DIST']}/(12*({rtd_target}-2*{IX['NH3_PORT']}))", "km/h", "#,##0.00",
    note="Holds NH3 capacity/BOR at their Inputs values. NH3 throughput does not depend on its "
         "own BOR (re-liquefaction loses no cargo), only on trip frequency."); r += 1
BE["speed_throughput_kn"] = calc_row(ws, r, "  → in knots",
                                      f"={BE['speed_throughput']}/1.852", "knot", "#,##0.00"); r += 1

BE["cap_throughput"] = calc_row(
    ws, r, "NH₃ capacity at which annual throughput matches LH₂",
    f"={M['annual_h2e'][0]}*{IX['RATIO']}/{IX['NH3_RHO']}/{IX['NH3_FILLFRAC']}/{M['trips'][1]}",
    "m³", "#,##0",
    note="Holds NH3 speed/port time/BOR at their Inputs values."); r += 1

BE["h2_price"] = calc_row(
    ws, r, "Hydrogen value at which boil-off cost per kg is equal (active mode)",
    f"=IF({M['cargo_lost'][0]}=0,\"n/a\",({M['cost_per_kg'][1]}*{M['delivered_h2e_voy'][0]}-{M['fuel_cost_active'][0]})/{M['cargo_lost'][0]})",
    "USD/kg", "$#,##0.0000",
    note="Below this value, LH2 is the cheaper carrier on the active cost basis; above it, "
         "ammonia is. Exact algebraic inversion — LH2 cost is linear in the H2 price."); r += 1

ws.freeze_panes = "A4"
print("Voyage Model sheet OK, last row", r)

MX = {k: (sheet_ref("Voyage Model", v[0]), sheet_ref("Voyage Model", v[1]))
      for k, v in M.items() if isinstance(v, tuple)}
BEX = {k: sheet_ref("Voyage Model", v) for k, v in BE.items()}

# ============================================================================
# SHEET 3: SENS - DISTANCE  (throughput vs one-way distance)
# ============================================================================
ws = wb.create_sheet("Sens - Distance")
set_widths(ws, [14, 15, 15, 15, 15, 40])
title_bar(ws, "Sensitivity — Distance",
          "Annual H₂-equivalent delivered per vessel against one-way distance, at the current "
          "LH2/NH3 vessel specs. Distance alone does not flip the winner in the realistic range.",
          ncols=6)

r = 4
hdrs = ["Distance (km)", "LH₂ (ktpa/vessel)", "NH₃ (ktpa/vessel)",
        "LH₂ fleet size", "NH₃ fleet size"]
for i, h in enumerate(hdrs, start=1):
    cell(ws, r, i, h, HEADER_F, SEC_FILL)
cell(ws, r, 6, "", HEADER_F, SEC_FILL)
first_data_row = r + 1
distances = list(range(1000, 40001, 1000))
r += 1
for d in distances:
    cell(ws, r, 1, d, FORMULA_F, None, "#,##0")
    ow_l = f"A{r}/{IX['LH2_SPEED']}/24"
    ow_n = f"A{r}/{IX['NH3_SPEED']}/24"
    # helper columns pushed off-screen (F onward) to keep the visible table clean
    cell(ws, r, 6, f"=2*({ow_l})+2*{IX['LH2_PORT']}", FORMULA_F, None, "0.0000")   # RTD LH2
    cell(ws, r, 7, f"=2*({ow_n})+2*{IX['NH3_PORT']}", FORMULA_F, None, "0.0000")   # RTD NH3
    cell(ws, r, 8, f"=1-(1-{IX['LH2_BOR']})^({ow_l})", FORMULA_F, None, "0.000000")  # bog_frac LH2
    bog_l = f"H{r}"
    lh2_annual_h2e = f"{MX['cargo'][0]}*(1-{bog_l})*(365/F{r}*{IX['AVAIL']})"
    nh3_annual_h2e = f"{MX['cargo'][1]}*(365/G{r}*{IX['AVAIL']})/{IX['RATIO']}"
    cell(ws, r, 2, f"=({lh2_annual_h2e})/1000000", FORMULA_F, LH2_FILL, "#,##0.00")
    cell(ws, r, 3, f"=({nh3_annual_h2e})/1000000", FORMULA_F, NH3_FILL, "#,##0.00")
    cell(ws, r, 4, f"=CEILING({IX['DEMAND']}*1000000/({lh2_annual_h2e}),1)", FORMULA_F, LH2_FILL, "0")
    cell(ws, r, 5, f"=CEILING({IX['DEMAND']}*1000000*{IX['RATIO']}/({nh3_annual_h2e}),1)", FORMULA_F, NH3_FILL, "0")
    for col in (1, 2, 3, 4, 5):
        ws.cell(row=r, column=col).border = BORDER
    r += 1
last_data_row = r - 1
for col in (6, 7, 8):
    ws.column_dimensions[get_column_letter(col)].hidden = True

r += 1
cell(ws, r, 1, "Suez reference: 10,260 km. Cape reference (primary): 21,200 km.", NOTE_F)
r += 2

chart = LineChart()
chart.title = "Annual H₂-equivalent delivered per vessel vs distance"
chart.style = 2
chart.y_axis.title = "ktpa H₂-eq per vessel"
chart.x_axis.title = "One-way distance (km)"
chart.height, chart.width = 10, 22
cats = Reference(ws, min_col=1, min_row=first_data_row, max_row=last_data_row)
s1 = Reference(ws, min_col=2, min_row=4, max_row=last_data_row)
s2 = Reference(ws, min_col=3, min_row=4, max_row=last_data_row)
chart.add_data(s1, titles_from_data=True)
chart.add_data(s2, titles_from_data=True)
chart.set_categories(cats)
chart.series[0].graphicalProperties.line.solidFill = "0C7C9E"
chart.series[0].graphicalProperties.line.width = 22000
chart.series[0].marker = Marker(symbol="none")
chart.series[0].smooth = False
chart.series[1].graphicalProperties.line.solidFill = "A9660B"
chart.series[1].graphicalProperties.line.width = 22000
chart.series[1].marker = Marker(symbol="none")
chart.series[1].smooth = False
ws.add_chart(chart, f"A{r}")
print("Sens - Distance sheet OK")

# ============================================================================
# SHEET 4: SENS - BOILOFF  (does boil-off cover the fuel bill?)
# ============================================================================
ws = wb.create_sheet("Sens - Boiloff")
set_widths(ws, [12, 15, 16, 16, 16, 40])
title_bar(ws, "Sensitivity — LH₂ Boil-off Rate",
          "At the current distance and LH2 vessel: does cargo boil-off cover the propulsion "
          "duty, and where does the boiled-off hydrogen actually go?", ncols=6)

r = 4
hdrs = ["LH₂ BOR (%/day)", "Covers demand (%)", "Useful (t, active basis)",
        "Surplus (t, active basis)", "VLSFO bought (t, active basis)"]
for i, h in enumerate(hdrs, start=1):
    cell(ws, r, i, h, HEADER_F, SEC_FILL)
first_bo_row = r + 1
bors = [round(i * 0.05, 4) for i in range(0, 81)]   # 0.00% .. 4.00% step 0.05%
r += 1
for b in bors:
    cell(ws, r, 1, b / 100.0, FORMULA_F, None, "0.00%")
    cell(ws, r, 7, f"=1-(1-A{r})^{MX['one_way'][0]}", FORMULA_F, None, "0.000000")          # bog_frac
    cell(ws, r, 8, f"={MX['cargo'][0]}*G{r}", FORMULA_F, None, "#,##0")                    # bog_kg
    cell(ws, r, 9, f"=H{r}*{IX['H2_LHV']}*{IX['ENGRATIO']}", FORMULA_F, None, "#,##0")     # bog_energy
    cell(ws, r, 10, f"=MIN(I{r},{MX['demand_mj'][0]})", FORMULA_F, None, "#,##0")          # useful_mj
    cell(ws, r, 11, f"=MAX(0,I{r}-{MX['demand_mj'][0]})", FORMULA_F, None, "#,##0")        # surplus_mj
    cell(ws, r, 12, f"=IF({MX['demand_mj'][0]}=0,0,I{r}/{MX['demand_mj'][0]})", FORMULA_F, None, "0%")  # coverage
    cell(ws, r, 13, f"=J{r}/({IX['H2_LHV']}*{IX['ENGRATIO']})", FORMULA_F, None, "#,##0")   # useful_kg
    cell(ws, r, 14, f"=K{r}/({IX['H2_LHV']}*{IX['ENGRATIO']})", FORMULA_F, None, "#,##0")   # surplus_kg
    cell(ws, r, 15, f"=MAX(0,{MX['demand_mj'][0]}-I{r})/{IX['VLSFO_LHV']}/1000", FORMULA_F, None, "#,##0.0")  # topup_t
    # active-basis (per leg vs per day) conversions
    per = f"IF({IX['BASIS']}=\"Per day\",{MX['one_way'][0]},1)"
    cell(ws, r, 2, f"=L{r}", FORMULA_F, None, "0%")
    cell(ws, r, 3, f"=M{r}/1000/({per})", FORMULA_F, None, "#,##0.0")
    cell(ws, r, 4, f"=N{r}/1000/({per})", FORMULA_F, None, "#,##0.0")
    cell(ws, r, 5, f"=O{r}/({per})", FORMULA_F, None, "#,##0.0")
    for col in (1, 2, 3, 4, 5):
        ws.cell(row=r, column=col).border = BORDER
    r += 1
last_bo_row = r - 1
for col in range(6, 16):
    ws.column_dimensions[get_column_letter(col)].hidden = True

r += 1
cell(ws, r, 1, "Column B: 100% = boil-off exactly meets propulsion demand.", NOTE_F)
r += 1
cell(ws, r, 1, "RSER-2026 literature reference (unpromoted): ~3.44%/day for a comparable vessel class.", NOTE_F)
r += 2

chart_a = LineChart()
chart_a.title = "Boil-off energy as a share of propulsion demand"
chart_a.style = 2
chart_a.y_axis.title = "% of propulsion demand"
chart_a.x_axis.title = "LH₂ voyage boil-off rate (%/day)"
chart_a.height, chart_a.width = 9, 20
cats = Reference(ws, min_col=1, min_row=first_bo_row, max_row=last_bo_row)
s1 = Reference(ws, min_col=2, min_row=4, max_row=last_bo_row)
chart_a.add_data(s1, titles_from_data=True)
chart_a.set_categories(cats)
chart_a.series[0].graphicalProperties.line.solidFill = "0C7C9E"
chart_a.series[0].graphicalProperties.line.width = 22000
chart_a.series[0].marker = Marker(symbol="none")
chart_a.series[0].smooth = False
ws.add_chart(chart_a, f"A{r}")

chart_b = BarChart()
chart_b.type = "col"
chart_b.grouping = "stacked"
chart_b.overlap = 100
chart_b.title = "Fate of the boil-off (active basis)"
chart_b.style = 2
chart_b.y_axis.title = "tonnes H₂ (or t/day)"
chart_b.x_axis.title = "LH₂ voyage boil-off rate (%/day)"
chart_b.height, chart_b.width = 9, 20
s2 = Reference(ws, min_col=3, min_row=4, max_row=last_bo_row)
s3 = Reference(ws, min_col=4, min_row=4, max_row=last_bo_row)
chart_b.add_data(s2, titles_from_data=True)
chart_b.add_data(s3, titles_from_data=True)
chart_b.set_categories(cats)
chart_b.series[0].graphicalProperties.solidFill = "0C7C9E"
chart_b.series[1].graphicalProperties.solidFill = "B3453A"
line_chart = LineChart()
s4 = Reference(ws, min_col=5, min_row=4, max_row=last_bo_row)
line_chart.add_data(s4, titles_from_data=True)
line_chart.series[0].graphicalProperties.line.solidFill = "6B7280"
line_chart.series[0].graphicalProperties.line.width = 16000
line_chart.series[0].graphicalProperties.line.dashStyle = "dash"
line_chart.series[0].marker = Marker(symbol="none")
line_chart.series[0].smooth = False
chart_b += line_chart
ws.add_chart(chart_b, f"A{r + 20}")
print("Sens - Boiloff sheet OK")

# ============================================================================
# SHEET 5: SENS - H2 PRICE  (boil-off cost vs hydrogen value)
# ============================================================================
ws = wb.create_sheet("Sens - H2Price")
set_widths(ws, [14, 15, 15, 40])
title_bar(ws, "Sensitivity — Hydrogen Value",
          "Cost of managing boil-off (active mode) per kg H₂ delivered, against the value "
          "placed on delivered hydrogen. At the current distance, LH2 vessel and NH3 vessel.",
          ncols=4)

r = 4
for i, h in enumerate(["H₂ value (USD/kg)", "LH₂ cost (USD/kg)", "NH₃ cost (USD/kg)"], start=1):
    cell(ws, r, i, h, HEADER_F, SEC_FILL)
first_p_row = r + 1
prices = [round(i * 0.25, 2) for i in range(0, 49)]   # 0 .. 12 step 0.25
r += 1
for p in prices:
    cell(ws, r, 1, p, FORMULA_F, None, "$#,##0.00")
    cell(ws, r, 2, f"=({MX['cargo_lost'][0]}*A{r}+{MX['fuel_cost_active'][0]})/{MX['delivered_h2e_voy'][0]}",
         FORMULA_F, LH2_FILL, "$#,##0.000")
    cell(ws, r, 3, f"={MX['cost_per_kg'][1]}", FORMULA_F, NH3_FILL, "$#,##0.000")
    for col in (1, 2, 3):
        ws.cell(row=r, column=col).border = BORDER
    r += 1
last_p_row = r - 1
r += 1
cell(ws, r, 1, f"Breakeven H₂ value (active mode): see Voyage Model!{BE['h2_price']}", NOTE_F)
r += 2

chart = LineChart()
chart.title = "Boil-off management cost per kg H₂ delivered"
chart.style = 2
chart.y_axis.title = "USD per kg H₂"
chart.x_axis.title = "Value placed on delivered hydrogen (USD/kg)"
chart.height, chart.width = 10, 22
cats = Reference(ws, min_col=1, min_row=first_p_row, max_row=last_p_row)
s1 = Reference(ws, min_col=2, min_row=4, max_row=last_p_row)
s2 = Reference(ws, min_col=3, min_row=4, max_row=last_p_row)
chart.add_data(s1, titles_from_data=True)
chart.add_data(s2, titles_from_data=True)
chart.set_categories(cats)
chart.series[0].graphicalProperties.line.solidFill = "0C7C9E"
chart.series[0].graphicalProperties.line.width = 22000
chart.series[0].marker = Marker(symbol="none")
chart.series[0].smooth = False
chart.series[1].graphicalProperties.line.solidFill = "A9660B"
chart.series[1].graphicalProperties.line.width = 22000
chart.series[1].marker = Marker(symbol="none")
chart.series[1].smooth = False
ws.add_chart(chart, f"A{r}")
print("Sens - H2Price sheet OK")

# ============================================================================
# SHEET 6: DECISION MAP  (H2 price x LH2 hull size)
# ============================================================================
ws = wb.create_sheet("Decision Map")
set_widths(ws, [14, 16, 16, 3])
title_bar(ws, "Decision Map — Hydrogen Value × LH₂ Vessel Size",
          "At what hydrogen price and LH2 hull size does LH2 beat ammonia on boil-off cost? "
          "Grid = LH2 cost minus NH3 cost, USD/kg (negative/green = LH2 cheaper). Duty scales "
          "with hull size per the Inputs exponent, anchored on the LH2 vessel's own selected "
          "capacity/duty pair (Inputs).", ncols=10)

r = 4
cell(ws, r, 1, "LH₂ capacity (m³)", HEADER_F, SEC_FILL)
cell(ws, r, 2, "Duty at this size (t/day)", HEADER_F, SEC_FILL)
cell(ws, r, 3, "Parity H₂ price (USD/kg)", HEADER_F, SEC_FILL)
r += 1
helper_first = r
caps = list(range(20000, 200001, 10000))
price_cols_start = 5   # column E onward holds the price grid
prices_grid = [round(i * 0.25, 2) for i in range(0, 17)]   # 0 .. 4.00 step 0.25
price_cols_end = price_cols_start + len(prices_grid) - 1
# hidden helper columns start two clear columns after the visible price grid,
# so they can never collide with it regardless of how many price points there are
H_CARGO, H_BOG, H_DEMAND, H_BOGE, H_DISP, H_DELIV = range(
    price_cols_end + 3, price_cols_end + 9)
cell(ws, r - 1, 4, "", HEADER_F, SEC_FILL)
for j, p in enumerate(prices_grid):
    c = price_cols_start + j
    cell(ws, r - 1, c, p, HEADER_F, SEC_FILL, "$#,##0.00")
    ws.column_dimensions[get_column_letter(c)].width = 9

nh3_cost = MX["cost_per_kg"][1]   # constant reference, boil-off-only or full per active mode
CL = get_column_letter
header_row = helper_first - 1   # the one fixed row holding the price-grid header, never r-1
for cap in caps:
    cell(ws, r, 1, cap, FORMULA_F, None, "#,##0")
    duty = f"={IX['LH2_DUTY']}*(A{r}/{IX['LH2_CAP']})^{IX['EXPO']}"
    cell(ws, r, 2, duty, FORMULA_F, None, "#,##0.0")
    # helper columns (hidden): cargo, bog_kg (fixed bog_frac from current LH2 BOR/one-way),
    # demand_mj(cap), bog_energy(cap fixed via bog_frac), displaced/delivered
    cell(ws, r, H_CARGO, f"=A{r}*{IX['LH2_RHO']}*{IX['LH2_FILLFRAC']}", FORMULA_F, None, "#,##0")
    cell(ws, r, H_BOG, f"={CL(H_CARGO)}{r}*{MX['bog_frac'][0]}", FORMULA_F, None, "#,##0")
    cell(ws, r, H_DEMAND, f"=B{r}*1000*{MX['one_way'][0]}*{IX['VLSFO_LHV']}", FORMULA_F, None, "#,##0")
    cell(ws, r, H_BOGE, f"={CL(H_BOG)}{r}*{IX['H2_LHV']}*{IX['ENGRATIO']}", FORMULA_F, None, "#,##0")
    cell(ws, r, H_DISP, f"=MIN({CL(H_BOGE)}{r},{CL(H_DEMAND)}{r})/{IX['VLSFO_LHV']}/1000",
         FORMULA_F, None, "#,##0.00")
    cell(ws, r, H_DELIV, f"={CL(H_CARGO)}{r}*(1-{MX['bog_frac'][0]})", FORMULA_F, None, "#,##0")
    bog_ref, disp_ref, deliv_ref = f"{CL(H_BOG)}{r}", f"{CL(H_DISP)}{r}", f"{CL(H_DELIV)}{r}"
    # Parity price: (NH3cost*delivered(cap) + displaced_t(cap)*VLSFOprice) / cargo_lost(cap)
    cell(ws, r, 3,
         f"=IF({bog_ref}=0,\"n/a\",({nh3_cost}*{deliv_ref}+{disp_ref}*{IX['VLSFOPRICE']})/{bog_ref})",
         FORMULA_F, FLAG_FILL, "$#,##0.0000")
    for j, p in enumerate(prices_grid):
        c = price_cols_start + j
        col_letter = CL(c)
        # LH2 cost per kg (boil-off-only) at (cap, price): (cargo_lost*price - displaced_t*VLSFOprice)/delivered
        lh2_cost = f"({bog_ref}*{col_letter}${header_row}-{disp_ref}*{IX['VLSFOPRICE']})/{deliv_ref}"
        cell(ws, r, c, f"={lh2_cost}-({nh3_cost})", FORMULA_F, None, "$#,##0.00")
    ws.cell(row=r, column=1).border = BORDER
    ws.cell(row=r, column=2).border = BORDER
    ws.cell(row=r, column=3).border = BORDER
    r += 1
last_map_row = r - 1
for col in range(H_CARGO, H_DELIV + 1):
    ws.column_dimensions[CL(col)].hidden = True

grid_ref_first_col = get_column_letter(price_cols_start)
grid_ref_last_col = get_column_letter(price_cols_end)
grid_range = f"{grid_ref_first_col}{helper_first}:{grid_ref_last_col}{last_map_row}"
rule = ColorScaleRule(
    start_type="min", start_color="1E8449",
    mid_type="num", mid_value=0, mid_color="FFFFFF",
    end_type="max", end_color="B7472A")
ws.conditional_formatting.add(grid_range, rule)

r += 1
cell(ws, r, 1, "Green = LH₂ cheaper. Red = NH₃ cheaper. White ≈ parity. "
     "Column C is the exact parity price per row (closed-form).", NOTE_F)
r += 1
cell(ws, r, 1, "The 40,000 m³ and 60,000... rows above land on exact 10,000 m³ steps; "
     "160,000 m³ is included as a grid row too.", NOTE_F)
r += 1
cell(ws, r, 1, f"NH₃ reference cost (active mode, current NH3 vessel/price): {nh3_cost}", NOTE_F)
print("Decision Map sheet OK")

# ============================================================================
# SHEET 7: NH3 SCENARIOS  (24k / 40k / 60k / 90k)
# ============================================================================
ws = wb.create_sheet("NH3 Scenarios")
set_widths(ws, [16, 16, 16, 16, 40])
title_bar(ws, "NH₃ Vessel Scenarios",
          "How many ammonia ships of each size equal one LH2 carrier at the current LH2 "
          "capacity/route? Speed, port time and BOR held at their Inputs values — only "
          "capacity varies here.", ncols=5)

r = 4
hdrs = ["NH₃ capacity (m³)", "Annual H₂-eq (ktpa/vessel)", "vs 1 LH₂ ship",
        "NH₃ ships per LH₂ ship"]
for i, h in enumerate(hdrs, start=1):
    cell(ws, r, i, h, HEADER_F, SEC_FILL)
first_n_row = r + 1
r += 1
nh3_scenarios = [24000, 40000, 60000, 90000]
for cap in nh3_scenarios:
    cell(ws, r, 1, cap, FORMULA_F, None, "#,##0")
    rtd = f"(2*({IX['DIST']}/{IX['NH3_SPEED']}/24)+2*{IX['NH3_PORT']})"
    trips = f"(365/{rtd}*{IX['AVAIL']})"
    cargo = f"(A{r}*{IX['NH3_RHO']}*{IX['NH3_FILLFRAC']})"
    annual_h2e = f"({cargo}*{trips}/{IX['RATIO']})"
    cell(ws, r, 2, f"={annual_h2e}/1000000", FORMULA_F, NH3_FILL, "#,##0.00")
    cell(ws, r, 3, f"=(B{r}*1000000)/{MX['annual_h2e'][0]}", FORMULA_F, None, "0.0%")
    cell(ws, r, 4, f"={MX['annual_h2e'][0]}/(B{r}*1000000)", FORMULA_F, None, "0.00")
    for col in (1, 2, 3, 4):
        ws.cell(row=r, column=col).border = BORDER
    r += 1
last_n_row = r - 1
r += 1
cell(ws, r, 1, "\"1 LH₂ ship\" uses the LH2 vessel currently selected on the Inputs sheet.", NOTE_F)
r += 2

chart = BarChart()
chart.type = "col"
chart.title = "Annual H₂-equivalent delivered per NH₃ vessel, by capacity"
chart.style = 10
chart.y_axis.title = "ktpa H₂-eq per vessel"
chart.x_axis.title = "NH₃ capacity (m³)"
chart.height, chart.width = 10, 18
cats = Reference(ws, min_col=1, min_row=first_n_row, max_row=last_n_row)
data = Reference(ws, min_col=2, min_row=4, max_row=last_n_row)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.series[0].graphicalProperties.solidFill = "A9660B"

lh2_line = LineChart()
cell(ws, 3, 6, None)  # keep column clear
lh2_ref_row_start, lh2_ref_row_end = first_n_row, last_n_row
for rr in range(lh2_ref_row_start, lh2_ref_row_end + 1):
    cell(ws, rr, 6, f"={MX['annual_ktpa'][0]}", FORMULA_F, None, "#,##0.00")
ws.column_dimensions["F"].hidden = True
lh2_data = Reference(ws, min_col=6, min_row=3, max_row=last_n_row)
lh2_line.add_data(lh2_data, titles_from_data=True)
lh2_line.series[0].graphicalProperties.line.solidFill = "0C7C9E"
lh2_line.series[0].graphicalProperties.line.width = 22000
lh2_line.series[0].graphicalProperties.line.dashStyle = "dash"
lh2_line.series[0].marker = Marker(symbol="none")
lh2_line.series[0].smooth = False
chart += lh2_line
ws.add_chart(chart, f"A{r}")
print("NH3 Scenarios sheet OK")

# ============================================================================
# SHEET 8: DASHBOARD
# ============================================================================
ws = wb.create_sheet("Dashboard")
set_widths(ws, [26, 26, 26, 26])
title_bar(ws, "Dashboard — LH₂ vs Ammonia Shipping",
          "Headline read at the current Inputs. Kakinada, India → Hamburg, Germany.", ncols=4)


def kpi(ws, row, col, label, formula, fmt="#,##0.00", note=None):
    if isinstance(formula, str) and not formula.startswith("="):
        formula = "=" + formula   # bare cell reference (e.g. from MX/BEX) -> live formula
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col)
    ws.merge_cells(start_row=row + 2, start_column=col, end_row=row + 2, end_column=col)
    lab = cell(ws, row, col, label, KPI_LABEL_F, KPI_FILL, align=Alignment(horizontal="left"))
    val = cell(ws, row + 1, col, formula, KPI_VALUE_F, KPI_FILL, fmt, align=Alignment(horizontal="left"))
    nt = cell(ws, row + 2, col, note or "", NOTE_F, KPI_FILL, align=Alignment(horizontal="left", wrap_text=True))
    for rr in (row, row + 1, row + 2):
        for cc in range(col, col + 1):
            ws.cell(row=rr, column=cc).border = BORDER
    return val


r = 4
kpi(ws, r, 1, "WINNER ON THROUGHPUT",
    f'=IF({MX["annual_ktpa"][0]}>{MX["annual_ktpa"][1]},"LH₂","NH₃")', "@",
    note="Annual H2-equivalent delivered per vessel, ktpa (see the two tiles at right).")
kpi(ws, r, 2, "LH₂ ANNUAL DELIVERY", MX["annual_ktpa"][0], "#,##0.0 \"ktpa\"",
    note="See Voyage Model row 16 for the fleet size this implies.")
kpi(ws, r, 3, "NH₃ ANNUAL DELIVERY", MX["annual_ktpa"][1], "#,##0.0 \"ktpa\"",
    note="See Voyage Model row 16 for the fleet size this implies.")
kpi(ws, r, 4, "NH₃ SHIPS PER LH₂ SHIP", f'={MX["annual_ktpa"][0]}/{MX["annual_ktpa"][1]}',
    "0.00\"×\"", note="At the currently selected capacities for both carriers.")
r += 4

kpi(ws, r, 1, "BOIL-OFF COVERS PROPULSION DEMAND", MX["coverage"][0], "0%",
    note='>100% = surplus is wasted; <100% = ship still buys top-up VLSFO.')
kpi(ws, r, 2, "LH₂ COST PER KG H₂ (ACTIVE MODE)", MX["cost_per_kg"][0], "$#,##0.000",
    note="Active mode set on the Inputs sheet.")
kpi(ws, r, 3, "NH₃ COST PER KG H₂ (ACTIVE MODE)", MX["cost_per_kg"][1], "$#,##0.000",
    note="Active mode set on the Inputs sheet.")
kpi(ws, r, 4, "CHEAPER CARRIER (ACTIVE MODE)",
    f'=IF({MX["cost_per_kg"][0]}<{MX["cost_per_kg"][1]},"LH₂","NH₃")', "@",
    note="Boil-off cost per kg H2 delivered, active mode.")
r += 4

kpi(ws, r, 1, "BREAKEVEN LH₂ BOIL-OFF (THROUGHPUT)", BEX["bor_throughput"], "0.000%",
    note="Above this LH2 BOR, NH3 delivers more annual H2-eq per vessel.")
kpi(ws, r, 2, "BREAKEVEN LH₂ BOIL-OFF (FUEL COVER)", BEX["bor_cover"], "0.000%",
    note="Above this LH2 BOR, boil-off exceeds propulsion demand and is wasted.")
kpi(ws, r, 3, "BREAKEVEN H₂ VALUE", BEX["h2_price"], "$#,##0.00",
    note="Above this hydrogen value, ammonia is cheaper on the active cost basis.")
kpi(ws, r, 4, "BREAKEVEN NH₃ CAPACITY", BEX["cap_throughput"], "#,##0 \"m³\"",
    note="NH3 capacity needed to match one LH2 ship's annual throughput.")
r += 5

r = section(ws, r, "OPEN GAPS — nothing here is fabricated; see Inputs sheet Tag column", 4)
gaps = [
    "LH₂ voyage boil-off rate: KHI never disclosed one — the single biggest lever in this workbook.",
    "LH₂ propulsion duty (25 t/day): carried over from the ammonia vessel; a 160,000 m³ hull "
    "at ~16 kn plausibly burns several times this. See the Suggested Duty cells on Inputs.",
    "Every NH₃ vessel figure (speed, capacity, port time, BOR, reliquefaction energy) is "
    "user-stated or estimated, pending the internal Gentari NH3 dataset (decision D4).",
    "Hydrogen value and VLSFO price are set by you — neither is logged in the repository; the "
    "model reports breakeven prices rather than asserting one.",
    "Corridor distance is a first-principles great-circle estimate, not an AIS/route-planner figure.",
]
for g in gaps:
    cell(ws, r, 1, "• " + g, NOTE_F, wrap=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    ws.row_dimensions[r].height = 28
    r += 1

ws.sheet_view.showGridLines = False
print("Dashboard sheet OK")

# ============================================================================
# SHEET 9: SOURCES & ASSUMPTIONS
# ============================================================================
ws = wb.create_sheet("Sources & Tags")
set_widths(ws, [14, 60, 50])
title_bar(ws, "Sources & Assumptions",
          "Every quantitative input in this workbook is cited, or tagged ASSUMPTION/ESTIMATE per "
          "CLAUDE.md §4 — no number here is fabricated.", ncols=3)

r = 4
cell(ws, r, 1, "Tag", HEADER_F, SEC_FILL)
cell(ws, r, 2, "Meaning", HEADER_F, SEC_FILL)
cell(ws, r, 3, "Appears on", HEADER_F, SEC_FILL)
r += 1
tags = [
    ("CITED", "Traceable to a named source (e.g. a Kawasaki Heavy Industries questionnaire reply, "
     "or their cost-basis slide).", "LH2 capacity, speed, port time — KHI questionnaire/"
     "supplemental replies Q23/Q27/Q29/Q33."),
    ("ASSUMPTION", "A value deliberately chosen to proceed, stated explicitly.", "NH3 vessel specs, "
     "fleet availability, fill fractions, engine efficiency ratios, the duty-scaling exponent."),
    ("ESTIMATE", "A rough figure that should be replaced with a sourced one.", "Voyage boil-off rates, "
     "VLSFO LHV, NH3 density, vented-H2 GWP100, reliquefaction energy."),
    ("needs-source", "A figure this repository has not yet formally cited.", "H2/LH2 LHV and density "
     "(pending NIST/CODATA/ISO citation approval)."),
    ("CHOICE", "A structural toggle you set, not a physical quantity.", "Cost basis mode, surplus "
     "disposal, boil-off fate basis."),
]
for t, m_, a in tags:
    tagfill = CITED_FILL if t == "CITED" else (FLAG_FILL if t in ("ASSUMPTION", "ESTIMATE") else None)
    cell(ws, r, 1, t, TAG_F, tagfill)
    cell(ws, r, 2, m_, LABEL_F, wrap=True)
    cell(ws, r, 3, a, NOTE_F, wrap=True)
    ws.row_dimensions[r].height = 30
    r += 1
r += 1

r = section(ws, r, "PRIMARY SOURCES", 3)
sources = [
    "Kawasaki Heavy Industries questionnaire replies (kawasaki-2026-questionnaire) — LH2 vessel "
    "capacity (40,000 / 160,000 m³), service speed (29.6 km/h), port time (1–1.5 days), "
    "BOG-as-fuel disposition, gas-combustion-unit surplus handling.",
    "Kawasaki cost-basis supplemental slide (kawasaki-2026-supplemental) — 160,000 m³ "
    "commercial-scale target vessel, service speed.",
    "docs/comparison/02-shipping-lh2-vs-nh3.md — full write-up of every pass of this study, "
    "including the fuel-balance derivation and the decision-map method.",
    "scripts/run_shipping_comparison.py, src/lh2/shipping.py — the Python reference "
    "implementation this workbook mirrors formula-for-formula.",
    "data/vessels/nh3-carriers.csv, data/routes/kakinada-hamburg.csv — the repository's tagged "
    "data tables for the ammonia vessel and the corridor distance.",
]
for s in sources:
    cell(ws, r, 1, "• " + s, NOTE_F, wrap=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
    ws.row_dimensions[r].height = 30
    r += 1

ws.sheet_view.showGridLines = False
print("Sources & Tags sheet OK")

# ------------------------------------------------------------------ finish --
tab_colors = {
    "Inputs": "1F3864", "Voyage Model": "2E5395", "Sens - Distance": "0C7C9E",
    "Sens - Boiloff": "0C7C9E", "Sens - H2Price": "0C7C9E", "Decision Map": "A9660B",
    "NH3 Scenarios": "A9660B", "Dashboard": "1F3864", "Sources & Tags": "6B7280",
}
for name, color in tab_colors.items():
    wb[name].sheet_properties.tabColor = color

for name in wb.sheetnames:
    if name not in ("Inputs",):
        wb[name].sheet_view.showGridLines = False

wb.move_sheet("Dashboard", offset=-(wb.sheetnames.index("Dashboard")))
wb.active = wb.sheetnames.index("Dashboard")

for name in wb.sheetnames:
    sh = wb[name]
    sh.page_setup.orientation = "landscape"
    sh.page_setup.fitToWidth = 1
    sh.page_setup.fitToHeight = 0
    sh.sheet_properties.pageSetUpPr.fitToPage = True
    sh.print_options.horizontalCentered = False

wb.save(OUT)
print("Saved (full workbook) ->", OUT)
