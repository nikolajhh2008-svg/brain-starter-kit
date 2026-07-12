# The onboarding interview (for Claude: offered in setup step 6 — or whenever the human says "interview me for my brain")

Goal: after this conversation the brain knows its human. The interview is
**optional and deferrable** — the brain already works without it; this is
the deepening. Two phases: an optional **local discovery** (with explicit
consent), then the **interview** — which works far better once you have
something concrete to ask about. It also works in pieces: a block now, a
block next week.

## Phase 0 — Ask THIS first (verbatim, before any question):

> "Before the interview: may I look around this computer — folders like
> Documents and your projects, and my own past sessions with you — to
> pre-fill your brain with what I find? I'll list everything I looked at,
> nothing leaves this machine, and you can veto any note. Yes or no is
> both fine — the interview works either way."

**If yes:** spend a few minutes scanning what the permissions allow —
`~/Documents`, `~/Desktop`, project folders, git repos (authors, README
names), and prior Claude session context if available. Extract people,
projects, deadlines, interests, tools. Then:
- pre-fill draft notes (marked `source: local discovery, {{DATE}}`),
- open the interview with what you found: **"I saw X — tell me about
  it"** beats every generic question,
- report the list of locations you touched, and delete anything they veto.

**If no:** skip silently, never mention it again.

## How to interview (people don't know what to say — help them)

Ask **block by block**, voice dumps welcome, any order, skipping allowed.
The golden rule: **never leave a thin answer thin.** When someone says
"hmm, not much" — give them three concrete options to react to (the
per-block nudges below), name examples, ask for names/dates/numbers.
React to what they said before moving on ("you mentioned a brother —
what's his name?"). Decompose everything into ATOMIC notes afterwards:
**one person = one note** (`30-knowledge/people/`), **one idea = one
note**, everything linked. Invent nothing; mark gaps as "open → ask
later". If they say "private": don't write it down, don't probe.

## Block 1 — You at a glance
1. Who are you in three sentences — name, age, where you live, what you
   mainly do right now (school / university / job / your own thing)?
2. How would you describe yourself — and which part would others
   instantly confirm?
   *Nudge if stuck: night owl or early bird? builder or planner?
   starts things or finishes things?*

## Block 2 — Your people
3. Who counts as family, and who actually plays a role in your daily
   life (who lives where, with whom)?
4. Who are your closest friends — names plus one line each?
5. Which people matter at school/university/work (mentor, boss, teacher,
   business partner)?
   *Nudge: who would you call first with a problem? who do you learn
   the most from? anyone you actively avoid?*

## Block 3 — Everyday life & obligations
6. What does a normal week look like — what's fixed, what's flexible?
7. Which dates, deadlines or exams are coming in the next 3 months?
   (Everything counts, official stuff too — the brain becomes your
   deadline memory.)
   *Nudge: exams · applications · renewals/contracts · trips · family
   dates · anything governmental (license, service, visa, taxes).*
8. Which ongoing duties are you carrying — and which are you pushing
   ahead of you?

## Block 4 — Zoom in: your work or your studies (adaptive)
This block is where the brain earns its keep: knowing someone's actual
tasks — not their title — is what later lets it take work off their
plate. **Narrow down first, then go deep.** Ask which applies (studying /
working / both) and follow only the fitting branch; both if both.

**If working:**
- What exactly is your job — what does the work consist of, concretely?
  *Nudge: not the title, the activities. "I check price lists, answer
  customer mails, prepare orders" beats "sales".*
- Which tasks come back every single week?
  *Nudge: reports? invoices? stock checks? the same three mails? List
  them — recurring work is the most valuable thing this block collects.*
- Where does most of your time actually go — and which part of that
  annoys you the most?
- Which programs or tools do you work in daily — and which one fights
  you the most?
- Who do you work with most closely (names, roles)?

**If studying (school or university):**
- Where are you (school/university, which year) — and what's the big
  goal right now (final exams, degree, a specific grade)?
- Which subjects or courses demand the most from you right now?
- What eats most of your learning time?
  *Nudge: summarizing? memorizing? writing? procrastinating one
  specific subject?*
- Which exams, submissions or presentations are coming up — with dates?
- Which apps or tools do you use for school — notes, flashcards,
  calendar?

## Block 5 — Projects & goals
9. What are you actually working on right now (work, school, personal) —
   and which of these projects is closest to your heart?
   *Nudge: also the unofficial stuff — a side project, something you
   build/learn at night, something you promised someone.*
10. What should be different 12 months from now?
11. The bigger picture: where do you want to be in ~5 years — which part
    is a dream, which is already a plan?

## Block 6 — Knowledge & interests
12. What are you genuinely good at — what do people come to you for?
13. What do you want to learn next?
    *Nudge: a skill for work/school · a language · a tool (AI? coding?) ·
    something physical (sport, instrument, license)?*
14. What do you consume regularly and gladly (books, podcasts, channels,
    creators) — and which of it actually shapes your thinking?
15. Which hobbies do you REALLY do regularly — and which only exist on
    paper?
    *Nudge: what did you actually do last weekend? what would friends
    say you always talk about?*

## Block 7 — Working style & energy
16. When during the day are you most productive, and what does your real
    (not ideal) sleep/energy rhythm look like?
17. How do you learn/work best — honestly, as it is?
18. What currently eats most of your time or nerves?
    *Nudge: a duty? a person? commuting? your phone? something you keep
    postponing?*
19. What should Claude do more often in your collaboration — and less?

## Block 8 — Closing
20. What do you have genuine respect for in the coming year?
21. What else should your brain absolutely know that I didn't ask about?
22. Are there areas that stay fundamentally "private"? (I'll create a
    no-go note so future sessions respect it too.)

## After the interview (mandatory processing)
- Merge the interview with any Phase-0 discovery drafts (interview wins
  on conflicts — the human's words beat file traces)
- People individually into `30-knowledge/people/` (template:
  `_templates/person-note.md`) · facts/principles/goals as atomic notes
  into `30-knowledge/` or `10-projects/` (templates: `knowledge-note.md`,
  `project-note.md`; fill `{{DATE}}` with real dates) — search before
  creating to avoid twins
- Dates into `Deadlines.md` (one line per date, date first) · self-image
  into `About me.md` (as a hub with links, including a "remaining gaps"
  list)
- Recurring tasks and time sinks from the zoom-in block become one note
  per area (`20-areas/`) — that's the raw material for everything an
  assistant can later take off their plate
- Refresh `Home.md` — new projects/deadlines/open questions from the
  interview belong on the dashboard immediately
- Set frontmatter, link everything, `git commit`
- Ask 3–5 follow-up questions about the biggest gaps
