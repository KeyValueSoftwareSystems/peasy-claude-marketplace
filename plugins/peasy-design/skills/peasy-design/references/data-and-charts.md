# Data, dashboards and charts

## Build
- Use the Dashboard artifact type. Follow its own instructions for datasets and marking, then apply Peasy styling to the page.
- Embed Grold Rounded Slim and any mascot image as `data:` URLs (see SKILL.md section 5).
- Peasy is light only (no dark mode). Set `#dash-root{--dash-gutter:0}` and give the page wrapper `page-bg` edge to edge with its own padding, no radius, so it reads as the page, not a box.

## Data honesty
- Prefer the user's real data or a connector. If you must make sample rows, title the dataset "Sample: …", show a "Voorbeelddata" tag on the page and say which numbers are sample.
- Never present sample savings or ratings as real.

## Charts
- Categorical series in order: chart-1 #394295, chart-2 #1E8FB0, chart-3 #D9468A, chart-4 #009B67, chart-5 #B87D00, chart-6 #464755. More than six: group as "Overige".
- One highlighted series: chart-1, others chart-muted #D1D1D5.
- Sequential: #D7D9EA → #B0B3D5 → #888EBF → #6168AA → #394295; label values.
- Never Peasy blue #66C6E2 or pink #F2A4C7 as chart marks on white (under 3:1).
- Grid #E4E4E4 1px, axis #D1D1D5, labels #747580 body-12, reference line #17192B dashed 4 4.
- Bars max 32px thick, rounded ends 3–4px; counts per month as bars, rates and running totals as straight lines.
- Label series directly or with a legend; tooltips must open on hover and on keyboard focus.

## Numbers
- Euro: `Intl.NumberFormat('nl-BE', {style:'currency', currency:'EUR'})` → "€ 42,00". Add the period ("per maand", "laatste 12 maanden") next to every figure.
- Change: sign + arrow in ink ("▲ + € 1,20"). Green only for a lower cost at 18px+ bold. Never ui-error red for a "bad" number.
- Prices in tables at 18px bold if green; otherwise ink.

## Cards and layout
- KPI cards: white, 1px stroke, 24px radius, padding 24/32/32, label body-14-medium dark-400, value title-36, note body-14 dark-300.
- Header: blue panel (40px radius) with ink title and one takeaway sentence; optional mascot standing on the panel's bottom edge; hide it below 640px.
- Explanation box: cream panel ending with one brand tag.
