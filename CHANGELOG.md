# Changelog

## Marketplace 1.0.1 — 11 Nov 2026
brainstormer 0.5.1.

## Marketplace 1.0.0 — 11 Nov 2026
Public repo under KeyValueSoftwareSystems: both plugins, examples, flow docs, validate/package scripts, CI + tag-based releases, README for the Peasy team, LICENSE (code) + NOTICE (Peasy brand assets). Internal Jira keys removed; Peasy's Jira format kept as conventions in `ticket-format.md`.

## peasy-brainstormer
- **0.5.1** (11 Nov 2026) — Brief playback is a formatted chat message (Problem / In v1 / Out / Flow / Decisions with source / Assumed / Still open) instead of one block of text inside the question; the question itself is just "Is the brief right?".
- **0.5.0** (11 Nov 2026) — Merged share package v1.2 into the Jira PRD output: `pm-thinking.md` replaces `question-bank.md` (draft the PRD silently, rate Known/Guess/Unknown, ask only the highest-impact gaps); `peasy-context.md` §11 "Domain traps"; quality bar checked before publishing; design brief lists non-happy states; "Peasy Jira conventions" section in `ticket-format.md`.
- **0.4.0** (4 Nov 2026) — Jira-style PRD output following Peasy's Jira structure. Skill writes only `prd.json`; `assets/prd/` has fixed template, `build.py` (embeds mockup, "Scherm N" deep links), `prd_lint.py`, `example-prd.json`. Senior dev + PM audit applied (metrics, NFRs, idempotency, price re-check, privacy, MoSCoW, risks, rollout, DoD). Old `ticket-template.html` removed.
- 0.3.0 — question bank; HTML ticket with PRD/Mockup tabs.
- 0.2.1 — attachments become "Decisions made".
- 0.2 — `peasy-context.md`, quick mode, plain-text question fallback.

## peasy-design
- **1.1.0** (30 Oct 2026) — offline Peasy Design System bundled (tokens.json + tokens.css, components, fonts, logos, 37 icons, mascot, backdrops), self-contained React mockup starter, offline mode + rebuild-in-own-account instructions; screens labelled "Scherm N · <name>", states as toggles.
