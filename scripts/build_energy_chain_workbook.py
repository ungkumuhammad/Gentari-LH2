#!/usr/bin/env python3
"""Build the Excel replica of the artifact "LH2 vs Ammonia Energy Value Chain".

Artifact : https://claude.ai/artifact/158AMxDjHB29ttVH3nsoiM (version of 2026-10-06)
Output   : docs/comparison/lh2-vs-nh3-energy-value-chain.xlsx

System boundary : GH2 at battery limit (electrolysis optional) -> gaseous H2 at
                  import-terminal send-out, one 40,000 m3 cargo, then scaled to
                  the contracted annual volume.
Units           : kg, t, kWh, MWh, GWh/y, MJ, USD (prices are user inputs, no
                  cost year asserted -- same as the artifact).

Sheets (one per artifact tab, inputs live on the sheet they drive):
  Upstream | Midstream (artifact "Shipping") | Downstream | Full Chain |
  Annual Energy (artifact "Case Study") | Energy Cost (artifact "Economic Origin")

Every number the artifact carries is kept with its provenance tag (user /
cited / [ASSUMPTION] / [ESTIMATE]) in the note column beside the input.
Formulas are live; cross-sheet links use workbook-level defined names.

Run:  python scripts/build_energy_chain_workbook.py [--cache cache.json]
The optional cache (cell -> value, produced by a LibreOffice recalculation
pass) is written as the cached result of each formula so viewers that do not
recalculate still show numbers.
"""

from __future__ import annotations

import argparse
import json
import os

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

OUT = "docs/comparison/lh2-vs-nh3-energy-value-chain.xlsx"
FONT = "Verdana"

# ------------------------------------------------------------ brand (docs/brand) --
PURPLE, CYAN = "#60269E", "#00C8E8"           # core
LEAD = "#7030A0"                              # lead-in title purple
DARK, BODY, GRID = "#1F2933", "#3A3935", "#E8E8E4"
ACCENT, ACC_FG = "#F1EAF6", "#441D62"
MUTED, GREEN, AMBER, BLUE = "#65758B", "#75BA75", "#F59F0A", "#2977D6"
LINKBG = "#E3F8FC"
# chart categorical palette (artifact c1..c6 -> brand)
C1, C2, C3, C4, C5, C6 = PURPLE, CYAN, BLUE, AMBER, GREEN, MUTED
S1, S2 = PURPLE, CYAN                         # LH2 / NH3 series
WHITE_LBL = {C1: "#FFFFFF", C3: "#FFFFFF", C6: "#FFFFFF"}

NF = {"int": "#,##0", "d1": "#,##0.0", "d2": "#,##0.00", "d3": "#,##0.000",
      "d4": "#,##0.0000", "gen": "General", "txt": "@", "pct": "0.0%"}

YES_NO = ["No", "Yes"]
B_UP = ["Per ship cargo (MWh)", "Per kg H2 (kWh)"]
B_DN = ["Per ship cargo (MWh)", "Per kg H2 (kWh)"]
B_CH = ["Per kg H2 delivered (kWh)", "Per cargo (MWh)"]
B_SH = ["Per ship-day", "Per tonne H2 carried"]
F_DF, F_VL = "Dual fuel NH3/VLSFO", "VLSFO only"
SRC = ["Bunkered", "Cargo"]
B_EC = ["H2 produced (Economic Origin)", "H2 delivered (Economics)"]

COL0 = 1          # B
CH_COL = 8        # charts anchor at column I
NCOLS = 15        # banner width B..P


class Book:
    def __init__(self, path, cache):
        self.wb = xlsxwriter.Workbook(path)
        self.cache = cache or {}
        self._f = {}
        self.names = {}

    def fmt(self, **kw):
        base = {"font_name": FONT, "font_size": 9, "font_color": BODY, "valign": "vcenter"}
        base.update(kw)
        key = json.dumps(base, sort_keys=True)
        if key not in self._f:
            self._f[key] = self.wb.add_format(base)
        return self._f[key]


class Sh:
    def __init__(self, bk: Book, name: str, tab: str):
        self.bk, self.name = bk, name
        self.ws = bk.wb.add_worksheet(name)
        self.ws.set_tab_color(tab)
        self.ws.hide_gridlines(2)
        self.ws.set_default_row(17)
        self.ws.set_zoom(90)
        self.ws.set_column(0, 0, 2)
        self.ws.set_column(1, 1, 42)
        self.ws.set_column(2, 30, 14)
        self.ws.set_landscape()
        self.ws.set_paper(8)
        self.ws.fit_to_pages(1, 0)
        self.r = 5
        self.chart_bottom = 5

    # ------------------------------------------------------------- addressing --
    def a(self, r, c):
        return f"'{self.name}'!{xl_rowcol_to_cell(r, c, True, True)}"

    def nm(self, name, r, c):
        self.bk.names[name] = (r, c)
        self.bk.wb.define_name(name, f"={self.a(r, c)}")

    def txt(self, r, c, v, fmt):
        """Unit / note cell: '=Name...' is a live formula, '= text' is literal text."""
        if isinstance(v, str) and v.startswith("=") and not v.startswith("= "):
            self.put(r, c, v, fmt)
        else:
            self.ws.write_string(r, c, v, fmt)

    # ------------------------------------------------------------------ writes --
    def put(self, r, c, v, fmt=None):
        if isinstance(v, str) and v.startswith("="):
            self.ws.write_formula(r, c, v, fmt, self.bk.cache.get(f"{self.name}|{r}|{c}", "" if self.bk.cache else 0))
        else:
            self.ws.write(r, c, v, fmt)

    # ----------------------------------------------------------------- banner --
    def banner(self, title, eyebrow, lede, boundary, basis, energy):
        f, ws = self.bk.fmt, self.ws
        ws.write(0, 1, "Confidential - For PETRONAS Staff Only", f(font_color=GREEN, font_size=8))
        ws.set_row(1, 30)
        ws.merge_range(1, 1, 1, NCOLS, title, f(bg_color=PURPLE, font_color="#FFFFFF", bold=True, font_size=16))
        ws.set_row(2, 16)
        ws.merge_range(2, 1, 2, NCOLS, eyebrow.upper(), f(bg_color=PURPLE, font_color=CYAN, bold=True, font_size=8))
        ws.set_row(3, 34)
        ws.merge_range(3, 1, 3, NCOLS, lede, f(bg_color=PURPLE, font_color="#FFFFFF", text_wrap=True, font_size=9, valign="top"))
        ws.merge_range(4, 1, 4, NCOLS, f"Boundary: {boundary}   |   Basis: {basis}   |   Energy: {energy}",
                       f(bg_color=ACCENT, font_color=ACC_FG, font_size=8))
        ws.merge_range(5, 1, 5, NCOLS, "Cell key:  purple-tint = input (edit)   ·   cyan-tint = link from another sheet   ·   white = calculation",
                       f(font_color=MUTED, italic=True, font_size=8))
        self.r = 7

    def sec(self, text, width=6):
        f = self.bk.fmt
        self.ws.write(self.r, 1, text, f(bold=True, font_size=10, font_color=LEAD, bottom=2, bottom_color=CYAN))
        for c in range(2, 1 + width):
            self.ws.write_blank(self.r, c, None, f(bottom=2, bottom_color=CYAN))
        self.r += 1

    def sub(self, text, color=PURPLE):
        self.ws.write(self.r, 1, text, self.bk.fmt(bold=True, font_color=color, font_size=9))
        self.r += 1

    def note(self, text, r=None, c=1, wrap_to=None):
        r = self.r if r is None else r
        self.ws.write_string(r, c, text, self.bk.fmt(italic=True, font_color=MUTED, font_size=8))
        if r == self.r:
            self.r += 1

    # ------------------------------------------------------------ labelled row --
    def row(self, name, label, val, unit="", note="", nf="d2", kind="calc", dv=None, bold=False):
        f, ws, r = self.bk.fmt, self.ws, self.r
        ws.write(r, 1, label, f(bold=bold))
        if kind == "input":
            cf = f(bg_color=ACCENT, font_color=ACC_FG, bold=True, num_format=NF.get(nf, nf), border=1, border_color="#C9B3E0", align="right")
        elif kind == "link":
            cf = f(bg_color=LINKBG, font_color=DARK, num_format=NF.get(nf, nf), border=1, border_color="#A9E6F2", align="right")
        elif kind == "key":
            cf = f(font_color=PURPLE, bold=True, font_size=10, num_format=NF.get(nf, nf), align="right")
        else:
            cf = f(num_format=NF.get(nf, nf), align="right", bold=bold)
        if nf == "txt" and kind in ("input", "link"):
            ws.merge_range(r, 2, r, 3, "", cf)
            self.put(r, 2, val, cf)
            unit = ""
        else:
            self.put(r, 2, val, cf)
        self.txt(r, 3, unit, f(font_color=MUTED))
        if note:
            self.txt(r, 4, note, f(italic=True, font_color=MUTED, font_size=8))
        if dv:
            ws.data_validation(r, 2, r, 2, {"validate": "list", "source": dv,
                                            "error_title": "Pick from the list", "error_message": "Choose one of the listed options."})
        if name:
            self.nm(name, r, 2)
        self.r += 1
        return r

    # ------------------------------------------------------------------ table --
    def table(self, r0, headers, rows, nfs=None, c0=1, total_last=False, hdr_h=30, first_bold=True):
        f, ws = self.bk.fmt, self.ws
        ws.set_row(r0, hdr_h)
        for j, h in enumerate(headers):
            ws.write(r0, c0 + j, h, f(bg_color=DARK, font_color="#FFFFFF", bold=True, text_wrap=True,
                                      align="left" if j == 0 else "right", font_size=8))
        for i, row in enumerate(rows):
            r = r0 + 1 + i
            last = total_last and i == len(rows) - 1
            for j, v in enumerate(row):
                nf = (nfs[j] if nfs else "d2")
                kw = dict(num_format=NF.get(nf, nf), bottom=1, bottom_color=GRID,
                          align="left" if j == 0 else "right")
                if (j == 0 and first_bold) or last:
                    kw["bold"] = True
                if last:
                    kw["bg_color"] = ACCENT
                    kw["font_color"] = ACC_FG
                self.put(r, c0 + j, v, f(**kw))
        return r0 + 1 + len(rows)

    # --------------------------------------------------------------- headline --
    def headline(self, name, formula):
        """A dynamic sentence (artifact h2) in column B; chart titles link to it."""
        r = self.r
        self.put(r, 1, formula, self.bk.fmt(bold=True, font_color=LEAD, font_size=9))
        self.nm(name, r, 1)
        self.r += 1
        return r

    # ----------------------------------------------------------------- charts --
    def place(self, chart, row, w, h, x_off=0):
        self.ws.insert_chart(row, CH_COL, chart, {"x_offset": x_off, "y_offset": 4, "object_position": 2})
        self.chart_bottom = max(self.chart_bottom, row + int(h / 22.7) + 2)


def cfont(sz=8, color=BODY, bold=False):
    return {"name": FONT, "size": sz, "color": color, "bold": bold}


def base_chart(bk, kind, title_ref, w, h, legend_delete=None, subtype=None):
    spec = {"type": kind}
    if subtype:
        spec["subtype"] = subtype
    ch = bk.wb.add_chart(spec)
    ch.set_title({"name": title_ref, "name_font": cfont(10, LEAD, True), "overlay": False})
    ch.set_legend({"position": "bottom", "font": cfont(8, BODY), "delete_series": legend_delete or []})
    ch.set_size({"width": w, "height": h})
    ch.set_chartarea({"border": {"color": GRID}, "fill": {"color": "#FFFFFF"}})
    ch.set_plotarea({"fill": {"none": True}})
    return ch


def rng(sh, r0, c0, r1, c1):
    return [sh.name, r0, c0, r1, c1]


def hbar(sh: Sh, title_ref, xname, cats, segs, tot_vals, tot_lbls, w, h, name_ref=None):
    """Stacked horizontal bars. segs: list of (name, vals_rng, colour, [label cells (r,c)])."""
    ch = base_chart(sh.bk, "bar", title_ref, w, h, legend_delete=[len(segs)], subtype="stacked")
    for nm_, vals, colr, lbls in segs:
        ch.add_series({
            "name": nm_, "categories": cats, "values": vals, "gap": 45,
            "fill": {"color": colr}, "border": {"color": "#FFFFFF", "width": 0.75},
            "data_labels": {"value": True, "position": "center",
                            "custom": [{"value": "=" + sh.a(r, c)} for r, c in lbls],
                            "font": cfont(8, WHITE_LBL.get(colr, DARK), True)},
        })
    ch.add_series({
        "name": " ", "categories": cats, "values": tot_vals, "gap": 45,
        "fill": {"none": True}, "border": {"none": True},
        "data_labels": {"value": True, "position": "inside_base",
                        "custom": [{"value": "=" + sh.a(r, c)} for r, c in tot_lbls],
                        "font": cfont(9, DARK, True)},
    })
    ch.set_y_axis({"num_font": cfont(8, DARK, True), "line": {"color": MUTED}, "major_gridlines": {"visible": False},
                   "major_tick_mark": "none"})
    ch.set_x_axis({"name": xname, "name_font": cfont(8, BODY), "num_font": cfont(8, MUTED), "min": 0,
                   "major_gridlines": {"visible": True, "line": {"color": GRID}}, "line": {"color": MUTED}})
    return ch


def lbl_formula(v, mx):
    """Excel text for a segment label: hidden if tiny or zero (artifact hides segments < 64 px)."""
    return (f'=IF({v}<0.04*{mx},"",TEXT({v},IF({v}<0.1,"0.000",IF({v}<100,"0.0","#,##0"))))')


def tot_formula(v, unit):
    return f'=TEXT({v},IF({v}<0.1,"0.000",IF({v}<100,"0.0","#,##0")))&" "&{unit}'


class BarBlock:
    """Chart-data block for a stacked bar chart.

    Rows are written bottom-to-top (Excel draws the first category at the bottom), so the
    caller passes `rows` in the order they should appear TOP-to-bottom and we reverse.
    columns: B name | C.. segments | next total | next total-label | segment labels
    """

    def __init__(self, sh: Sh, r0, names, segnames, colors, vals, unit_ref, caption=None):
        # vals[i][j] = formula text for chain i (top-to-bottom order), segment j
        f = sh.bk.fmt
        n, m = len(names), len(segnames)
        self.sh, self.r0, self.n, self.m = sh, r0, n, m
        self.segnames, self.colors = segnames, colors
        hdr = ["Chart data (bottom-to-top)"] + segnames + ["Total", "Total label (padding)"] + [f"Label: {s}" for s in segnames] + ["Total label"]
        sh.table(r0, hdr, [], c0=1)
        sh.ws.set_row(r0, 42)
        for j, h in enumerate(hdr):
            sh.ws.write(r0, 1 + j, h, f(bg_color=DARK, font_color="#FFFFFF", bold=True, text_wrap=True,
                                         align="left" if j == 0 else "right", font_size=8))
        order = list(range(n))[::-1]
        self.rows = []
        for k, i in enumerate(order):
            r = r0 + 1 + k
            self.rows.append(r)
            sh.put(r, 1, names[i], f(bold=True, bottom=1, bottom_color=GRID))
            for j in range(m):
                sh.put(r, 2 + j, vals[i][j], f(num_format="General", bottom=1, bottom_color=GRID, align="right"))
        self.c_tot = 2 + m
        self.c_pad = 3 + m
        self.c_lbl0 = 4 + m
        self.c_tlbl = 4 + 2 * m
        first, last = r0 + 1, r0 + n
        for k, r in enumerate(self.rows):
            tot = f"SUM({xl_rowcol_to_cell(r, 2)}:{xl_rowcol_to_cell(r, 1 + m)})"
            sh.put(r, self.c_tot, "=" + tot, f(num_format="General", bottom=1, bottom_color=GRID, align="right"))
            allt = f"{xl_rowcol_to_cell(first, self.c_tot, True, True)}:{xl_rowcol_to_cell(last, self.c_tot, True, True)}"
            sh.put(r, self.c_pad, f"=0.3*MAX({allt})", f(num_format="General", bottom=1, bottom_color=GRID, align="right"))
            for j in range(m):
                v = xl_rowcol_to_cell(r, 2 + j)
                sh.put(r, self.c_lbl0 + j, lbl_formula(v, f"MAX({allt})"), f(bottom=1, bottom_color=GRID, align="right"))
            sh.put(r, self.c_tlbl, tot_formula(xl_rowcol_to_cell(r, self.c_tot), unit_ref),
                   f(bottom=1, bottom_color=GRID, align="right"))
        self.cats = rng(sh, first, 1, last, 1)
        self.end = r0 + 1 + n

    def chart(self, title_ref, xname, w, h, keep=None):
        sh = self.sh
        first, last = self.r0 + 1, self.r0 + self.n
        segs = []
        for j in range(self.m):
            if keep is not None and j not in keep:
                continue
            segs.append((self.segnames[j], rng(sh, first, 2 + j, last, 2 + j), self.colors[j],
                         [(r, self.c_lbl0 + j) for r in self.rows]))
        tot_vals = rng(sh, first, self.c_pad, last, self.c_pad)
        tlbls = [(r, self.c_tlbl) for r in self.rows]
        return hbar(sh, title_ref, xname, self.cats, segs, tot_vals, tlbls, w, h)


def sweep(sh: Sh, r0, headers, xs, cols, xnf="d2", nfs=None, every=20, lab_fmt="0"):
    """Write a chart-data sweep: column B = x (constants), cols = formula templates with {r}/{x} placeholders.

    The last column is an axis-label column (text, blank except every `every` points) so every
    spreadsheet viewer shows the same tick labels regardless of its tick-skip support.
    """
    f = sh.bk.fmt
    sh.ws.set_row(r0, 42)
    headers = list(headers) + ["Axis label"]
    for j, h in enumerate(headers):
        sh.ws.write(r0, 1 + j, h, f(bg_color=DARK, font_color="#FFFFFF", bold=True, text_wrap=True,
                                     align="left" if j == 0 else "right", font_size=8))
    for i, x in enumerate(xs):
        r = r0 + 1 + i
        sh.put(r, 1, x, f(num_format=NF[xnf], align="left"))
        xr = xl_rowcol_to_cell(r, 1, False, True)
        for j, tpl in enumerate(cols):
            nfk = (nfs[j] if nfs else "gen")
            sh.put(r, 2 + j, tpl.replace("{x}", xr).replace("{r}", str(r + 1)), f(num_format=NF.get(nfk, nfk), align="right"))
        sh.put(r, 2 + len(cols), f'=IF(MOD({i},{every})=0,TEXT({xr},"{lab_fmt}"),"")', f(align="right"))
    sweep.last_label = (r0 + 1, 2 + len(cols), r0 + len(xs))
    return r0 + 1, r0 + len(xs)


def frange(a, b, step, nd=4):
    out, k = [], 0
    while True:
        v = round(a + k * step, nd)
        if v > b + 1e-9:
            break
        out.append(v)
        k += 1
    return out


def marker(ch, name_ref, cats, vals, color, label_pos="above", line_color=None, dash="dash", drop=True, label=True, size=8):
    spec = {"name": name_ref, "categories": cats, "values": vals, "line": {"none": True},
            "marker": {"type": "circle", "size": size, "fill": {"color": color}, "border": {"color": "#FFFFFF", "width": 1.5}}}
    # Excel draws no marker and no label for #N/A points, so a series-name label shows once, at the marker.
    # (LibreOffice labels #N/A points; PREVIEW_NO_LABELS=1 builds a label-free copy for visual checks there.)
    if label and not os.environ.get("PREVIEW_NO_LABELS"):
        spec["data_labels"] = {"series_name": True, "position": label_pos, "font": cfont(8, DARK, True)}
    if drop:
        spec["y_error_bars"] = {"type": "percentage", "value": 100, "direction": "minus", "end_style": 0,
                                "line": {"color": line_color or color, "width": 1, "dash_type": dash}}
    return spec


def line(name, cats, vals, color, width=2.25, dash=None):
    ln = {"color": color, "width": width}
    if dash:
        ln["dash_type"] = dash
    return {"name": name, "categories": cats, "values": vals, "line": ln, "marker": {"type": "none"}}


def axes_line(ch, xname, yname, xint, ynf="General", xnf="General", ymin=None, xname_is_ref=False):
    ch.set_x_axis({"name": xname, "name_font": cfont(8, BODY), "num_font": cfont(8, MUTED), "num_format": xnf,
                   "interval_unit": 1, "interval_tick": xint, "line": {"color": MUTED},
                   "major_tick_mark": "outside", "label_position": "low"})
    y = {"name": yname, "name_font": cfont(8, BODY), "num_font": cfont(8, MUTED), "num_format": ynf,
         "major_gridlines": {"visible": True, "line": {"color": GRID}}, "line": {"none": True}}
    if ymin is not None:
        y["min"] = ymin
    ch.set_y_axis(y)


# =============================================================================
#  SHEETS
# =============================================================================
def build_midstream(sh: Sh):
    bk, ws, f = sh.bk, sh.ws, sh.bk.fmt
    sh.banner("Midstream · LH₂ Boil-off Bunker Check",
              "Shipping segment only · 40,000 m³ LH₂ vs NH₃ carrier",
              "Does the LH₂ carrier's boil-off cover its own fuel bill, and at what hydrogen price does burning cargo H₂ lose "
              "to an ammonia carrier running 95 % on ammonia fuel?",
              "LH₂/NH₃ loaded → discharged, laden sea day", "per ship-day (t/d, kg/d, USD/d)",
              "LHV basis · USD, prices are user inputs (no cost year asserted)")

    sh.sec("Key results")
    sh.row("Ship_BorStar", "Crossover boil-off rate", "=Ship_HCap/Ship_CargoL*100", "%/day", "Below it the ship buys VLSFO; above it excess H₂ does no work", "d3", "key")
    sh.row(None, "H₂ boil-off at your rate", "=Ship_BOG", "kg/d", "", "int", "key")
    sh.row(None, "Boil-off as % of what the engine can burn", "=Ship_BOG/Ship_HCap", "%", "", "pct", "key")
    sh.row(None, "VLSFO still bought", "=Ship_Vlsfo", "t/d", "of total fuel demand (t/d VLSFO-eq)", "d2", "key")
    sh.row(None, "Surplus H₂ (GCU or vent)", "=Ship_Surplus", "kg/d", "", "int", "key")
    sh.row(None, "Breakeven H₂ price", "=Ship_BE", "USD/kg", "LH₂ and NH₃ ship fuel cost equal (selected basis)", "d2", "key")
    sh.row(None, "LH₂ carrier fuel cost at slider H₂ price", "=Ship_BOG*Ship_P_H2+Ship_FixedL", "USD/d", "", "int", "key")
    sh.row(None, "NH₃ carrier fuel cost (selected basis)", "=Ship_CostNcmp", "USD/d", "", "int", "key")
    sh.row(None, "LH₂ saves (−) / costs extra (+)", "=Ship_BOG*Ship_P_H2+Ship_FixedL-Ship_CostNcmp", "USD/d", "", "int", "key")
    sh.r += 1

    sh.sec("Inputs · common")
    sh.row("Ship_Vol", "Cargo capacity", 40000, "m³", "both ships · user", "int", "input")
    sh.row("Ship_LHV_VLSFO", "VLSFO LHV", 41.0, "MJ/kg", "implied by user table · [ASSUMPTION]", "d1", "input")
    sh.row("Ship_P_VLSFO", "VLSFO price", 600, "USD/t", "[ASSUMPTION] placeholder · edit", "int", "input")
    sh.sub("LH₂ carrier (no reliq)", S1)
    sh.row("Ship_BOR_L", "Boil-off rate", 0.40, "%/day", "user", "d2", "input")
    sh.row("Ship_Duty_L", "Fuel demand", 39, "t/d VLSFO-eq", "user", "d1", "input")
    sh.row("Ship_Rho_L", "LH₂ density", 70.8, "kg/m³", "repo · needs source (lh2-properties.csv)", "d1", "input")
    sh.row("Ship_Fill_L", "Fill, % of capacity", 100, "%", "100 matches user table", "int", "input")
    sh.row("Ship_LHV_H2", "H₂ LHV", 120, "MJ/kg", "repo · needs source (lh2-properties.csv)", "d1", "input")
    sh.row("Ship_Pilot_L", "Pilot VLSFO on H₂", 0, "% energy", "0 matches user table", "d1", "input")
    sh.sub("NH₃ carrier (with reliq)", S2)
    sh.row("Ship_BOR_N", "Boil-off rate", 0.15, "%/day", "user · re-liquefied, no loss", "d2", "input")
    sh.row("Ship_Duty_N", "Fuel demand", 30, "t/d VLSFO-eq", "user · incl. reliq power", "d1", "input")
    sh.row("Ship_Share_N", "NH₃ share of fuel energy", 95, "%", "user · rest is VLSFO pilot", "int", "input")
    sh.row("Ship_LHV_N", "NH₃ LHV", 18.6, "MJ/kg", "repo · [ESTIMATE] (chain-energy-defaults.csv)", "d1", "input")
    sh.row("Ship_Rho_N", "NH₃ density", 682, "kg/m³", "repo · [ESTIMATE] (chain-energy-defaults.csv)", "int", "input")
    sh.row("Ship_P_N", "NH₃ fuel price", 600, "USD/t", "[ASSUMPTION] placeholder · edit", "int", "input")
    sh.row("Ship_H2inNH3", "H₂ mass fraction in NH₃", 0.1775, "kg/kg", "[ASSUMPTION] stoichiometric (chain-energy-defaults.csv)", "d4", "input")
    sh.sub("Price assessment")
    sh.row("Ship_P_H2", "H₂ price (slider in artifact)", 4.0, "USD/kg", "set between 0 and 10", "d2", "input")
    sh.row("Ship_Basis", "Comparison basis", B_SH[0], "", "dropdown", "txt", "input", dv=B_SH)
    sh.r += 1

    # ---- derived model ----
    sh.sec("Model · derived values")
    sh.row("Ship_CargoL", "LH₂ cargo on board", "=Ship_Vol*Ship_Fill_L/100*Ship_Rho_L", "kg", "= capacity × fill × density", "int")
    sh.row("Ship_BOG", "H₂ boil-off", "=Ship_CargoL*Ship_BOR_L/100", "kg/d", "= cargo × BOR", "int")
    sh.row("Ship_HFull", "H₂ to cover whole fuel duty", "=Ship_Duty_L*1000*Ship_LHV_VLSFO/Ship_LHV_H2", "kg/d", "= duty × LHV(VLSFO) ÷ LHV(H₂)", "d1")
    sh.row("Ship_HCap", "H₂ the engine can burn", "=Ship_HFull*(1-Ship_Pilot_L/100)", "kg/d", "less pilot VLSFO", "d1")
    sh.row("Ship_Burned", "H₂ burned", "=MIN(Ship_BOG,Ship_HCap)", "kg/d", "", "int")
    sh.row("Ship_Surplus", "Surplus H₂", "=MAX(0,Ship_BOG-Ship_HCap)", "kg/d", "to GCU or vent", "int")
    sh.row("Ship_VlsfoSigned", "VLSFO required (user convention)", "=Ship_Duty_L-Ship_BOG*Ship_LHV_H2/Ship_LHV_VLSFO/1000", "t/d", "negative = surplus", "d2")
    sh.row("Ship_Vlsfo", "VLSFO actually bought", "=Ship_Duty_L-Ship_Burned*Ship_LHV_H2/Ship_LHV_VLSFO/1000", "t/d", "", "d2")
    sh.row("Ship_CargoN", "NH₃ cargo (full, reliq → no loss)", "=Ship_Vol*Ship_Rho_N", "kg", "", "int")
    sh.row("Ship_NH3Fuel", "NH₃ fuel", "=Ship_Duty_N*Ship_Share_N/100*Ship_LHV_VLSFO/Ship_LHV_N", "t/d", "", "d2")
    sh.row("Ship_PilotN", "Pilot VLSFO (NH₃ ship)", "=Ship_Duty_N*(1-Ship_Share_N/100)", "t/d", "", "d2")
    sh.row("Ship_CostN", "NH₃ ship fuel cost", "=Ship_NH3Fuel*Ship_P_N+Ship_PilotN*Ship_P_VLSFO", "USD/d", "", "int")
    sh.row("Ship_H2N", "H₂ contained in NH₃ cargo", "=Ship_CargoN*Ship_H2inNH3", "kg", "", "int")
    sh.row("Ship_ScaleN", "Cargo-H₂ ratio (LH₂ ÷ NH₃)", "=Ship_CargoL/Ship_H2N", "–", "scales NH₃ cost to same H₂ carried", "d3")
    sh.row("Ship_CostNcmp", "NH₃ ship cost on selected basis", '=IF(Ship_Basis="Per ship-day",Ship_CostN,Ship_CostN*Ship_ScaleN)', "USD/d", "", "int")
    sh.row("Ship_FixedL", "LH₂ ship VLSFO cost", "=Ship_Vlsfo*Ship_P_VLSFO", "USD/d", "", "int")
    sh.row("Ship_BE", "Breakeven H₂ price", "=IF(Ship_BOG>0,(Ship_CostNcmp-Ship_FixedL)/Ship_BOG,NA())", "USD/kg", "= (NH₃ cost − LH₂ VLSFO cost) ÷ boil-off", "d2")
    sh.row("Ship_SW", "Forced-boil-off line (H₂ = VLSFO per GJ)", "=Ship_P_VLSFO/1000*Ship_LHV_H2/Ship_LHV_VLSFO", "USD/kg", "below this H₂ is cheaper than VLSFO per GJ", "d2")
    sh.row("Ship_BogN", "NH₃ boil-off (re-liquefied to cargo)", "=Ship_CargoN*Ship_BOR_N/100", "kg/d", "", "int")
    sh.row("Ship_BEh2", "Breakeven on per-tonne-H₂ basis", "=IF(Ship_BOG>0,(Ship_CostN*Ship_ScaleN-Ship_FixedL)/Ship_BOG,NA())", "USD/kg", "", "d2")
    sh.r += 1
    sh.sec("Chart headlines (feed the chart titles)")
    sh.headline("Ship_T1", '="Boil-off covers the full fuel demand above "&TEXT(Ship_BorStar,"0.000")&" %/day"')
    sh.headline("Ship_T3", '=IF(ISNUMBER(Ship_BE),IF(Ship_BE>0,"Burning boil-off beats the ammonia ship while H2 is below USD "&TEXT(Ship_BE,"0.00")&"/kg","The ammonia ship is cheaper at any H2 price with these inputs"),"No boil-off: no breakeven")')
    sh.headline("Ship_L1", '="Crossover "&TEXT(Ship_BorStar,"0.000")&" %/d · "&TEXT(Ship_HCap,"#,##0")&" kg/d H2"')
    sh.headline("Ship_L2", '="Your case "&TEXT(Ship_BOR_L,"0.00")&" %/d · "&IF(Ship_Surplus>0,TEXT(Ship_Surplus,"#,##0")&" kg/d surplus",TEXT(Ship_HCap-Ship_BOG,"#,##0")&" kg/d short")')
    sh.headline("Ship_L3", '=TEXT(Ship_Vlsfo,"0.00")&" t/d at "&TEXT(Ship_BOR_L,"0.00")&" %/d"')
    sh.headline("Ship_L4", '="H2 = VLSFO per GJ at USD "&TEXT(Ship_SW,"0.00")&"/kg"')
    sh.headline("Ship_L5", '=IF(ISNUMBER(Ship_BE),"Breakeven USD "&TEXT(Ship_BE,"0.00")&"/kg","")')
    sh.headline("Ship_L6", '="H2 price USD "&TEXT(Ship_P_H2,"0.00")&"/kg"')
    sh.headline("Ship_L7", '=IF(Ship_BOG>0,"USD "&TEXT((Ship_CostN-Ship_FixedL)/Ship_BOG,"0.00")&"/kg at NH3 USD "&TEXT(Ship_P_N,"#,##0")&"/t","")')
    sh.headline("Ship_T4", '="Breakeven H2 price vs NH3 fuel price (per ship-day and per tonne H2 carried)"')
    sh.headline("Ship_T2", '="VLSFO the LH2 ship still buys, by boil-off rate"')
    sh.headline("Ship_NoteBasis", '=IF(Ship_Basis="Per ship-day","Per ship-day is not like-for-like on cargo: the NH3 ship carries "&TEXT(Ship_H2N/1000,"#,##0")&" t of H2 (as NH3) against "&TEXT(Ship_CargoL/1000,"#,##0")&" t on the LH2 ship, about "&TEXT(1/Ship_ScaleN,"0.00")&"x more. Per-tonne basis breakeven: USD "&TEXT(Ship_BEh2,"0.00")&"/kg.","Per tonne H2 carried: NH3 ship daily cost scaled by "&TEXT(Ship_ScaleN,"0.000")&" so both ships move the same hydrogen (upper bound for ammonia: assumes full cracking).")')
    sh.r += 1

    # ---- Check 1: user's surplus table ----
    user = [[0.20, 22.42, 5664.00, None], [0.25, 18.28, 7080.00, None], [0.30, 14.13, 8496.00, None], [0.35, 9.99, 9912.00, None],
            [0.40, 5.84, 11328.00, None], [0.45, 1.70, 12744.00, None], [0.46, 0.87, 13027.20, None], [0.47, 0.04, 13310.40, None],
            [0.48, -0.79, 13593.60, 268.60], [0.49, -1.62, 13876.80, 551.80], [0.50, -2.44, 14160.00, 835.00],
            [0.55, -6.59, 15576.00, 2251.00], [0.60, -10.73, 16992.00, 3667.00]]
    sh.sec("Check 1 · user's surplus column recomputed", 12)
    t0 = sh.r
    rows = []
    for i, u in enumerate(user):
        r = t0 + 1 + i
        x = f"$B{r + 1}"
        bog = f"Ship_CargoL*{x}/100"
        rows.append([u[0], f"=Ship_Duty_L-{bog}*Ship_LHV_H2/Ship_LHV_VLSFO/1000", u[1], f"={bog}", u[2],
                     f"=MAX(0,{bog}-Ship_HCap)", u[3] if u[3] is not None else "–",
                     f'=IF(AND(ABS(C{r + 1}-D{r + 1})<0.006,ABS(E{r + 1}-F{r + 1})<0.01,IF(ISNUMBER(H{r + 1}),ABS(G{r + 1}-H{r + 1})<0.5,G{r + 1}<0.5)),"✓","differs")'])
    end = sh.table(t0, ["Boil-off, %/day", "VLSFO req, t/d", "User", "H₂ boil-off, kg/d", "User", "Surplus H₂, kg/d", "User", "Match"],
                   rows, ["d2", "d2", "d2", "d2", "d2", "d2", "d2", "gen"])
    sh.put(end, 1, f'=IF(COUNTIF(I{t0 + 2}:I{end},"✓")={len(user)},"Verified: every row reproduces to the rounding the user used (H₂ LHV 120, VLSFO LHV ≈ 41.0 MJ/kg, 70.8 kg/m³ on the full 40,000 m³). At the stated 0.40 %/day there is no surplus.","Inputs differ from the user basis or some rows differ: see the Match column.")',
           f(bold=True, font_color=LEAD))
    sh.r = end + 2

    # ---- chart data sweeps ----
    sh.sec("Chart data · sweep A (boil-off rate, charts 1–2)", 12)
    xsA = frange(0.1, 0.7, 0.005, 3)
    colsA = ["=Ship_CargoL*{x}/100", "=Ship_HCap", "=MAX(0,{x_}-Ship_HCap)", "=Ship_Duty_L-MIN({x_},Ship_HCap)*Ship_LHV_H2/Ship_LHV_VLSFO/1000",
             "=IF(E{r}>0,Ship_Duty_L-{x_}*Ship_LHV_H2/Ship_LHV_VLSFO/1000,NA())",
             "=IF(ABS({x}-Ship_BorStar)<=0.0025,Ship_HCap,NA())", "=IF(ABS({x}-Ship_BOR_L)<=0.0025,Ship_BOG,NA())",
             "=IF(ABS({x}-Ship_BOR_L)<=0.0025,Ship_Vlsfo,NA())", "=IF(ABS({x}-Ship_BorStar)<=0.0025,MAX(Ship_Duty_L,0),NA())"]
    cols = [c.replace("{x_}", "C{r}") for c in colsA]
    a0, a1 = sweep(sh, sh.r, ["Boil-off, %/day", "H₂ boil-off, kg/d", "Engine can burn, kg/d", "Surplus (stack), kg/d", "VLSFO bought, t/d",
                              "VLSFO user convention, t/d", "Crossover marker", "Your-case marker (kg/d)", "Your-case marker (t/d)", "Crossover marker (t/d)"],
                   xsA, cols, "d3", lab_fmt="0.0")
    A = dict(x=rng(sh, a0, sweep.last_label[1], a1, sweep.last_label[1]), bog=rng(sh, a0, 2, a1, 2), cap=rng(sh, a0, 3, a1, 3), sur=rng(sh, a0, 4, a1, 4), vl=rng(sh, a0, 5, a1, 5),
             vs=rng(sh, a0, 6, a1, 6), mc=rng(sh, a0, 7, a1, 7), mu=rng(sh, a0, 8, a1, 8), mv=rng(sh, a0, 9, a1, 9), mc2=rng(sh, a0, 10, a1, 10))
    sh.r = a1 + 3
    sh.sec("Chart data · sweep B (H₂ price, chart 3)", 12)
    xsB = frange(0, 10, 0.05, 2)
    b0, b1 = sweep(sh, sh.r, ["H₂ price, USD/kg", "LH₂ carrier, USD/d", "NH₃ carrier, USD/d", "Slider marker", "Breakeven marker", "H₂=VLSFO line marker"],
                   xsB, ["=Ship_BOG*{x}+Ship_FixedL", "=Ship_CostNcmp", "=IF(ABS({x}-Ship_P_H2)<=0.025,C{r},NA())",
                         "=IF(ISNUMBER(Ship_BE),IF(ABS({x}-Ship_BE)<=0.025,Ship_CostNcmp,NA()),NA())",
                         "=IF(ABS({x}-Ship_SW)<=0.025,MAX(Ship_BOG*10+Ship_FixedL,Ship_CostNcmp),NA())"], "d2", ["int", "int", "int", "int", "int"])
    B = dict(x=rng(sh, b0, sweep.last_label[1], b1, sweep.last_label[1]), l=rng(sh, b0, 2, b1, 2), n=rng(sh, b0, 3, b1, 3), ms=rng(sh, b0, 4, b1, 4), mb=rng(sh, b0, 5, b1, 5), mw=rng(sh, b0, 6, b1, 6))
    sh.r = b1 + 3
    sh.sec("Chart data · sweep C (NH₃ price, chart 4)", 12)
    xsC = list(range(200, 1201, 10))
    c0_, c1_ = sweep(sh, sh.r, ["NH₃ price, USD/t", "Breakeven per ship-day", "Breakeven per t H₂", "H₂=VLSFO", "Marker (ship-day)", "Marker (t H₂)"],
                     xsC, ["=((Ship_NH3Fuel*{x}+Ship_PilotN*Ship_P_VLSFO)-Ship_FixedL)/Ship_BOG",
                           "=((Ship_NH3Fuel*{x}+Ship_PilotN*Ship_P_VLSFO)*Ship_ScaleN-Ship_FixedL)/Ship_BOG", "=Ship_SW",
                           "=IF(ABS({x}-Ship_P_N)<=5,C{r},NA())", "=IF(ABS({x}-Ship_P_N)<=5,D{r},NA())"], "int", ["d2"] * 5, every=10)
    Cc = dict(x=rng(sh, c0_, sweep.last_label[1], c1_, sweep.last_label[1]), bd=rng(sh, c0_, 2, c1_, 2), bh=rng(sh, c0_, 3, c1_, 3), sw=rng(sh, c0_, 4, c1_, 4), m1=rng(sh, c0_, 5, c1_, 5), m2=rng(sh, c0_, 6, c1_, 6))
    sh.r = c1_ + 2

    # ---- charts ----
    n = lambda nm: "=" + sh.a(*sh.bk.names[nm])  # noqa: E731  (defined-name -> absolute cell)
    W, H = 640, 330
    # Chart 1
    ar = base_chart(bk, "area", n("Ship_T1"), W, H, legend_delete=[0], subtype="stacked")
    ar.add_series({"name": "base", "categories": A["x"], "values": A["cap"], "fill": {"none": True}, "line": {"none": True}})
    ar.add_series({"name": "Surplus: GCU or vent", "categories": A["x"], "values": A["sur"], "fill": {"color": PURPLE, "transparency": 80}, "line": {"none": True}})
    ln = bk.wb.add_chart({"type": "line"})
    ln.add_series(line("H₂ boil-off available", A["x"], A["bog"], S1, 2.5))
    ln.add_series(line("H₂ the engine can burn (whole fuel demand)", A["x"], A["cap"], MUTED, 1.6, "dash"))
    ln.add_series(marker(ln, n("Ship_L1"), A["x"], A["mc"], S1, "above", S1, "dash"))
    ln.add_series(marker(ln, n("Ship_L2"), A["x"], A["mu"], DARK, "below", DARK, "round_dot"))
    ar.combine(ln)
    ar.set_legend({"position": "bottom", "font": cfont(8), "delete_series": [0, 4, 5]})
    axes_line(ar, "LH₂ voyage boil-off rate, %/day", "H₂, kg/day", 20, "#,##0,\"k\"", "0.0")
    sh.place(ar, 7, W, H)
    # Chart 2
    c2 = base_chart(bk, "line", n("Ship_T2"), W, H)
    c2.add_series(line("VLSFO bought, t/day", A["x"], A["vl"], S2, 2.5))
    c2.add_series(line("User table's negative VLSFO (surplus as VLSFO-eq)", A["x"], A["vs"], MUTED, 1.6, "dash"))
    c2.add_series(marker(c2, n("Ship_L3"), A["x"], A["mv"], DARK, "above", DARK, "round_dot"))
    c2.add_series(marker(c2, "Crossover", A["x"], A["mc2"], S1, "above", S1, "dash", label=False))
    c2.set_legend({"position": "bottom", "font": cfont(8), "delete_series": [2, 3]})
    axes_line(c2, "LH₂ voyage boil-off rate, %/day", "VLSFO, t/day", 20, "0", "0.0")
    sh.place(c2, 7, W, H, W + 12)
    # Chart 3
    c3 = base_chart(bk, "line", n("Ship_T3"), W, H, legend_delete=[2, 3, 4])
    c3.add_series(line('NH₃ carrier (NH₃ fuel + VLSFO pilot)', B["x"], B["n"], S2, 2.5))
    c3.add_series(line("LH₂ carrier (boil-off × H₂ price + VLSFO)", B["x"], B["l"], S1, 2.5))
    c3.add_series(marker(c3, n("Ship_L6"), B["x"], B["ms"], S1, "above", S1, "round_dot", size=7))
    c3.add_series(marker(c3, n("Ship_L5"), B["x"], B["mb"], DARK, "below", DARK, "dash", drop=False))
    c3.add_series(marker(c3, n("Ship_L4"), B["x"], B["mw"], MUTED, "right", MUTED, "dash", size=3))
    axes_line(c3, "H₂ price, USD/kg", "Fuel cost, USD k/day", 20, "#,##0,\"k\"", "0")
    sh.place(c3, 7 + 15, W, H)
    # Chart 4
    c4 = base_chart(bk, "line", n("Ship_T4"), W, H, legend_delete=[3, 4])
    c4.add_series(line("Breakeven, per ship-day", Cc["x"], Cc["bd"], S1, 2.5))
    c4.add_series(line("Breakeven, per tonne H₂ carried", Cc["x"], Cc["bh"], S1, 2, "dash"))
    c4.add_series(line("H₂ = VLSFO per GJ (forced boil-off threshold)", Cc["x"], Cc["sw"], MUTED, 1.4, "round_dot"))
    c4.add_series(marker(c4, n("Ship_L7"), Cc["x"], Cc["m1"], S1, "above", S2, "dash"))
    c4.add_series(marker(c4, "t H2 marker", Cc["x"], Cc["m2"], S1, "above", S2, "dash", label=False))
    axes_line(c4, "NH₃ fuel price, USD/t", "Breakeven H₂, USD/kg", 10, "0.0", "0")
    sh.place(c4, 7 + 15, W, H, W + 12)
    ws.merge_range(7 + 15 * 2 + 1, CH_COL, 7 + 15 * 2 + 3, CH_COL + 11, "", f(text_wrap=True, valign="top"))
    sh.put(7 + 15 * 2 + 1, CH_COL, "=Ship_NoteBasis", f(text_wrap=True, valign="top", bg_color="#FDF0DA", font_size=8))
    sh.chart_bottom = max(sh.chart_bottom, 7 + 15 * 2 + 5)

    # Method note (end)
    sh.r = max(sh.r, sh.chart_bottom)
    methods = [
        "Method, assumptions and gaps",
        "Energy parity: 1 MJ of H₂ displaces 1 MJ of VLSFO in the engine (LHV basis, equal engine efficiency) [ASSUMPTION].",
        "Pilot fuel: the user table lets VLSFO fall to zero; set 'Pilot VLSFO on H₂' to see the crossover move right [ESTIMATE – needs source].",
        "VLSFO LHV 41.0 MJ/kg is back-calculated from the user table; the repo shipping study uses 40.2 MJ/kg [ESTIMATE].",
        "Full cargo, laden leg: boil-off taken on 100 % of 40,000 m³; ballast leg (heel only) is not modelled.",
        "NH₃ carrier: 0.15 %/day boil-off is re-liquefied back to cargo; reliq power is assumed inside the 30 t/d demand [ASSUMPTION].",
        "Prices default to USD 600/t placeholders [ASSUMPTION], not market quotes. Carbon cost / FuelEU, N₂O slip and CO₂e of vented H₂ are excluded (no sourced value).",
        "Sources: user inputs (2026-09-24); kawasaki-2026-questionnaire (40,000 m³ carrier, BOG burned in DF engine, no reliq, GCU for excess); "
        "data/properties/lh2-properties.csv; data/carriers/chain-energy-defaults.csv.",
    ]
    sh.sec(methods[0], 12)
    for t in methods[1:]:
        sh.note("• " + t)


def build_upstream(sh: Sh):
    bk, ws, f = sh.bk, sh.ws, sh.bk.fmt
    sh.banner("Upstream · Liquefaction vs Haber-Bosch",
              "Upstream · gaseous H₂ at battery limit → cargo in export tank",
              "How much energy does it take to make one ship's cargo: liquefying H₂ for the LH₂ carrier, or synthesising NH₃ for the ammonia "
              "carrier, including reliquefaction of boil-off in a 60,000 m³ export tank? Electrolysis of the H₂ each route consumes can be switched on below.",
              "GH₂ (electrolysis optional) → cargo ready to load", "one full 40,000 m³ cargo, or per kg H₂",
              "MWh, electricity as delivered kWh")
    sh.sec("Electrolysis switch")
    sh.row("Up_ElzOn", "Include electrolysis of the H₂ each route consumes", "No", "", "dropdown · feeds Full Chain, Annual Energy, Energy Cost", "txt", "input", dv=YES_NO)
    sh.row("Up_ElzSec", "Electrolyser SEC", 60, "kWh/kg H₂", "[ASSUMPTION] repo · user-set placeholder", "int", "input")
    sh.r += 1
    sh.sec("Key results")
    sh.row(None, "LH₂ route upstream energy", "=Up_TotL", "=Up_Unit", "", "d2", "key")
    sh.row(None, "NH₃ route upstream energy", "=Up_TotN", "=Up_Unit", "", "d2", "key")
    sh.row(None, "LH₂ ÷ NH₃", "=Up_Ratio", "×", "", "d2", "key")
    sh.row(None, "H₂ used per cargo, LH₂ route", "=Ship_CargoL/1000", "t", "", "int", "key")
    sh.row(None, "H₂ used per cargo, NH₃ route", "=Up_H2N/1000", "t", "=TEXT(Up_H2N/Ship_CargoL,\"0.00\")&\"× the LH₂ route\"", "int", "key")
    sh.row("Up_Par", "Parity liquefaction SEC", "=Up_Par0", "kWh/kg H₂", "same upstream energy on both routes", "d2", "key")
    sh.row(None, "Minimum possible (para-H₂)", "=Up_MinPara", "kWh/kg", "", "d2", "key")
    sh.row(None, "Gap to the minimum", "=Up_MinPara-Up_Par", "kWh/kg", "", "d2", "key")
    sh.row(None, "User liquefier vs ideal (para basis)", "=Up_MinPara/Up_SecL", "%", "", "pct", "key")
    sh.r += 1
    sh.sec("Cargo basis (linked from Midstream)")
    sh.row(None, "Cargo capacity", "=Ship_Vol", "m³", "Midstream", "int", "link")
    sh.row(None, "LH₂ density", "=Ship_Rho_L", "kg/m³", "Midstream", "d1", "link")
    sh.row(None, "LH₂ fill", "=Ship_Fill_L", "%", "Midstream", "int", "link")
    sh.row(None, "NH₃ density", "=Ship_Rho_N", "kg/m³", "Midstream", "int", "link")
    sh.sec("Inputs · LH₂ liquefaction")
    sh.row("Up_SecL", "Liquefaction", 9, "kWh/kg H₂", "user · KHI 8–9 (kawasaki-2026-questionnaire)", "d1", "input")
    sh.row("Up_BorL", "Export tank BOR", 0.1, "%/day", "user · KHI 0.1 (kawasaki-2026-supplemental)", "d2", "input")
    sh.row("Up_RlqL", "BOG reliq", 3.94, "kWh/kg BOG", "repo [ASSUMPTION] (condensation-only duty)", "d2", "input")
    sh.sec("Inputs · NH₃ Haber-Bosch")
    sh.row("Up_SecN", "Haber-Bosch", 1, "kWh/kg H₂", "user · ASU included? (open question)", "d1", "input")
    sh.row("Up_Stoich", "Stoichiometric NH₃", 5.6, "kg/kg H₂", "user · exact 5.632", "d2", "input")
    sh.row("Up_Loss", "H₂ lost in synthesis loop", 0, "%", "0 = none assumed", "d1", "input")
    sh.row("Up_BorN", "Export tank BOR", 0.05, "%/day", "user", "d2", "input")
    sh.row("Up_RlqN", "BOG reliq", 0.25, "kWh/kg BOG", "repo · [ESTIMATE]", "d2", "input")
    sh.sec("Inputs · export tank (both)")
    sh.row("Up_Tank", "Tank size", 60000, "m³", "user", "int", "input")
    sh.row("Up_Fill", "Average inventory", 100, "% of tank", "100 = full, conservative", "int", "input")
    sh.row("Up_Days", "Storage days per cargo", 5, "days", "[ASSUMPTION] repo placeholder · edit", "int", "input")
    sh.sec("Inputs · liquefaction thermodynamic floor")
    sh.row("Up_MinNorm", "Minimum work, normal-H₂", 3.3, "kWh/kg", "cited: doe-2009-h2-liquefaction-energy", "d1", "input")
    sh.row("Up_MinPara", "Minimum work, para-H₂", 3.9, "kWh/kg", "cited: doe-2009-h2-liquefaction-energy", "d1", "input")
    sh.sec("Chart basis")
    sh.row("Up_Basis", "Show", B_UP[0], "", "dropdown", "txt", "input", dv=B_UP)
    sh.r += 1

    # ---- model ----
    sh.sec("Model · per cargo", 12)
    sh.row("Up_H2N", "H₂ fed to Haber-Bosch", "=Ship_CargoN/Up_Stoich/(1-Up_Loss/100)", "kg", "= NH₃ cargo ÷ stoich ÷ (1 − loss)", "int")
    sh.row("Up_InvL", "LH₂ export-tank inventory", "=Up_Tank*Up_Fill/100*Ship_Rho_L", "kg", "", "int")
    sh.row("Up_InvN", "NH₃ export-tank inventory", "=Up_Tank*Up_Fill/100*Ship_Rho_N", "kg", "", "int")
    sh.row("Up_BogL", "LH₂ tank boil-off", "=Up_InvL*Up_BorL/100", "kg/d", "", "int")
    sh.row("Up_BogN", "NH₃ tank boil-off", "=Up_InvN*Up_BorN/100", "kg/d", "", "int")
    sh.row("Up_Liq", "Liquefaction energy", "=Ship_CargoL*Up_SecL", "kWh", "= cargo × SEC", "int")
    sh.row("Up_RlL", "LH₂ tank reliq energy", "=Up_BogL*Up_Days*Up_RlqL", "kWh", "", "int")
    sh.row("Up_HB", "Haber-Bosch energy", "=Up_H2N*Up_SecN", "kWh", "= H₂ fed × SEC", "int")
    sh.row("Up_RlN", "NH₃ tank reliq energy", "=Up_BogN*Up_Days*Up_RlqN", "kWh", "", "int")
    sh.row("Up_ElzL", "Electrolysis, LH₂ route", '=IF(Up_ElzOn="Yes",Ship_CargoL*Up_ElzSec,0)', "kWh", "H₂ consumed × electrolyser SEC", "int")
    sh.row("Up_ElzN", "Electrolysis, NH₃ route", '=IF(Up_ElzOn="Yes",Up_H2N*Up_ElzSec,0)', "kWh", "H₂ consumed × electrolyser SEC", "int")
    sh.row("Up_Unit", "Chart unit", '=IF(Up_Basis="Per kg H2 (kWh)","kWh/kg H2","MWh")', "", "", "txt")
    sh.row("Up_DivL", "Divisor, LH₂", '=IF(Up_Basis="Per kg H2 (kWh)",Ship_CargoL,1000)', "", "", "int")
    sh.row("Up_DivN", "Divisor, NH₃", '=IF(Up_Basis="Per kg H2 (kWh)",Up_H2N,1000)', "", "", "int")
    sh.row("Up_TotL", "LH₂ route total", "=(Up_ElzL+Up_Liq+Up_RlL)/Up_DivL", "=Up_Unit", "", "d2")
    sh.row("Up_TotN", "NH₃ route total", "=(Up_ElzN+Up_HB+Up_RlN)/Up_DivN", "=Up_Unit", "", "d2")
    sh.row("Up_Ratio", "LH₂ ÷ NH₃", "=Up_TotL/Up_TotN", "×", "", "d2")
    sh.row("Up_Par0", "Parity liquefaction SEC (basis-consistent)",
           '=IF(Up_Basis="Per kg H2 (kWh)",(Up_HB+Up_RlN+Up_ElzN)/Up_H2N-(Up_RlL+Up_ElzL)/Ship_CargoL,((Up_HB+Up_RlN+Up_ElzN)-Up_RlL-Up_ElzL)/Ship_CargoL)',
           "kWh/kg", "SEC at which both routes use equal upstream energy", "d2")
    sh.r += 1
    sh.headline("Up_T7", '=IF(Up_ElzOn="No","Liquefaction takes about "&TEXT(Up_Ratio,"0.0")&"× the energy of Haber-Bosch",IF(Up_Ratio>=1,"With electrolysis, the LH2 route takes about "&TEXT(Up_Ratio,"0.0")&"× the energy of the NH3 route","With electrolysis, the NH3 route takes about "&TEXT(1/Up_Ratio,"0.0")&"× the energy of the LH2 route"))&IF(Up_Basis="Per kg H2 (kWh)"," per kg H2"," per cargo")')
    sh.headline("Up_T7b", '=IF(Up_Par0<0,"Even a liquefier using no energy would not match the NH3 route ("&TEXT(Up_Par0,"0.00")&" kWh/kg needed)",IF(Up_Par0<Up_MinPara,"A liquefier would need "&TEXT(Up_Par0,"0.00")&" kWh/kg to match Haber-Bosch — below the "&TEXT(Up_MinPara,"0.0")&" kWh/kg thermodynamic minimum, so it is unreachable","A liquefier at "&TEXT(Up_Par0,"0.00")&" kWh/kg would match Haber-Bosch — above the "&TEXT(Up_MinPara,"0.0")&" kWh/kg minimum, so it is physically possible"))')
    sh.headline("Up_XT7", '=IF(Up_Basis="Per kg H2 (kWh)","Energy, kWh per kg H2","Energy per 40,000 m3 cargo, MWh")')
    sh.headline("Up_YT7b", '=IF(Up_Basis="Per kg H2 (kWh)","Upstream energy, kWh/kg H2","Upstream energy, MWh per cargo")')
    sh.headline("Up_LblUser", '="Your input "&TEXT(Up_SecL,"0.0")&" kWh/kg"')
    sh.headline("Up_LblPar", '="Parity at "&TEXT(Up_Par0,"0.00")&" kWh/kg"')
    sh.headline("Up_LblN", '="3.3 normal-H2"')
    sh.headline("Up_LblP", '="3.9 para-H2 minimum"')
    sh.r += 1

    # tables
    sh.sec("Production basis · what each ship needs", 12)
    t0 = sh.r
    end = sh.table(t0, ["Route", "Cargo made, kg", "H₂ used, kg", "H₂ in cargo, kg", "Export tank inventory, kg"],
                   [["LH₂ · liquefaction", "=Ship_CargoL", "=Ship_CargoL", "=Ship_CargoL", "=Up_InvL"],
                    ["NH₃ · Haber-Bosch", "=Ship_CargoN", "=Up_H2N", "=Ship_CargoN/Up_Stoich", "=Up_InvN"]], ["gen", "int", "int", "int", "int"])
    sh.r = end + 1
    sh.sec("Energy build-up per cargo", 12)
    t0 = sh.r
    end = sh.table(t0, ["Line", "LH₂, MWh", "NH₃, MWh", "LH₂, kWh/kg H₂", "NH₃, kWh/kg H₂"],
                   [["Electrolysis", "=Up_ElzL/1000", "=Up_ElzN/1000", "=Up_ElzL/Ship_CargoL", "=Up_ElzN/Up_H2N"],
                    ["Liquefaction / Haber-Bosch", "=Up_Liq/1000", "=Up_HB/1000", "=Up_Liq/Ship_CargoL", "=Up_HB/Up_H2N"],
                    ["Export-tank BOG reliq", "=Up_RlL/1000", "=Up_RlN/1000", "=Up_RlL/Ship_CargoL", "=Up_RlN/Up_H2N"],
                    ["Total", "=SUM(C%d:C%d)" % (t0 + 2, t0 + 4), "=SUM(D%d:D%d)" % (t0 + 2, t0 + 4), "=SUM(E%d:E%d)" % (t0 + 2, t0 + 4), "=SUM(F%d:F%d)" % (t0 + 2, t0 + 4)]],
                   ["gen", "d1", "d1", "d3", "d3"], total_last=True)
    sh.r = end + 1
    sh.sec("Export tank boil-off, per day", 12)
    t0 = sh.r
    end = sh.table(t0, ["Export tank", "Inventory, kg", "BOR, %/day", "Boil-off, kg/day", "Reliq, kWh/kg", "Reliq energy, MWh/day", "Per cargo, MWh"],
                   [["LH₂", "=Up_InvL", "=Up_BorL", "=Up_BogL", "=Up_RlqL", "=Up_BogL*Up_RlqL/1000", "=Up_RlL/1000"],
                    ["NH₃", "=Up_InvN", "=Up_BorN", "=Up_BogN", "=Up_RlqN", "=Up_BogN*Up_RlqN/1000", "=Up_RlN/1000"]],
                   ["gen", "int", "d2", "int", "d2", "d2", "d1"])
    sh.r = end + 2

    # chart data: chart 7
    sh.sec("Chart data · chart 7 (energy to make one cargo)", 14)
    bb = BarBlock(sh, sh.r, ["LH₂ · liquefaction", "NH₃ · Haber-Bosch"], ["Electrolysis", "Liquefaction", "Haber-Bosch", "Export-tank BOG reliq"],
                  [C5, C1, C2, C6],
                  [["=Up_ElzL/Up_DivL", "=Up_Liq/Up_DivL", "=0", "=Up_RlL/Up_DivL"], ["=Up_ElzN/Up_DivN", "=0", "=Up_HB/Up_DivN", "=Up_RlN/Up_DivN"]], "Up_Unit")
    sh.r = bb.end + 2
    # chart 7b sweep
    sh.sec("Chart data · chart 7b (sweep of liquefaction SEC)", 14)
    xs = frange(0, 10, 0.05, 2)
    kg = '(Up_Basis="Per kg H2 (kWh)")'
    s0, s1 = sweep(sh, sh.r, ["SEC, kWh/kg", "LH₂ route", "NH₃ route", "Below minimum (band)", "KHI 8–9 (band)", "Normal-H₂ min", "Para-H₂ min", "Your input", "Parity"],
                   xs, [f"=IF({kg},{{x}}+(Up_RlL+Up_ElzL)/Ship_CargoL,({{x}}*Ship_CargoL+Up_RlL+Up_ElzL)/1000)",
                        f"=IF({kg},(Up_HB+Up_RlN+Up_ElzN)/Up_H2N,(Up_HB+Up_RlN+Up_ElzN)/1000)",
                        "=IF({x}<=Up_MinPara,1,0)", "=IF(AND({x}>=8,{x}<=9),1,0)",
                        "=IF(ABS({x}-Up_MinNorm)<=0.025,Up_YTop,NA())",
                        "=IF(ABS({x}-Up_MinPara)<=0.025,Up_YTop,NA())",
                        "=IF(ABS({x}-Up_SecL)<=0.025,C{r},NA())",
                        "=IF(AND(Up_Par0>=0,Up_Par0<=10),IF(ABS({x}-Up_Par0)<=0.025,D{r},NA()),NA())"], "d2",
                   ["d2", "d2", "int", "int", "d2", "d2", "d2", "d2"])
    S = dict(x=rng(sh, s0, sweep.last_label[1], s1, sweep.last_label[1]), l=rng(sh, s0, 2, s1, 2), n=rng(sh, s0, 3, s1, 3), b1=rng(sh, s0, 4, s1, 4), b2=rng(sh, s0, 5, s1, 5),
             mn=rng(sh, s0, 6, s1, 6), mp=rng(sh, s0, 7, s1, 7), mu=rng(sh, s0, 8, s1, 8), mpar=rng(sh, s0, 9, s1, 9))
    sh.r = s1 + 2
    sh.row("Up_YTop", "Top of the 7b data (marker height)", f"=MAX(MAX({xl_rowcol_to_cell(s0, 2, True, True)}:{xl_rowcol_to_cell(s1, 3, True, True)}),1)", "", "", "d1")

    # ---- charts ----
    n = lambda nm: "=" + sh.a(*sh.bk.names[nm])  # noqa: E731
    ch7 = bb.chart(n("Up_T7"), n("Up_XT7"), 640, 250)
    sh.place(ch7, 7, 640, 250)
    W, H = 640, 360
    c = base_chart(bk, "line", n("Up_T7b"), W, H, legend_delete=[2, 3, 4, 5, 6, 7])
    c.add_series(line("LH₂ route: liquefaction + tank reliq (+ electrolysis)", S["x"], S["l"], S1, 2.5))
    c.add_series(line("NH₃ route: Haber-Bosch + tank reliq (+ electrolysis)", S["x"], S["n"], S2, 2.5))
    c.add_series(marker(c, n("Up_LblN"), S["x"], S["mn"], AMBER, "left", AMBER, "dash", drop=True, label=True, size=3))
    c.add_series(marker(c, n("Up_LblP"), S["x"], S["mp"], AMBER, "right", AMBER, "dash", drop=True, label=True, size=3))
    c.add_series(marker(c, n("Up_LblUser"), S["x"], S["mu"], S1, "above", S1, "round_dot"))
    c.add_series(marker(c, n("Up_LblPar"), S["x"], S["mpar"], DARK, "below", DARK, "round_dot", drop=False))
    area = bk.wb.add_chart({"type": "area"})
    area.add_series({"name": "Below minimum liquefaction work (unreachable)", "categories": S["x"], "values": S["b1"], "y2_axis": True,
                     "fill": {"color": AMBER, "transparency": 80}, "line": {"none": True}})
    area.add_series({"name": "KHI disclosed 8–9 kWh/kg", "categories": S["x"], "values": S["b2"], "y2_axis": True,
                     "fill": {"color": PURPLE, "transparency": 80}, "line": {"none": True}})
    area.set_y2_axis({"min": 0, "max": 1, "label_position": "none", "line": {"none": True}, "major_tick_mark": "none",
                      "major_gridlines": {"visible": False}})
    c.combine(area)
    c.set_legend({"position": "bottom", "font": cfont(8), "delete_series": [2, 3, 4, 5]})
    axes_line(c, "Liquefaction SEC, kWh per kg H₂", n("Up_YT7b"), 20, "#,##0", "0")
    sh.place(c, 7 + 12, W, H)

    sh.r = max(sh.r, sh.chart_bottom)
    sh.sec("Method, assumptions and gaps", 12)
    for t in [
        "Production follows the ship: the liquefier makes one LH₂ cargo (40,000 m³ × 70.8 kg/m³ at the fill); the ammonia plant makes one NH₃ cargo (40,000 m³ × 682 kg/m³). Its H₂ feed is cargo ÷ stoichiometric ratio, so the NH₃ route consumes more H₂ per cargo.",
        "Haber-Bosch 1 kWh/kg H₂ is a user figure (= 0.18 kWh/kg NH₃). Repo placeholder is 0.5–0.7 kWh/kg NH₃ (≈ 2.8–3.9 kWh/kg H₂) incl. ASU, syngas compression and refrigeration [ESTIMATE]. Check whether the 1 kWh/kg includes the ASU.",
        "No synthesis heat credit (exothermic steam excluded, as agreed for the chain study).",
        "Tank boil-off on the full 60,000 m³ tank for the storage days per cargo, linear in days. LH₂ reliq 3.94 kWh/kg is a condensation-only duty [ASSUMPTION]; set 9 to charge full liquefaction. NH₃ reliq 0.25 kWh/kg is a repo placeholder [ESTIMATE].",
        "Storage days per cargo depends on plant output and ship schedule, neither fixed yet; five days is a placeholder [ASSUMPTION].",
        "Electrolysis (dropdown above): H₂ consumed by each route × electrolyser SEC. Off by default because both routes start from the same GH₂; on, it penalises the route that consumes more H₂ per cargo. Chart 7b then includes electrolysis in both routes. 60 kWh/kg is a placeholder [ASSUMPTION].",
        "Not included: loading pumps and arms, flare or vent losses.",
        "Minimum liquefaction work 3.3 (normal-H₂) / 3.9 (para-H₂) kWh/kg: doe-2009-h2-liquefaction-energy. KHI 8–9 kWh/kg: kawasaki-2026-questionnaire. Export tank BOR 0.1 %/day: kawasaki-2026-supplemental.",
    ]:
        sh.note("• " + t)


def build_downstream(sh: Sh):
    bk, ws, f = sh.bk, sh.ws, sh.bk.fmt
    sh.banner("Downstream · Regas vs Ammonia Cracking",
              "Downstream · one ship cargo, discharged → gaseous H₂",
              "How much energy does it take to turn one ship's cargo into gaseous hydrogen: vaporising LH₂ in a seawater ORV, or cracking NH₃ back to H₂?",
              "cargo at receiving terminal → gaseous H₂ at send-out", "one full 40,000 m³ cargo, or per kg H₂ delivered",
              "MWh; fuels on LHV, electricity as delivered kWh")
    sh.sec("Key results")
    sh.row(None, "H₂ delivered per cargo, LH₂ ship", "=Dn_H2L/1000", "t", "", "int", "key")
    sh.row(None, "H₂ delivered per cargo, NH₃ (NG-fired)", "=Dn_H2NG/1000", "t", "", "int", "key")
    sh.row(None, "H₂ delivered per cargo, NH₃ (clean fuel)", "=Dn_H2CL/1000", "t", "", "int", "key")
    sh.row(None, "LH₂ regas", "=Dn_VRg", "=Dn_Unit", "=TEXT(Dn_RegasPerKg/(Ship_LHV_H2/3.6)*100,\"0.00\")&\" % of delivered H2 LHV\"", "d2", "key")
    sh.row(None, "Cracker, NG-fired", "=Dn_VNG", "=Dn_Unit", "=TEXT(Dn_TotNG/Dn_H2NG/(Ship_LHV_H2/3.6)*100,\"0.0\")&\" % of delivered H2 LHV\"", "d2", "key")
    sh.row(None, "Cracker, clean fuel", "=Dn_VCL", "=Dn_Unit", "=TEXT(Dn_TotCL/Dn_H2CL/(Ship_LHV_H2/3.6)*100,\"0.0\")&\" % of delivered H2 LHV\"", "d2", "key")
    sh.row(None, "Cracking ÷ regas (NG-fired, per kg H₂)", "=(Dn_TotNG/Dn_H2NG)/Dn_RegasPerKg", "×", "", "int", "key")
    sh.r += 1
    sh.sec("Cargo basis (linked from Midstream)")
    sh.row(None, "Cargo capacity", "=Ship_Vol", "m³", "Midstream", "int", "link")
    sh.row(None, "LH₂ density", "=Ship_Rho_L", "kg/m³", "Midstream", "d1", "link")
    sh.row(None, "NH₃ density", "=Ship_Rho_N", "kg/m³", "Midstream", "int", "link")
    sh.row(None, "NH₃ LHV", "=Ship_LHV_N", "MJ/kg", "Midstream", "d1", "link")
    sh.sec("Inputs · LH₂ regas, ORV seawater")
    sh.row("Dn_Duty", "Regas heat duty", 3.8, "MJ/kg", "KHI · cited (kawasaki-2026-questionnaire)", "d1", "input")
    sh.row("Dn_SendP", "Send-out pressure", 30, "barg", "[ASSUMPTION]", "int", "input")
    sh.row("Dn_EtaP", "LH₂ pump efficiency", 70, "%", "[ASSUMPTION]", "int", "input")
    sh.row("Dn_DT", "Seawater ΔT", 5, "K", "[ASSUMPTION]", "d1", "input")
    sh.row("Dn_Cp", "Seawater cp", 4.0, "kJ/kg·K", "[ASSUMPTION]", "d2", "input")
    sh.row("Dn_Head", "Seawater pump head", 20, "m", "[ASSUMPTION]", "int", "input")
    sh.row("Dn_EtaSW", "Seawater pump efficiency", 75, "%", "[ASSUMPTION]", "int", "input")
    sh.sec("Inputs · NH₃ cracker")
    sh.row("Dn_FeedNG", "NH₃ feed, NG-fired", 6.5, "kg/kg H₂", "user", "d1", "input")
    sh.row("Dn_FeedCl", "NH₃ feed, clean fuel (NH₃-fired)", 7.2, "kg/kg H₂", "user", "d1", "input")
    sh.row("Dn_Stoich", "Stoichiometric NH₃", 5.6, "kg/kg H₂", "user · exact 5.632", "d2", "input")
    sh.row("Dn_Elec", "Cracker electricity", 0.29, "kWh/kg H₂", "user", "d2", "input")
    sh.row("Dn_Annual", "Annual H₂ for the check", 100000, "t/y", "implied by user table", "int", "input")
    sh.sec("Inputs · import-tank boil-off (storage)")
    sh.row("Dn_Tank", "Include re-liquefaction of import-tank boil-off", "Yes", "", "dropdown", "txt", "input", dv=["Yes", "No"])
    sh.row("Dn_Hold", "Hold time", 5, "days", "[ASSUMPTION] repo", "int", "input")
    sh.row("Dn_BorL", "LH₂ tank BOR", 0.1, "%/day", "KHI · cited (kawasaki-2026-supplemental)", "d2", "input")
    sh.row("Dn_SecL", "LH₂ reliq", 3.94, "kWh/kg BOG", "repo [ASSUMPTION]", "d2", "input")
    sh.row("Dn_BorN", "NH₃ tank BOR", 0.05, "%/day", "repo · [ESTIMATE]", "d2", "input")
    sh.row("Dn_SecN", "NH₃ reliq", 0.25, "kWh/kg BOG", "repo · [ESTIMATE]", "d2", "input")
    sh.sec("Chart basis")
    sh.row("Dn_Basis", "Show", B_DN[0], "", "dropdown", "txt", "input", dv=B_DN)
    sh.r += 1

    sh.sec("Model · per cargo", 12)
    sh.row("Dn_PumpL", "LH₂ send-out pump", "=(1/Ship_Rho_L)*Dn_SendP*100000/(Dn_EtaP/100)/3600000", "kWh/kg", "= (1 ÷ ρ) × ΔP ÷ η", "d4")
    sh.row("Dn_SwKg", "Seawater flow", "=Dn_Duty*1000/(Dn_Cp*Dn_DT)", "kg/kg LH₂", "= duty ÷ (cp × ΔT)", "int")
    sh.row("Dn_PumpSW", "Seawater pump", "=Dn_SwKg*9.81*Dn_Head/(Dn_EtaSW/100)/3600000", "kWh/kg", "g = 9.81 m/s²", "d4")
    sh.row("Dn_TankL", "Import-tank BOG reliq (per kg LH₂)", '=IF(Dn_Tank="Yes",(1-(1-Dn_BorL/100)^Dn_Hold)*Dn_SecL,0)', "kWh/kg", "", "d4")
    sh.row("Dn_RegasPerKg", "Regas total", "=Dn_PumpL+Dn_PumpSW+Dn_TankL", "kWh/kg", "", "d4")
    sh.row("Dn_TankN", "Import-tank BOG reliq, NH₃ cargo", '=IF(Dn_Tank="Yes",Ship_CargoN*(1-(1-Dn_BorN/100)^Dn_Hold)*Dn_SecN,0)', "kWh", "", "int")
    sh.row("Dn_kN", "NH₃ energy content", "=Ship_LHV_N/3.6", "kWh/kg NH₃", "", "d3")
    sh.row("Dn_H2L", "H₂ in LH₂ cargo", "=Ship_CargoL", "kg", "", "int")
    sh.row("Dn_H2NG", "H₂ from NH₃ cargo, NG-fired", "=Ship_CargoN/Dn_FeedNG", "kg", "= cargo ÷ feed", "int")
    sh.row("Dn_H2CL", "H₂ from NH₃ cargo, clean fuel", "=Ship_CargoN/Dn_FeedCl", "kg", "= cargo ÷ feed", "int")
    sh.row("Dn_TotL", "Regas per cargo", "=Dn_RegasPerKg*Ship_CargoL", "kWh", "", "int")
    sh.row("Dn_TotNG", "Cracker per cargo, NG-fired", "=(Dn_FeedNG-Dn_Stoich)*Dn_H2NG*Dn_kN+(Dn_FeedCl-Dn_FeedNG)*Dn_H2NG*Dn_kN+Dn_Elec*Dn_H2NG+Dn_TankN", "kWh", "NH₃ burned + NG (NH₃-eq) + power + tank", "int")
    sh.row("Dn_TotCL", "Cracker per cargo, clean fuel", "=(Dn_FeedCl-Dn_Stoich)*Dn_H2CL*Dn_kN+Dn_Elec*Dn_H2CL+Dn_TankN", "kWh", "NH₃ burned + power + tank", "int")
    sh.row("Dn_Unit", "Chart unit", '=IF(Dn_Basis="Per kg H2 (kWh)","kWh/kg H2","MWh")', "", "", "txt")
    sh.row("Dn_DivRg", "Divisor, regas", '=IF(Dn_Basis="Per kg H2 (kWh)",Dn_H2L,1000)', "", "", "int")
    sh.row("Dn_DivNG", "Divisor, cracker NG", '=IF(Dn_Basis="Per kg H2 (kWh)",Dn_H2NG,1000)', "", "", "int")
    sh.row("Dn_DivCL", "Divisor, cracker clean", '=IF(Dn_Basis="Per kg H2 (kWh)",Dn_H2CL,1000)', "", "", "int")
    sh.row("Dn_VRg", "Regas on chart basis", "=Dn_TotL/Dn_DivRg", "=Dn_Unit", "", "d3")
    sh.row("Dn_VNG", "Cracker NG-fired on chart basis", "=Dn_TotNG/Dn_DivNG", "=Dn_Unit", "", "d2")
    sh.row("Dn_VCL", "Cracker clean fuel on chart basis", "=Dn_TotCL/Dn_DivCL", "=Dn_Unit", "", "d2")
    sh.r += 1
    sh.headline("Dn_T5", '="Cracking takes about "&TEXT(Dn_VNG/Dn_VRg,"0")&"× the energy of regas"&IF(Dn_Basis="Per kg H2 (kWh)"," per kg H2"," per cargo")')
    sh.headline("Dn_T6", '="LH2 regas needs "&TEXT(Dn_VRg,IF(Dn_VRg<0.1,"0.000",IF(Dn_VRg<100,"0.0","#,##0")))&" "&Dn_Unit&", all of it electricity"')
    sh.headline("Dn_X5", '=IF(Dn_Basis="Per kg H2 (kWh)","Energy, kWh per kg H2 delivered","Energy per 40,000 m3 cargo, MWh")')
    sh.headline("Dn_X6", '=IF(Dn_Basis="Per kg H2 (kWh)","kWh per kg H2","MWh per cargo")')
    sh.headline("Dn_Mode", '="Why the two cracker bars differ per cargo: per kg H2 both modes fire the same "&TEXT(Dn_FeedCl-Dn_Stoich,"0.0")&" kg NH3-eq = "&TEXT((Dn_FeedCl-Dn_Stoich)*Ship_LHV_N,"0.0")&" MJ. The clean-fuel mode burns more of the cargo itself, so the same "&TEXT(Ship_CargoN/1000,"#,##0")&" t NH3 yields "&TEXT(Dn_H2CL/1000,"#,##0")&" t H2 instead of "&TEXT(Dn_H2NG/1000,"#,##0")&" t. The gap is the feed-rate ratio "&TEXT(Dn_FeedCl/Dn_FeedNG,"0.000")&", not an efficiency gain."')
    sh.r += 1

    # ---- cracker check table ----
    sh.sec("Check · user's cracker fuel table", 12)
    t0 = sh.r
    r1, r2, r3 = t0 + 2, t0 + 3, t0 + 4
    rows = [["Natural gas · (feed clean − feed NG) × H₂", "=(Dn_FeedCl-Dn_FeedNG)*Dn_Annual*1000", 70e6, f"=C{r1}*Ship_LHV_N", 1302e6, f"=E{r1}/1055.056", 1234057.72, f"=E{r1}/3600", 361666.67],
            ["Ammonia · (feed NG − stoich) × H₂", "=(Dn_FeedNG-Dn_Stoich)*Dn_Annual*1000", 90e6, f"=C{r2}*Ship_LHV_N", 1674e6, f"=E{r2}/1055.056", "–", f"=E{r2}/3600", 465000],
            ["Electricity · kWh × H₂", "–", "–", "=Dn_Elec*Dn_Annual*1000*3.6", "–", f"=E{r3}/1055.056", "–", "=Dn_Elec*Dn_Annual*1000/1000", "–"]]
    end = sh.table(t0, ["Cracking fuel", "kg NH₃(-eq)/y", "User", "MJ/y", "User", "MMBtu/y", "User", "MWh/y", "User"], rows,
                   ["gen", "int", "int", "int", "int", "d2", "d2", "d2", "d2"])
    sh.put(end, 1, f'=IF(AND(ABS(C{r1}-D{r1})<1,ABS(C{r2}-D{r2})<1,Ship_LHV_N=18.6),"Verified: the user table reproduces exactly on a "&TEXT(Dn_Annual,"#,##0")&" t/y H2 basis (MMBtu uses 1,055.056 MJ/MMBtu). Both modes fire the same "&TEXT(Dn_FeedCl-Dn_Stoich,"0.0")&" kg NH3-eq/kg H2 = "&TEXT((Dn_FeedCl-Dn_Stoich)*Ship_LHV_N,"0.0")&" MJ/kg H2.","Inputs differ from the user table basis, so the User columns no longer apply.")',
           f(bold=True, font_color=LEAD))
    sh.r = end + 2
    sh.sec("Regas energy build-up (per kg LH₂ and per cargo)", 12)
    t0 = sh.r
    end = sh.table(t0, ["Component", "kWh/kg LH₂", "MWh per cargo"],
                   [["LH₂ send-out pump", "=Dn_PumpL", "=Dn_PumpL*Ship_CargoL/1000"], ["Seawater pump", "=Dn_PumpSW", "=Dn_PumpSW*Ship_CargoL/1000"],
                    ["Import-tank BOG reliq", "=Dn_TankL", "=Dn_TankL*Ship_CargoL/1000"],
                    ["Total", f"=SUM(C{t0 + 2}:C{t0 + 4})", f"=SUM(D{t0 + 2}:D{t0 + 4})"]], ["gen", "d4", "d1"], total_last=True)
    sh.r = end + 2

    # ---- chart data ----
    sh.sec("Chart data · chart 5 (three bars) and chart 6 (regas zoom)", 14)
    seg5 = ["NH₃ burned as fuel", "Natural gas (NH₃-eq)", "Cracker electricity", "LH₂ send-out pump", "Seawater pump", "Import-tank BOG reliq"]
    col5 = [C2, C3, C1, C4, C5, C6]
    vNG = ["=(Dn_FeedNG-Dn_Stoich)*Dn_H2NG*Dn_kN/Dn_DivNG", "=(Dn_FeedCl-Dn_FeedNG)*Dn_H2NG*Dn_kN/Dn_DivNG", "=Dn_Elec*Dn_H2NG/Dn_DivNG", "=0", "=0", "=Dn_TankN/Dn_DivNG"]
    vCL = ["=(Dn_FeedCl-Dn_Stoich)*Dn_H2CL*Dn_kN/Dn_DivCL", "=0", "=Dn_Elec*Dn_H2CL/Dn_DivCL", "=0", "=0", "=Dn_TankN/Dn_DivCL"]
    vRg = ["=0", "=0", "=0", "=Dn_PumpL*Dn_H2L/Dn_DivRg", "=Dn_PumpSW*Dn_H2L/Dn_DivRg", "=Dn_TankL*Dn_H2L/Dn_DivRg"]
    b5 = BarBlock(sh, sh.r, ["LH₂ regas (ORV)", "NH₃ cracker · NG-fired", "NH₃ cracker · clean fuel"], seg5, col5, [vRg, vNG, vCL], "Dn_Unit")
    sh.r = b5.end + 2
    b6 = BarBlock(sh, sh.r, ["LH₂ regas (ORV)"], seg5[3:], col5[3:], [vRg[3:]], "Dn_Unit")
    sh.r = b6.end + 2

    n = lambda nm: "=" + sh.a(*sh.bk.names[nm])  # noqa: E731
    sh.place(b5.chart(n("Dn_T5"), n("Dn_X5"), 640, 290), 7, 640, 290)
    sh.place(b6.chart(n("Dn_T6"), n("Dn_X6"), 640, 190), 7 + 13, 640, 190)
    ws.merge_range(7 + 13 + 9, CH_COL, 7 + 13 + 12, CH_COL + 6, "", f(text_wrap=True, valign="top"))
    sh.put(7 + 13 + 9, CH_COL, "=Dn_Mode", f(text_wrap=True, valign="top", bg_color="#FDF0DA", font_size=8))
    sh.chart_bottom = max(sh.chart_bottom, 7 + 13 + 14)

    sh.r = max(sh.r, sh.chart_bottom)
    sh.sec("Method, assumptions and gaps", 12)
    for t in [
        "The ORV heat is free: the 3.8 MJ/kg regas duty comes from ambient seawater; the only purchased energy is the pumps for LH₂ and seawater (kawasaki-2026-questionnaire). Pump settings (30 barg, 70 %, ΔT 5 K, 20 m, 75 %) are first-principles repo assumptions that reproduce the 0.031 kWh/kg ORV figure [ASSUMPTION].",
        "Not included: seawater electro-chlorination, lighting and control power, cold-energy recovery [ESTIMATE – needs source]; they are small next to the pumps.",
        "Cracker firing modes: NG-fired burns (6.5 − 5.6) = 0.9 kg NH₃/kg H₂ as PSA tail gas and 0.7 kg NH₃-eq as natural gas. Clean-fuel fires 1.6 kg NH₃/kg H₂ with no gas. Fired energy per kg H₂ is the same by construction (1.6 × 18.6 = 29.8 MJ).",
        "Thermodynamic sanity check: minimum cracking heat 15.2 MJ/kg H₂ (45.9 kJ/mol NH₃, repo, needs source) ⇒ ~51 % of fired heat goes into the reaction: plausible.",
        "Mixed energy quality: cracker bars add fuel (LHV) to electricity; regas is electricity only. Quantity of energy, not primary energy.",
        "Same send-out pressure assumed for both routes; no extra H₂ compression [ASSUMPTION].",
        "Each bar is one full 40,000 m³ cargo before voyage losses. Stoichiometry 5.6 rounds the exact 5.632 (2 × 17.031 ÷ (3 × 2.016)).",
        "Sources: user inputs (2026-09-24); kawasaki-2026-questionnaire (ORV, 3.8 MJ/kg); kawasaki-2026-supplemental (BOR 0.1 %/day); data/carriers/chain-energy-defaults.csv.",
    ]:
        sh.note("• " + t)


def build_chain(sh: Sh):
    bk, ws, f = sh.bk, sh.ws, sh.bk.fmt
    sh.banner("Full Chain · End-to-End Energy",
              "Full chain · GH₂ at battery limit → gaseous H₂ at send-out",
              "Total energy to move hydrogen from the export plant to gaseous H₂ at the import terminal, for one 40,000 m³ cargo. "
              "Every number is pulled live from the Upstream, Midstream and Downstream sheets.",
              "Upstream + Midstream + Downstream, electrolysis optional (set on Upstream)", "one cargo, or per kg H₂ delivered",
              "MWh; fuels and H₂ burned on LHV, electricity as delivered kWh")
    sh.sec("Key results (per kg H₂ delivered)")
    for lbl, nmv, d in [("LH₂ chain", "L", ""), ("NH₃ chain · NG-fired cracker", "G", ""), ("NH₃ chain · clean-fuel cracker", "C", "")]:
        sh.row(None, lbl, f"=Ch_Tot_{nmv}/Ch_Del_{nmv}", "kWh/kg H₂", f'=TEXT(Ch_Del_{nmv}/1000,"#,##0")&" t H2 delivered · "&TEXT(Ch_Tot_{nmv}/Ch_Del_{nmv}/(Ship_LHV_H2/3.6)*100,"0")&" % of its LHV"', "d2", "key")
    sh.row(None, "LH₂ vs NH₃ (NG-fired)", "=(Ch_Tot_L/Ch_Del_L)/(Ch_Tot_G/Ch_Del_G)", "×", "per kg H₂ delivered", "d2", "key")
    sh.r += 1
    sh.sec("Inputs · voyage")
    sh.row("Ch_Days", "Sea days charged per cargo", 20, "days", "[ASSUMPTION] laden leg · no corridor fixed", "int", "input")
    sh.row("Ch_Ballast", "Also charge the ballast leg (same days, VLSFO only)", "No", "", "dropdown", "txt", "input", dv=YES_NO)
    sh.sec("Inputs · NH₃ vessel fuel")
    sh.row("Ch_Fuel", "NH₃ vessel fuel", F_DF, "", "dropdown · shared with Annual Energy and Energy Cost", "txt", "input", dv=[F_DF, F_VL])
    sh.row("Ch_Src", "Ammonia fuel taken from", SRC[0], "", "dropdown · applies to dual fuel only", "txt", "input", dv=SRC)
    sh.sec("Electrolysis (set on Upstream)")
    sh.row(None, "Include electrolysis", "=Up_ElzOn", "", "Upstream", "txt", "link")
    sh.row(None, "Electrolyser SEC", "=Up_ElzSec", "kWh/kg H₂", "Upstream", "int", "link")
    sh.sec("Chart basis")
    sh.row("Ch_Basis", "Show", B_CH[0], "", "dropdown", "txt", "input", dv=B_CH)
    sh.r += 1

    sh.sec("Model · voyage and fuel", 12)
    sh.row("Ch_DF", "Dual fuel? (1 = yes)", f'=IF(Ch_Fuel="{F_DF}",1,0)', "", "", "int")
    sh.row("Ch_FromCargo", "Ammonia fuel from cargo? (1 = yes)", '=IF(AND(Ch_DF=1,Ch_Src="Cargo"),1,0)', "", "", "int")
    sh.row("Ch_Ball", "Ballast leg charged? (1 = yes)", '=IF(Ch_Ballast="Yes",1,0)', "", "", "int")
    sh.row("Ch_BogKg", "LH₂ boil-off over voyage", "=Ship_BOG*Ch_Days", "kg", "", "int")
    sh.row("Ch_BurnedKg", "…of which burned in engine", "=Ship_Burned*Ch_Days", "kg", "", "int")
    sh.row("Ch_SurplusKg", "…of which surplus to GCU / vent", "=Ship_Surplus*Ch_Days", "kg", "", "int")
    sh.row("Ch_VlsfoL_t", "LH₂ ship VLSFO bought", "=Ship_Vlsfo*Ch_Days+Ch_Ball*Ship_Duty_L*Ch_Days", "t", "", "d1")
    sh.row("Ch_NH3FuelT", "NH₃ ship ammonia fuel", "=Ch_DF*Ship_NH3Fuel*Ch_Days", "t NH₃", "", "d1")
    sh.row("Ch_VlsfoN_t", "NH₃ ship VLSFO (pilot or all)", "=IF(Ch_DF=1,Ship_PilotN*Ch_Days,Ship_Duty_N*Ch_Days)+Ch_Ball*Ship_Duty_N*Ch_Days", "t", "", "d1")
    sh.row("Ch_ArrN", "NH₃ cargo arriving", "=Ship_CargoN-Ch_FromCargo*Ch_NH3FuelT*1000", "kg", "", "int")
    sh.row("Ch_Sc", "Arriving ÷ loaded", "=Ch_ArrN/Ship_CargoN", "", "", "d4")
    sh.row("Ch_DelL", "LH₂ delivered", "=Ship_CargoL-Ch_BogKg", "kg", "cargo − voyage boil-off", "int")
    sh.row("Ch_Unit", "Chart unit", f'=IF(Ch_Basis="{B_CH[0]}","kWh/kg H2","MWh")', "", "", "txt")
    sh.r += 1

    sh.sec("Energy ledger per cargo, kWh", 12)
    t0 = sh.r
    kV, kH, kN = "(Ship_LHV_VLSFO/3.6)", "(Ship_LHV_H2/3.6)", "(Ship_LHV_N/3.6)"
    ledger = [
        ["Electrolysis", "=Up_ElzL", "=Up_ElzN", "=Up_ElzN"],
        ["Liquefaction / Haber-Bosch", "=Up_Liq", "=Up_HB", "=Up_HB"],
        ["Export-tank BOG reliq", "=Up_RlL", "=Up_RlN", "=Up_RlN"],
        ["Ship fuel bought (VLSFO / NH₃ + pilot)", f"=Ch_VlsfoL_t*1000*{kV}", f"=Ch_VlsfoN_t*1000*{kV}+(1-Ch_FromCargo)*Ch_NH3FuelT*1000*{kN}",
         f"=Ch_VlsfoN_t*1000*{kV}+(1-Ch_FromCargo)*Ch_NH3FuelT*1000*{kN}"],
        ["Cargo burned as ship fuel (H₂ or NH₃)", f"=Ch_BogKg*{kH}", f"=Ch_FromCargo*Ch_NH3FuelT*1000*{kN}", f"=Ch_FromCargo*Ch_NH3FuelT*1000*{kN}"],
        ["Regas / cracking (incl. import tank)", "=Dn_RegasPerKg*Ch_DelL", "=Dn_TotNG*Ch_Sc", "=Dn_TotCL*Ch_Sc"],
        ["Total", f"=SUM(C{t0 + 2}:C{t0 + 7})", f"=SUM(D{t0 + 2}:D{t0 + 7})", f"=SUM(E{t0 + 2}:E{t0 + 7})"],
        ["H₂ delivered, kg", "=Ch_DelL", "=Dn_H2NG*Ch_Sc", "=Dn_H2CL*Ch_Sc"],
        ["H₂ into the plant, kg", "=Ship_CargoL", "=Up_H2N", "=Up_H2N"],
        ["Energy per kg H₂ delivered, kWh/kg", "=Ch_Tot_L/Ch_Del_L", "=Ch_Tot_G/Ch_Del_G", "=Ch_Tot_C/Ch_Del_C"],
    ]
    end = sh.table(t0, ["Line item", "LH₂ chain", "NH₃ · NG-fired", "NH₃ · clean fuel"], ledger, ["gen", "int", "int", "int"])
    for i, key in enumerate(["El", "Liq", "Rl", "Ship", "Cargo", "Down", "Tot", "Del", "Hin"]):
        for j, ch in enumerate(["L", "G", "C"]):
            sh.nm(f"Ch_{key}_{ch}", t0 + 1 + i, 2 + j)
    bk.wb.define_name("Ch_PerKg", f"={sh.a(t0 + 10, 2)}:{xl_rowcol_to_cell(t0 + 10, 4, True, True)}")
    for j in range(4):
        sh.put(t0 + 10, 1 + j, ledger[9][j], f(bold=True, num_format=NF["d3"] if j else NF["gen"], align="left" if j == 0 else "right", bottom=1, bottom_color=GRID))
    # total row styling
    for j in range(4):
        sh.put(t0 + 7, 1 + j, ledger[6][j], f(bold=True, bg_color=ACCENT, font_color=ACC_FG, num_format=NF["int"], align="left" if j == 0 else "right"))
    sh.r = end + 1

    sh.sec("Hydrogen mass balance · one cargo", 12)
    t1 = sh.r
    mb = [["LH₂", "=Ship_CargoL/1000", "=Ship_CargoL/1000", "=Ch_BogKg/1000", "–", "=Ch_Del_L/1000", "=Ch_Del_L/Ch_Hin_L"],
          ["NH₃ · NG-fired", "=Up_H2N/1000", "=Ship_CargoN/Up_Stoich/1000", "=Ch_FromCargo*Ch_NH3FuelT/Up_Stoich", f"=(Ch_ArrN/Up_Stoich-Ch_Del_G)/1000", "=Ch_Del_G/1000", "=Ch_Del_G/Ch_Hin_G"],
          ["NH₃ · clean fuel", "=Up_H2N/1000", "=Ship_CargoN/Up_Stoich/1000", "=Ch_FromCargo*Ch_NH3FuelT/Up_Stoich", f"=(Ch_ArrN/Up_Stoich-Ch_Del_C)/1000", "=Ch_Del_C/1000", "=Ch_Del_C/Ch_Hin_C"]]
    end = sh.table(t1, ["Chain", "H₂ into plant, t", "H₂ in cargo loaded, t", "Burned as ship fuel, t H₂(-eq)", "Burned in cracker, t H₂-eq", "H₂ delivered, t", "Delivered ÷ H₂ in"],
                   mb, ["gen", "int", "int", "int", "int", "int", "pct"])
    sh.put(end, 1, '="LH2 surplus boil-off sent to GCU / vent over the voyage: "&TEXT(Ch_SurplusKg/1000,"#,##0")&" t (counted as burned)."', f(italic=True, font_color=MUTED, font_size=8))
    sh.r = end + 2

    sh.sec("Line items · MWh and kWh per kg H₂ delivered", 12)
    t2 = sh.r
    names = ["Electrolysis", "Liquefaction / Haber-Bosch", "Export-tank BOG reliq", "Ship fuel bought", "Cargo burned as ship fuel (H₂ or NH₃)", "Regas / cracking"]
    keys = ["El", "Liq", "Rl", "Ship", "Cargo", "Down"]
    rows = [[names[i]] + sum([[f"=Ch_{keys[i]}_{c}/1000", f"=Ch_{keys[i]}_{c}/Ch_Del_{c}"] for c in "LGC"], []) for i in range(6)]
    rows.append(["Total"] + sum([[f"=Ch_Tot_{c}/1000", f"=Ch_Tot_{c}/Ch_Del_{c}"] for c in "LGC"], []))
    end = sh.table(t2, ["Line item", "LH₂, MWh", "kWh/kg", "NH₃ NG-fired, MWh", "kWh/kg", "NH₃ clean fuel, MWh", "kWh/kg"], rows,
                   ["gen", "int", "d3", "int", "d3", "int", "d3"], total_last=True)
    sh.r = end + 1
    sh.sec("Stage totals per cargo, kWh (feeds charts 8, 9, 13–14)", 12)
    t3 = sh.r
    stg = [["Electrolysis", "=Ch_El_L", "=Ch_El_G", "=Ch_El_C"],
           ["Upstream (liquefaction / Haber-Bosch + tank)", "=Ch_Liq_L+Ch_Rl_L", "=Ch_Liq_G+Ch_Rl_G", "=Ch_Liq_C+Ch_Rl_C"],
           ["Shipping fuel", "=Ch_Ship_L", "=Ch_Ship_G", "=Ch_Ship_C"],
           ["Shipping: cargo burned as fuel", "=Ch_Cargo_L", "=Ch_Cargo_G", "=Ch_Cargo_C"],
           ["Downstream (regas / cracking)", "=Ch_Down_L", "=Ch_Down_G", "=Ch_Down_C"]]
    end = sh.table(t3, ["Stage", "LH₂ chain", "NH₃ · NG-fired", "NH₃ · clean fuel"], stg, ["gen", "int", "int", "int"])
    for i, k in enumerate(["El", "Up", "Sh", "ShH", "Dn"]):
        for j, c in enumerate("LGC"):
            sh.nm(f"Stg_{k}_{c}", t3 + 1 + i, 2 + j)
    sh.r = end + 1
    sh.headline("Ch_Best", '=INDEX({"LH2","NH3 with NG-fired cracker","NH3 with clean-fuel cracker"},MATCH(MIN(Ch_PerKg),Ch_PerKg,0))')
    sh.headline("Ch_T8", f'=IF(Ch_Basis="{B_CH[0]}","End to end, the "&Ch_Best&" uses the least energy per kg H2 delivered","End-to-end energy per 40,000 m3 cargo")')
    sh.headline("Ch_X8", f'=IF(Ch_Basis="{B_CH[0]}","Energy, kWh per kg H2 delivered","Energy per 40,000 m3 cargo, MWh")')
    sh.r += 1

    sh.sec("Chart data · chart 8", 14)
    dv = f'IF(Ch_Basis="{B_CH[0]}",{{d}},1000)'
    stages = ["Electrolysis", "Upstream (liquefaction / Haber-Bosch + tank)", "Shipping fuel", "Shipping: cargo burned as fuel", "Downstream (regas / cracking)"]
    cols = [C5, C1, C2, C4, C3]
    vals = [[f"=Stg_{k}_{c}/" + dv.replace("{d}", f"Ch_Del_{c}") for k in ["El", "Up", "Sh", "ShH", "Dn"]] for c in "LGC"]
    bb = BarBlock(sh, sh.r, ["LH₂ chain", "NH₃ chain · NG-fired cracker", "NH₃ chain · clean-fuel cracker"], stages, cols, vals, "Ch_Unit")
    sh.r = bb.end + 2
    n = lambda nm: "=" + sh.a(*sh.bk.names[nm])  # noqa: E731
    sh.place(bb.chart(n("Ch_T8"), n("Ch_X8"), 700, 300), 7, 700, 300)
    sh.chart_bottom = max(sh.chart_bottom, 7 + 14)
    sh.r = max(sh.r, sh.chart_bottom)
    sh.sec("Method, assumptions and gaps", 12)
    for t in [
        "Per kg H₂ delivered divides total chain energy by the gaseous H₂ leaving the import terminal. LH₂: cargo less voyage boil-off. NH₃: cargo ÷ cracker feed rate (6.5 or 7.2 kg NH₃/kg H₂).",
        "Voyage: sea days × the Midstream daily figures, linear in days. Twenty laden days is a placeholder [ASSUMPTION]; no corridor fixed yet. Ballast leg off by default; when on, each ship burns its full daily demand as VLSFO for the same days, heel boil-off ignored [ASSUMPTION].",
        "Hydrogen burned on the LH₂ ship counts as energy used (120 MJ/kg), whether engine or, above the crossover rate, GCU.",
        "NH₃ vessel fuel is selectable. Dual fuel burns the Midstream NH₃ share (95 %) of the 30 t/d VLSFO-eq demand as ammonia, rest VLSFO pilot; VLSFO only burns it all as VLSFO. Default: ammonia fuel bunkered separately and cargo arrives whole [ASSUMPTION]. 'Cargo' moves that energy into 'cargo burned' and lowers H₂ delivered per cargo.",
        "Downstream is charged on the delivered cargo, so regas is slightly lower here than on the Downstream sheet (full cargo).",
        "Energy quality is mixed: electricity, fuel heat and burned hydrogen are added on an LHV basis. Quantity of energy, not primary energy or exergy.",
        "Electrolysis (Upstream dropdown): charges the H₂ each chain consumes; penalises the route losing more H₂ per kg delivered. 60 kWh/kg is a placeholder [ASSUMPTION].",
        "All Upstream, Midstream and Downstream caveats carry over (notably the Haber-Bosch 1 kWh/kg H₂ ASU question and placeholder reliq/storage values).",
    ]:
        sh.note("• " + t)


def build_annual(sh: Sh):
    bk, ws, f = sh.bk, sh.ws, sh.bk.fmt
    sh.banner("Annual Energy · Annual Supply Case",
              "Case study · contracted annual delivery",
              "What it takes, in energy, cargoes, ships and plant size, to deliver a contracted annual volume of gaseous H₂ by each chain. "
              "Per-kg results come live from the Full Chain sheet.",
              "same as Full Chain: GH₂ at battery limit → gaseous H₂ at send-out", "per year, at the contracted delivered volume",
              "GWh/y; average MW = GWh/y ÷ 8.76")
    sh.sec("Inputs · contract and fleet")
    sh.row("An_Target", "H₂ delivered", 100, "ktpa", "user · default 100", "int", "input")
    sh.row("An_Port", "Port days per call", 1.25, "days", "KHI 1–1.5 midpoint (kawasaki-2026-questionnaire)", "d2", "input")
    sh.row("An_Avail", "Fleet availability", 90, "%", "repo [ASSUMPTION] (chain-energy-defaults.csv)", "int", "input")
    sh.sec("Linked from Full Chain")
    sh.row(None, "Sea days", "=Ch_Days", "days", "Full Chain", "int", "link")
    sh.row(None, "Ballast charged", "=Ch_Ballast", "", "Full Chain", "txt", "link")
    sh.row(None, "NH₃ vessel fuel", "=Ch_Fuel", "", "Full Chain", "txt", "link")
    sh.row(None, "Ammonia fuel taken from", "=Ch_Src", "", "Full Chain", "txt", "link")
    sh.row(None, "Electrolysis included", "=Up_ElzOn", "", "Upstream", "txt", "link")
    sh.r += 1
    sh.sec("Key results")
    for lbl, c in [("LH₂ chain", "L"), ("NH₃ chain · NG-fired cracker", "G"), ("NH₃ chain · clean-fuel cracker", "C")]:
        sh.row(None, lbl, f"=An_E_{c}", "GWh/y", f'="≈ "&TEXT(An_E_{c}/8.76,"#,##0")&" MW average, around the clock"', "int", "key")
    sh.row(None, "LH₂ minus NH₃ (NG-fired)", "=An_E_L-An_E_G", "GWh/y", '=TEXT(An_E_L/An_E_G,"0.00")&"× on the same delivered H2"', "int", "key")
    sh.r += 1

    sh.sec("Model", 12)
    sh.row("An_T", "Contracted H₂ delivered", "=An_Target*1000000", "kg/y", "", "int")
    sh.row("An_RT", "Round trip", "=2*Ch_Days+2*An_Port", "days", "= 2 × sea + 2 × port (ballast leg assumed as long as laden)", "d2")
    sh.row("An_VPS", "Voyages per ship per year", "=IF(An_RT>0,365*An_Avail/100/An_RT,0)", "1/y", "= 365 × availability ÷ round trip", "d2")
    sh.r += 1
    sh.sec("Logistics · what the contract needs", 12)
    t0 = sh.r
    rows = []
    for i, (lbl, c, prod, what) in enumerate([("LH₂", "L", "Ship_CargoL", "LH₂"), ("NH₃ · NG-fired", "G", "Ship_CargoN", "NH₃"), ("NH₃ · clean fuel", "C", "Ship_CargoN", "NH₃")]):
        r = t0 + 2 + i
        rows.append([lbl, f"=Ch_Del_{c}/1000", f"=An_T/Ch_Del_{c}", f"=IF(An_VPS>0,ROUNDUP(D{r}/An_VPS-0.000000001,0),0)", f"=IF(An_VPS>0,D{r}/An_VPS,0)",
                     f"=An_T*Ch_Hin_{c}/Ch_Del_{c}/1000000", f"=D{r}*{prod}/1000000", f"=D{r}*{prod}/1000/365", what])
    end = sh.table(t0, ["Chain", "H₂ delivered per cargo, t", "Cargoes per year", "Ships needed", "Ships (unrounded)", "H₂ into plant, ktpa", "Plant output, ktpa", "Plant output, t/day", "Product"],
                   rows, ["gen", "int", "d1", "int", "d2", "d1", "d1", "int", "gen"])
    sh.r = end
    sh.headline("An_TLog", '="Round trip "&TEXT(An_RT,"0.0")&" days (2 × "&TEXT(Ch_Days,"0")&" sea + 2 × "&TEXT(An_Port,"0.00")&" port). Each ship makes "&TEXT(An_VPS,"0.00")&" voyages a year at "&TEXT(An_Avail,"0")&" % availability."')
    sh.r = end + 1
    sh.sec("Annual energy by line item", 12)
    t1 = sh.r
    names = ["Electrolysis", "Liquefaction / Haber-Bosch", "Export-tank BOG reliq", "Ship fuel bought", "Cargo burned as ship fuel (H₂ or NH₃)", "Regas / cracking"]
    keys = ["El", "Liq", "Rl", "Ship", "Cargo", "Down"]
    rows = [[names[i]] + sum([[f"=Ch_{keys[i]}_{c}/Ch_Del_{c}*An_T/1000000", f"=({xl_rowcol_to_cell(t1 + 1 + i, 2 + 2 * j)})/8.76"] for j, c in enumerate("LGC")], []) for i in range(6)]
    rows.append(["Total"] + sum([[f"=SUM({xl_rowcol_to_cell(t1 + 1, 2 + 2 * j)}:{xl_rowcol_to_cell(t1 + 6, 2 + 2 * j)})", f"={xl_rowcol_to_cell(t1 + 7, 2 + 2 * j)}/8.76"] for j in range(3)], []))
    end = sh.table(t1, ["Line item", "LH₂, GWh/y", "MW avg", "NH₃ NG-fired, GWh/y", "MW avg", "NH₃ clean fuel, GWh/y", "MW avg"], rows,
                   ["gen", "d1", "d1", "d1", "d1", "d1", "d1"], total_last=True)
    for j, c in enumerate("LGC"):
        sh.nm(f"An_E_{c}", t1 + 7, 2 + 2 * j)       # total, GWh/y
    sh.r = end + 1
    sh.sec("Ship fuel burned per year", 12)
    t2 = sh.r
    rows = [["LH₂", f"=Ch_VlsfoL_t*D{t0 + 2}", "–", f"=Ch_BogKg/1000*D{t0 + 2}", "–"],
            ["NH₃ · NG-fired", f"=Ch_VlsfoN_t*D{t0 + 3}", f"=IF(Ch_NH3FuelT>0,Ch_NH3FuelT*D{t0 + 3},0)", "–", '=IF(Ch_DF=1,IF(Ch_FromCargo=1,"cargo","bunkers"),"–")'],
            ["NH₃ · clean fuel", f"=Ch_VlsfoN_t*D{t0 + 4}", f"=IF(Ch_NH3FuelT>0,Ch_NH3FuelT*D{t0 + 4},0)", "–", '=IF(Ch_DF=1,IF(Ch_FromCargo=1,"cargo","bunkers"),"–")']]
    end = sh.table(t2, ["Chain", "VLSFO, t/y", "NH₃ fuel, t/y", "H₂ burned, t/y", "NH₃ fuel from"], rows, ["gen", "int", "int", "int", "gen"])
    sh.r = end + 2

    # fix key results: An_E_* is GWh already in table; key rows divided by 1e6 above -> correct formulas
    sh.sec("Stage totals, GWh per year (chart 9)", 12)
    t3 = sh.r
    stg_names = ["Electrolysis", "Upstream (liquefaction / Haber-Bosch + tank)", "Shipping fuel", "Shipping: cargo burned as fuel", "Downstream (regas / cracking)"]
    stg = [[stg_names[i]] + [f"=Stg_{k}_{c}/Ch_Del_{c}*An_T/1000000" for c in "LGC"] for i, k in enumerate(["El", "Up", "Sh", "ShH", "Dn"])]
    stg.append(["Total, GWh/y", "=An_E_L", "=An_E_G", "=An_E_C"])
    end = sh.table(t3, ["Stage", "LH₂ chain", "NH₃ · NG-fired", "NH₃ · clean fuel"], stg, ["gen", "d1", "d1", "d1"], total_last=True)
    bk.wb.define_name("An_Es", f"={sh.a(t3 + 6, 2)}:{xl_rowcol_to_cell(t3 + 6, 4, True, True)}")
    sh.r = end + 1
    sh.headline("An_T9", '=INDEX({"LH2","NH3 NG-fired","NH3 clean fuel"},MATCH(MIN(An_Es),An_Es,0))&" needs the least: "&TEXT(MIN(An_Es),"#,##0")&" GWh/y, "&TEXT(MAX(An_Es)-MIN(An_Es),"#,##0")&" GWh/y less than the worst chain"')
    sh.headline("An_X9", '="Energy, GWh per year at "&TEXT(An_Target,"#,##0")&" ktpa delivered"')
    sh.headline("An_Unit", '="GWh/y"')
    sh.r += 1
    sh.sec("Chart data · chart 9", 14)
    vals = [[f"=Stg_{k}_{c}/Ch_Del_{c}*An_T/1000000" for k in ["El", "Up", "Sh", "ShH", "Dn"]] for c in "LGC"]
    bb = BarBlock(sh, sh.r, ["LH₂ chain", "NH₃ chain · NG-fired cracker", "NH₃ chain · clean-fuel cracker"], stg_names, [C5, C1, C2, C4, C3], vals, "An_Unit")
    sh.r = bb.end + 2
    n = lambda nm: "=" + sh.a(*sh.bk.names[nm])  # noqa: E731
    sh.place(bb.chart(n("An_T9"), n("An_X9"), 700, 300), 7, 700, 300)
    sh.chart_bottom = max(sh.chart_bottom, 7 + 14)
    sh.r = max(sh.r, sh.chart_bottom)
    sh.sec("Method, assumptions and gaps", 12)
    for t in [
        "Scaling: annual energy = Full Chain energy per kg H₂ delivered × contracted volume. Cargoes per year = contract ÷ H₂ delivered per cargo, kept fractional for energy (part cargo = part of a year-round flow).",
        "Fleet: round trip = 2 × sea days + 2 × port days; ballast leg as long as laden whether or not its fuel is charged. Voyages per ship per year = 365 × availability ÷ round trip; ships = cargoes per year ÷ voyages per ship, rounded up. 40,000 m³ hull for both chains. Port days: KHI 1–1.5 midpoint (kawasaki-2026-questionnaire). Availability 90 % [ASSUMPTION].",
        "NH₃ vessel fuel: dual fuel burns 95 % of the 30 t/d VLSFO-eq demand as ammonia; VLSFO only burns it all as VLSFO. Taking ammonia from cargo shrinks the cargo reaching the cracker, lowers H₂ delivered per cargo and raises cargoes needed; the plant still makes a full cargo. Heel and boil-off not modelled.",
        "Export-tank boil-off is charged per cargo (storage days per cargo, Upstream) and scales with cargoes per year; a tank farm holding inventory all year would boil off more. Tank count not sized.",
        "Plant capacity = annual output ÷ 365 at 100 % utilisation; a real plant needs margin for availability and turndown [ASSUMPTION].",
        "CO₂ is not calculated: no sourced VLSFO emission factor is held in this repo. All Full Chain, Upstream, Midstream and Downstream caveats carry over.",
    ]:
        sh.note("• " + t)


def build_cost(sh: Sh):
    bk, ws, f = sh.bk, sh.ws, sh.bk.fmt
    sh.banner("Energy Cost · Chain Energy Cost at Origin",
              "Economic origin · energy cost per kg H₂ produced at the electrolyser (or delivered, via dropdown)",
              "The annual energy bill of each chain at the Annual Energy volume, divided by the hydrogen the electrolyser plant produces (default) "
              "or by the hydrogen delivered. Charter, CapEx and non-energy OpEx are excluded.",
              "same as Full Chain and Annual Energy", "USD per kg H₂ produced (or delivered), and USD M per year",
              "USD; prices are user inputs, no cost year stated")
    sh.sec("Inputs · energy prices")
    sh.row("Ec_Up", "Upstream electricity", 140, "USD/MWh", "user", "int", "input")
    sh.row("Ec_Dn", "Import-terminal electricity", 140, "USD/MWh", "[ASSUMPTION] placeholder = upstream · set yours", "int", "input")
    sh.row("Ec_V", "VLSFO", 553, "USD/t", "user", "int", "input")
    sh.row("Ec_NG", "Natural gas (applied on LHV)", 13, "USD/MMBtu", "user", "d1", "input")
    sh.row("Ec_N", "Ammonia", 700, "USD/t NH₃", "user", "int", "input")
    sh.row("Ec_H2", "H₂ price (cargo H₂ burned by the LH₂ ship)", 4.0, "USD/kg", "slider in artifact · between 0 and 10", "d2", "input")
    sh.row("Ec_MMBtu", "Energy per MMBtu", 1055.056, "MJ/MMBtu", "unit conversion", "d3", "input")
    sh.sec("Chart basis")
    sh.row("Ec_Basis", "Per kg of", B_EC[0], "", "dropdown · Economic Origin (produced) or Economics (delivered)", "txt", "input", dv=B_EC)
    sh.sec("Linked from other sheets")
    sh.row(None, "Annual volume delivered", "=An_Target", "ktpa", "Annual Energy", "int", "link")
    sh.row(None, "NH₃ vessel fuel", "=Ch_Fuel", "", "Full Chain", "txt", "link")
    sh.row(None, "Ammonia fuel from", "=Ch_Src", "", "Full Chain", "txt", "link")
    sh.row(None, "Electrolysis included", "=Up_ElzOn", "", "Upstream", "txt", "link")
    sh.r += 1
    sh.sec("Key results")
    for lbl, c in [("LH₂ chain", "L"), ("NH₃ · NG-fired cracker", "G"), ("NH₃ · clean-fuel cracker", "C")]:
        sh.row(None, lbl, f"=Ec_Cost_{c}", "USD/kg H₂", f'=TEXT(Ec_Cost_{c}*Ec_Q_{c}/1000000,"#,##0.0")&" USD M/y · "&TEXT(Ec_Q_{c}/1000000,"#,##0.0")&" ktpa on this basis"', "d3", "key")
    sh.row(None, "LH₂ − NH₃ (NG-fired)", "=Ec_Cost_L-Ec_Cost_G", "USD/kg", '=TEXT((Ec_Cost_L*Ec_Q_L-Ec_Cost_G*Ec_Q_G)/1000000,"#,##0.0")&" USD M/y"', "d3", "key")
    sh.row(None, "Breakeven H₂ price vs NG-fired", "=Ec_BE_G", "USD/kg", "LH₂ chain cost = NG-fired chain cost", "d2", "key")
    sh.row(None, "Breakeven H₂ price vs clean fuel", "=Ec_BE_C", "USD/kg", "LH₂ chain cost = clean-fuel chain cost", "d2", "key")
    sh.r += 1

    # ---- quantities ----
    sh.sec("Energy quantities per cargo", 12)
    t0 = sh.r
    h2G, h2C = "(Ship_CargoN/Dn_FeedNG*Ch_Sc)", "(Ship_CargoN/Dn_FeedCl*Ch_Sc)"
    q = [["Upstream electricity, MWh", "=(Ch_El_L+Ch_Liq_L+Ch_Rl_L)/1000", "=(Ch_El_G+Ch_Liq_G+Ch_Rl_G)/1000", "=(Ch_El_C+Ch_Liq_C+Ch_Rl_C)/1000", "=Ec_Up"],
         ["VLSFO, t", "=Ch_VlsfoL_t", "=Ch_VlsfoN_t", "=Ch_VlsfoN_t", "=Ec_V"],
         ["Ammonia fuel, t NH₃", "=0", f"=Ch_NH3FuelT+(Dn_FeedNG-Dn_Stoich)*{h2G}/1000", f"=Ch_NH3FuelT+(Dn_FeedCl-Dn_Stoich)*{h2C}/1000", "=Ec_N"],
         ["Natural gas, MMBtu", "=0", f"=(Dn_FeedCl-Dn_FeedNG)*{h2G}*Ship_LHV_N/Ec_MMBtu", "=0", "=Ec_NG"],
         ["Import-terminal electricity, MWh", "=Dn_RegasPerKg*Ch_DelL/1000", f"=(Dn_Elec*{h2G}+Dn_TankN*Ch_Sc)/1000", f"=(Dn_Elec*{h2C}+Dn_TankN*Ch_Sc)/1000", "=Ec_Dn"],
         ["Cargo H₂ burned, kg (priced at H₂ price)", "=Ch_BogKg", "=0", "=0", "=Ec_H2"]]
    end = sh.table(t0, ["Energy line (per cargo)", "LH₂, qty", "NH₃ NG-fired, qty", "NH₃ clean fuel, qty", "Price (USD per unit)"], q, ["gen", "d1", "d1", "d1", "d2"])
    sh.r = end + 1
    sh.sec("Cost per cargo, USD", 12)
    t1 = sh.r
    rows = []
    for i in range(6):
        rr = t0 + 2 + i
        rows.append([q[i][0].split(",")[0]] + [f"={xl_rowcol_to_cell(t0 + 1 + i, 2 + j)}*{xl_rowcol_to_cell(t0 + 1 + i, 5, False, True)}" for j in range(3)])
    rows.append(["Total, excluding cargo H₂ burned"] + [f"=SUM({xl_rowcol_to_cell(t1 + 1, 2 + j)}:{xl_rowcol_to_cell(t1 + 5, 2 + j)})" for j in range(3)])
    end = sh.table(t1, ["Line", "LH₂", "NH₃ NG-fired", "NH₃ clean fuel"], rows, ["gen", "int", "int", "int"], total_last=True)
    sh.r = end + 1
    sh.sec("Denominator and cost per kg", 12)
    t2 = sh.r
    hin = ["=Ch_Hin_L", "=Ch_Hin_G", "=Ch_Hin_C"]
    dl = ["=Ch_Del_L", "=Ch_Del_G", "=Ch_Del_C"]
    org = f'(Ec_Basis="{B_EC[0]}")'
    rows = [["H₂ produced per cargo, kg"] + hin, ["H₂ delivered per cargo, kg"] + dl,
            ["Denominator on chosen basis, kg"] + [f"=IF({org},{xl_rowcol_to_cell(t2 + 1, 2 + j)},{xl_rowcol_to_cell(t2 + 2, 2 + j)})" for j in range(3)],
            ["Annual kg on this basis"] + [f"=An_T*{xl_rowcol_to_cell(t2 + 3, 2 + j)}/{xl_rowcol_to_cell(t2 + 2, 2 + j)}" for j in range(3)],
            ["Fixed cost a, USD/kg"] + [f"={xl_rowcol_to_cell(t1 + 7, 2 + j)}/{xl_rowcol_to_cell(t2 + 3, 2 + j)}" for j in range(3)],
            ["Price slope b, kg burned H₂ per kg"] + [f"={xl_rowcol_to_cell(t0 + 6, 2 + j)}/{xl_rowcol_to_cell(t2 + 3, 2 + j)}" for j in range(3)],
            ["Energy cost at the H₂ price, USD/kg"] + [f"={xl_rowcol_to_cell(t2 + 5, 2 + j)}+{xl_rowcol_to_cell(t2 + 6, 2 + j)}*Ec_H2" for j in range(3)],
            ["Annual energy cost, USD M/y"] + [f"={xl_rowcol_to_cell(t2 + 7, 2 + j)}*{xl_rowcol_to_cell(t2 + 4, 2 + j)}/1000000" for j in range(3)]]
    end = sh.table(t2, ["Item", "LH₂", "NH₃ NG-fired", "NH₃ clean fuel"], rows, ["gen", "int", "int", "int"])
    # number formats on a/b/cost rows differ -> rewrite with decimals
    for i, nfk in [(4, "d4"), (5, "d4"), (6, "d4"), (7, "d1")]:
        for j in range(3):
            sh.put(t2 + 1 + i, 2 + j, rows[i][1 + j], f(num_format=NF[nfk], bottom=1, bottom_color=GRID, align="right"))
    for j, c in enumerate("LGC"):
        sh.nm(f"Ec_Den_{c}", t2 + 3, 2 + j)
        sh.nm(f"Ec_Q_{c}", t2 + 4, 2 + j)
        sh.nm(f"Ec_A_{c}", t2 + 5, 2 + j)
        sh.nm(f"Ec_B_{c}", t2 + 6, 2 + j)
        sh.nm(f"Ec_Cost_{c}", t2 + 7, 2 + j)
        sh.nm(f"Ec_Usd_{c}", t2 + 8, 2 + j)
    sh.r = end + 1
    sh.row("Ec_BE_G", "Breakeven H₂ price vs NG-fired", "=IF(Ec_B_L>0,(Ec_A_G-Ec_A_L)/Ec_B_L,NA())", "USD/kg", "", "d2")
    sh.row("Ec_BE_C", "Breakeven H₂ price vs clean fuel", "=IF(Ec_B_L>0,(Ec_A_C-Ec_A_L)/Ec_B_L,NA())", "USD/kg", "", "d2")
    sh.r += 1

    sh.sec("Cost lines, USD per kg on the chosen basis", 12)
    t3 = sh.r
    names = ["Upstream electricity", "VLSFO", "Ammonia fuel", "Cargo H₂ burned", "Natural gas", "Import-terminal electricity"]
    order = [0, 1, 2, 5, 3, 4]       # cost-table row order for the artifact's segment order
    rows = []
    for k, nme in enumerate(names):
        src = order[k]
        cells = []
        for j, c in enumerate("LGC"):
            if src == 5:
                cells.append(f"=Ec_B_{c}*Ec_H2")
            else:
                cells.append(f"={xl_rowcol_to_cell(t1 + 1 + src, 2 + j)}/Ec_Den_{c}")
        rows.append([nme] + cells)
    rows.append(["Total"] + [f"=SUM({xl_rowcol_to_cell(t3 + 1, 2 + j)}:{xl_rowcol_to_cell(t3 + 6, 2 + j)})" for j in range(3)])
    end = sh.table(t3, ["USD per kg H₂ (chosen basis)", "LH₂", "NH₃ NG-fired", "NH₃ clean fuel"], rows, ["gen", "d3", "d3", "d3"], total_last=True)
    sh.r = end + 1
    sh.sec("Energy intensity, kWh per kg on the chosen basis", 12)
    t4 = sh.r
    rows = [[stg_n] + [f"=Stg_{k}_{c}/Ec_Den_{c}" for c in "LGC"] for stg_n, k in
            [("Electrolysis", "El"), ("Upstream (liquefaction / Haber-Bosch + tank)", "Up"), ("Shipping fuel", "Sh"), ("Shipping: cargo burned as fuel", "ShH"), ("Downstream (regas / cracking)", "Dn")]]
    rows.append(["Total, chosen basis"] + [f"=SUM({xl_rowcol_to_cell(t4 + 1, 2 + j)}:{xl_rowcol_to_cell(t4 + 5, 2 + j)})" for j in range(3)])
    rows.append(["H₂ on this basis per cargo, t"] + [f"=Ec_Den_{c}/1000" for c in "LGC"])
    rows.append(["Reference: per kg on the other basis"] + [f"=Ch_Tot_{c}/IF({org},Ch_Del_{c},Ch_Hin_{c})" for c in "LGC"])
    end = sh.table(t4, ["kWh per kg H₂ (chosen basis)", "LH₂", "NH₃ NG-fired", "NH₃ clean fuel"], rows, ["gen", "d3", "d3", "d3"])
    sh.r = end + 1
    sh.headline("Ec_Word", f'=IF({org},"produced","delivered")')
    sh.headline("Ec_Unit", '="USD/kg"')
    sh.headline("Ec_UnitK", '="kWh/kg"')
    sh.headline("Ec_T12", f'=IF(AND(NOT(ISNUMBER(Ec_BE_G)),NOT(ISNUMBER(Ec_BE_C))),"No boil-off to price",IF(AND(Ec_BE_G<=0,Ec_BE_C<=0),"Both NH3 chains have a lower energy cost than LH2 at any H2 price",IF(Ec_BE_G<=0,"LH2 beats clean-fuel cracking below H2 USD "&TEXT(Ec_BE_C,"0.00")&"/kg, but never beats NG-fired cracking",IF(Ec_BE_C<=0,"LH2 beats NG-fired cracking below H2 USD "&TEXT(Ec_BE_G,"0.00")&"/kg, but never beats clean-fuel cracking","LH2 has the lower energy cost below H2 USD "&TEXT(Ec_BE_G,"0.00")&"/kg (vs NG-fired) and USD "&TEXT(Ec_BE_C,"0.00")&"/kg (vs clean fuel)"))))')
    sh.headline("Ec_Y12", '="Energy cost, USD/kg H2 "&Ec_Word')
    sh.headline("Ec_X13", '="Energy cost, USD per kg H2 "&Ec_Word')
    sh.headline("Ec_T13", '="Energy cost by carrier, per kg H2 "&Ec_Word')
    sh.headline("Ec_X14", '="Energy, kWh per kg H2 "&Ec_Word')
    sh.headline("Ec_T14", f'=INDEX({{"LH2","NH3 NG-fired","NH3 clean fuel"}},MATCH(MIN(Ec_TotK),Ec_TotK,0))&" uses the least energy per kg H2 "&Ec_Word&": "&TEXT(MIN(Ec_TotK),"0.00")&" kWh/kg"')
    sh.headline("Ec_L12a", '="H2 price USD "&TEXT(Ec_H2,"0.00")&"/kg"')
    sh.headline("Ec_L12b", '=IF(ISNUMBER(Ec_BE_G),IF(AND(Ec_BE_G>=0,Ec_BE_G<=10),"USD "&TEXT(Ec_BE_G,"0.00")&"/kg vs NG-fired",""),"")')
    sh.headline("Ec_L12c", '=IF(ISNUMBER(Ec_BE_C),IF(AND(Ec_BE_C>=0,Ec_BE_C<=10),"USD "&TEXT(Ec_BE_C,"0.00")&"/kg vs clean fuel",""),"")')
    sh.r += 1
    # named range for MIN over total kWh row
    bk.wb.define_name("Ec_TotK", f"={sh.a(t4 + 6, 2)}:{xl_rowcol_to_cell(t4 + 6, 4, True, True)}")

    # ---- chart data ----
    sh.sec("Chart data · chart 12 (H₂ price sweep)", 12)
    xs = frange(0, 10, 0.05, 2)
    s0, s1 = sweep(sh, sh.r, ["H₂ price, USD/kg", "LH₂ chain", "NH₃ · NG-fired", "NH₃ · clean fuel", "Slider marker", "Breakeven vs NG-fired", "Breakeven vs clean fuel"],
                   xs, ["=Ec_A_L+Ec_B_L*{x}", "=Ec_A_G", "=Ec_A_C", "=IF(ABS({x}-Ec_H2)<=0.025,C{r},NA())",
                        "=IF(ISNUMBER(Ec_BE_G),IF(ABS({x}-Ec_BE_G)<=0.025,Ec_A_G,NA()),NA())", "=IF(ISNUMBER(Ec_BE_C),IF(ABS({x}-Ec_BE_C)<=0.025,Ec_A_C,NA()),NA())"],
                   "d2", ["d3"] * 6)
    S = dict(x=rng(sh, s0, sweep.last_label[1], s1, sweep.last_label[1]), l=rng(sh, s0, 2, s1, 2), g=rng(sh, s0, 3, s1, 3), c=rng(sh, s0, 4, s1, 4), ms=rng(sh, s0, 5, s1, 5), mg=rng(sh, s0, 6, s1, 6), mc=rng(sh, s0, 7, s1, 7))
    sh.r = s1 + 3
    sh.sec("Chart data · chart 13 (cost by carrier)", 14)
    seg13 = ["Upstream electricity", "VLSFO", "Ammonia fuel", "Cargo H₂ burned", "Natural gas", "Import-terminal electricity"]
    col13 = [C1, C2, C5, C4, C3, C6]
    vals = [[f"={xl_rowcol_to_cell(t3 + 1 + k, 2 + j)}" for k in range(6)] for j in range(3)]
    b13 = BarBlock(sh, sh.r, ["LH₂ chain", "NH₃ · NG-fired cracker", "NH₃ · clean-fuel cracker"], seg13, col13, vals, "Ec_Unit")
    sh.r = b13.end + 2
    sh.sec("Chart data · chart 14 (energy intensity)", 14)
    seg14 = ["Electrolysis", "Upstream (liquefaction / Haber-Bosch + tank)", "Shipping fuel", "Shipping: cargo burned as fuel", "Downstream (regas / cracking)"]
    vals = [[f"={xl_rowcol_to_cell(t4 + 1 + k, 2 + j)}" for k in range(5)] for j in range(3)]
    b14 = BarBlock(sh, sh.r, ["LH₂ chain", "NH₃ chain · NG-fired cracker", "NH₃ chain · clean-fuel cracker"], seg14, [C5, C1, C2, C4, C3], vals, "Ec_UnitK")
    sh.r = b14.end + 2

    n = lambda nm: "=" + sh.a(*sh.bk.names[nm])  # noqa: E731
    W, H = 640, 330
    c = base_chart(bk, "line", n("Ec_T12"), W, H, legend_delete=[3, 4, 5])
    c.add_series(line("LH₂ chain (rises with H₂ price)", S["x"], S["l"], S1, 2.5))
    c.add_series(line("NH₃ · NG-fired cracker", S["x"], S["g"], S2, 2.5))
    c.add_series(line("NH₃ · clean-fuel cracker", S["x"], S["c"], S2, 2, "dash"))
    c.add_series(marker(c, n("Ec_L12a"), S["x"], S["ms"], S1, "above", S1, "round_dot", size=7))
    c.add_series(marker(c, n("Ec_L12b"), S["x"], S["mg"], DARK, "below", DARK, "dash", drop=False))
    c.add_series(marker(c, n("Ec_L12c"), S["x"], S["mc"], DARK, "below", DARK, "dash", drop=False))
    axes_line(c, "H₂ price, USD/kg", n("Ec_Y12"), 20, "0.00", "0")
    sh.place(c, 7, W, H)
    sh.place(b13.chart(n("Ec_T13"), n("Ec_X13"), W, 280), 7 + 15, W, 280)
    sh.place(b14.chart(n("Ec_T14"), n("Ec_X14"), W, 280), 7 + 15 + 13, W, 280)
    sh.chart_bottom = max(sh.chart_bottom, 7 + 15 + 13 + 13)

    sh.r = max(sh.r, sh.chart_bottom)
    sh.sec("Method, assumptions and gaps", 12)
    for t in [
        "Energy cost only: each Full Chain energy line is priced at its own carrier price. Charter hire, CapEx, fixed OpEx, port fees, carbon cost and the price of the H₂ feed itself are excluded.",
        "Losses only: hydrogen and ammonia are charged only where burned (LH₂ boil-off at the H₂ price; ammonia burned on the ship and in the cracker at the ammonia price). H₂ feed into the plant is not charged; switch on electrolysis on Upstream to charge it as electricity.",
        "Natural gas is the cracker's NH₃-equivalent LHV gas demand at 1,055.056 MJ/MMBtu and 13 USD/MMBtu, no HHV adjustment (user choice). HHV-priced gas would cost about 10 % more [ESTIMATE – needs source].",
        "Electricity: upstream covers liquefaction, Haber-Bosch, export-tank reliq and electrolysis if on. Import-terminal electricity covers regas pumps, import-tank reliq and the cracker's 0.29 kWh/kg. Import price is a placeholder equal to upstream until set [ASSUMPTION].",
        "Denominator: dropdown. 'Produced' (Economic Origin) divides the annual bill by the H₂ the electrolyser makes (H₂ into the liquefier / Haber-Bosch loop); 'delivered' (Economics) by the H₂ leaving the import terminal. USD M/y is identical on both; the route losing more H₂ looks relatively cheaper on the produced basis.",
        "Prices here are separate from the Midstream VLSFO / NH₃ inputs, which only drive that sheet's ship-day breakeven. Volumes, fuel mode, sea days and every energy assumption come from Annual Energy and Full Chain.",
    ]:
        sh.note("• " + t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--cache", default=None)
    a = ap.parse_args()
    cache = json.load(open(a.cache)) if a.cache else {}
    bk = Book(a.out, cache)
    sheets = {}
    tabs = [("Upstream", PURPLE), ("Midstream", CYAN), ("Downstream", BLUE), ("Full Chain", AMBER), ("Annual Energy", GREEN), ("Energy Cost", MUTED)]
    for name, col in tabs:
        sheets[name] = Sh(bk, name, col)

    # two-pass inside a run: names must be known before charts reference them -> build data first
    for fn, nm_ in [(build_midstream, "Midstream"), (build_upstream, "Upstream"), (build_downstream, "Downstream"),
                    (build_chain, "Full Chain"), (build_annual, "Annual Energy"), (build_cost, "Energy Cost")]:
        fn(sheets[nm_])
    # activate Upstream first
    sheets["Upstream"].ws.activate()
    bk.wb.set_properties({"title": "LH2 vs Ammonia Energy Value Chain (Excel replica)", "author": "Gentari",
                          "comments": "Replica of the artifact LH2 vs Ammonia Energy Value Chain; live formulas, dropdown switches, native charts."})
    bk.wb.close()
    print("wrote", a.out)


if __name__ == "__main__":
    main()
