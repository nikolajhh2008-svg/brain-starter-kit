---
name: brain-review
description: Weekly review of the Brain (~/Brain) — inbox to zero, surface open loops, archive stale items. Use on "brain review", "clean up my brain", "what's in the inbox", ideally on a fixed weekday.
---

# Brain review (5–10 minutes, weekly)

Keeps the brain alive — the #1 killer of second brains is an inbox nobody
empties.

## Steps
1. **Inbox to ZERO** (hard rule): PROCESS every file in `~/Brain/00-inbox/`
   (except `Inbox rule.md`) — never just move it:
   - paraphrase into a proper note (frontmatter, vault language, matching
     template from `_templates/` — knowledge-note / project-note /
     area-note / person-note; fill `{{DATE}}` with the real date) and file
     by ACTIONABILITY: project → `10-projects/…` · area → `20-areas/…` ·
     keeper knowledge → `30-knowledge/…` · person → `30-knowledge/people/`
   - **dedup first:** `python3 ~/Brain/.tools/search.py <name/topic>` —
     extend an existing note rather than creating a twin
   - **triage:** reference material (links, clippings, recommendations —
     "find it again later") gets the light treatment: one note, tags,
     done. Full atomization is only for material the person builds on.
   - or delete it (say so — deleting is a feature).
   **More than ~20 inbox files?** Work in prioritized batches (deadlines →
   decisions → people → rest) and report what remains — never half-process
   silently.
2. **Sweep the week (the safety net):** captures are best-effort — the
   review is the guarantee. Look at what the week ACTUALLY produced and
   compare it against the brain: recently modified files in their project
   folders, `git log` of active repos, and session context if available.
   Decisions, deadlines, people or milestones that never got captured →
   into the inbox now, then process them like everything else.
3. **Deadlines:** new dates from the week → `Deadlines.md`; past dates out.
4. **Contradiction check:** compare this week's new/changed notes against
   `40-decisions/` — flag anything that quietly contradicts a recorded
   decision ("this clashes with [[2026-05-10-x]], decided because Y —
   revisit or comply?"). A reversal is a NEW decision record, never an
   edit of the old one.
5. **Open loops:** list 3–5 things that look stalled (projects without
   recent notes, "open → ask" markers) and ask about them — and offer:
   "want me to research the researchable ones?" (→ skill `brain-research`).
6. **Connections:** name 1–3 non-obvious connections between this week's
   notes and older ones — the things search never surfaces because nobody
   thinks to search for them. Add the `[[link]]` only where it truly
   changes how a note reads.
7. **Hygiene:** orphan notes (no inbound links), dead `[[links]]`, empty
   files — fix or report.
8. **Structure check (quarterly-ish):** if an area/folder no longer matches
   the person's life, propose renaming/archiving it. The onboarding interview
   was a starting point, not a cage.
9. **Refresh `Home.md`:** active projects under "Right now", next 3 dates
   under "Next deadlines", the open loops under "Open questions", this
   week's notes under "New this week". Home must always show the current
   state of the brain.
10. **Commit:** `cd ~/Brain && git add -A && git commit -m "review YYYY-MM-DD"`.
11. Report: what was filed where, what was deleted, what needs their
    input — every filing decision visible, everything reversible via Git.

## Rules
- Never let the inbox survive a review.
- Archive beats delete for finished projects; delete beats archive for noise.
- Missed weeks are normal — the review is built to catch up (batches),
  never to guilt-trip. Welcome them back, don't scold.
