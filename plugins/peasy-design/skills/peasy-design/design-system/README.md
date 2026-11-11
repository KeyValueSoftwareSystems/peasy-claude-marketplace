Peasy compares and arranges household fixed costs (mortgages, insurance, energy, internet/TV) for Belgian families. The brand promise is "easy": plain words, honest numbers, three simple steps and an expert nearby. Build every Peasy screen from these tokens and components; never invent a colour, size or component.

## Content fundamentals

- Write Dutch (nl-BE) first; French (fr-BE) is required for final copy. Address the reader as "je/jij" (French "vous"). Peasy speaks as "we", the mascot as "ik".
- Sound like a helpful, slightly cheeky friend: a wink in headlines, calm precision in prices, forms and conditions. Real examples: "Bespaar slim op al je vaste lasten... Peeeeeasy!", "Oei… je betaalt €20 te veel. Peasy to the rescue!", "Vergelijk en regel in 3 stappen klaar binnen 5 minuten... Peasy toch!", "Hulp nodig? Ik sta voor je klaar!".
- Sentence case everywhere. No emoji in product UI. End a section with a brand tag ("Easy met Peasy!", "Da's Peasy.") at most once per screen.
- Buttons: verb + outcome, 1–3 words ("Bespaar nu", "Kies dit pack"). Errors: what happened and how to fix it, no blame.
- Every price carries a unit and what is included ("€ 42,00 per maand"). Never show savings, ratings or partner names without a real source; use "€ XX" placeholders in mockups.

## Visual foundations

- **Colour.** Ink `dark-500` on white for text. Primary actions are filled `secondary-500` (purple) with white labels. Big section panels rotate through `primary-500` (blue hero and closing panels), `cream-500` (why-Peasy), `secondary-500` (3-steps and footer) and `tertiary-500` (offers). Put ink, not white, on blue and pink panels. Prices and checkmarks use `green-500`; highlight badges use `ui-warning`.
- **Text hierarchy.** `dark-500` headlines, `dark-400` secondary, `dark-300` body copy in cards, `dark-200` only for placeholders, units and disabled text.
- **Type.** Grold Rounded Slim by Typesketchbook (Regular 400, Medium 500, Bold 700), supplied by Peasy as web fonts in `fonts/`. Headlines use the Titles styles in Medium (`title-56` hero, `title-48` H1, `title-36` sections, `title-24` cards); body uses `body-16`; form labels `body-14-medium`. Nunito is only a fallback if the font fails to load.
- **Shape.** Section panels `rounded-panel` (40px), inset 24px from the page edge; cards `rounded-3xl`; buttons and tags `rounded-lg`; inputs `rounded`; pills and discs `rounded-full`.
- **Surfaces.** White cards with a 1px `stroke` border; shadows are rare (`shadow-default` on offer and brand cards only).
- **Layout.** Desktop frame 1512px, panels 1464px, content 1278–1392px; panels are spaced 80–200px apart. Mobile frame 320px. Breakpoints `screen-sm` to `screen-2xl`.
- **Imagery.** The furry blue 3D mascot "Peasy" peeks in from a panel edge or stands beside a blue speech bubble; at most one per viewport, never recoloured or cropped across the face. Scene backdrops are the mascot on Peasy blue. Blog cards use warm lifestyle photos. The mascot is decorative: below 640px, hide it or swap to a peek cut-out (cropped by the panel edge, face visible) whenever it would squeeze text, figures or actions.
- **Theme.** Light only; Peasy has no dark mode. Surfaces that follow a viewer's dark setting keep Peasy's light surfaces edge to edge (no boxed wrapper).
- **Focus.** A 2px `focus-ring` (purple) with 2px offset on every interactive element (proposed; the file draws no focus states). See States, feedback and charts.

## Iconography

37 line icons on a 32px grid, single ink (`dark-500` on light, white on dark), shown in the Icons group. Use 16px in text rows and buttons, 24–32px in tiles. The bundle's `Icon` component carries the common ones (ArrowRight, Check, Dropdown, MagnifyingGlass, House, Headset, CalendarDots, Question, PhoneCall, PhoneTransfer, MapPin, Tag). No emoji as icons.

## States, feedback and charts (proposed)

All tokens in this section are proposals added on 2026-10-26; confirm with Peasy before final delivery.

- **Interaction states.** Full button: `secondary-500` → hover `secondary-600` → pressed `secondary-700`. Outline controls, list rows and icon buttons: hover `state-hover-tint`, pressed `state-pressed-tint`, border to `state-hover-border`. Disabled everywhere: `state-disabled-bg`, `state-disabled-fg`, `state-disabled-border`, no hover, cursor not-allowed.
- **Focus.** Every interactive element gets a `focus-ring-width` ring in `focus-ring` with `focus-ring-offset`, shown on keyboard focus (`:focus-visible`); `focus-ring-on-dark` on purple. Peasy blue is not used for focus because it fails 3:1 on white.
- **Feedback.** Banners and inline messages use the `-bg`, `-border` and `-fg` set for success, warning, error and info, always with an icon and text, never colour alone. Errors state what happened and how to fix it. `ui-error` and `error-*` are for errors only, never for "bad" numbers.
- **Charts.** Categorical series take `chart-1` to `chart-6` in order; one highlighted series uses `chart-1` with the rest `chart-muted`. Sequential data uses `chart-seq-100` to `-500`. Peasy blue and pink as-is are panel colours, not chart colours (under 3:1 on white). Gridlines `chart-grid`, axes `chart-axis`, labels `chart-label` at body-12. Prices in charts follow the price rules (unit, period). Increases and decreases are shown with a sign and an arrow in ink; green only for a lower cost at 18px+ bold. Label series directly or with a legend; tooltips must also work on keyboard focus.

## Back-office (Energy Engine Admin)

Learned from a Peasy energy-admin epic (electricity product specifications: Figma, Jira stories, UAT build, Oct 2026). Admin screens use the same tokens and type but are denser, calmer and task-first: no mascot, no brand tags, no playful copy, Dutch UI with NL/FR/EN-ready labels. Everything below is proposed until Peasy confirms.

- **Shell.** Logo left, user menu right (avatar, name, role). Domain tabs (Elektriciteit, Gas, DualFuel Pack, Promoties, Leveranciers) as underline tabs: `title-18` Medium, active ink with a 2px `primary-500` underline, inactive `dark-300`. Under it a sub-navigation bar in a `background` pill container (`rounded-full`): icon + label tabs, active on `secondary-100` with ink text.
- **Entity toolbar.** Row of labelled selectors (Leverancier, then Product) plus the create action (Full button, `+` icon, "Nieuw product") and, right-aligned, the secondary action (Outline, "Product dupliceren"). Selectors appear progressively: supplier always; product and create only after a supplier; duplicate, save and the record only after a product.
- **Combobox (searchable select).** Replaces the native select for long lists: search field at the top of the panel, keyboard navigation, min width 240px (never wrap a name onto three lines), max panel height ~10 rows. Each option can carry a status: show a status dot plus text colour, never colour alone; inactive options in `dark-300`.
- **Record panel.** Large `background` panel (`rounded-panel`) holding the record: title (`title-24`) + status badge, metadata strip, then the form. Primary save sits top-right and repeats bottom-left on long forms (both do the same).
- **Status badge.** Pill (`rounded-full`, 24px, `body-12` Medium) with dot: Actief = `success-bg` / `success-fg`, Niet actief = `background` / `dark-300`. Same mapping in the combobox options.
- **Metadata strip.** IDs in a `primary-100` chip (`rounded-xl`), label `dark-400` + value Bold, divided by a 1px line; dates with a calendar icon, `body-12` `dark-400`, format `dd/mm/jjjj uu:mm`, labels "Aangemaakt op" and "Laatst bijgewerkt". Read-only, never editable.
- **Form grid.** Two columns from 1024px (one below), 20–24px row gap. Every field group has one label style: `title-16` Bold (no mixing 12px and 14px labels). Radio/checkbox groups lay out inline with 24px gaps. Required fields marked consistently (all or none: when every field is mandatory, say so once above the form instead of 20 asterisks).
- **Selection colour.** Checked radios and checkboxes in admin use `secondary-500` (purple) for contrast; consumer pages keep the component defaults until Peasy decides one colour for both.
- **Modes of one page.** Edit, Create and Duplicate are modes of the same screen, not new pages. Create/Duplicate: title ("Nieuw product aanmaken" / "Product dupliceren"), the fixed parent shown as read-only text ("Leverancier: ENGIE"), product selector, status, metadata, duplicate and save hidden; footer actions Annuleren (Outline) + confirm (Full). Cancel and page refresh return to the previous state without saving.
- **Locked fields.** A field forced by another (Toon in vergelijking = Nee when Niet actief) is shown disabled with a one-line reason under it, not silently locked.
- **Validation.** Inline under the field, `error-fg`, field border `error-border`; on submit, scroll to and focus the first error and show a summary banner at the top of the form. Copy (NL / FR / EN): "Dit veld is verplicht." / "Ce champ est obligatoire." / "This field is required."; uniqueness: "Er bestaat al een product met deze naam voor deze leverancier." / "Un produit avec ce nom existe déjà pour ce fournisseur." / "A product with this name already exists for this supplier."
- **Feedback after actions.** Saved, created and duplicated each confirm with a success toast (`success-*`, 4–6 s, polite live region) and update "Laatst bijgewerkt". Leaving a record with unsaved edits asks to confirm.
- **Empty states.** Before a supplier is chosen, show one calm line of guidance in the record area ("Kies een leverancier om zijn producten te bekijken.") rather than a blank page.
- **No results.** A combobox search that finds nothing shows "Geen resultaten voor ‘…’" in the panel, never an empty panel.
- **Loading.** When a record takes longer than about 300 ms to load, show a skeleton of the record panel (or a spinner in the selector) so a selection never looks ignored.
- **Number and link fields.** Whole numbers only, with the allowed range in the help text ("1–60 maanden"); reject signs, decimals and exponents as you type. Links must start with https:// and are checked on blur. Error text in `error-fg` at 14px, never pale pink at 12px.
- **Status badge parity.** Actief and Niet actief use the same pill shape; only the colours differ.

## Open decisions

The Figma error state uses pink (`tertiary-500`) for border and message; messages here use `ui-error` for contrast. Title styles are named "bold" but set in Medium. White hero text on `primary-500` fails contrast (2.0:1). Confirm all three with Peasy. Also confirm the proposed state, feedback and chart tokens.

Decided (2026-10-26): no dark mode; mascot may be hidden or swapped for a peek on small screens.
