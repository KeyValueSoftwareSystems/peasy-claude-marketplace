# Peasy context

Public facts about Peasy, collected from peasy.be and press on 29 Oct 2026. Use them to ask sharper questions and write accurate tickets. Facts can go stale: when a ticket depends on one (a partner, a number, a legal entity), add "verify with Peasy" to Open questions. Never show these numbers in UI copy as if confirmed.

## Contents
1. Company and brands
2. Verticals and current flows
3. Login and account today
4. Languages and channels
5. Legal entities, regulators, complaints
6. Privacy facts
7. Partners named publicly
8. itsme facts
9. Known gaps on the site
10. Sources
11. Domain traps per area (what a Peasy PM checks)

## 1. Company and brands

- Peasy compares and arranges household fixed costs in Belgium; tagline "Bespaar slim op al je vaste lasten" / FR "Économiser sur vos frais fixes ? Easy avec Peasy!".
- Three-step promise: tell us your situation → compare and choose → we contact the provider and arrange the switch.
- Free for consumers. Partners pay Peasy a referral fee when a customer signs through Peasy. The customer signs the contract with the provider, not with Peasy.
- CEO: David Geerts. HQ Zaventem (Leuvensesteenweg 643 bus 14). Customer care in Hasselt and Oujda (Morocco).
- Size claims on the site: ~70 offices ("winkels"), 150 experts (FAQ says "almost 200" people), 50,000+ contracts a year, ~50 partners, 4.5/5 customer rating.
- **Family of brands** (site footer: "Onderdeel van een familie van merken"):

| Brand | What it does | Entity |
|---|---|---|
| Peasy | Consumer brand and comparison site | Not named as a separate entity on the site |
| Hypotheek.winkel | Mortgage advice, physical offices in Flanders and Brussels | BV hypotheek.winkel, 0474.087.795 |
| Verzekeringen.be | Insurance distribution, claims via schade@verzekeringen.be | Verzekeringen NV, 0472.905.781 |
| Aanbieders.be | Energy and telecom comparison | e-Contract BV, BE0892.798.886 |

- Parent named in the privacy policy: Horizon Holdco NV (Horizon Group).
- Dec 2025: Meilleurtaux (France, majority-owned by Silver Lake) signed a definitive agreement to acquire Peasy. David Geerts would lead combined Meilleurtaux operations in Belgium and Luxembourg. Meilleurtaux already owns MiD Finance (Wallonia). Closing status not confirmed in public sources found. **Ask** whether a ticket must also work for Meilleurtaux / MiD Finance brands.

So, "sister brands" in questions means: Hypotheek.winkel, Verzekeringen.be, Aanbieders.be (and possibly Meilleurtaux Belgium later).

## 2. Verticals and current flows

| Vertical | Products on peasy.be | What the flow asks today |
|---|---|---|
| Mortgage (hypothecaire lening) | Borrowing capacity, monthly payment, feasibility check, notary costs, financial plan, refinancing, upload your offer | Calculators + appointment (video or office). ~20 FSMA-registered lenders compared. Approval typically 1–2 weeks |
| Insurance (verzekeringen) | Car, fire/home, funeral, credit life (schuldsaldo) | Car: build year, brand, fuel → model/series → cover (BA, mini-omnium, omnium) → contact details → results. ~9 insurers compared. Online sign-up |
| Energy (energie) | Supplier comparison | Postcode, solar panels, single/dual meter, electricity and gas usage, current supplier, green preference. Peasy handles the switch; legal notice 35 days; meter unchanged; yearly re-check for better deals |
| Telecom | Mentioned in FAQ, handled via Aanbieders.be | Not a full section on peasy.be |
| Other | Budgetbarometer, blog, newsletter | |

Offices handle mortgages and consumer credit; insurance, energy and telecom are online or by phone.

Regional context (general knowledge, not from peasy.be): energy prices and grid operators differ by region. Regulators: VREG (Flanders), CWaPE (Wallonia), BRUGEL (Brussels), CREG (federal).

## 3. Login and account today

- peasy.be shows Login and Register with **email + password** and "Forgot Password?". No social login, no itsme.
- No FAQ or privacy text describes what the account does. **Ask** what users can see in their account (quotes, contracts, documents) before scoping account features.

## 4. Languages and channels

- Dutch (nl-BE) at peasy.be/, French at peasy.be/fr/. The FR site is mostly complete but has Dutch leftovers and placeholder links, and a thinner energy section.
- FR labels in use: Prêt hypothécaire, Assurances (auto, habitation, obsèques, solde restant dû), Énergie, Économisez maintenant, Prenez un rendez-vous.
- Channels: phone 03 501 22 22 (office hours), callback, appointment (video or office, mortgages), contact form, newsletter. Socials: Facebook, Instagram, LinkedIn ("easy-met-peasy").

## 5. Legal entities, regulators, complaints

- FSMA register of insurance intermediaries: hypotheek.winkel 061.433 A; Verzekeringen NV 047.138 A. Legal basis cited: law of 4 April 2014 (insurance), IDD conduct rules.
- Complaints: Ombudsfin (mortgage, consumer credit); Ombudsdienst Verzekeringen (insurance).
- Data protection authority: GBA/APD.
- Any feature touching insurance or mortgage advice, ranking or commission needs a **Legal** open question (IDD/FSMA conduct rules, transparency on remuneration).

## 6. Privacy facts

- Controller: Verzekeringen NV. Data shared within the group: Hypotheekwinkel BV, e-Contract BV (Aanbieders), parent Horizon Holdco NV.
- Data shared intra-group can include identification, contact, insurance, financial data and health data (for credit life insurance).
- Retention stated: service users 5 years; contact requests 2 years; customer service 10 years after contract end.
- Privacy contact: privacy@peasy.be. No DPO named; processors list on request.
- Legal bases used: contract, legitimate interest, consent (analytics/marketing cookies, newsletter).

## 7. Partners named publicly

Use only as examples in questions, never as confirmed integrations.

- Site "about" page: Engie, Keytrade Bank, Ethias, AG, BNP Paribas Fortis, Frank Energie, Santévet, Hypostart.
- Energy featured: Elegant, Eneco, Engie, Frank Energie, Luminus, Mega, Octa+, TotalEnergies, EnergyVision (+ ~20 smaller suppliers).
- Insurance direct insurers mentioned: Yuzzu, Belfius Direct, Ethias.
- Telecom: Orange promo on the blog.

## 8. itsme facts

- Belgian digital identity app; 8+ million users in Belgium (press release, March 2026).
- Notified under eIDAS at level of assurance **high** (Dec 2019).
- Uses: identification, login, transaction approval, qualified e-signature, sharing data from authentic sources.
- Exact attributes Peasy could receive (name, address, date of birth, national register number) depend on the itsme contract and scopes: always an open question for Tech + Legal.

## 9. Known gaps on the site

Useful when scoping fixes or when a ticket touches these areas:
- Office count shows both 70 and 75; staff 150 vs ~200; mortgage FAQ says 25 banks but lists ~20; car insurance says 9 and 10 insurers.
- FR site: Dutch strings ("Verander taal", "Toggle mobiel menu"), "#terugbel" / "#afspraak" placeholder anchors, "Forgot Password?" links to "#".
- No FSMA/disclaimer details on product pages; ranking and remuneration not explained on comparison pages.

## 10. Sources (accessed 29 Oct 2026)

- https://peasy.be/ · https://peasy.be/fr/ · https://peasy.be/over-ons/ · https://peasy.be/faqs/
- https://peasy.be/disclaimer/ · https://peasy.be/privacy-policy/
- https://peasy.be/energie/energieleveranciers-vergelijken/ · https://peasy.be/verzekeringen/autoverzekering
- Business Wire, 22 Dec 2025: Meilleurtaux enters into a definitive agreement to acquire Peasy
- Finyear, 5 Jan 2026: Meilleurtaux acquiert Peasy
- itsme press, 17 Mar 2026: itsme grows to eight million users

## 11. Domain traps per area (what a Peasy PM checks)

Not questions to read out: things to cover in the ticket or turn into a question only if they're a real gap.

- **Identity & login:** today email + password only. Belgians expect itsme next to Google/Apple. Don't store the national register number unless legally needed. Cover: account linking on matching verified email, Apple private relay emails, consent for itsme data (NL/FR), logout, session length, provider down / user cancels / email already in use, keeping password as fallback, mobile app vs web.
- **Partner onboarding (energy, insurance, bank, telecom):** data source (API, feed, aggregator, manual), refresh frequency, validation rules, stale-data behaviour (hide vs show with date), field mapping (energy: fixed/variable, € per kWh per meter type, fixed fee, green %, contract length, region; insurance: cover, excess, exclusions, premium), logo usage rights, who owns the relationship and the SLA on data errors.
- **Ranking & money:** Peasy is paid by partners. Ranking neutral by price unless decided otherwise, and any commercial weighting must be disclosed. Never invent commission. "Beste prijs" or "Nieuw" badges need a real basis. Remuneration transparency applies for insurance (IDD).
- **Energy specifics:** prices, grid operators and regulators differ per region (VREG Flanders, CWaPE Wallonia, BRUGEL Brussels, CREG federal); nothing may leak across regions. Today's flow asks postcode, solar panels, single/dual meter, usage, current supplier, green preference. 35-day notice; meter stays the same. EAN code is 18 digits. Clarify what "jaarkost" includes (energy, grid, levies, btw).
- **Insurance specifics:** FSMA/IDD duties, Verzekeringen.be NV is the broker and privacy controller. IDD means a demands-and-needs check before advice, a product information sheet (IPID) before signing, and remuneration transparency. Plan for out-of-profile outcomes: no quote, cover above an insurer's ceiling (underwriting needed), broker callback as fallback. Car insurance asks build year, brand, fuel, model, cover (BA / mini-omnium / omnium). The fire/home flow is not documented here: treat its details as Unknown. In Belgium, contents (inboedel) cover is usually part of a fire policy (owner or tenant), not a standalone product (general knowledge, verify).
- **Switch & hand-over:** what data is needed and what can be pre-filled; documents (ID, meter reading, previous policy) with format/size limits; signature (itsme sign, click-to-accept, partner handles); re-check price before commit; idempotent submit; sync vs async partner status; what the customer sees and receives (email/SMS); failure fallback (retry, callback) and what is counted as placed.
- **Comparison & results:** default sort and its fairness, empty/no-results state and what we suggest, loading state, events to track.
- **Cross-cutting:** NL first, FR required for final; GDPR basis, consent, retention (service users 5 yrs), controller vs recipient, processor agreements; sister brands in or out; WCAG 2.2 AA; analytics funnel; rollout (flag, %, region first).

