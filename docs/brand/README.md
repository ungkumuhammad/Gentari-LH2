# Gentari brand — main brand for all deliverables

> **Status:** registered as this repo's **main brand** (user instruction, 2026-10-09).
> Every deck, report, chart or page made in this repo follows this file unless
> the user says otherwise for a specific deliverable.
>
> **Provenance:** a working draft compiled from the assets and theme tokens in the
> user's `frontendengineeringmodel` repository
> ([`assets/gentari-brand-reference.webp`](assets/gentari-brand-reference.webp)),
> plus two reference slides the user supplied as the house deck style
> ([`assets/deck-reference-cover.webp`](assets/deck-reference-cover.webp),
> [`assets/deck-reference-leadin.png`](assets/deck-reference-leadin.png)).
> It is **not** Gentari's official brand guideline. If an official guideline or
> PowerPoint master arrives, it overrides this file — record it in
> `sources/raw/` and update this page.

---

## 1. Logo

| Asset | Use |
|-------|-----|
| Primary lockup: cyan icon + purple `gentari` wordmark | Light backgrounds only (the purple wordmark needs contrast) |
| Icon alone (cyan) | On Gentari Purple or dark backgrounds |
| Cover lockup: cyan icon + cyan wordmark on purple | As on the reference cover; reused through [`assets/cover-background.png`](assets/cover-background.png) |

Only full-colour versions are available. No white, mono, horizontal or vector
(SVG/EPS) version has been supplied — the cover artwork in this repo is a
1600 × 900 px raster taken from the reference cover.

## 2. Core colours

| Name | Hex | RGB | Use |
|------|-----|-----|-----|
| **Gentari Purple** | `#60269E` | 96 38 158 | Wordmark colour; headings, title backgrounds, primary actions. Cover background (sampled `#60269D` on the reference cover — same colour) |
| **Gentari Cyan** | `#00C8E8` | 0 200 232 | Icon colour; accents and highlights. White text on cyan fails contrast — use dark text |

## 3. Dashboard UI palette (light theme, from `Dashboard/app/globals.css`)

| Token | Hex | | Token | Hex |
|-------|-----|-|-------|-----|
| primary | `#6B2E99` | | background | `#F8FAFC` |
| accent-foreground | `#441D62` | | muted | `#F1F5F9` |
| accent | `#F1EAF6` | | card | `#FFFFFF` |
| foreground | `#0F1729` | | success | `#21C45D` |
| muted-foreground | `#65758B` | | warning | `#F59F0A` |
| border | `#E1E7EF` | | destructive | `#DC2828` |

The dashboard `primary` (`#6B2E99`) is close to, but not, the logo purple —
for brand work such as decks use `#60269E`. The dashboard dark theme switches
primary to blue (`#3C83F6`), which is not a brand colour.

## 4. Typography

No brand typeface is defined in the source repo (the wordmark is lettering, not
an installable font). House deck fonts, per the user's instruction:

| Element | Font | Notes |
|---------|------|-------|
| Deck cover title and date | **Verdana** (title Bold) | Matches the reference cover |
| Deck headings and body (all other slides) | **Calibri** | Theme heading and body font |
| Web / dashboard pages | Inter or another clean geometric sans | Neutral stand-in until the official typeface is confirmed |

## 5. House deck style (PowerPoint)

Built from the two reference slides. 16:9, 13.333 × 7.5 in.

**Cover** — full-bleed Gentari Purple, logo top-left, glass swirl artwork on the
right (both in `assets/cover-background.png`, with the title area cleared).
Title white Verdana Bold, left-aligned, ~32 pt; date white Verdana below it.

**Content ("lead-in") slides** — white background.

| Element | Spec |
|---------|------|
| Confidentiality marking | `Confidential - For PETRONAS Staff Only`, top centre, ~10 pt, green `#75BA75` |
| Lead-in title | A full-sentence message carrying the slide's finding (the numbers in it), Calibri Bold ~28 pt, purple **`#7030A0`**, top-left, up to two lines, no period |
| Chart series | purple `#4A3AA7`, blue `#2977D6`; highlight / break-even marks dark `#1F2933` |
| Tables | Header row dark `#1F2933` with white bold text; row rules `#E8E8E4`; first column bold |
| Body / notes text | warm dark grey `#3A3935`; method/basis note under the chart ~11 pt |
| Gridlines | `#E8E8E4` |
| Footer | Bottom-left one-line topic + unit line (e.g. "Ammonia cracker CAPEX · … · MM USD"); page number bottom-right |

The lead-in title purple (`#7030A0`) is what the reference slide uses; it is
slightly lighter than Gentari Purple (`#60269E`). Keep `#7030A0` for lead-in
titles as instructed, and Gentari Purple for covers and filled shapes.

Machine-readable values: [`tokens.json`](tokens.json).

## 6. Not yet available — get from Gentari Brand / Comms

- Official brand typeface(s) and type scale
- Logo clear space, minimum size and misuse rules
- White, mono and horizontal logo versions, and vector (SVG/EPS) files
- Secondary / extended palette and approved gradients
- Photography, iconography, graphic devices and tone of voice
- Official PowerPoint master / slide template
