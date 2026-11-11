# PRD format (Jira-style issue view)

The ticket follows Peasy's own Jira epic structure (see **Peasy Jira conventions** below). Write **only** `prd.json`; `assets/prd/template-jira.html` renders it and `assets/prd/build.py` bundles it with the mockup. `assets/prd/example-prd.json` is the quality bar: copy its shape and tone.

Goal: crisp tickets developers can groom fast. Content freedom is allowed: add a detail block, table or note whenever the ticket needs it. Length rules are guidance (lint warnings), structure rules are not (lint errors).

## Peasy Jira conventions

Modelled on Peasy's real energy epics (keys are kept out of this repo).

- **Keys:** `<PROJECT>-<number>`. Use the key the user gives; otherwise `PEASY-XXX` for the epic and `PEASY-XXX+1`, `+2`… for children. In dependencies, lead with the key when one exists.
- **Titles:** `<Vertical> - <Area>: <action>`, same prefix on every ticket (e.g. `Energy - New Engine Admin: add supplier`).
- **Epic description sections, in order:** Summary · Goal & Business Value · People (Business Owner, Functional Analyst, Key Stakeholder, QA) · Scope & Impact (included / excluded) · Dependencies · Design & Details · Technical Design Document.
- **Story sections:** Description · AC1…ACn, each titled, written Given / When / Then / And · Design & Details (Figma link, NL/FR/EN copy table, Notes) · Technical Implementation Details (FE / BE docs).
- **Design work** is a separate Task, not part of a story.
- Grooming notes are comments; decisions go in history (who, when).

## Files and commands

```bash
cp -r <skill>/assets/prd ./prd && cd prd
# write prd.json (start from example-prd.json)
python3 prd_lint.py prd.json                       # fix every ERROR; fix WARN unless there's a reason
python3 build.py prd.json mockup.html > <kebab-title>-prd.html   # mockup optional
```

## prd.json schema

```jsonc
{
 "epic": {
  "key": "PEASY-XXX",                       // or the user's key
  "title": "<Vertical> - <Area>: <outcome>", // e.g. "Energy - Supplier integration: New supplier via API"
  "fields": {"Type":"Epic","Status":"To groom","Priority":"Medium","Assignee":"TBD","Reporter":"<user>",
             "Created":"YYYY-MM-DD","Updated":"YYYY-MM-DD","Components":"Web, Back-office","Fix version":"TBD",
             "Labels":["energy","provider-onboarding","gdpr"]},
  "figma": "TBD",  "tdd": "TBD",             // links or TBD
  "summary": "≤ 2 sentences: what changes, for whom.",
  "problem": "1–2 sentences: the problem today.",
  "goals": ["outcome, ≤ 15 words", "..."],  // 2–5
  "metrics": [["Metric","Baseline","Target"]], // rows; use [X] / [current] placeholders, never invented numbers
  "people": {"Business Owner(s)":"TBD","Functional Analyst(s)":"TBD","Key Stakeholder(s)":"...","QA / Tester(s)":"TBD"},
  "scope": {"included":["label"], "excluded":["label"]},
  "dependencies": ["PEASY-123 Supplier screen: why", "..."],  // lead with a Jira key when one exists
  "details": [ BLOCK ],                      // e.g. Non-functional table (security, privacy, a11y, perf, observability, release)
  "notes": ["one fact per bullet"]
 },
 "tickets": [{
  "key": "PEASY-XXX+1", "type": "Story" | "Task",
  "title": "<Vertical> - <Area>: <action>",  // same prefix as the epic
  "moscow": "Must|Should|Could", "points": 1|2|3|5,  // > 5 → split
  "status": "To groom", "assignee": "TBD", "priority": "Medium",
  "description": "≤ 2 sentences: what changes.",
  "depends": ["PEASY-XXX+n"],               // becomes "is blocked by / blocks" links
  "ac": [{"title":"≤ 8 words","given":"…","when":"…","then":"one outcome" | ["outcome","outcome"],"and":["optional"]}],
  "copy": [["Use","NL","FR or empty","EN or empty"]], // empty FR/EN render as [FR: todo]/[EN: todo]
  "details": [ BLOCK ],                     // state tables, Visible/Hidden tables, mapping tables …
  "notes": ["Privacy: …", "rules, constraints, edge facts"],
  "mock": "Scherm N",                       // screen in the mockup this story shows
  "figma": "TBD", "fe": "TBD", "be": "TBD", // Frontend / Backend Technical Document links
  "briefing": "TBD"                         // Task (design) only
 }],
 "grooming": {                              // never part of the ticket description; shown as a comment + history
  "questions": [["Question","Owner","Due","Blocks: All | KEY, KEY"]],
  "assumptions": ["…"],
  "decisions": [["Question","Decision","By","YYYY-MM-DD"]],
  "risks": [["Risk","Likelihood","Impact","Mitigation"]],
  "rollout": ["Phase 0 …","Phase 1 …"],
  "dod": ["…"]
 },
 "mockup": {"file":"x.html"} | {"url":"https://claude.ai/artifact/…"}   // set by build.py for local files
}
```

`BLOCK` = `{"title":"…","table":[["Head","Head"],["cell","cell"]]}` or `{"title":"…","items":["…"]}` or `{"title":"…","text":"…"}`.

## What the page shows (fixed by the template)

- **Left:** PRD navigation: the epic, every child issue, and the sections of the current issue (ACs nested). Scroll-tracked.
- **Epic:** Description (Summary + Problem panel, Goal & Business Value + Success metrics, People, Scope & Impact, Dependencies, Design & Details, Technical Design Document), Attachments, Child issues, Activity (grooming notes as a comment, decisions as history).
- **Story:** Description, Acceptance Criteria (AC1 — title, Given / When / Then / And), Design & Details (Figma, Copy & messages NL/FR/EN, blocks, Notes), Technical Implementation Details (FE/BE docs), Attachments (mockup screen), Linked work items.
- **Right:** status, Details (assignee, reporter, labels, priority, components, fix version, story points, parent), Definition of Ready (computed: missing Figma, tech docs, FR copy, > 5 pts, blocking questions).
- "Copy as Jira markup" exports the open issue without grooming notes.

## Writing rules

- One behaviour per AC. Outcomes as a list, not "X and Y and Z" in one line. Observable results only ("is shown", "is stored"), never "works", "correctly", "dashboard shows".
- Use "must"/present tense; no "should", "might", "ideally", "etc.".
- At least one error or edge AC per story (timeouts, invalid input, double submit, stale data, user mid-flow).
- Split a story above 5 points; frontend, backend and Ops work are usually separate stories.
- Story touching personal data (EAN, address, email, consent, payload) → add a `Privacy:` note.
- Every UX string in `copy`. NL first; FR empty until provided (lint warns, release is blocked).
- Name Peasy components (Button, TextField, OfferCard, SelectorPill…) when specifying UI. New UI = "proposed".
- Design work is a separate `Task` ticket, listed before the stories that need it in `depends`.
- No invented numbers, partners, fees or legal text: `€ XX`, `[X]`, `[Partner]`, `[Legal text: todo]`, `[SLA]`.
- Plain English, short sentences. Dutch only in UI strings.

## Readability guidance (lint warns above these)

| Field | Guide |
|---|---|
| epic.summary, ticket.description | ≤ 45 words |
| goal, scope item | ≤ 15 / ≤ 10 words |
| AC title | ≤ 8 words |
| given / when / each then line | ≤ 20 words |
| ACs per story | ≤ 8 |
| note, open question | ≤ 25 / ≤ 20 words |
