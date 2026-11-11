# Peasy brand rules (compact copy)

Snapshot of the Peasy Design System on 2026-10-26. The artifact wins on any conflict.

## Contents
1. Colour
2. Type
3. Spacing, shape, surfaces, layout
4. States, focus, feedback (proposed)
5. Voice and copy
6. Logo, icons, imagery, mascot
7. Components available

## 1. Colour

| Token | Hex | Use |
|---|---|---|
| dark-500 | #17192B | Ink: headlines, primary text and icons |
| dark-400 | #464755 | Secondary text, menu links |
| dark-300 | #747580 | Body copy in cards (4.6:1) |
| dark-200 | #A2A3AA | Placeholders, units, disabled only |
| dark-100 | #D1D1D5 | Disabled borders |
| primary-500 | #66C6E2 | Peasy blue: hero and closing panels, logo, active radio. Never text on white |
| primary-100…400 | #E0F4F9 #C2E8F3 #A3DDEE #85D1E8 | Blue tints |
| secondary-500 | #394295 | Peasy purple: primary buttons, footer, 3-steps panel |
| secondary-600 / 700 | #2E3577 / #232859 | Button hover / pressed (proposed) |
| secondary-100…400 | #D7D9EA #B0B3D5 #888EBF #6168AA | Purple tints |
| tertiary-500 | #F2A4C7 | Peasy pink: accent panels, USP tiles, step discs. Never text on white |
| tertiary-100 | #FCEDF4 | Pink tint |
| cream-500 | #F9F4EA | Warm panels, reassurance boxes |
| green-500 | #009B67 | Prices (18px+ bold), checkmarks, active checkbox |
| ui-warning | #F5C011 | Badge fill with ink text |
| ui-error | #F24236 | Errors only |
| white / page-bg / background | #FFFFFF / #FDFDFD / #F5F5F5 | Cards / page / flows and disabled |
| stroke / stroke-soft | #DDDDDD / #E4E4E4 | Borders / inner dividers |

Panel rotation on a page: blue (hero, closing) → cream (why Peasy) → purple (3 steps, footer) → pink (offers). Ink on blue, cream and pink; white on purple.

## 2. Type

Family: "Grold Rounded Slim", "Nunito", "Varela Round", system-ui, sans-serif. Weights 400, 500, 700.

| Style | Size / line | Weight | Use |
|---|---|---|---|
| display | 72/64 | 500 | Rare hero statement |
| title-56 | 56/56 | 500 | Homepage hero |
| title-48 | 48/48 | 500 | Page H1 |
| title-36 | 36/36 | 500 | Section headline |
| title-30 | 30/36 | 500 | Sub-section, flow step title |
| title-24 | 24/24 | 500 (Bold on offer cards) | Card title |
| title-18 | 18/22 | 500 | Small card title, FAQ question |
| title-16 | 16/24 | 700 | Emphasised label |
| body-18 | 18/24 | 400 | Lead paragraph |
| body-16 | 16/20 | 400 | Default body; -medium for button labels |
| body-14 | 14/20 | 400 | Helper text; -medium for form labels |
| body-12 | 12 | 400/500/700 | Tags, badges, captions |

No mobile type scale exists yet: scale titles down one or two steps on screens under 640px and label it as a proposal.

## 3. Spacing, shape, surfaces, layout

- Spacing: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96 (s-1 … s-24).
- Radius: rounded 4 (inputs, badge), lg 8 (buttons, tags), xl 12, 2xl 16, 3xl 24 (cards), panel 40, full.
- Shadows: shadow-default `0 3px 4px rgba(196,196,196,.25)` on offer and brand cards only; shadow-s `0 2px 0 #f8f8f8` on select and content card.
- Borders: 1px cards and inputs, 2px outline buttons, focused and error fields.
- Layout: desktop frame 1512, panels 1464 inset 24px, content 1278–1392, panels 80–200px apart. Mobile frame 320. Breakpoints 640, 768, 1024, 1280, 1400.

## 4. States, focus, feedback (proposed)

- Full button: secondary-500 → hover secondary-600 → pressed secondary-700.
- Outline controls and rows: hover #E0F4F9, pressed #C2E8F3, border #747580 on hover.
- Disabled: fill #F5F5F5, label #A2A3AA, border #D1D1D5.
- Focus: 2px #394295 ring, 2px offset, on `:focus-visible`; white ring on purple.
- Banners: success #E6F5EF / #009B67 / text #00704A; warning #FEF6DB / #F5C011 / #7A5C00; error #FEECEB / #F24236 / #C42B21; info #E0F4F9 / #66C6E2 / #1E6A80. Always icon + text.

## 5. Voice and copy

- Helpful, slightly cheeky friend: a wink in headlines, calm precision in prices, forms and conditions.
- Real examples: "Bespaar slim op al je vaste lasten... Peeeeeasy!", "Oei… je betaalt €20 te veel. Peasy to the rescue!", "Hulp nodig? Ik sta voor je klaar!".
- Buttons: verb + outcome, 1–3 words ("Bespaar nu", "Kies dit pack").
- Errors: what happened + how to fix it, no blame.
- Brand tag ("Easy met Peasy!", "Da's Peasy.") at most once per screen, at the end of a section.
- Prices: "€ 42,00 per maand" (nl-BE: euro sign, space, comma decimals), always unit and what's included.
- Dates nl-BE: "26 okt. 2026"; months short "okt.".

## 6. Logo, icons, imagery, mascot

- Logo: `peasy-logo.svg` (blue) on white, cream, pink; `peasy-logo-white.svg` on purple and photos. 41px header height, never under 24px, clear space half the letter height, never recoloured.
- Icons: 37 line icons on a 32px grid, single ink (dark-500, white on dark). 16px in text rows and buttons, 24–32px in tiles. Only a combined sheet exists in the system; the bundle's `Icon` has 12. No emoji as icons. Stroke (proposed): keep the rendered line optically even, 1.5px at 12–16px and 2px at 24–32px; the outlined SVGs need an added `stroke: currentColor` (round joins and caps) of 2 / 1 / 0.67 / 0 viewBox units at 12 / 16 / 24 / 32px.
- Speech bubbles: six shapes in Peasy blue holding a short mascot line.
- Photos: warm lifestyle photos on blog cards; none in the system yet, use placeholders.
- Mascot assets: `peasy-mascot-full.png` (full body), `peasy-mascot-peek-side/tall/bottom.png` (peeks from a panel edge, masked by the panel radius), `backdrop-1…11.jpg` (16:9 scenes on Peasy blue for hero halves). One per viewport, never recoloured or cropped across the face, keep text off the mascot, hide or swap to a peek below 640px, Dutch alt text such as "Peasy, de blauwe mascotte, kijkt om de hoek".

## 7. Components available

Badge, Breadcrumb, Button, Checkbox, ContactOption, FAQ, IconButton, NewsCard, OfferCard, PerkCard, Radio, Search, Select, SelectorPill, Tag, TextArea, TextField, TextLink, UspBar. React bundle: `project/components/bundle.js` (offline: `design-system/components/bundle.js`) (global `window.Peasy` namespace as declared in the system), types in `index.d.ts`.

Anything else (header, footer, modal, tooltip, table, stepper, result card, charts…) does not exist yet: design it from tokens and label it as a proposal.

## 8. Proven UI patterns

- **Choices.** 2–4 exclusive options: SelectorPills on a blue (or pink) card, or Radios on white. Never a native Select for 4 or fewer; it shows the OS menu, not Peasy. 5+ options: Select.
- **Progress in flows.** One indicator only: a line "Step 2 of 5 · Household" above a 5-segment bar (done and current `secondary-500`, upcoming `primary-100`). No percentage counters, step pills or repeated step labels next to it.
- **Password fields.** Grold Rounded's mask dots are tiny: once typed, switch the field to `Verdana, "Segoe UI", system-ui` at 18px with 0.12em letter-spacing (placeholder stays Grold). Add an inline "Show / Hide" (Toon / Verberg) text button inside the field, with `aria-pressed`.
- **Mascot reactions.** In forms the mascot can react to choices in a speech bubble ("ik" voice, playful, no claims), announced politely to screen readers.
- **Known component bug.** TextField's `optional` label is hard-coded Dutch "(optioneel)"; supply your own label text in other languages until fixed.
