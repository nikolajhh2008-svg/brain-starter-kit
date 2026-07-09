# Changelog

## [1.0.0] — 2026-07-09

Initial public release.

- **Setup built around the first win:** three questions, then Claude
  builds your real first notes itself — areas, first project, deadlines
  and a populated `Home` dashboard, minutes in. The deep onboarding
  interview comes after that, and only if you want it.
- **`Home.md`** — a living dashboard Claude keeps current: active
  projects, next deadlines, open questions, new this week
- Vault template: PARA-inspired structure (`00-inbox` / `10-projects` /
  `20-areas` / `30-knowledge` / `40-decisions` / `90-archive`) with
  deliberate numbering gaps for optional modules (journal, media,
  health, money, or your own)
- Five Claude Code skills: `brain-capture`, `brain-ingest` (with
  reference-vs-build triage), `brain-ask` (cited answers from your own
  notes), `brain-review` (weekly sweep, contradiction check against past
  decisions, connection surfacing), `brain-research` (sourced enrichment)
- Guided setup: TUTORIAL.md for humans, SETUP-FOR-CLAUDE.md as the
  AI-driven installer; global rules make the brain ambient in every
  Claude session; existing vaults are adopted (or quarantined into
  `OLD_VAULT/`), never overwritten
- Local search tool (`.tools/search.py`), a named template for every
  note type, examples, troubleshooting/FAQ, MIT license
