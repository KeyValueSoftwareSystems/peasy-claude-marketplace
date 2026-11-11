---
name: "peasy-design"
description: "Design, write and review anything for Peasy, the Belgian service that compares and arranges household fixed costs (mortgage, insurance, energy, internet/TV). Use this skill whenever the user mentions Peasy, the Peasy design system, the Peasy mascot, or asks for a Peasy screen, landing page, flow, dashboard, chart, slide deck, document, email, banner, social post, UX copy, component spec or design audit, even if they only say 'make it on-brand' or 'use our design system' in a Peasy context. It loads the Peasy Design System artifact as the source of truth and enforces its tokens, components, voice (Dutch first, French required) and accessibility rules. When the user wants to brainstorm, scope or write a ticket, epic or spec for a feature, let peasy-brainstormer lead; it calls this skill for the mockup."
---

# Peasy design

Peasy compares and arranges household fixed costs for Belgian families. The brand promise is "easy": plain words, honest numbers, three simple steps and an expert nearby. Everything you make for Peasy must look and sound like it came from the same team, so build from the design system and never invent a colour, size, font or component.

## 1. Load the source of truth first

The Peasy Design System artifact is the single source of truth:
https://claude.ai/artifact/TcQQNoz5D9TEN9MQbDENe4

Before designing, writing copy or reviewing:

1. Read it with the Artifact tool (`action: "read"`, `url` above). If the link fails, list artifacts of the type "Design System" and pick "Peasy Design System" (this also finds a copy the user made in their own account). Do not fall back to the organisation default (CoFee) or another brand.
2. Open `project/README.md` (brand book), `project/tokens.json` (all tokens with usage notes), the relevant `project/components/<Comp>/README.md`, and `project/assets/<Group>/README.md` for any logo, icon, mascot or shape you use.
3. If the system and this skill disagree, the system wins; say so in your reply.
4. **No access to any Peasy Design System?** Don't stop and don't improvise. Use the complete offline copy bundled with this skill in `design-system/` (see section 1b). It has the same content without the `project/` prefix.

`references/brand-rules.md` is a compact copy of the rules for quick checks. It can lag behind the system; re-read the system for exact values.

## 1b. Offline mode (bundled `design-system/`)

Everything needed to work without the artifact is in `design-system/`:

| Need | File |
|---|---|
| Brand book, voice, layout, admin patterns, open decisions | `README.md` |
| All tokens with usage notes | `tokens.json` |
| Same tokens as CSS variables + `@font-face` + type classes (`.title-48`, `.body-16`…) | `tokens.css` |
| Components (React 18, `window.Peasy.*`), props, per-component rules | `components/bundle.js`, `bundle.css`, `index.d.ts`, `components/<Comp>/README.md` |
| Fonts (Grold Rounded Slim 400/500/700) | `fonts/` |
| Logo (blue + white), 37 icons as separate SVGs + sheet, mascot cut-outs, 11 backdrops, speech bubbles | `assets/Logos/`, `assets/Icons/svg/`, `assets/Mascot/`, `assets/Shapes/` |
| Ready, fully self-contained mockup page (fonts, tokens, components, React inline; no network) | `starter/peasy-mockup-starter.html` |

How to deliver each output offline:

- **Screens, flows, mockups:** copy `starter/peasy-mockup-starter.html`, replace only the SCREEN script (or add plain HTML using the token classes and `pe-*` component classes), inline any asset you use as a `data:` URL (mascot: resize to a WebP ≤ 480px tall first), and publish it with the Artifact tool as a page; without the Artifact tool, send it as a file. One file per screen, or one page with the screens stacked and labelled.
- **Want the Design, Slides or Dashboard types on-brand?** Offer once to set up the user's own Peasy Design System: create an artifact from the "Design System" type titled "Peasy Design System", follow that type's instructions, and import this folder (README → `project/README.md`, `tokens.json`, `components/`, `fonts/`, and upload the files of each `assets/<Group>/` into the asset group of the same name). After that, section 1 finds it and everything runs as normal.
- **Slide deck without a Peasy Design System:** if the user declines the setup, build the deck as a .pptx (pptx skill) using `tokens.json` colours, the logo SVG, mascot backdrops and Grold Rounded Slim, and say the font must be installed to display.
- **Dashboard:** use the Dashboard type and embed fonts and the mascot as in section 5, taking the files from `fonts/` and `assets/Mascot/`.

The bundle is a snapshot (29 Oct 2026). Say in your hand-over when you worked offline.

## 2. Precedence

1. The Peasy Design System artifact (tokens, components, assets, README), or the bundled `design-system/` copy when offline.
2. Peasy Figma files or screenshots the user supplies.
3. Peasy's live website.
4. Your own proposals, always labelled "Voorstel / proposed – confirm with Peasy".

Tokens whose usage starts with "Proposed" are usable but must be flagged as unconfirmed in your hand-over.

## 3. Pick the deliverable

| Request | Deliverable | Extra reference |
|---|---|---|
| Screen, landing page, mockup, poster, flyer | Design artifact type on the Peasy design system | brand-rules.md |
| Dashboard, chart, KPI page, report with charts | Dashboard artifact type | data-and-charts.md |
| Slide deck | Slides artifact type on the Peasy design system | brand-rules.md |
| Document, brief, PRD, spec | Claude Doc (Word only if asked). Brainstorm or Jira ticket → peasy-brainstormer | product-docs.md |
| Mockup requested by peasy-brainstormer | Design artifact (or standalone HTML), screens from its brief | brand-rules.md |
| UX copy, microcopy, error texts | In the reply, Dutch and French | brand-rules.md (Voice) |
| Audit or review | In the reply, findings table by severity | audit-checklist.md |

If the request is clear, proceed. Ask one short question only when the answer changes what you build.

## 4. Non-negotiables

- **Language.** Dutch (nl-BE) first, French (fr-BE) required before anything is final. "je/jij" in Dutch, "vous" in French. Peasy speaks as "we", the mascot as "ik". Sentence case, no emoji in product UI.
- **Honest numbers.** Every price has a unit and what's included ("€ 42,00 per maand"). Never invent savings, ratings, reviews, partner names or prices: use "€ XX" placeholders in mockups and label sample data as "Voorbeelddata". Badges like "Beste prijs" need a real basis.
- **Colour.** Ink `dark-500` text on white, cream, blue and pink. Never white text on Peasy blue (2.0:1) and never blue or pink as text on white. Primary action = filled `secondary-500` with a white label, one per view or card.
- **Type.** Grold Rounded Slim (Regular 400, Medium 500, Bold 700) from `project/fonts/`. Headlines use the Titles styles in Medium; body `body-16`.
- **Shape.** Panels 40px radius, cards 24px, buttons and tags 8px, inputs 4px, pills full. White cards with a 1px `stroke` border; shadows only on offer and brand cards.
- **Mascot.** At most one per viewport, never recoloured, never cropped across the face. Dutch alt text. It is decorative: below 640px hide it or swap to a peek cut-out whenever it would squeeze text, figures or actions.
- **Theme.** Light only, no dark mode. Where a surface follows the viewer's dark setting, keep Peasy's light page surface edge to edge; never wrap the page in a boxed off-white card.
- **Accessibility.** WCAG 2.2 AA: text 4.5:1 (3:1 at 18px+ bold or 24px+), graphics and focus 3:1, keyboard access, `focus-ring` on every interactive element, never colour alone.
- **Status of new things.** Anything not in the system (a new component, token or pattern) is a proposal: say so in the output and in your hand-over.

## 5. Working on surfaces that cannot load the system's files

Dashboard pages and some published pages cannot fetch fonts or images from the design system. Embed what you need:

- Fonts: inline `@font-face` with `data:font/woff2;base64,...` for the three Grold Rounded Slim weights (~115 KB together). Keep the system's fallback stack.
- Mascot: inline a small WebP `data:` URL (~40 KB for 480px tall) of the asset you use, and name the source asset in your hand-over so it can be refreshed later.
- Watch per-file caps (dashboard page 256 KB).

## 6. Quality gate before you hand over

Run `references/audit-checklist.md` against your own output. Then end with a short hand-over: what you made, what you assumed, which items are proposals, and which open decisions affect it.

## 7. Open decisions (do not decide these silently)

Error colour (pink vs red), title weight (Medium vs Bold), white text on blue, Grold Rounded Slim vs regular width and its web licence, and all "Proposed" tokens. Mention the ones your output touches.

Decided: no dark mode; the mascot may be hidden or swapped for a peek on small screens. French is required for final copy but the team has parked it for now: write Dutch, and don't flag missing French on drafts unless asked.

## References

- `references/brand-rules.md` – compact tokens, voice, imagery and mascot rules. Read for any visual or copy task.
- `references/data-and-charts.md` – dashboards, charts, tables, numbers. Read for any data visual.
- `references/audit-checklist.md` – review checklist and findings format. Read for audits and before hand-over.
- `references/product-docs.md` – PRD, flow, component spec and hand-over formats.
- `design-system/` – offline snapshot of the Peasy Design System (tokens, brand book, component READMEs + bundle, fonts, logo, icons, mascot). Use when the artifact link can't be opened.
