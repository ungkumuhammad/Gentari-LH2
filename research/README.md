# `research/` — Zane, the LH2 Research Agent

This folder is the workspace for **Zane**, a Senior Principal Hydrogen & Ammonia
Engineer sub-agent focused on **liquid hydrogen (LH2)** research. Zane pulls from
research papers, licensor/OEM material, standards bodies, institutional reports,
and market news — and **cites every number**.

## How to use Zane

- **On demand:** address the agent by name — *"Zane, find the latest on
  large-scale LH2 liquefier efficiency"* — or dispatch the `zane` sub-agent
  (`.claude/agents/zane.md`). Calling Zane grants standing consent to research
  public sources autonomously (see the consent model in
  [`AGENT.md`](AGENT.md) §4).
- **Automatically:** a scheduled trigger runs the **weekly LH2 news digest**
  every **Monday 07:00 Malaysia Time (Sunday 23:00 UTC)**, writes a dated file
  to [`digests/`](digests/), commits & pushes, and notifies you.

## Layout

```
research/
  AGENT.md                 ← Zane's operating charter (READ FIRST when acting as Zane)
  README.md                ← this file
  digests/                 ← dated weekly LH2 news digests (YYYY-MM-DD-lh2-weekly.md)
  profiles/                ← sourced licensor / technology-provider profiles
  sources/
    staging.csv            ← isolated source registry for everything Zane cites
  templates/
    weekly-digest-template.md
```

## Ground rules (full detail in `AGENT.md`)

- **No fabricated numbers.** Every figure is cited (`(Org, Year)` + a row in
  `sources/staging.csv` with URL/DOI + access date) or explicitly tagged
  `[ASSUMPTION: …]` / `[ESTIMATE – needs source: …]`.
- **Isolated by default.** Zane's findings live in this folder. Promoting a
  figure into the repo-wide `../data/references.csv` and `../data/` tables is a
  **separate, explicit approval** — this keeps the proprietary Kawasaki database
  clean.
- **LH2 is the standing focus.** Zane's broader expertise (NH3, e-methane, SAF,
  e-methanol, LOHC) is available when you name that carrier in a request; the
  weekly loop is LH2-only.
- **Source terms respected.** Cite and link; summarize paywalled material, don't
  reproduce it.
