# Changelog

## [Unreleased]

- **Interview goes deeper where it counts:** new adaptive block 4
  ("Zoom in: your work or your studies") — narrow down first
  (studying / working / both), then follow the fitting branch into
  concrete tasks, recurring work, time sinks and tools. Recurring
  tasks land as area notes: the raw material for everything an
  assistant can later take off your plate.
- **Deadlines.md states its format:** one line per deadline, date
  first (`2026-08-15` or `15.08.2026`) — readable for humans and
  parseable for tools that treat the file as the deadline source.

## [1.2.0] — 2026-07-10

For everyone: works with the vault you already have, wherever it lives.

- **The vault path is no longer hardcoded.** Setup records your real
  vault location in a `Brain vault:` line in the global rules, and all
  five skills follow it — an adopted vault stays exactly where it is
  (iCloud folder, different name, anything). `~/Brain` is just the
  default for fresh installs. The plugin install now genuinely works
  for people who already have a vault.
- **Non-English setups fixed end-to-end** (found by a fresh from-zero
  test): the "leave templates untouched" rule no longer contradicts the
  translate instruction (tokens stay, prose translates), and the raw
  zone's README joined the translate list.
- **Search stops indexing templates** — no more placeholder noise in
  results — and the decision template uses one date format throughout.
- **Windows made calmer:** the tutorial's stage 1 is jargon-free (one
  install, one sentence), details moved to the Windows section in
  TROUBLESHOOTING; the skills name the `py -3` fallback.

## [1.1.0] — 2026-07-10

Depth release: notes now grow over time instead of staying thin — plus
platform hardening from real end-to-end tests.

- **Maturity status for knowledge notes:** `status: seed | growing |
  evergreen` in the note schema — thinness stays honest, and the review
  gets its deepening queue
- **The review compounds depth:** two new steps — deepen 2–3 seed notes
  toward the anatomy each week, and a random revisit that keeps old
  corners alive; plus explicit autonomous-mode rules for scheduled runs
- **Note anatomy per type** documented in the vault CLAUDE.md (a
  knowledge note wants evidence, one concrete case and a
  counter-position — "atomic" means one idea, not few words)
- **"The red line"** — the AI-gardens-it-does-not-author doctrine is now
  an operational rule Claude loads every session, not just philosophy
- **Optional unattended weekly review** documented (Claude Desktop
  Routines or a scheduler job) with an honest subscription-cost warning
- **Windows hardening:** Git-for-Windows guidance up front, `py -3`
  fallback for the search tool, a Windows quirks section in
  TROUBLESHOOTING; **mobile capture** gets an honest FAQ (Sync vs.
  shortcut vs. notes-app — and what we don't promise)
- **Safety fixes from adopt/update end-to-end tests** (also shipped as a
  hotfix to 1.0.0): adopting an existing vault can no longer overwrite
  the user's files, no duplicate first-win projects, migration backlog
  lands on Home, updates refresh the whole vault CLAUDE.md, and the
  vault ships its own `.gitignore`

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
