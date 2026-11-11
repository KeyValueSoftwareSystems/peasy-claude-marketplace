# Peasy audit checklist

Use for reviews and as the final check on your own output. Do not invent usability evidence.

## Findings format
A table per severity (High, Medium, Low) with columns: #, problem, Peasy rule, fix. Then "Already matching", then a "Ready for review" checklist, then the open decisions it touches.

Severity: High = breaks a non-negotiable or WCAG AA; Medium = inconsistent with the system or missing a required state; Low = proposal, polish or naming.

## Checks
**Source**
- Uses the Peasy Design System artifact, not another brand or the org default.
- Every colour, size, radius, spacing and font comes from tokens; new values are labelled as proposals.
- Components match their README (sizes, radius, states); new components labelled as proposals.

**Colour and contrast**
- Text 4.5:1 (3:1 at 18px+ bold or 24px+); graphics, chart marks and focus 3:1.
- No white text on Peasy blue, no blue or pink text on white, green prices 18px+ bold only.
- ui-error / error-* only for errors.

**Type**
- Grold Rounded Slim loads (embedded where the surface can't fetch it); titles in Medium; sizes from the type scale; sentence case.

**Layout and shape**
- Panel, card, button, input radii correct; white cards with 1px stroke; shadows only where allowed.
- Responsive down to 320px; no horizontal page scroll; mascot hidden or a peek below 640px.
- Light only: no dark-mode styles, no boxed wrapper around the page.

**States and accessibility**
- Hover, pressed, focus, disabled, loading, empty and error states present where relevant.
- Visible focus ring, keyboard access to every interaction including chart tooltips; nothing communicated by colour alone; Dutch alt text.

**Content**
- Dutch first (French parked for now; flag only if asked).
- Buttons verb + outcome; errors say what happened and how to fix it.
- Every price has unit and period; no invented savings, ratings, partners or prices; sample data labelled.
- Brand tag at most once per screen; no emoji in UI.

**Patterns**
- No native Select for 4 or fewer options; one progress indicator per flow; password fields readable with Show/Hide; icons at the proposed stroke weight.

**Imagery**
- Correct logo variant for the background; mascot at most once per viewport, uncropped face; icons single ink from the Peasy set.
