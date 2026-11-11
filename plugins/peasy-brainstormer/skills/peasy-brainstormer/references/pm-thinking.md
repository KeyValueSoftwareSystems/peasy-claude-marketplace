# PM thinking: how to find the questions

There is no question list. You think like a senior Peasy PM writing a PRD, find what you don't know, and ask only about what matters most. Use `peasy-context.md` for facts and domain traps so questions name real things.

## 1. Draft the PRD in your head first

From the user's words alone, fill each part with what you know or would guess:

| Part | What a PM wants to know |
|---|---|
| Problem & value | What's broken or missing today, for whom, and why it matters now. Is it a user problem, a business problem, or both? |
| Users | Every actor: the household, Peasy experts/ops, partners (supplier, insurer, bank), internal systems ("the energy engine"). Internal users get stories too. |
| Business model | How Peasy earns from this (referral fee, commission, lead). Does it create a conflict with neutral advice or ranking? What must be disclosed? |
| Scope | Smallest v1 that proves value; what's explicitly out (brands, verticals, app, regions). Is this a one-off or a reusable template for the next partner? |
| Main flow | Step by step from the user's view, plus what the system does behind each step. |
| Data & integrations | What comes in, from where, how often, and how it's validated. What goes out, to whom. Sync or async? |
| Failure & recovery | What breaks (API down, stale data, rejected order, user cancels, double submit) and what the user and ops see then. Who is alerted? Is it retry-safe? |
| States | Loading, empty, error, success, partial. Each needs copy and usually a mockup frame. |
| Trust & compliance | GDPR basis, consent, retention, who's controller vs recipient; regulators for the vertical; claims that need a real basis ("Beste prijs"). |
| Measurement | How we'll know it worked: a funnel or metric, target TBD if unknown. Analytics events per step. |
| Rollout & dependencies | Contracts, sandbox, legal review, ops process, feature flag, region order. |

## 2. Rate each part

Mark every part as **Known** (user said it or context answers it; a context fact that could be stale stays Known but gets "verify with Peasy" in Open questions), **Guess** (you can propose a sensible Belgian default) or **Unknown**.

Then rank Guesses and Unknowns by: *if this answer changed, would the stories change?* High impact + low confidence goes first. Low impact items become **Assumptions** in the ticket, not questions.

## 3. Turn the top gaps into questions

- Round 1 = the gaps that change scope (who, what's in v1, which brands/regions, the core flow). Round 2 = gaps that change behaviour (data, failure, compliance, copy).
- Each question: one decision, 2–4 concrete options, your best guess first as "(Recommended)", one-line why when not obvious.
- Ask about **decisions**, not facts you can look up or reasonably assume.
- Prefer the question a sharp PM would ask that the user hasn't thought of (the conflict of interest, the failure path, the reusable template) over the obvious one.
- Don't ask a generic question ("Who is the user?") when you can propose a specific answer ("Households switching energy, plus ops managing the feed?").
- **Check the framing first.** If the user's words don't match Belgian reality (a Dutch-market term, a product sold differently here, a flow Peasy doesn't have), the first question clarifies what we're really building. Say in the question when your basis is general knowledge: "(general knowledge, verify)".
- **Ordering.** The round decides *what kind* of gap (scope vs behaviour); impact decides the order *within* a round. A "sharp PM" gap that changes scope (who pays and therefore what we build, reusable template) goes in round 1; one that changes behaviour (failure paths, ranking rules) leads round 2.
- **Multi-select.** Put the recommended combination in the question ("Recommended: a + b") and mark those options "(Recommended)".
- **Skip round 2** when no high-impact gap remains after round 1; say so and go to the brief.

## 4. Always cover (fold into the rounds or the ticket)

Language (NL first, FR `[FR: todo]`), GDPR, sister brands, the vertical's regulator, success measure, and the domain traps in `peasy-context.md` section 11. These are checks, not mandatory questions: ask one only if it changes scope or behaviour for *this* idea (sister brands usually does). Otherwise write it as an Assumption or Non-functional line. Anything unanswered becomes an Open question with an owner.

When the idea touches an area `peasy-context.md` doesn't describe (e.g. the fire/home flow), treat its current flow as Unknown and say so, rather than assuming it works like a documented one.

## 5. Quality bar for the ticket

A good ticket from this skill (see `assets/prd/example-prd.json`):

- Summary says what changes and, if true, that it becomes a reusable pattern.
- Context separates Peasy facts from general knowledge ("general knowledge, verify with Legal").
- Stories cover the system and ops as well as the household, and every story has an error or edge case.
- Failure paths are designed: retry, fallback (callback, hide), what's counted, who's alerted.
- Integrity rules are explicit: re-check price before commit, idempotent submit, no live calls in results, nothing leaks across regions.
- Numbers you don't know are placeholders: `[N] hours`, `[X] s`, `€ XX`. Never invented.
- Neutral ranking and disclosure are stated when money flows from partners.
- Analytics events named per step; success metric owned in Open questions.
- Stories ≤ 5 points; anything bigger is split.
- Mockup brief lists the states to show (loading, error, success, failure), not just the happy path.
