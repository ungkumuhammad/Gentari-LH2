# `literature/` — Source dossiers

Structured, cited one-file-per-source dossiers that Zane builds when digesting an
individual paper/report in depth (as opposed to the weekly `digests/` scan).
Filename: `YYYY-<venue>-<short-title>.md`.

Each dossier carries the full citation, the paper's scope, its extractable
findings (**each cited to the paper**), the relevance to this repo, and — where
the full text could not be accessed — an explicit **"full-text extraction
pending"** list of items to confirm. Nothing here is promoted into the repo-wide
`../../data/` registry without separate user approval (see `../AGENT.md` §3–§4).
Sources are also mirrored into [`../sources/staging.csv`](../sources/staging.csv).

## File kinds here

- `YYYY-<venue>-<short-title>.md` — **curated dossier** (Zane's synthesis: key
  items, figures, repo relevance).
- `*.fulltext.md` — **machine-generated full-text Markdown** of a source PDF,
  converted with [Microsoft markitdown](https://github.com/microsoft/markitdown).
  Faithful to the PDF text but may carry two-column/subscript artifacts — verify
  figures against the original PDF in `../sources/raw/` before citing.

Current sources with in-repo full text (PDF + `*.fulltext.md`):
- **JMSE 2025** — Passalacqua & Traverso, *From LNG to LH2 in Maritime Transport*
  (DOI 10.3390/jmse13091748).
- **RSER 2026** — Towhid & Hossain, *Advances and challenges in cryogenic LH2
  maritime transportation* (DOI 10.1016/j.rser.2026.116850).
