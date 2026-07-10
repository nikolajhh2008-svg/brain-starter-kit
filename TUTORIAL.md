# Tutorial: from zero to a running brain (≈ 20 minutes + optional interview)

For people who have **never used Obsidian or Claude Code**. Every stage
ends with a checkpoint ("how you know it worked").

---

## Stage 1 — Install the tools (10 min)

**Obsidian** (your window into the brain):
1. [obsidian.md](https://obsidian.md) → download → install → open.
2. Don't configure anything yet — just leave it open.

**Claude Code** (the engine):
1. You need a Claude subscription with Claude Code access → [claude.com](https://claude.com).
2. Open a terminal (Mac: `Cmd+Space` → "Terminal" · Windows: Start →
   "PowerShell" · Linux: any shell) and install — current guide:
   [claude.com/claude-code](https://claude.com/claude-code).

   **On Windows, do these two things first** (they prevent 90 % of
   Windows problems): install
   [Git for Windows](https://git-scm.com/downloads/win) with default
   settings — even if "Git" means nothing to you, it's the piece that
   lets Claude run the setup commands — and stay on native Windows
   (skip WSL unless you already live in it; Obsidian is a Windows app
   and struggles with WSL paths). After installing Claude Code, run
   `claude doctor` — it should find Git Bash. Anything acting up?
   → the Windows section in [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
3. Type `claude`, sign in with your account.

*(Would rather never touch a terminal? Install
[VS Code](https://code.visualstudio.com) and its
[Claude Code extension](https://code.claude.com/docs/en/vs-code) instead —
you get a graphical chat panel, and every later step works the same by
pasting into that panel.)*

✅ **Checkpoint:** Claude greets you with a prompt in the terminal (or in
the VS Code chat panel).

---

## Stage 2 — Start the setup (5–10 min, ends with your first win)

You don't need to download anything — **Claude does that too.** Open the
terminal, type `claude`, then say literally:

> Set up the second brain from this GitHub repo for me:
> https://github.com/nikolajhh2008-svg/brainwarden — clone it and
> follow SETUP-FOR-CLAUDE.md step by step.

Claude fetches the kit, checks your prerequisites, asks **three short
questions** (your life situation, the first thing the brain should help
with, **your brain's language** — German works fine) — and then builds
your first real notes from your answers: your areas, your first project,
your deadlines, and a `Home` page that shows it all.

*(Advanced alternative: clone the repo yourself, `cd` into it, start
`claude` and say: "Read SETUP-FOR-CLAUDE.md and set up my brain
accordingly.")*

✅ **Checkpoint:** `ls ~/Brain` shows the six core folders (`00-inbox` …
`90-archive`; the extra `_templates` folder is normal — that's where note
blueprints live) — and Claude tells you your first project is already in
there. (If "capture:" isn't recognized right away, restart Claude Code
once — fresh skills load with a new session.)

---

## Stage 3 — See it in Obsidian (2 min)

Obsidian → **"Open folder as vault"** → pick `~/Brain` → click **Home**.

This is the moment: your dashboard already shows *your* project, *your*
deadlines — a brain that's alive before you wrote a single note yourself.

✅ **Checkpoint:** `Home` names your first project under "Right now" and
you can click through to [[Deadlines]].

---

## Stage 4 — The onboarding interview (10–15 min, optional but worth it)

Claude offers this at the end of the setup — **your call, now or later.**
It's what turns a running brain into one that really *knows* you: your
people, your goals, your working style. Just talk — voice dumps welcome,
skipping allowed. Anything that shouldn't go in: just say "private".

✅ **Checkpoint:** Obsidian shows "About me" and individual people notes
under `30-knowledge/people/` — and the graph view shows its first
connections. (Skipped it? Fine — it waits as an open question on `Home`.)

---

## Stage 5 — Practice the five verbs (5 min)

**1. Capture** — in any Claude session:
> capture: idea for the next project — draft the outline by Friday

**2. Ingest** — drop a PDF (handout, paper, contract, manual) into
`~/Brain/00-inbox/raw/` and say:
> ingest

**3. Ask** — the librarian, answers only from your notes:
> what does my brain know about my first project?

**4. Review** — weekly (or right now, to test it):
> brain review

**5. Research** — the power move:
> research my brain

✅ **Checkpoint:** After the review `00-inbox/` is empty, your thought has
become a linked note — and `Home` shows it under "New this week".

---

## Your first week

| Day | What to do |
|---|---|
| Day 1 | Setup (this tutorial) — interview now or later |
| Day 2–4 | Only **capture** — every idea, date, person. No sorting! |
| Day 5 | First **"brain review"** — watch the inbox turn into notes and `Home` refresh itself |
| Day 6–7 | Pull the first **output**: "Build me a study sheet / project plan / draft for X from my notes" — and try **"research my brain"** (Claude fills your open questions with sourced facts) |

After that the system carries itself: capture on the side, ten minutes of
review per week — and if you disappear for a month, the next review just
catches up. **The success metric is output** — if the brain hasn't gifted
you a text, plan or study sheet after two weeks, tell Claude exactly that.

---

## If something breaks

→ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — and when in doubt: **just ask
Claude** ("why isn't my inbox empty?").
