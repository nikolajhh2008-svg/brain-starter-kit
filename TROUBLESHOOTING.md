# FAQ & troubleshooting

**Obsidian shows nothing?** Obsidian → "Open folder as vault" → pick
`~/Brain`. Done — Obsidian and Claude work on the same files.

**Do I need to know Markdown?** No. You dump ("capture: …"), Claude does
structure. In Obsidian you just click [[links]].

**Why not iCloud/Dropbox?** Cloud sync + Git on the same folder causes
file conflicts and corrupted vaults. For your phone: Obsidian Sync.

**Can my brain be in German (or any language)?** Yes — the repo is
English, but during setup Claude asks for your vault language and writes
(and translates the starter pages) accordingly. Only folder names stay
English so the skills keep working.

**Inbox overflowing?** That's what the weekly ritual is for: "brain
review" — Claude processes the inbox to zero. Second brains die of full
inboxes, not missing features.

**I stopped using it for weeks — is it dead?** No. That's a design case,
not a failure: the next "brain review" catches up in prioritized batches
(deadlines first), sweeps what the weeks actually produced, and refreshes
`Home`. No guilt, no restart needed — just say "brain review".

**Claude filed something wrong (or I want to undo something)?** Every
review and ingest reports exactly what went where — nothing is silent.
To undo: tell Claude ("move that note / undo the last review") or use
Git yourself (`git log`, `git checkout -- <file>`). The brain is
versioned; every change is one commit away from undone.

**`Home` looks stale?** The weekly review refreshes all four blocks
(projects, deadlines, open questions, new notes); deadline captures
update the deadline block immediately. Out of sync anyway? Say
"refresh Home".

**Claude doesn't know my brain in a new session?** The rules from setup
step 4 (in `~/.claude/CLAUDE.md`) tell every session where the brain
lives. Test it: ask "search my brain for X".

**Why do the folder numbers jump (…40, then 90)?** The gap is expansion
space: optional modules (journal, media log, health, money …) slot in as
50–80 without re-sorting anything. Ask Claude to add one anytime.

**Can I rename folders?** Area folders are named after YOUR life —
Claude creates them with your words during setup. Keep the numbered
top-level scheme (stable sorting) and the English top-level names (the
skills depend on them).

**What does NOT belong in the brain?** Operational knowledge of active
code projects (belongs in that repo's CLAUDE.md) and anything you call
"private".

**Setup died halfway?** A fresh install can simply be removed
(`rm -rf ~/Brain`) and restarted — nothing else on your machine changed
except `~/.claude/skills/` and the rules block in `~/.claude/CLAUDE.md`,
both safe to re-run. An adopted vault: ask Claude to undo its last
changes via Git.

**Broke Git / wrong commit?** No drama: `cd ~/Brain && git log --oneline`
shows history, `git checkout -- <file>` restores a file. When in doubt,
ask Claude — the brain is versioned, nothing is ever truly gone.

**I already have an Obsidian vault.** Tell Claude during setup — it will
adopt your existing structure (scan, map, add only what's missing)
instead of overwriting anything.

**A newer kit version came out — how do I update?** One sentence to
Claude: *"Update my brainwarden setup from
https://github.com/nikolajhh2008-svg/brainwarden — follow the Updating
section in SETUP-FOR-CLAUDE.md."* Your notes are never touched; updates
only replace skills, the search tool and the dashboard scaffolding.

**How do I uninstall completely?** Three things and you're clean:
`rm -rf ~/Brain` (or keep it — it's just Markdown), delete the five
`brain-*` folders from `~/.claude/skills/`, and remove the "Brain" block
from `~/.claude/CLAUDE.md`. Nothing else was touched.

**Does it work with Obsidian's Canvas and Bases?** Yes — the vault is
plain Markdown, so every Obsidian feature works on top. If you want
Claude to build canvases (visual maps) or bases (table views) for you,
install Obsidian's official Claude skills for markdown/canvas/bases and
just ask ("build me a canvas map of my thesis project").

**Can Claude run the weekly review on its own (unattended)?** Yes — but
it's opt-in, and you should know the trade-offs first:
- **It spends your Claude subscription.** Every unattended run uses plan
  usage like a normal session. A weekly review is cheap; anything more
  frequent adds up fast. Weekly is the sweet spot — never sub-daily.
- **It edits and commits on its own.** Safe *because* the vault is
  Git-backed — every change stays one `git checkout` from undo — and it
  follows the review skill's autonomous rules: it deletes nothing
  uncertain, archives nothing unasked, and parks every question under
  Home's "Open questions" instead of a chat you'll never see.
- **It's a convenience, not the system.** The manual "brain review" is
  the real ritual; the scheduler just presses the button on weeks you
  forget. A phone reminder is the simpler, free alternative.

Two ways to set it up: the easiest is **Claude Code Desktop → Routines**
(same on macOS/Windows/Linux: New routine → Local → your `~/Brain` →
instructions "run the brain-review skill on this vault" → Weekly).
Terminal users can instead ask Claude — *"set up an automatic weekly
brain review"* — and it writes the scheduler job for your OS (launchd /
cron / Task Scheduler, with the full path to `claude` — scheduled tasks
don't know your PATH).

## Windows quirks

**`claude` says "not recognized" although the install reported success?**
Re-run the install from CMD instead of PowerShell:
`curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`

**Setup hangs at `mkdir`/copy commands?** Almost always: Git for Windows
is missing, so Unix-style commands run in PowerShell where they're
invalid. Install [Git for Windows](https://git-scm.com/downloads/win)
(default settings), open a fresh terminal, restart `claude`. Check with
`claude doctor` — it should find Git Bash. Paths looking mangled
(`C:Userscl`)? Same cause, same fix.

**`python3` "not recognized"?** Windows Python usually ships `python`
and `py`, not `python3`. Tell Claude: *"python3 doesn't exist here, use
py -3"* — it will also fix the search command in your global CLAUDE.md
so future sessions use the right one.

**Using WSL and Obsidian can't open the vault (or is very slow)?**
Obsidian is a Windows app and handles `\\wsl$` paths badly — known
Obsidian limitation, not a kit bug. Put the vault on the Windows side
(`C:\Users\You\Brain` = `/mnt/c/Users/You/Brain` from WSL): Obsidian
opens it normally, and the speed difference is not noticeable at a few
hundred Markdown files.

## Capturing on the go (mobile)

Your vault lives locally and is versioned with Git — three honest ways
to feed it from your phone, each with a catch:

1. **Obsidian Sync** (easiest, ~$4/month): install the Obsidian app on
   your phone, enable Sync for the vault. The rule that keeps it safe:
   **Git on the desktop, Sync to the phone — never both on the same
   device against the same folder** (that's where corrupted-vault
   stories come from).
2. **Quick-capture shortcut into `00-inbox/`** (free, still needs a
   sync): an iOS Shortcut or Android automation that appends text to an
   inbox file — but the text only reaches your desktop via some sync
   (way 1, or iCloud with all its Git caveats). A typing shortcut, not a
   transport.
3. **Phone notes app + one capture** (free, zero setup, always works):
   jot or dictate into your normal notes app; back at the computer, one
   *"capture: [paste]"* to Claude. Costs you one manual step in the
   evening — and nothing else.

What we don't promise: real-time sync everywhere, zero-cost + zero-setup
at once, or running Git itself from the phone (possible via Working
Copy/MGit, but far more setup than this kit asks of anyone).
