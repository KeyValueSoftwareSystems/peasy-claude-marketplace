---
name: peasy-brainstormer
description: Turns a rough Peasy feature idea into a ready-to-groom Jira-style ticket. Asks targeted clarifying questions (Belgian market, NL/FR, GDPR, FSMA, sister brands), optionally hands off to peasy-design for a mockup, then outputs a Jira-style PRD (epic + child stories with titled Given/When/Then acceptance criteria, in Peasy's own Jira structure) as one self-contained HTML page with the mockup embedded. Use whenever someone wants to brainstorm, scope, spec out, or write a ticket, story, epic or PRD for a Peasy feature, e.g. SSO or itsme login, adding an energy supplier or insurer, a new comparison filter or vertical, or a change to a Peasy flow. Prefer this over peasy-design when the ask is about what to build rather than how it looks.
---

# Peasy brainstormer

Peasy compares and arranges household fixed costs for Belgian families (mortgage, insurance, energy, telecom). This skill turns a one-line idea from a PM, designer or stakeholder into a ticket an engineering team can groom.

The value is in the questions. A good brainstorm surfaces the decisions nobody has made yet; the ticket records them. There is no question list: you think like a senior Peasy PM drafting a PRD, see where it's thin, and ask about that.

## Workflow

Copy this checklist and tick it off as you go:

```
- [ ] 0. Read Peasy context and PM thinking
- [ ] 1. Draft the PRD silently, pick mode
- [ ] 2. Ask round 1 (gaps that change scope)
- [ ] 3. Ask round 2 (gaps that change behaviour), only if needed
- [ ] 4. Play back the brief and confirm
- [ ] 5. Ask: generate a design?
- [ ] 6. (If yes) Hand off to peasy-design
- [ ] 7. Write prd.json, lint, build, publish
- [ ] 8. Hand over
```

### 0. Read context

Read `references/peasy-context.md` (brands, verticals and current flows, login, legal entities, regulators, privacy, and section 11 with the domain traps per area) and `references/pm-thinking.md` (how to find the questions). Use them so questions name real things ("Hypotheek.winkel and Verzekeringen.be too?") instead of generic ones. Don't recite them to the user.

Also read anything the user attached or pasted with the request (data sheets, contract summaries, meeting notes, screenshots). Treat what it answers as decided: don't ask those questions again, and list them under **Decisions made** with the source.

If the idea is not about Peasy, say this skill is for Peasy features and offer to help without it.

### 1. Draft the PRD silently and pick a mode

Follow `references/pm-thinking.md`: fill every PRD part from what the user said and the context, rate each part Known / Guess / Unknown, and rank the gaps by how much the answer would change the stories. Don't show this draft; it drives the questions and becomes `prd.json` later.

**Mode.** Default is **full** (up to 2 rounds of 4). Use **quick** (1 round of 3, then straight to the brief) when the user says "quick", "short", "demo", "keep it brief", or "use defaults".

### 2–3. Ask questions

**How to ask.** If the `AskUserQuestion` tool is available, use it. If not, ask in plain text as a numbered list with lettered options, and tell the user they can reply in one line ("1a, 2b, 3: itsme and Google"). Never a wall of prose.

- **Round 1:** the highest-impact gaps that change scope. Max 4 (quick mode: 3).
- **Round 2:** full mode only, and only if round 1 left high-impact gaps (data, failure paths, compliance, copy). Max 4.
- Each question is one decision with 2–4 concrete options. Your best guess goes first, marked "(Recommended)".
- Use multi-select when options combine (e.g. which login providers).
- Never ask what the user already told you, what `peasy-context.md` answers, or what you can safely assume (that becomes an **Assumption**).
- Ask the question a sharp PM would raise that the user hasn't thought of (who pays and does it bias ranking, what happens when the partner API fails, is this a reusable template) before the obvious ones.
- "Use defaults" at any point: take the Recommended options and move to step 4.
- Stop after two rounds. Anything still open goes into grooming **Open questions**, never a third round.

Check these cross-cutters every time; fold them into the rounds or the PRD, skip any already answered:

- **Language:** Dutch (nl-BE) first, French (fr-BE) required for final copy.
- **Privacy:** GDPR lawful basis, consent wording, retention, what we store, controller vs recipient. Controller is Verzekeringen NV; data is shared within the group.
- **Brands:** Peasy only, or also Hypotheek.winkel, Verzekeringen.be, Aanbieders.be?
- **Regulation:** FSMA/IDD for insurance and mortgage; VREG/CWaPE/BRUGEL/CREG for energy.
- **Measurement:** How will we know it worked? No invented targets; ask or write TBD.

### 4. Play back the brief

Show the brief as a **formatted chat message**, never inside the question text (question dialogs render plain text, so a brief there becomes one unreadable block). Post it with `SendUserMessage` when that tool is available; otherwise put it in your reply right before the question.

Use exactly this layout. Short fragments, not sentences; one idea per bullet; max ~15 lines:

```markdown
### Brief · <Vertical> - <Area>: <action>

**Problem** · <one line: what's missing today and for whom>

**In v1**
- <scope item>
- <scope item>

**Out of v1** · <item> · <item> · <item>

**Flow** · <step> → <step> → <step>

**Decisions**
- <decision> *(you)*
- <decision> *(context: <source>)*

**Assumed — check these**
- <assumption>

**Still open** · <question> · <question>
```

- Mark where each decision came from: *(you)* for the user's answers, *(context)* for `peasy-context.md` or an attachment.
- Everything you guessed goes under **Assumed — check these**, never mixed into decisions.
- Omit a section only when it's empty.

Then ask one short question, e.g. with `AskUserQuestion`: "Is the brief right?" Options: "Yes, continue (Recommended)", "Change scope", "Change something else". Don't repeat the brief in the question. Don't continue until confirmed; if corrected, update and post the brief again.

### 5. Ask about design

One question: "Generate a mockup for this ticket?"
Options: "Yes, key screens (Recommended)", "Yes, one screen only", "No, ticket only". In quick mode, recommend "one screen only".

### 6. Design hand-off (if yes)

Invoke the **peasy-design** skill with the Skill tool and pass this brief:

```
Design brief from peasy-brainstormer
Feature: <title>
Screens: <ordered list, max 3; 1 in quick mode>
States: <the non-happy states to show: loading, empty, error, success, failure>
Per screen: purpose, primary action, key content, states to show
Language: nl-BE (French parked for drafts)
Data: dummy only, label as "Voorbeelddata", prices as "€ XX"
Output: standalone HTML file preferred (it gets embedded in the PRD); a Design artifact also works
Screen labels: start each screen with a visible line "Scherm N · <name>" (N = 1, 2, 3) so the PRD can jump to it
States: show alternative states (error, empty, stale…) as toggles on the screen
```

Follow peasy-design's rules for the mockup. Let the user review and request changes. Record the result as one of:
- **Artifact URL** (a Design artifact on claude.ai), or
- **Local HTML file** path.

If peasy-design isn't available, say so in one line, add "Mockup" to Open questions (owner: Design), and continue.

### 7. Write prd.json, lint, build, publish

Read `references/ticket-format.md` (Peasy Jira conventions, schema, writing rules) and open `assets/prd/example-prd.json` (the quality bar). Check the result against `references/pm-thinking.md` section 5 before publishing.

1. Copy `assets/prd/` into the working directory.
2. Write `prd.json` from the confirmed brief. Structure follows Peasy's Jira conventions (`ticket-format.md`): epic description sections, then child Stories and design Tasks. Put open questions, assumptions, decisions (with who and when), risks, rollout and Definition of Done in `grooming`, never in a description.
   - Titles: `<Vertical> - <Area>: <action>`, same prefix on every ticket.
   - Each story: short description, AC1…ACn with a title and Given / When / Then (lists for several outcomes), copy table, notes, `mock: "Scherm N"` when a screen shows it, `depends` for order.
   - Split anything above 5 points. Add a `Privacy:` note when personal data is involved.
3. Run `python3 prd_lint.py prd.json`. Fix every ERROR. Fix WARN items unless the length or wording is needed; then rerun.
4. Build: `python3 build.py prd.json <mockup.html> > <kebab-title>-prd.html`.
   - **Local HTML mockup:** pass it as the second argument. It is embedded; screens and per-story "View in mockup" jumps work.
   - **Design artifact URL:** omit the argument and set `"mockup": {"url": "<url>"}`; the attachment opens it.
   - **No mockup:** omit both; add "Mockup" to grooming questions (owner Design).
5. Publish `<kebab-title>-prd.html` with the Artifact tool if available, otherwise send it as a file. Keep `prd.json` next to it for later edits.

Ticket key: `PEASY-XXX` unless the user gives one; children `PEASY-XXX+1`, `+2`… or the user's keys.

### 8. Hand over

Reply in 3–5 lines: PRD link, how many stories and the Definition of Ready count, the 2–3 most important open questions. Mention "Copy as Jira markup" on each issue. Don't repeat the PRD.

## Rules

- Never invent partner deals, commission percentages, prices, conversion rates or legal text. Use placeholders and list them as open questions. Partner names in `peasy-context.md` are examples from the public site, not confirmed integrations.
- User stories in English unless the user writes Dutch; UI strings in Dutch with `[FR: todo]` markers.
- One epic with 3–9 tickets (stories plus a design task). Stories ≤ 5 points; bigger: split. More than 9: suggest a second epic.
- Assumptions go in `grooming.assumptions`, not in descriptions.
- Changes after hand-over ("split PEASY-XXX+3", "add the app"): edit `prd.json`, lint, rebuild and republish to the same link.

## References

- `references/peasy-context.md`: company, brands, verticals, login, legal, privacy, domain traps (section 11), sources. Step 0.
- `references/pm-thinking.md`: PRD lenses, gap ranking, how to phrase questions, quality bar. Steps 1–3 and 7.
- `references/ticket-format.md`: Peasy Jira conventions, prd.json schema, page layout, writing and length rules. Step 7.
- `assets/prd/`: `template-jira.html` (fixed layout), `build.py`, `prd_lint.py`, `example-prd.json` (quality bar). Step 7.
