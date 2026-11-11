Text input (Figma "Inputfield"): label above (or a 112px label column when horizontal), field 44px high, radius 4, white with 1px `stroke`. States: default, focused (2px `primary-500`), error (2px pink border + message), disabled (`background` fill), required (pink asterisk), optional ("(optioneel)" in `dark-200`).

**Error colour:** the Figma error state uses pink for border and message; pink text fails contrast, so the message here uses `ui-error`. Confirm with Peasy.

**Consumer supplies:** `label`, `placeholder` (an example, not an instruction), validation `error` text in plain Dutch.
