// LH2 Value Chain Technology Database (Rev 0) — all-departments syndication deck.
// Output: docs/reports/lh2-database-syndication-rev0.pptx
// Run:    PPTX_SKILL=<pptx skill dir, for scripts/apply_theme.js> NODE_PATH=<node_modules with pptxgenjs> node scripts/decks/database-syndication/build.js
// Images: ./img (logos, tank and ship photos extracted from the database .docx); cover artwork from docs/brand/assets.
// Brand: docs/brand/README.md (Gentari). Every number below is taken from
// "LiqH2VC - Database Rev 0.docx" (uploaded 2026-10-09); the section is cited on each slide.
const path = require("path");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const DIR = __dirname;
const IMG = (f) => path.join(DIR, "img", f);
const REPO = path.join(DIR, "..", "..", "..");
const OUT = path.join(REPO, "docs", "reports", "lh2-database-syndication-rev0.pptx");

const THEME = {
  name: "Gentari",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "3A3935", lt1: "FFFFFF", dk2: "1F2933", lt2: "F1EAF6",
    accent1: "7030A0", accent2: "4A3AA7", accent3: "2977D6",
    accent4: "60269E", accent5: "75BA75", accent6: "00C8E8",
    hlink: "2977D6", folHlink: "7030A0",
  },
};
const HEX = { title: "7030A0", purple: "4A3AA7", blue: "2977D6", brand: "60269E", dark: "1F2933",
  text: "3A3935", grid: "E8E8E4", tint: "F1EAF6", lilac: "B4AAE6", grey: "6E6E68", teal: "0B7FA8" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "LH2 Value Chain Technology Database: Syndication";
pres.author = "Gentari";
const C = pres.SchemeColor;

// ---------- Layouts ----------
pres.defineSlideMaster({
  title: "COVER",
  background: { path: path.join(REPO, "docs", "brand", "assets", "cover-background.png") },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.35, y: 2.6, w: 6.9, h: 2.05,
      fontFace: "Verdana", fontSize: 32, bold: true, color: C.background1, align: "left", valign: "bottom", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "date", type: "body", x: 0.35, y: 4.78, w: 6.9, h: 0.5,
      fontFace: "Verdana", fontSize: 18, color: C.background1, align: "left", valign: "middle", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "LEADIN",
  background: { color: "FFFFFF" },
  objects: [
    { text: { text: "Confidential - For PETRONAS Staff Only",
      options: { x: 4.17, y: 0.05, w: 5.0, h: 0.25, fontSize: 10, color: C.accent5, align: "center", margin: 0 } } },
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.38, w: 12.13, h: 0.95,
      fontSize: 28, bold: true, color: C.accent1, align: "left", valign: "top", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "footer", type: "body", x: 0.6, y: 7.05, w: 10.8, h: 0.3,
      fontSize: 11, color: C.text1, valign: "middle", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: 12.28, y: 7.05, w: 0.45, h: 0.3, fontSize: 11, color: C.text1, align: "right" },
});

// ---------- Helpers ----------
const X0 = 0.6, W = 12.13;
function lead(section, title, footer, notes) {
  const s = pres.addSlide({ masterName: "LEADIN", sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  s.addText(footer, { placeholder: "footer" });
  if (notes) s.addNotes(notes);
  return s;
}
function txt(s, text, o) {
  s.addText(text, Object.assign({ isTextBox: true, margin: 0, fontSize: 14, color: C.text1, valign: "top" }, o));
}
function note(s, text, y = 6.3, h = 0.6) { txt(s, text, { x: X0, y, w: W, h, fontSize: 11, objectName: "basis-note" }); }
function box(s, x, y, w, h, fill, name, line) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.06, fill: { color: fill },
    line: { color: line || fill, width: 0.75 }, objectName: name });
}
function stat(s, x, y, w, big, label, o = {}) {
  txt(s, big, { x, y, w, h: o.bh || 0.7, fontSize: o.size || 36, bold: true, color: o.color || C.accent4, valign: "bottom", objectName: "stat-" + (o.name || big) });
  txt(s, label, { x, y: y + (o.bh || 0.7) + 0.08, w, h: o.lh || 0.85, fontSize: o.lsize || 14, objectName: "stat-label-" + (o.name || big) });
}
function bullets(items, o = {}) {
  return items.map((t, i) => ({ text: t, options: Object.assign({ bullet: { indent: 14 }, paraSpaceAfter: o.gap || 6, breakLine: i < items.length - 1 }, o.run || {}) }));
}
function fit(wpx, hpx, bw, bh) { const r = Math.min(bw / wpx, bh / hpx); return { w: wpx * r, h: hpx * r }; }
function chartOpts(extra) {
  return Object.assign({
    catAxisLabelFontSize: 12, catAxisLabelColor: HEX.text, catAxisLabelFontFace: "+mn-lt",
    valAxisLabelFontSize: 11, valAxisLabelColor: HEX.text, valAxisLabelFontFace: "+mn-lt",
    dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt", dataLabelColor: HEX.text,
    legendFontSize: 12, legendFontFace: "+mn-lt", legendColor: HEX.text,
    valGridLine: { color: HEX.grid, size: 0.75 }, catGridLine: { style: "none" },
  }, extra);
}
const TH = (t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: HEX.dark } } });
function table(s, header, rows, o) {
  const body = rows.map((r) => r.map((c, j) => (typeof c === "object" ? c : { text: String(c), options: { bold: j === 0 } })));
  s.addTable([header.map(TH), ...body], Object.assign({ fontSize: 13, color: HEX.text, fontFace: "Calibri",
    border: { type: "solid", pt: 0.75, color: HEX.grid }, valign: "middle", margin: [3, 6, 3, 6] }, o));
}
// Chevron flow header used on the chain slides (the deck's recurring motif)
function chain(s, labels, y, h, fills) {
  const n = labels.length, gap = 0.2, w = (W - gap * (n - 1)) / n;
  labels.forEach((l, i) => {
    s.addShape(i === 0 ? pres.shapes.PENTAGON : pres.shapes.CHEVRON, {
      x: X0 + i * (w + gap), y, w, h, fill: { color: fills ? fills[i] : HEX.brand }, line: { color: fills ? fills[i] : HEX.brand },
      objectName: "chain-step-" + (i + 1) });
    txt(s, l, { x: X0 + i * (w + gap) + (i === 0 ? 0.2 : 0.45), y, w: w - 0.75, h, fontSize: 15, bold: true, color: C.background1, valign: "middle" });
  });
  return { w, gap };
}

// ================= 1. Cover =================
pres.addSection({ title: "Cover" });
let s = pres.addSlide({ masterName: "COVER", sectionTitle: "Cover" });
s.addText([{ text: "LH" }, { text: "2", options: { subscript: true } },
  { text: " Value Chain: Technology Database Syndication" }], { placeholder: "title" });
s.addText("Rev 0 · October 2026", { placeholder: "date" });
s.addNotes("Purpose: walk all departments through the LH2 Value Chain Technology Database, Rev 0 (18 Sep 2026): what it covers, the key numbers, and what is still open.");

// ================= 2. What the database covers =================
pres.addSection({ title: "Overview" });
s = lead("Overview",
  "The database is a single reference for the LH₂ chain, from the liquefier to hydrogen gas at the import terminal, in 13 sections",
  "LiqH₂VC Database Rev 0 · scope and structure",
  "One document, four links in the chain plus four cross-cutting sections. Hydrogen production itself is outside the database.");
const ch = chain(s, ["Liquefaction", "Export storage & loading", "Shipping", "Import & regasification"], 1.65, 0.85);
const covers = [
  ["Properties, liquefaction cycles, technology players, plants built", "Sections 1–5, 8.1, 10.1"],
  ["Tank types, boil-off, export-terminal cost", "Sections 6, 8.2, 10.2"],
  ["LH₂ carriers, marine projects, road and rail, ship boil-off", "Sections 7, 10.3, 12.2"],
  ["Vaporisers and the receiving terminal", "Sections 9, 10.4"],
];
covers.forEach((c, i) => {
  const x = X0 + i * (ch.w + ch.gap);
  box(s, x, 2.7, ch.w, 1.75, HEX.tint, "covers-" + (i + 1));
  txt(s, c[0], { x: x + 0.18, y: 2.85, w: ch.w - 0.36, h: 0.95, fontSize: 15 });
  txt(s, c[1], { x: x + 0.18, y: 3.85, w: ch.w - 0.36, h: 0.45, fontSize: 13, bold: true, color: C.accent4 });
});
box(s, X0, 4.65, W, 0.75, "FFFFFF", "cross-cutting", HEX.lilac);
txt(s, [{ text: "Across the chain:  ", options: { bold: true, color: C.accent4 } },
  { text: "Export-facility cost (8)  ·  Regulation (11)  ·  Key challenges (12)  ·  LH₂ vs NH₃ as hydrogen carrier (13)" }],
  { x: X0 + 0.2, y: 4.65, w: W - 0.4, h: 0.75, fontSize: 15, valign: "middle" });
note(s, "Boundary: gaseous hydrogen at the export plant to gaseous hydrogen at import send-out; producing the hydrogen is outside the database. Use: technology benchmarking, project screening and preliminary techno-economic assessment.\nRev 0, 18 Sep 2026. Prepared by Jasmin Suraya and Ungku M Zulhilmi Ungku Zakaria; reviewed by Wan M Ikhwan Wan Yussoff and Octavian Partenie; approved by Danial Khairi Ahmad; accepted by Alex Bower.", 5.65, 1.2);

// ================= 3. Why liquefy =================
pres.addSection({ title: "Technology" });
s = lead("Technology",
  "Cooling hydrogen to −253 °C makes it about 800 times more compact than the gas, which is what makes bulk shipping possible",
  "LiqH₂VC Database Rev 0 · Sections 1.1 and 2.2 · properties of liquid hydrogen",
  "Four numbers to remember. The ortho-para point explains why liquefiers include catalysts and why boil-off is never zero.");
const stats3 = [
  ["−253 °C", "Boiling point at atmospheric pressure (about 20.3 K)"],
  ["70.8 kg/m³", "Density of liquid hydrogen, against 0.0899 kg/m³ for the gas"],
  ["~800×", "Less storage volume than the gas at standard conditions"],
  ["120 MJ/kg", "Lower heating value, the highest per kilogram of any fuel"],
];
stats3.forEach((st, i) => {
  const x = X0 + (i % 2) * 3.35, y = 1.65 + Math.floor(i / 2) * 2.3;
  box(s, x, y, 3.15, 2.1, HEX.tint, "stat-card-" + (i + 1));
  stat(s, x + 0.25, y + 0.2, 2.7, st[0], st[1], { size: 34, name: "p" + i });
});
box(s, 7.45, 1.65, 5.28, 4.4, "FFFFFF", "ortho-para-panel", HEX.grid);
txt(s, "Ortho-para conversion drives boil-off", { x: 7.7, y: 1.8, w: 4.8, h: 0.4, fontSize: 16, bold: true, color: C.text2 });
// 100 % bars drawn to scale (75/25 at room temperature; nearly all para as a liquid)
const bx = 7.7, bw = 4.75;
txt(s, "Room temperature", { x: bx, y: 2.35, w: bw, h: 0.3, fontSize: 13 });
s.addShape(pres.shapes.RECTANGLE, { x: bx, y: 2.68, w: bw * 0.75, h: 0.42, fill: { color: HEX.purple }, line: { color: HEX.purple }, objectName: "bar-ortho" });
s.addShape(pres.shapes.RECTANGLE, { x: bx + bw * 0.75, y: 2.68, w: bw * 0.25, h: 0.42, fill: { color: HEX.blue }, line: { color: HEX.blue }, objectName: "bar-para" });
txt(s, "75 % ortho", { x: bx + 0.1, y: 2.68, w: 2.5, h: 0.42, fontSize: 13, bold: true, color: C.background1, valign: "middle" });
txt(s, "25 % para", { x: bx + bw * 0.75 + 0.05, y: 2.68, w: 1.15, h: 0.42, fontSize: 13, bold: true, color: C.background1, valign: "middle" });
txt(s, "Liquid hydrogen", { x: bx, y: 3.25, w: bw, h: 0.3, fontSize: 13 });
s.addShape(pres.shapes.RECTANGLE, { x: bx, y: 3.58, w: bw, h: 0.42, fill: { color: HEX.blue }, line: { color: HEX.blue }, objectName: "bar-para-liquid" });
txt(s, "Nearly 100 % para", { x: bx + 0.1, y: 3.58, w: 3, h: 0.42, fontSize: 13, bold: true, color: C.background1, valign: "middle" });
txt(s, "Ortho turns into para as hydrogen cools, and the change releases heat. If it happens in the tank, that heat boils off LH₂, so catalysts convert it stage by stage inside the liquefier.",
  { x: 7.7, y: 4.2, w: 4.8, h: 1.7, fontSize: 14 });

// ================= 4. Liquefaction energy =================
s = lead("Technology",
  "Today's liquefiers use 10–13 kWh/kg H₂, about three times the 3.3 kWh/kg minimum; Kawasaki targets 8–9 now and 6 at large scale",
  "LiqH₂VC Database Rev 0 · Sections 2.1, 3.4, 5.5, 10.1, 13.3 · liquefaction energy · kWh per kg H₂",
  "Linde-Hampson is simple but energy hungry; Claude adds expansion turbines; Brayton is used for pre-cooling. Most commercial plants run modified Claude cycles. The shaded zone cannot be reached by any liquefier.");
const rows4 = [
  ["Linde-Hampson cycle", 10, 15, HEX.purple, "10–15"],
  ["Claude cycle", 7, 10, HEX.purple, "7–10"],
  ["Brayton cycle (pre-cooling)*", 6, 8, HEX.purple, "6–8*"],
  ["Commercial plants today", 10, 13, HEX.dark, "10–13"],
  ["Linde Leuna, reported", 11.9, 11.9, HEX.dark, "11.9"],
  ["Kawasaki, current development", 8, 9, HEX.blue, "8–9"],
  ["Kawasaki, large-scale target", 6, 6, HEX.blue, "6"],
];
const px0 = 3.7, px1 = 12.3, vmax = 16, sx = (v) => px0 + (px1 - px0) * v / vmax;
const ry0 = 1.75, rh = 0.56;
s.addShape(pres.shapes.RECTANGLE, { x: sx(0), y: ry0 - 0.1, w: sx(3.9) - sx(0), h: rows4.length * rh + 0.1, fill: { color: HEX.tint }, line: { color: HEX.tint }, objectName: "unreachable-zone" });
s.addShape(pres.shapes.LINE, { x: sx(3.3), y: ry0 - 0.1, w: 0, h: rows4.length * rh + 0.1, line: { color: HEX.title, width: 1.25, dashType: "dash" }, objectName: "min-3.3" });
s.addShape(pres.shapes.LINE, { x: sx(3.9), y: ry0 - 0.1, w: 0, h: rows4.length * rh + 0.1, line: { color: HEX.title, width: 1.25 }, objectName: "min-3.9" });
for (let v = 0; v <= vmax; v += 2) {
  s.addShape(pres.shapes.LINE, { x: sx(v), y: ry0 + rows4.length * rh, w: 0, h: 0.08, line: { color: HEX.text, width: 0.75 } });
  txt(s, String(v), { x: sx(v) - 0.3, y: ry0 + rows4.length * rh + 0.1, w: 0.6, h: 0.25, fontSize: 11, align: "center" });
}
s.addShape(pres.shapes.LINE, { x: px0, y: ry0 + rows4.length * rh, w: px1 - px0, h: 0, line: { color: HEX.text, width: 0.75 }, objectName: "axis" });
txt(s, "kWh per kg H₂", { x: px1 - 2.0, y: ry0 + rows4.length * rh + 0.36, w: 2.0, h: 0.25, fontSize: 11, align: "right" });
rows4.forEach((r, i) => {
  const y = ry0 + i * rh;
  txt(s, r[0], { x: X0, y, w: 3.0, h: rh - 0.12, fontSize: 14, valign: "middle", bold: i >= 3 });
  if (r[1] === r[2]) s.addShape(pres.shapes.OVAL, { x: sx(r[1]) - 0.13, y: y + (rh - 0.12) / 2 - 0.13, w: 0.26, h: 0.26, fill: { color: r[3] }, line: { color: r[3] }, objectName: "point-" + i });
  else s.addShape(pres.shapes.RECTANGLE, { x: sx(r[1]), y: y + 0.06, w: sx(r[2]) - sx(r[1]), h: rh - 0.24, fill: { color: r[3] }, line: { color: r[3] }, objectName: "range-" + i });
  txt(s, r[4], { x: sx(r[2]) + 0.18, y, w: 0.9, h: rh - 0.12, fontSize: 13, bold: true, valign: "middle" });
});
txt(s, "Unreachable: below the minimum work to liquefy, 3.3 kWh/kg (dashed) or 3.9 with ortho-para conversion", { x: sx(0) + 0.08, y: ry0 + 0.05, w: 1.65, h: 2.2, fontSize: 11, color: C.accent1 });
note(s, "*Brayton is a pre-cooling cycle inside integrated plants, so its figure is not directly comparable with the other cycles. Most commercial plants use modified Claude cycles with pre-cooling, expansion turbines and staged ortho-para conversion. Minimum work: US DOE Hydrogen Program Record 9013 (2009), as cited in Section 13.3.", 6.35, 0.6);

// ================= 5. Technology players =================
s = lead("Technology",
  "Five companies lead LH₂ technology, and Kawasaki is the only one offering the full chain from liquefier to receiving terminal",
  "LiqH₂VC Database Rev 0 · Sections 4 and 10 · technology players",
  "Linde and Air Liquide build the largest liquefiers; Chart supplies equipment; Plug Power integrates electrolysis and liquefaction; Kawasaki covers liquefaction, ships and terminals.");
const players = [
  ["Linde", "Munich, Germany", "trim-linde.png", 267, 72, "Claude-cycle liquefiers, heat exchangers, compressors, storage",
    ["Leuna, Germany: 5 to 10 t/day", "La Porte, Texas: over 30 t/day", "LH₂ supply to NASA"]],
  ["Air Liquide", "Paris, France", "trim-airliquide.png", 331, 63, "Helium-cycle liquefiers and full cryogenic equipment",
    ["North Las Vegas: 30 t/day", "South Korea: 90 t/day, world's largest", "Wenchang, China: 1,500 L/h"]],
  ["Chart Industries (Baker Hughes)", "Georgia, USA", "trim-chart.png", 680, 251, "Cold boxes, turboexpanders, heat exchangers, modular plants",
    ["Two 15 t/day plants for Plug Power", "Standard plants of 5–30 t/day"]],
  ["Kawasaki Heavy Industries", "Tokyo, Japan", "trim-khi.png", 224, 82, "Liquefiers, cryogenic tanks, LH₂ carriers, receiving terminals",
    ["HESC Australia–Japan chain", "Suiso Frontier, 1,250 m³ carrier", "Hy touch Kobe terminal", "40,000 m³ carrier by 2030"]],
  ["Plug Power", "New York, USA", "trim-plug.png", 281, 98, "In-house liquefaction with PEM electrolysis and trailer logistics",
    ["Woodbine, Georgia: 15–17.5 t/day", "Graham, Texas: 45 t/day design", "Alabama, NY: 74 t/day target"]],
];
const pw = (W - 4 * 0.2) / 5;
players.forEach((p, i) => {
  const x = X0 + i * (pw + 0.2), y = 1.65, khi = i === 3;
  box(s, x, y, pw, 4.55, "FFFFFF", "player-" + (i + 1), khi ? HEX.brand : HEX.grid);
  const f = fit(p[3], p[4], pw - 0.5, 0.62);
  s.addImage({ path: IMG(p[2]), x: x + (pw - f.w) / 2, y: y + 0.18 + (0.62 - f.h) / 2, w: f.w, h: f.h, altText: p[0] + " logo", objectName: "logo-" + (i + 1) });
  txt(s, p[0], { x: x + 0.15, y: y + 0.95, w: pw - 0.3, h: 0.55, fontSize: 15, bold: true, color: C.text2, valign: "middle" });
  txt(s, p[1], { x: x + 0.15, y: y + 1.5, w: pw - 0.3, h: 0.3, fontSize: 12, color: C.accent4 });
  txt(s, p[5], { x: x + 0.15, y: y + 1.85, w: pw - 0.3, h: 0.95, fontSize: 13 });
  txt(s, bullets(p[6], { gap: 3 }), { x: x + 0.15, y: y + 2.8, w: pw - 0.3, h: 1.65, fontSize: 13 });
});
txt(s, "Full chain", { x: X0 + 3 * (pw + 0.2) + 0.15, y: 6.28, w: pw - 0.3, h: 0.32, fontSize: 12, bold: true, color: C.background1, align: "center", valign: "middle", fill: { color: HEX.brand }, objectName: "khi-tag" });
note(s, "Capacities as stated in each company profile (Section 4); Section 10 notes Kawasaki is currently the single player covering liquefaction, shipping, receiving and regasification.", 6.7, 0.3);

// ================= 6. Plants built =================
s = lead("Technology",
  "The largest liquefier operating today is 90 t/day at Incheon; Kawasaki's planned 115 t/day train would be bigger than any plant built",
  "LiqH₂VC Database Rev 0 · Sections 5 and 10.1 · liquefaction capacity · t/day LH₂",
  "Most plants built in the last 20 years are 5 to 35 t/day. Incheon (SK E&S, Air Liquide equipment) is three 30 t/day trains. The dark bar is Kawasaki's design train, not a built plant.");
const plants = [
  ["Chiba, JP · Iwatani · 2009", 5], ["Akashi, JP · Kawasaki · 2014", 5],
  ["Osaka, JP · Iwatani · 2006", 10], ["Yamaguchi, JP · Iwatani, Tokuyama · 2017", 10],
  ["Leuna, DE · Linde · 2021", 10], ["Woodbine, US · Plug Power · 2024", 17.5],
  ["La Porte, US · Air Products & Praxair · 2021", 27.2], ["Las Vegas, US · Air Liquide · 2022", 27.2],
  ["Ulsan, KR · Hyosung–Linde · 2024", 35.6], ["Incheon, KR · SK E&S, Air Liquide · 2024", 90],
  ["Kawasaki unit train (planned)", 115],
];
s.addChart(pres.charts.BAR, [{ name: "Capacity, t/day", labels: plants.map((p) => p[0]), values: plants.map((p) => p[1]) }], chartOpts({
  x: 0.5, y: 1.55, w: 8.4, h: 4.75, barDir: "bar", barGapWidthPct: 45,
  chartColors: plants.map((p, i) => (i === plants.length - 1 ? HEX.dark : HEX.purple)),
  showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "0.#", dataLabelFontBold: true,
  valAxisMinVal: 0, valAxisMaxVal: 130, valAxisMajorUnit: 20, valAxisHidden: true, valGridLine: { style: "none" },
  catAxisLabelFontSize: 12, showLegend: false, objectName: "plants-chart",
}));
box(s, 9.25, 1.65, 3.48, 4.55, HEX.tint, "plants-stats");
stat(s, 9.5, 1.8, 3.0, "90 t/day", "Incheon, three 30 t/day trains, completed May 2024", { size: 32, bh: 0.6, lh: 0.65, name: "incheon" });
stat(s, 9.5, 3.25, 3.0, "115 t/day", "Kawasaki's design train size per liquefier", { size: 32, bh: 0.6, lh: 0.65, name: "khi" });
stat(s, 9.5, 4.7, 3.0, "11.9 kWh/kg", "Reported energy use at Linde Leuna", { size: 32, bh: 0.6, lh: 0.65, name: "leuna" });
note(s, "Woodbine shown at the top of its 15–17.5 t/day range. Sources disagree within the database: Las Vegas is 27.2 t/day in Table 5.6 but 30 t/day in Section 5.4, and La Porte is 27.2 t/day in Table 5.6 but over 30 t/day in Section 4.1.", 6.4, 0.5);

// ================= 7. Storage =================
pres.addSection({ title: "Infrastructure" });
s = lead("Infrastructure",
  "Large double-wall vacuum-insulated tanks lose about 0.1 % of their LH₂ a day, and the boil-off has to be vented, used or re-liquefied",
  "LiqH₂VC Database Rev 0 · Sections 6 and 8.2 · LH₂ storage · boil-off in % of tank contents per day",
  "Bigger tanks lose less per tonne because of their smaller surface-to-volume ratio. 0.1 %/day is the planning value used across the database.");
const tf = fit(344, 256, 3.4, 2.5);
s.addImage({ path: IMG("tank-linde.jpg"), x: X0, y: 1.65, w: tf.w, h: tf.h, altText: "Cutaway of a Linde double-wall LH2 tank", objectName: "tank-image" });
txt(s, "Double-wall vacuum-insulated LH₂ tank (Linde, Figure 7)", { x: X0, y: 1.7 + tf.h, w: 3.4, h: 0.3, fontSize: 11 });
txt(s, "Boil-off options: vent it, compress it, re-liquefy it, or stop it with active zero-boil-off refrigeration.", { x: X0, y: 4.65, w: 3.4, h: 1.3, fontSize: 14, bold: true, color: C.text2 });
const types = [
  ["Large stationary tanks", "Plants and terminals. Lowest boil-off per tonne; high CAPEX and footprint"],
  ["Transport tanks", "Road, rail and ships. Flexible; more heat ingress, boil-off to manage"],
  ["Small and medium tanks", "Refuelling stations and buffers. Low investment; higher relative losses"],
  ["Pressurised LH₂ tanks", "Higher delivery pressure, less compression; tougher design and safety"],
];
const tw = (12.73 - 4.3 - 0.2) / 2;
types.forEach((t, i) => {
  const x = 4.3 + (i % 2) * (tw + 0.2), y = 1.65 + Math.floor(i / 2) * 1.4;
  box(s, x, y, tw, 1.25, HEX.tint, "tank-type-" + (i + 1));
  txt(s, t[0], { x: x + 0.2, y: y + 0.12, w: tw - 0.4, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
  txt(s, t[1], { x: x + 0.2, y: y + 0.5, w: tw - 0.4, h: 0.7, fontSize: 14 });
});
const bor = [["~0.07 %/day", "NASA Kennedy 3,000 m³ sphere, the largest LH₂ tank in use"],
  ["≤0.1 %/day", "Kawasaki 11,200 m³ design target"],
  ["0.1 %/day", "Database planning value (S&P input, likely conservative)"]];
const sw = (12.73 - 4.3 - 0.4) / 3;
bor.forEach((b, i) => stat(s, 4.3 + i * (sw + 0.2), 4.6, sw, b[0], b[1], { size: 28, bh: 0.55, lh: 0.8, name: "bor" + i }));
note(s, "Boil-off depends on tank size, insulation, storage time and fill level; sloshing, stratification and ortho-para conversion add to it (Section 6.3).", 6.45, 0.4);

// ================= 8. Shipping =================
s = lead("Infrastructure",
  "Only a 1,250 m³ demonstration carrier has sailed; the commercial design is 160,000 m³, 128 times larger",
  "LiqH₂VC Database Rev 0 · Sections 7 and 10.3 · LH₂ carriers · cargo capacity in m³",
  "Suiso Frontier proved the concept in 2022. The 40,000 m3 carrier was contracted in January 2026 with an ocean-going demonstration targeted by FY2030. 128x is 160,000 divided by 1,250.");
const sf = fit(1220, 476, 5.6, 2.3);
s.addImage({ path: IMG("suiso-frontier.png"), x: X0, y: 1.65, w: sf.w, h: sf.h, altText: "Suiso Frontier LH2 carrier at sea", objectName: "ship-image" });
txt(s, "Suiso Frontier (Kawasaki): 116 m long, 1,250 m³ (~75 t LH₂), 13 knots, about 8,000 gross tonnes. First international LH₂ voyage in 2022.",
  { x: X0, y: 1.75 + sf.h, w: 5.6, h: 0.65, fontSize: 13 });
s.addChart(pres.charts.BAR, [{ name: "Cargo capacity, m³", labels: ["Suiso Frontier (sailing)", "KHI–JSE carrier (contracted)", "Commercial design (target)"], values: [1250, 40000, 160000] }], chartOpts({
  x: 6.5, y: 1.55, w: 6.3, h: 3.0, barDir: "col", barGapWidthPct: 60, chartColors: [HEX.purple, HEX.purple, HEX.dark],
  showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "#,##0", dataLabelFontBold: true,
  valAxisHidden: true, valGridLine: { style: "none" }, valAxisMaxVal: 185000, showLegend: false, objectName: "ship-size-chart",
}));
table(s, ["Mode", "Best suited to", "Main limits"], [
  ["Road", "Regional distribution, refuelling stations, smaller deliveries", "Lower capacity; higher cost per kg over long distances"],
  ["Rail", "Larger volumes over longer inland distances", "Needs rail infrastructure and dedicated handling"],
  ["Marine", "Large-scale, long-distance and international supply", "High ship and terminal CAPEX; boil-off management"],
], { x: X0, y: 4.75, w: W, colW: [1.3, 5.2, 5.63], rowH: 0.36, fontSize: 13, objectName: "modes-table" });
note(s, "Road and rail all use vacuum-insulated cryogenic tanks; mode choice depends on distance, volume, delivery frequency, infrastructure, boil-off and cost (Section 7.3).", 6.4, 0.4);

// ================= 9. Kawasaki chain specification =================
s = lead("Infrastructure",
  "Kawasaki's specification is the chain's design basis: 8–9 kWh/kg to liquefy, 0.1 %/day boil-off in tanks and 0.2 %/day at sea",
  "LiqH₂VC Database Rev 0 · Section 10 · KHI technical specification",
  "These are the values the rest of the database and Section 13 build on. The ship's dual-fuel engine is still in development, so the 0.2 %/day burned as fuel is not yet proven.");
const kc = chain(s, ["Liquefier", "Export terminal", "LH₂ carrier", "Import & regasification"], 1.65, 0.75);
const kspec = [
  ["115 t/day per train", "8–9 kWh/kg H₂ now; 6 at large scale, gains expected 2035–2040", "H₂ Claude cycle with N₂ pre-cooling", "Iron-based ortho-para catalyst inside the liquefier", "Minimum economic scale ~10,000 tpa"],
  ["Up to 4,000 t (~56,000 m³) per tank, not yet built", "Boil-off 0.1 %/day", "Boil-off re-liquefied at 8 kWh/kg", "Jetty and loading arms costed on an LNG basis"],
  ["160,000 m³ commercial design; 40,000 m³ being built", "29.6 km/h (about 16 knots)", "Boil-off 0.2 %/day, burned in a dual-fuel engine", "No onboard re-liquefaction", "1.30 % vaporised at loading, 1.25 % at unloading"],
  ["65,000 m³ tanks, boil-off 0.1 %/day", "Open-rack vaporiser using seawater", "3.8 MJ/kg of heat from seawater, not counted as purchased energy", "Ship-to-ship transfer and floating storage not yet considered"],
];
kspec.forEach((k, i) => {
  const x = X0 + i * (kc.w + kc.gap);
  box(s, x, 2.6, kc.w, 3.55, HEX.tint, "spec-" + (i + 1));
  txt(s, bullets(k, { gap: 8 }), { x: x + 0.12, y: 2.75, w: kc.w - 0.25, h: 3.3, fontSize: 14 });
});
note(s, "Source: Kawasaki questionnaire reply and supplemental information, as recorded in Section 10. Export-terminal CAPEX factors are in Section 8.2.", 6.4, 0.4);

// ================= 10. Cost of an export facility =================
pres.addSection({ title: "Cost" });
s = lead("Cost",
  "Export-facility cost is a Class 5 estimate (±30–50 %): the liquefier dominates, and its power use should fall from ~10 to ~6 kWh/kg",
  "LiqH₂VC Database Rev 0 · Sections 8 and 10.1–10.2 · export-facility CAPEX inputs · USD, cost year not stated",
  "No LH2 export terminal has been built at this scale, hence the wide range. The chart applies the database's own scaling rule to show why bigger liquefiers are cheaper per tonne.");
const costRows = [
  ["H₂ liquefier (largest item)", "2,250 kUSD per t/day at 30 t/day · scaling exponent −0.38 · fixed O&M 4 %/yr, power extra"],
  ["LH₂ storage tanks", "24 USD/kg LH₂ (steel sphere ×2.5 for insulation and installation) · scaling factor 0.6"],
  ["Boil-off re-liquefaction", "30 MUSD for a 6 t/day unit · scaling factor 0.85 · 8 kWh/kg, to be confirmed"],
  ["Jetty and cryogenic loading arms", "15,960 USD per m³/h of loading rate (LNG benchmark +20 % for LH₂)"],
  ["Adders on the subtotal", "+25 % utilities and civil · +20 % indirects and contingency · ×0.85 India · O&M 2.5 %/yr"],
];
costRows.forEach((r, i) => {
  const y = 1.65 + i * 0.93;
  box(s, X0, y, 7.0, 0.82, i === 0 ? HEX.tint : "FFFFFF", "cost-row-" + (i + 1), i === 0 ? HEX.tint : HEX.grid);
  txt(s, r[0], { x: X0 + 0.15, y: y + 0.06, w: 6.7, h: 0.3, fontSize: 14, bold: true, color: C.text2 });
  txt(s, r[1], { x: X0 + 0.15, y: y + 0.38, w: 6.7, h: 0.4, fontSize: 13 });
});
const sizes = [30, 60, 115, 200, 300];
const spec = sizes.map((t) => Math.round(2250 * Math.pow(t / 30, -0.38) / 10) * 10);
txt(s, "Liquefier CAPEX per t/day of capacity, kUSD", { x: 7.95, y: 1.65, w: 4.8, h: 0.3, fontSize: 14, bold: true, color: C.text2 });
s.addChart(pres.charts.BAR, [{ name: "kUSD per t/day", labels: sizes.map((t) => t + " t/day"), values: spec }], chartOpts({
  x: 7.85, y: 1.95, w: 4.95, h: 2.75, barDir: "col", barGapWidthPct: 55, chartColors: [HEX.purple],
  showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "#,##0", dataLabelFontBold: true,
  valAxisHidden: true, valGridLine: { style: "none" }, valAxisMaxVal: 2700, showLegend: false, objectName: "capex-scaling-chart",
}));
txt(s, "Computed with the Section 10.1 rule: 2,250 × (size ÷ 30)^−0.38, rounded to 10. 115 t/day = one Kawasaki train.", { x: 7.95, y: 4.72, w: 4.8, h: 0.5, fontSize: 11 });
stat(s, 7.95, 5.25, 4.8, "10 → 6 kWh/kg", "Liquefier power use today and as plants grow (Section 8.1, Figure 10)", { size: 28, bh: 0.5, lh: 0.5, name: "sec-path" });
note(s, "Tank cost reference size is still ‘xx m³’ in Section 10.2. Storage is sized from plant output, ship size and calls a year (6 loadings a year, 5 % minimum heel assumed).", 6.45, 0.45);

// ================= 11. Regulation =================
pres.addSection({ title: "Regulation and challenges" });
s = lead("Regulation and challenges",
  "There is no dedicated LH₂ regulation yet: Japan has approved projects case by case, so a permitting timeline cannot be set",
  "LiqH₂VC Database Rev 0 · Section 11 · regulatory compliance",
  "Regulation is an open item for any LH2 project outside Japan. Each gap below is something we would need to resolve before committing to a schedule.");
box(s, X0, 1.65, 4.5, 4.5, HEX.brand, "exists-panel");
txt(s, "What exists today", { x: X0 + 0.3, y: 1.85, w: 3.9, h: 0.4, fontSize: 18, bold: true, color: C.background1 });
txt(s, bullets(["Japan: project elements not covered by existing rules were reviewed and approved by a special evaluation committee",
  "Elsewhere: a similar country-by-country approach may follow, but this is not confirmed"], { gap: 10 }),
  { x: X0 + 0.3, y: 2.4, w: 3.9, h: 3.5, fontSize: 15, color: C.background1 });
txt(s, "Not yet identified in the sources reviewed", { x: 5.4, y: 1.65, w: 7.3, h: 0.4, fontSize: 18, bold: true, color: C.text2 });
const gaps = ["Classification-society rules or Approval in Principle for LH₂ carriers",
  "Classification of ship cargo tanks", "Design and safety standards for liquefiers, ships and terminals",
  "Carbon-border or emissions-reporting requirements",
  "Carbon-intensity disclosure for the liquefier: needs a feasibility study, as it varies with plant size"];
gaps.forEach((g, i) => {
  const y = 2.2 + i * 0.78;
  s.addShape(pres.shapes.OVAL, { x: 5.4, y: y + 0.08, w: 0.42, h: 0.42, fill: { color: i === 4 ? HEX.blue : HEX.title }, line: { color: i === 4 ? HEX.blue : HEX.title }, objectName: "gap-icon-" + (i + 1) });
  txt(s, i === 4 ? "?" : "×", { x: 5.4, y: y + 0.08, w: 0.42, h: 0.42, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle" });
  txt(s, g, { x: 6.0, y, w: 6.7, h: 0.6, fontSize: 15, valign: "middle" });
});

// ================= 12. Key challenges =================
s = lead("Regulation and challenges",
  "Two challenges dominate: liquefying 100,000 t a year needs about 103 MW non-stop, and ship boil-off is still unproven at full scale",
  "LiqH₂VC Database Rev 0 · Section 12 · key challenges",
  "103 MW is liquefaction only, at 8-9 kWh/kg; producing the hydrogen is extra. The 3.4 %/day figure comes from small-scale Suiso Frontier studies and is a reference value, not project data.");
box(s, X0, 1.65, 5.9, 2.15, HEX.tint, "challenge-energy");
stat(s, X0 + 0.3, 1.8, 5.3, "103 MW", "of power running all the time, just to liquefy 100,000 t of hydrogen a year. Finding that much low-carbon power at a low price is critical.", { size: 40, bh: 0.7, lh: 1.1, name: "103" });
box(s, X0, 4.0, 5.9, 2.15, HEX.tint, "challenge-bog");
stat(s, X0 + 0.3, 4.15, 5.3, "0.2 vs ~3.4 %/day", "Planned ship boil-off against rates reported in smaller-scale Suiso Frontier studies. No full-scale vessel data yet; one voyage vented significant hydrogen.", { size: 34, bh: 0.7, lh: 1.1, name: "bog" });
txt(s, "Other challenges", { x: 6.85, y: 1.65, w: 5.88, h: 0.4, fontSize: 18, bold: true, color: C.text2 });
const other = [["Bigger ships cost more", "Only a demo ship has sailed; large cargo tanks are hard to build; ship price not shared"],
  ["Costs are still unclear", "Liquefaction and regas cost per kg not shared; needs a feasibility study"],
  ["Rules and permits uncertain", "Case by case so far, mainly in Japan (see previous slide)"],
  ["Materials and safety need detail", "Cargo-tank metal not confirmed; likely needs a bigger safety zone than ammonia"]];
other.forEach((o, i) => {
  const y = 2.2 + i * 1.0;
  s.addShape(pres.shapes.OVAL, { x: 6.85, y: y + 0.05, w: 0.42, h: 0.42, fill: { color: HEX.brand }, line: { color: HEX.brand }, objectName: "challenge-num-" + (i + 1) });
  txt(s, String(i + 1), { x: 6.85, y: y + 0.05, w: 0.42, h: 0.42, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle" });
  txt(s, o[0], { x: 7.45, y, w: 5.28, h: 0.32, fontSize: 15, bold: true, color: C.text2 });
  txt(s, o[1], { x: 7.45, y: y + 0.34, w: 5.28, h: 0.6, fontSize: 14 });
});

// ================= 13. LH2 vs NH3: basis =================
pres.addSection({ title: "LH2 vs NH3" });
s = lead("LH2 vs NH3",
  "LH₂ and NH₃ are compared on the same job: one 40,000 m³ cargo, from hydrogen gas at the export plant to hydrogen gas at the import terminal",
  "LiqH₂VC Database Rev 0 · Section 13.1 · basis of the LH₂ vs NH₃ comparison",
  "Same ship size, same distance, same end product. The NH3 cargo carries 1.72 times more hydrogen, but has to be cracked back at the far end.");
const lanes = [
  ["LH₂ route", "2,832 t of H₂ per cargo", HEX.purple, [
    ["Prepare cargo", "Liquefier, 9 kWh/kg H₂"], ["Export tank", "Boil-off 0.1 %/day, re-liquefied"],
    ["Voyage, 20 days", "Boil-off 0.40 %/day burned as engine fuel"], ["Import terminal", "Seawater vaporiser, 3.8 MJ/kg of free heat"]]],
  ["NH₃ route", "27,280 t of NH₃ = 4,871 t of H₂", HEX.blue, [
    ["Prepare cargo", "Haber-Bosch, 1 kWh/kg H₂ (team input)"], ["Export tank", "Boil-off 0.05 %/day, re-liquefied"],
    ["Voyage, 20 days", "Boil-off 0.15 %/day re-liquefied; ammonia bought as fuel"], ["Import terminal", "Cracker: 6.5 kg NH₃ per kg H₂ gas-fired, 7.2 clean fuel"]]],
];
lanes.forEach((ln, li) => {
  const y = 1.65 + li * 2.15;
  box(s, X0, y, 2.3, 1.95, ln[2], "lane-" + (li + 1));
  txt(s, ln[0], { x: X0 + 0.18, y: y + 0.2, w: 2.0, h: 0.45, fontSize: 18, bold: true, color: C.background1 });
  txt(s, ln[1], { x: X0 + 0.18, y: y + 0.75, w: 2.0, h: 1.0, fontSize: 14, color: C.background1 });
  const sw4 = (12.73 - 3.1 - 3 * 0.2) / 4;
  ln[3].forEach((st, k) => {
    const x = 3.1 + k * (sw4 + 0.2);
    box(s, x, y, sw4, 1.95, HEX.tint, "lane-" + (li + 1) + "-step-" + (k + 1));
    txt(s, st[0], { x: x + 0.15, y: y + 0.15, w: sw4 - 0.3, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
    txt(s, st[1], { x: x + 0.15, y: y + 0.55, w: sw4 - 0.3, h: 1.3, fontSize: 14 });
  });
});
note(s, "Both export tanks 60,000 m³ with 5 days per cargo. Energy on a lower-heating-value basis; electricity as delivered kWh. Chosen values: 20 sea days, tank size and storage time, 3.94 kWh/kg to re-liquefy LH₂ boil-off. Several NH₃ values are team inputs or estimates that still need sources.", 6.05, 0.75);

// ================= 14. Full-chain energy =================
s = lead("LH2 vs NH3",
  "On current inputs, ammonia with a gas-fired cracker uses about 14 % less energy than LH₂: 11.36 against 13.27 kWh/kg of hydrogen delivered",
  "LiqH₂VC Database Rev 0 · Section 13.6 · end-to-end energy · kWh per kg H₂ delivered",
  "LH2's energy sits upstream in the liquefier; ammonia's sits downstream in the cracker. LH2 delivers more of the hydrogen it starts with.");
const cats14 = ["NH₃, clean-fuel cracker · 11.66", "NH₃, gas-fired cracker · 11.36", "LH₂ route · 13.27"];
const ser14 = [
  ["Liquefaction or Haber-Bosch", [1.29, 1.16, 9.78], HEX.purple],
  ["Export-tank boil-off", [0.01, 0.01, 0.03], HEX.lilac],
  ["Ship fuel bought", [1.80, 1.63, 0.51], HEX.grey],
  ["Cargo H₂ burned as ship fuel", [0, 0, 2.90], HEX.dark],
  ["Regasification or cracking", [8.56, 8.56, 0.05], HEX.blue],
];
s.addChart(pres.charts.BAR, ser14.map((r) => ({ name: r[0], labels: cats14, values: r[1] })), chartOpts({
  x: 0.5, y: 1.55, w: 8.0, h: 4.6, barDir: "bar", barGrouping: "stacked", barGapWidthPct: 45,
  chartColors: ser14.map((r) => r[2]), showValue: true, dataLabelPosition: "ctr", dataLabelColor: "FFFFFF", dataLabelFontBold: true,
  dataLabelFormatCode: '[<0.6]"";0.00', valAxisMinVal: 0, valAxisMaxVal: 14, valAxisMajorUnit: 2, valAxisLabelFormatCode: "0",
  showLegend: true, legendPos: "t", catAxisLabelFontSize: 13, objectName: "full-chain-chart",
}));
txt(s, "Share of hydrogen delivered", { x: 8.9, y: 1.65, w: 3.83, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
table(s, ["Route", "Burned on the way", "Delivered"], [
  ["LH₂", "227 t as ship fuel", { text: "92.0 %", options: { bold: true, color: HEX.title } }],
  ["NH₃, gas-fired", "675 t in cracker", "86.2 %"],
  ["NH₃, clean fuel", "1,083 t in cracker", "77.8 %"],
], { x: 8.9, y: 2.1, w: 3.83, colW: [1.25, 1.53, 1.05], rowH: 0.48, fontSize: 13, objectName: "delivered-table" });
txt(s, "Tonnes are per 40,000 m³ cargo (H₂ or H₂ equivalent). NH₃ ship fuel is bought separately, so the NH₃ cargo arrives whole (assumption).", { x: 8.9, y: 4.25, w: 3.83, h: 1.0, fontSize: 12 });
note(s, "Labels under 0.6 kWh/kg hidden (export-tank boil-off 0.01–0.03; LH₂ ship fuel bought 0.51; LH₂ regas 0.05). LH₂ ship boil-off 0.40 %/day; Haber-Bosch 1 kWh/kg H₂ (team input). Totals are 34 % and 40 % of the hydrogen LHV.", 6.4, 0.45);

// ================= 15. Stream by stream =================
s = lead("LH2 vs NH3",
  "LH₂ pays 8.6 kWh/kg more upstream and 1.8 more at sea, then wins back 8.5 downstream because vaporising needs almost no energy",
  "LiqH₂VC Database Rev 0 · Sections 13.2–13.6 · energy by stream, LH₂ against gas-fired NH₃ · kWh per kg H₂ delivered",
  "Read left to right: the liquefier is LH2's big cost, the cracker is ammonia's. Net, LH2 uses 1.9 kWh/kg more on these inputs.");
txt(s, "LH₂ minus NH₃ (gas-fired cracker), kWh/kg H₂", { x: X0, y: 1.6, w: 6.3, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
s.addChart(pres.charts.BAR, [{ name: "LH2 minus NH3", labels: ["Upstream", "At sea", "Downstream", "Full chain"], values: [8.6, 1.8, -8.5, 1.9] }], chartOpts({
  x: 0.5, y: 1.95, w: 6.4, h: 4.2, barDir: "col", barGapWidthPct: 70, chartColors: [HEX.purple, HEX.purple, HEX.blue, HEX.dark],
  showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: "+0.0;-0.0;0", dataLabelFontBold: true,
  valAxisMinVal: -10, valAxisMaxVal: 10, valAxisMajorUnit: 5, valAxisLabelFormatCode: "0", catAxisLabelPos: "low",
  catAxisLabelFontSize: 13, showLegend: false, objectName: "stream-chart",
}));
table(s, ["Stream", "LH₂", "NH₃", "Difference"], [
  ["Upstream", "9.81", "1.17", "+8.6"], ["At sea", "3.41", "1.63", "+1.8"],
  ["Downstream", "0.05", "8.56", "−8.5"],
  [{ text: "Full chain", options: { bold: true } }, { text: "13.27", options: { bold: true } }, { text: "11.36", options: { bold: true } }, { text: "+1.9", options: { bold: true, color: HEX.title } }],
], { x: 7.3, y: 1.95, w: 5.43, colW: [1.6, 1.25, 1.25, 1.33], rowH: 0.5, fontSize: 14, align: "left", objectName: "stream-table" });
txt(s, bullets(["Upstream: the liquefier needs about nine times the energy per kg of the ammonia plant",
  "At sea: LH₂ burns 227 t of its own cargo as engine fuel",
  "Downstream: the cracker burns ammonia and natural gas; LH₂ regas uses free seawater heat"], { gap: 4 }),
  { x: 7.3, y: 4.6, w: 5.43, h: 1.6, fontSize: 14 });
note(s, "Positive = LH₂ uses more energy. At sea includes the cargo hydrogen LH₂ burns. Haber-Bosch power and sea days are still placeholders, so the net figure will move with them.", 6.4, 0.45);

// ================= 15b. How efficient would the liquefier have to be? =================
s = lead("LH2 vs NH3",
  "To match the ammonia plant a liquefier would need 3.27 kWh/kg H₂, below the 3.9 minimum, so no liquefier can close the upstream gap",
  "LiqH₂VC Database Rev 0 · Section 13.3 · power at the plant fence, MW · 100,000 t H₂ a year, 8,000 operating hours a year",
  "Hold the ammonia route fixed and sweep the liquefier's energy use. The LH2 line rises with the liquefier energy; the NH3 lines are flat. They would cross at 3.27 kWh/kg with the placeholder Haber-Bosch demand and at 0.94 kWh/kg with the team's 1 kWh/kg H2. Both points sit inside the shaded region, below the minimum work to liquefy hydrogen, so no liquefier can reach them. Even at the top of the placeholder range, 0.7 kWh/kg NH3, the crossing is 3.83 kWh/kg, just below 3.9. Liquefaction cannot be engineered into a win on upstream electricity; it could only win if the ammonia plant drew far more than assumed.");
const LQ = { x0: 1.25, x1: 8.3, y0: 1.95, y1: 5.2, ymax: 150, xmax: 12 };
const lqx = (v) => LQ.x0 + (LQ.x1 - LQ.x0) * v / LQ.xmax, lqy = (v) => LQ.y1 - (LQ.y1 - LQ.y0) * v / LQ.ymax;
txt(s, "Power at the plant fence, MW", { x: X0, y: 1.55, w: 4.0, h: 0.3, fontSize: 12, bold: true, color: C.text2 });
s.addShape(pres.shapes.RECTANGLE, { x: lqx(0), y: LQ.y0, w: lqx(3.9) - lqx(0), h: LQ.y1 - LQ.y0, fill: { color: HEX.tint }, line: { color: HEX.tint }, objectName: "liq-unreachable-zone" });
s.addShape(pres.shapes.RECTANGLE, { x: lqx(8), y: LQ.y0, w: lqx(9) - lqx(8), h: LQ.y1 - LQ.y0, fill: { color: HEX.lilac, transparency: 45 }, line: { type: "none" }, objectName: "liq-khi-band" });
[0, 50, 100, 150].forEach((v) => {
  s.addShape(pres.shapes.LINE, { x: LQ.x0, y: lqy(v), w: LQ.x1 - LQ.x0, h: 0, line: { color: HEX.grid, width: 0.75 } });
  txt(s, String(v), { x: X0, y: lqy(v) - 0.12, w: 0.5, h: 0.24, fontSize: 11, align: "right", valign: "middle" });
});
for (let v = 0; v <= LQ.xmax; v += 2) {
  s.addShape(pres.shapes.LINE, { x: lqx(v), y: LQ.y1, w: 0, h: 0.08, line: { color: HEX.text, width: 0.75 } });
  txt(s, String(v), { x: lqx(v) - 0.3, y: LQ.y1 + 0.1, w: 0.6, h: 0.25, fontSize: 11, align: "center" });
}
s.addShape(pres.shapes.LINE, { x: LQ.x0, y: LQ.y1, w: LQ.x1 - LQ.x0, h: 0, line: { color: HEX.text, width: 0.75 }, objectName: "liq-axis" });
txt(s, "Liquefier energy, kWh per kg H₂", { x: LQ.x1 - 3.0, y: LQ.y1 + 0.36, w: 3.0, h: 0.25, fontSize: 11, align: "right" });
s.addShape(pres.shapes.LINE, { x: lqx(3.3), y: LQ.y0, w: 0, h: LQ.y1 - LQ.y0, line: { color: HEX.title, width: 1.25, dashType: "dash" }, objectName: "liq-min-3.3" });
s.addShape(pres.shapes.LINE, { x: lqx(3.9), y: LQ.y0, w: 0, h: LQ.y1 - LQ.y0, line: { color: HEX.title, width: 1.25 }, objectName: "liq-min-3.9" });
txt(s, "Unreachable: below the minimum work to liquefy, 3.3 kWh/kg (dashed) or 3.9 with ortho-para conversion", { x: lqx(0) + 0.08, y: LQ.y0 + 0.08, w: 1.8, h: 1.1, fontSize: 11, color: C.accent1 });
txt(s, "KHI 8–9", { x: lqx(8) - 0.2, y: LQ.y0 + 0.05, w: lqx(9) - lqx(8) + 0.4, h: 0.25, fontSize: 11, bold: true, align: "center" });
// LH2 line (liquefier 12.5 MW per kWh/kg + 0.683 MW export-tank boil-off), clipped at the top of the plot
const lqEnd = (LQ.ymax - 0.683) / 12.5;
s.addShape(pres.shapes.LINE, { x: lqx(0), y: lqy(LQ.ymax), w: lqx(lqEnd) - lqx(0), h: lqy(0.683) - lqy(LQ.ymax), flipV: true, line: { color: HEX.purple, width: 3 }, objectName: "liq-lh2-line" });
s.addShape(pres.shapes.LINE, { x: LQ.x0, y: lqy(41.6), w: LQ.x1 - LQ.x0, h: 0, line: { color: HEX.blue, width: 3 }, objectName: "liq-nh3-placeholder" });
s.addShape(pres.shapes.LINE, { x: LQ.x0, y: lqy(12.5), w: LQ.x1 - LQ.x0, h: 0, line: { color: HEX.blue, width: 3, dashType: "dash" }, objectName: "liq-nh3-team" });
[[3.27, 41.6, "liq-parity-1"], [0.94, 12.5, "liq-parity-2"]].forEach((p) =>
  s.addShape(pres.shapes.OVAL, { x: lqx(p[0]) - 0.1, y: lqy(p[1]) - 0.1, w: 0.2, h: 0.2, fill: { color: HEX.dark }, line: { color: "FFFFFF", width: 1.5 }, objectName: p[2] }));
txt(s, "3.27", { x: lqx(3.27) - 0.68, y: lqy(41.6) - 0.31, w: 0.5, h: 0.25, fontSize: 12, bold: true, align: "right" });
txt(s, "0.94", { x: lqx(0.94) + 0.2, y: lqy(12.5) + 0.05, w: 0.7, h: 0.22, fontSize: 12, bold: true });
// legend row
const lgY = 5.88;
[[X0 + 0.65, "LH₂ route", HEX.purple, null, 1.0], [X0 + 2.5, "NH₃ placeholder Haber-Bosch", HEX.blue, null, 2.45], [X0 + 5.75, "NH₃ team input (dashed)", HEX.blue, "dash", 2.0]].forEach((l, i) => {
  s.addShape(pres.shapes.LINE, { x: l[0], y: lgY + 0.14, w: 0.4, h: 0, line: { color: l[2], width: 3, dashType: l[3] || "solid" }, objectName: "liq-legend-line-" + (i + 1) });
  txt(s, l[1], { x: l[0] + 0.5, y: lgY, w: l[4], h: 0.28, fontSize: 12, valign: "middle" });
});
box(s, 8.65, 1.65, 4.08, 4.45, HEX.tint, "liq-stats");
stat(s, 8.9, 1.8, 3.6, "113 vs 42 MW", "LH₂ liquefier route against the ammonia route at 9 kWh/kg: 2.7 times the power", { size: 26, bh: 0.5, lh: 0.65, name: "liq-power" });
stat(s, 8.9, 3.1, 3.6, "3.27 → 0.94 kWh/kg", "Liquefier energy that would match ammonia, with the placeholder and then the team Haber-Bosch input", { size: 24, bh: 0.5, lh: 0.8, name: "liq-parity" });
stat(s, 8.9, 4.6, 3.6, "3.9 kWh/kg", "Minimum work to liquefy (3.3 without ortho-para conversion); Kawasaki's 8–9 is 49–43 % of it", { size: 26, bh: 0.5, lh: 0.8, name: "liq-min" });
note(s, "Placeholder Haber-Bosch 0.60 kWh/kg NH₃ (about 3.4 kWh/kg H₂, estimate, source needed); team input 1 kWh/kg H₂; 60,000 m³ export tank each route. Minimum work: US DOE Hydrogen Program Record 9013 (2009); the 49–43 % is an upper bound because Kawasaki's feed pressure is unconfirmed. Today's liquefier would match ammonia only if Haber-Bosch drew 1.46–1.64 kWh/kg NH₃, 2.4–2.7 times the placeholder.", 6.3, 0.65);

// ================= 16. Sensitivities and annual case =================
s = lead("LH2 vs NH3",
  "The ranking can flip: LH₂ uses the least energy if Haber-Bosch needs more than ~2.65 kWh/kg H₂, or once electrolysis is counted",
  "LiqH₂VC Database Rev 0 · Sections 13.6 and 13.8 · kWh per kg H₂ delivered; supply case 100,000 t H₂ a year",
  "Haber-Bosch energy is the swing input: the team value of 1 kWh/kg H2 may exclude the air separation unit. The placeholder range with air separation, 2.8-3.9 kWh/kg H2, is above the break-even.");
const hl = (t) => ({ text: t, options: { bold: true, color: HEX.title } });
table(s, ["Case", "LH₂", "NH₃ gas-fired", "NH₃ clean fuel"], [
  ["Default inputs", "13.27", hl("11.36"), "11.66"],
  ["LH₂ ship boil-off 0.2 %/day, not 0.40", "12.72", hl("11.36"), "11.66"],
  ["Haber-Bosch 2.65 kWh/kg H₂, not 1", hl("13.27"), hl("13.27"), "13.78"],
  ["Haber-Bosch 3 kWh/kg H₂, not 1", hl("13.27"), "13.68", "14.23"],
  ["Electrolysis counted, 60 kWh/kg", hl("78.49"), "81.00", "88.80"],
], { x: X0, y: 1.65, w: 7.6, colW: [3.7, 1.2, 1.35, 1.35], rowH: 0.62, fontSize: 14, objectName: "sensitivity-table" });
txt(s, "Lowest energy in each case shown in purple. Electrolysis case: slides 18 and 19.", { x: X0, y: 5.5, w: 7.6, h: 0.3, fontSize: 12 });
box(s, 8.55, 1.65, 4.18, 4.45, HEX.tint, "annual-case");
txt(s, "Delivering 100,000 t of H₂ a year", { x: 8.8, y: 1.8, w: 3.7, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
stat(s, 8.8, 2.2, 3.7, "5 vs 4 ships", "40,000 m³ ships for LH₂ against gas-fired NH₃; LH₂ needs 4.97, close to a sixth", { size: 28, bh: 0.5, lh: 0.65, name: "ships" });
stat(s, 8.8, 3.5, 3.7, "108.7 vs 116.1 ktpa", "Hydrogen to produce for 100 ktpa delivered (LH₂ against gas-fired NH₃)", { size: 26, bh: 0.5, lh: 0.65, name: "produced" });
stat(s, 8.8, 4.8, 3.7, "152 vs 130 MW", "Average chain power, 1,327 against 1,136 GWh a year", { size: 26, bh: 0.5, lh: 0.65, name: "power" });
note(s, "Round trip 42.5 days (two 20-day legs, two 1.25-day port calls), 90 % ship availability (assumption), 7.73 voyages per ship a year. The liquefier draws about 112 MW here, against 103 MW in Section 12.1, because it must make 108.7 ktpa.", 6.3, 0.6);

// ================= 16b. Full value chain including electrolysis =================
s = lead("LH2 vs NH3",
  "Counting the electrolysis of the hydrogen each route consumes adds 65–77 kWh/kg and puts LH₂ ahead: 78.49 against 81.00 kWh/kg",
  "LiqH₂VC Database Rev 0 · Section 13.7 · full value chain with electrolysis · kWh per kg H₂ delivered · electrolyser 60 kWh/kg H₂ (assumption)",
  "Until now both routes started from the same hydrogen gas. In practice each route consumes a different amount of hydrogen for the same delivery: 2,832 t per LH2 cargo and 4,871 t per NH3 cargo. Adding the electrolysis of that hydrogen on top of the earlier chain makes electrolysis 83-87 % of the energy. The NH3 routes pay more for it because they lose more hydrogen, which outweighs what they save in the rest of the chain. One point needs care: the earlier chain counts hydrogen burned on the ship and ammonia burned in the cracker as energy used, and once electrolysis is added those are already paid for, so counting them again overstates the totals. The corrected totals are 75.59, 76.35 and 80.53 kWh/kg, and LH2 is still lowest but by only about 1 %.");
const cats16b = ["NH₃, clean-fuel cracker · 88.80", "NH₃, gas-fired cracker · 81.00", "LH₂ route · 78.49"];
const ser16b = [
  ["Electrolysis of the hydrogen consumed", [77.14, 69.64, 65.22], HEX.purple],
  ["Rest of the chain (Section 13.6)", [11.66, 11.36, 13.27], HEX.blue],
];
s.addChart(pres.charts.BAR, ser16b.map((r) => ({ name: r[0], labels: cats16b, values: r[1] })), chartOpts({
  x: 0.5, y: 1.55, w: 8.0, h: 4.6, barDir: "bar", barGrouping: "stacked", barGapWidthPct: 45,
  chartColors: ser16b.map((r) => r[2]), showValue: true, dataLabelPosition: "ctr", dataLabelColor: "FFFFFF", dataLabelFontBold: true,
  dataLabelFormatCode: "0.00", valAxisMinVal: 0, valAxisMaxVal: 100, valAxisMajorUnit: 20, valAxisLabelFormatCode: "0",
  showLegend: true, legendPos: "t", catAxisLabelFontSize: 13, objectName: "electrolysis-chart",
}));
txt(s, "NH₃ energy as % of LH₂ (LH₂ = 100)", { x: 8.9, y: 1.65, w: 3.83, h: 0.35, fontSize: 15, bold: true, color: C.text2 });
const up = (t) => ({ text: t, options: { bold: true, color: HEX.title } });
table(s, ["NH₃ route", "Without", "With", "Corrected*"], [
  ["Gas-fired", "86", up("103"), up("101")],
  ["Clean fuel", "88", up("113"), up("107")],
], { x: 8.9, y: 2.1, w: 3.83, colW: [1.05, 0.9, 0.7, 1.18], rowH: 0.45, fontSize: 12, objectName: "electrolysis-views-table" });
txt(s, "Above 100 = NH₃ uses more energy than LH₂ (shown in purple). Without and With electrolysis are the chain on slide 14 and the same chain plus electrolysis.", { x: 8.9, y: 3.6, w: 3.83, h: 0.85, fontSize: 12 });
txt(s, [{ text: "*Corrected: ", options: { bold: true } },
  { text: "the earlier chain counts hydrogen burned on the ship (2.90 kWh/kg) and ammonia burned in the cracker (4.65 and 8.27) as energy used. With electrolysis they are already paid for, so they are removed. Totals become 75.59, 76.35 and 80.53 kWh/kg." }],
  { x: 8.9, y: 4.5, w: 3.83, h: 1.65, fontSize: 12 });
note(s, "Electrolysis is 83 % of the LH₂ route's energy and 86–87 % of the NH₃ routes'. The NH₃ routes consume more hydrogen per kg delivered (4,871 t against 2,832 t a cargo; 86.2 % and 77.8 % delivered against 92.0 %). At 100,000 t a year: 7,849, 8,100 and 8,880 GWh, or 896, 925 and 1,014 MW average.", 6.3, 0.65);

// ================= 16c. What the electrolysis result depends on =================
s = lead("LH2 vs NH3",
  "The tie hinges on the electrolyser: LH₂ leads above ~50 kWh/kg H₂, gas-fired NH₃ below it; the cost gap is only USD 0.21/kg",
  "LiqH₂VC Database Rev 0 · Sections 13.7 and 13.9 · NH₃ minus LH₂, kWh per kg H₂ delivered · cost in USD per kg H₂ delivered, cost year not stated",
  "Plotted is the energy of each NH3 route minus the LH2 route as the electrolyser energy changes; above zero means NH3 uses more. As computed, gas-fired NH3 and LH2 tie at about 26 kWh/kg, below the 33.3 kWh/kg that the hydrogen itself contains, so LH2 would lead for any electrolyser above that. With the overlap removed they tie at about 50 kWh/kg, and the clean-fuel route at about 35. So the electrolyser energy needs a sourced value before the ranking can be settled. On cost, charging the hydrogen feed through the electrolysis electricity at USD 140/MWh makes the feed by far the largest cost, and the gap between the routes shrinks from USD 0.545 to USD 0.21 per kg. Gas-fired NH3 stays cheapest because part of its energy is natural gas, about USD 44/MWh against USD 140/MWh for electricity.");
const sweepE = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70];
// Burned cargo per kg delivered: LH2 2.8985, gas-fired NH3 4.65, clean-fuel NH3 8.2667 kWh/kg; without electrolysis 13.275, 11.356, 11.658;
// hydrogen consumed per kg delivered 1.08695 (LH2), 1.16072 (gas-fired), 1.28572 (clean fuel). Checked against the model at 26, 40, 50, 60 and 65 kWh/kg.
const dAs = sweepE.map((e) => +((11.356 + 1.16072 * e) - (13.275 + 1.08695 * e)).toFixed(2));
const dGas = sweepE.map((e) => +((11.356 - 4.65 + 1.16072 * e) - (13.275 - 2.8985 + 1.08695 * e)).toFixed(2));
const dClean = sweepE.map((e) => +((11.658 - 8.2667 + 1.28572 * e) - (13.275 - 2.8985 + 1.08695 * e)).toFixed(2));
txt(s, "NH₃ minus LH₂, kWh per kg H₂ delivered (above zero = NH₃ uses more)", { x: X0, y: 1.6, w: 7.9, h: 0.3, fontSize: 14, bold: true, color: C.text2 });
s.addChart(pres.charts.LINE, [
  { name: "Gas-fired NH₃, overlap removed", labels: sweepE.map(String), values: dGas },
  { name: "Gas-fired NH₃, as computed", labels: sweepE.map(String), values: dAs },
  { name: "Clean-fuel NH₃, overlap removed", labels: sweepE.map(String), values: dClean },
], chartOpts({
  x: 0.5, y: 1.95, w: 8.0, h: 4.2, chartColors: [HEX.blue, "9DBFEA", HEX.dark], lineSize: 3, lineDataSymbol: "none",
  valAxisMinVal: -4, valAxisMaxVal: 8, valAxisMajorUnit: 2, valAxisLabelFormatCode: "0",
  catAxisLabelPos: "low", showCatAxisTitle: true, catAxisTitle: "Electrolyser energy, kWh per kg H₂ produced",
  catAxisTitleFontSize: 12, catAxisTitleColor: HEX.text, catAxisTitleFontFace: "+mn-lt",
  showLegend: true, legendPos: "t", objectName: "electrolyser-sweep-chart",
}));
box(s, 8.9, 1.65, 3.83, 4.5, HEX.tint, "electrolysis-stats");
stat(s, 9.15, 1.8, 3.4, "~50 kWh/kg", "Electrolyser energy at which gas-fired NH₃ and LH₂ tie, overlap removed (about 35 for clean fuel; 26 as computed)", { size: 26, bh: 0.5, lh: 0.9, name: "tie" });
stat(s, 9.15, 3.2, 3.4, "USD 10.33 vs 10.54", "per kg with the hydrogen feed charged, gas-fired NH₃ against LH₂; the gap falls from USD 0.545 to 0.21", { size: 24, bh: 0.5, lh: 0.9, name: "cost-feed" });
stat(s, 9.15, 4.65, 3.4, "795 / 881 vs 744 MW", "Average electrolyser power, gas-fired / clean-fuel NH₃ against LH₂: 7 % and 18 % more", { size: 22, bh: 0.5, lh: 0.8, name: "electrolyser-size" });
note(s, "Electrolyser 60 kWh/kg H₂ is an assumption and needs a sourced value. Cost charges the electrolysis electricity at USD 140/MWh (team input) and removes burned hydrogen and ammonia already paid for; the assessment's own cost sheet does not remove them and shows USD 10.88, 10.96 and 12.38 per kg.", 6.35, 0.6);

// ================= 17. Energy cost =================
s = lead("LH2 vs NH3",
  "On energy cost alone, gas-fired ammonia is cheapest at USD 1.208/kg H₂ against USD 1.754 for LH₂; liquefier power is ~78 % of the LH₂ bill",
  "LiqH₂VC Database Rev 0 · Section 13.9 · energy cost · USD per kg H₂ delivered, cost year not stated",
  "Only energy is priced: no capital, charter, port, carbon or hydrogen-feed cost. The hydrogen price only affects LH2, through the cargo it burns.");
const cats17 = ["NH₃, clean-fuel cracker · 1.579", "NH₃, gas-fired cracker · 1.208", "LH₂ route · 1.754"];
const ser17 = [
  ["Export plant electricity", [0.181, 0.163, 1.374], HEX.purple],
  ["Marine fuel oil", [0.004, 0.004, 0.025], HEX.grey],
  ["Ammonia fuel", [1.352, 0.840, 0], HEX.blue],
  ["Natural gas", [0, 0.160, 0], HEX.teal],
  ["Import terminal electricity", [0.041, 0.041, 0.007], HEX.lilac],
  ["Cargo H₂ burned as ship fuel", [0, 0, 0.348], HEX.dark],
];
s.addChart(pres.charts.BAR, ser17.map((r) => ({ name: r[0], labels: cats17, values: r[1] })), chartOpts({
  x: 0.5, y: 1.55, w: 8.0, h: 4.6, barDir: "bar", barGrouping: "stacked", barGapWidthPct: 45,
  chartColors: ser17.map((r) => r[2]), showValue: true, dataLabelPosition: "ctr", dataLabelColor: "FFFFFF", dataLabelFontBold: true,
  dataLabelFormatCode: '[<0.1]"";0.00', valAxisMinVal: 0, valAxisMaxVal: 2, valAxisMajorUnit: 0.5, valAxisLabelFormatCode: "0.0",
  showLegend: true, legendPos: "t", catAxisLabelFontSize: 13, objectName: "energy-cost-chart",
}));
box(s, 8.9, 1.65, 3.83, 4.45, HEX.tint, "cost-stats");
stat(s, 9.15, 1.8, 3.4, "USD 54.5 M a year", "Energy-cost gap between LH₂ and gas-fired NH₃ at 100,000 t a year", { size: 26, bh: 0.5, lh: 0.65, name: "gap" });
stat(s, 9.15, 3.1, 3.4, "USD 1.406/kg", "LH₂ energy cost even at a hydrogen price of zero, still above gas-fired NH₃", { size: 26, bh: 0.5, lh: 0.65, name: "zero" });
stat(s, 9.15, 4.4, 3.4, "USD 1.99/kg", "Hydrogen price below which LH₂ beats the clean-fuel NH₃ route", { size: 26, bh: 0.5, lh: 0.65, name: "breakeven" });
note(s, "Prices are team inputs in USD with no cost year: electricity 140 USD/MWh, marine fuel oil 553 USD/t, natural gas 13 USD/MMBtu (LHV), ammonia 700 USD/t; hydrogen 4.00 USD/kg (assumption); import electricity held equal to export (placeholder). Labels under 0.10 hidden.", 6.3, 0.6);

// ================= 18. Summary =================
s = lead("LH2 vs NH3",
  "Neither carrier wins on every measure: ammonia leads on energy cost and ships, LH₂ on hydrogen delivered and energy with electrolysis",
  "LiqH₂VC Database Rev 0 · Section 13.10 · summary of the LH₂ vs NH₃ screening",
  "This is a screening view of energy and energy cost. The capital-cost and shipping-economics comparison still needs feasibility-study cost data.");
const cols = [
  ["Where LH₂ is ahead", HEX.purple, ["Delivers 92.0 % of the hydrogen it starts with, against 86.2 % and 77.8 % for NH₃",
    "The import terminal only vaporises the liquid: 0.05 kWh/kg, no chemical conversion",
    "Uses the least energy once electrolysis is counted: 78.49 against 81.00 kWh/kg, but by only ~1 % with burned cargo not counted twice"]],
  ["Where NH₃ (gas-fired cracker) is ahead", HEX.blue, ["Less energy per kg delivered before electrolysis: 11.36 against 13.27 kWh/kg",
    "Lower energy cost: USD 1.208 against 1.754 per kg; with the hydrogen feed charged the gap falls to USD 0.21",
    "Fewer ships for 100,000 t a year: 4 against 5",
    "Upstream, even a perfect liquefier could not match the ammonia plant"]],
];
cols.forEach((c, i) => {
  const x = X0 + i * 6.165, w = 5.965;
  s.addShape(pres.shapes.RECTANGLE, { x, y: 1.65, w, h: 0.6, fill: { color: c[1] }, line: { color: c[1] }, objectName: "summary-head-" + (i + 1) });
  txt(s, c[0], { x: x + 0.2, y: 1.65, w: w - 0.4, h: 0.6, fontSize: 18, bold: true, color: C.background1, valign: "middle" });
  box(s, x, 2.25, w, 3.35, HEX.tint, "summary-body-" + (i + 1));
  txt(s, bullets(c[2], { gap: 14 }), { x: x + 0.25, y: 2.5, w: w - 0.5, h: 3.0, fontSize: 17 });
});
box(s, X0, 5.8, W, 0.65, "FFFFFF", "summary-caveat", HEX.lilac);
txt(s, [{ text: "Not yet decided:  ", options: { bold: true, color: C.accent4 } },
  { text: "capital cost, ship cost and shipping economics still need cost data from a full feasibility study." }],
  { x: X0 + 0.2, y: 5.8, w: W - 0.4, h: 0.65, fontSize: 15, valign: "middle" });

// ================= 19. Open items =================
s = lead("LH2 vs NH3",
  "Six open items could change the result; closing them needs supplier and vessel data, the internal ammonia dataset and a feasibility study",
  "LiqH₂VC Database Rev 0 · Sections 10.2, 11, 12.3 and 13.10 · open items",
  "These are the inputs to firm up next. The first two matter most for the ranking.");
table(s, ["Open item", "Current value", "Why it matters"], [
  ["Haber-Bosch energy", "1 kWh/kg H₂ (team input)", "May exclude air separation. NH₃ stays ahead only below ~2.65 kWh/kg H₂ (2.25 with a clean-fuel cracker)"],
  ["LH₂ ship boil-off", "0.40 %/day (team input); 0.2 %/day in Section 12.2", "No full-scale data. Each extra 0.1 %/day removes about 2 % of the cargo over 20 sea days"],
  ["Sea days per cargo", "20 (assumption)", "No corridor fixed. Sets ship count and fuel; LH₂ is close to a sixth ship (4.97)"],
  ["Electrolyser energy", "Not counted in 13.2–13.6; 60 kWh/kg H₂ in 13.7 (assumption)", "Puts LH₂ ahead by only ~1 % once burned cargo is not counted twice; the routes tie at ~50 kWh/kg, so it needs a source"],
  ["Other NH₃ values", "Re-liquefaction 0.25 kWh/kg, density 682 kg/m³, LHV 18.6 MJ/kg (estimates)", "To be replaced with the internal ammonia dataset and the import-terminal power price"],
  ["Not yet included", "—", "Plant, ship and terminal CAPEX and OPEX, charter, carbon cost (CO₂, N₂O), safety and permitting"],
], { x: X0, y: 1.6, w: W, colW: [2.6, 3.9, 5.63], rowH: [0.42, 0.68, 0.68, 0.6, 0.6, 0.68, 0.6], fontSize: 13, objectName: "open-items-table" });
note(s, "Database-wide gaps also open: LH₂ regulation and permitting (Section 11), liquefaction, regas and ship costs (Section 12.3), and the reference tank size behind 24 USD/kg (Section 10.2).", 6.4, 0.45);

// ================= 20. Close =================
pres.addSection({ title: "Close" });
s = pres.addSlide({ masterName: "COVER", sectionTitle: "Close" });
s.addText("Questions and discussion", { placeholder: "title" });
s.addText([{ text: "LH" }, { text: "2", options: { subscript: true } }, { text: " Value Chain Technology Database, Rev 0" }], { placeholder: "date" });

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
