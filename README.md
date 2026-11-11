# Peasy skills for Claude

Two Claude skills, built by [KeyValue](https://www.keyvalue.systems) for the Peasy team, that take a feature from rough idea to groomable Jira epic with an on-brand mockup.

| Plugin | What it does |
|---|---|
| **peasy-brainstormer** | Turns a one-line feature idea into a Jira-style PRD. Thinks like a senior Peasy PM, asks only the questions that matter (sister brands, NL/FR, GDPR, FSMA, regulators), plays back the brief, optionally gets a mockup, then outputs an epic + child stories with Given/When/Then acceptance criteria as one HTML page. |
| **peasy-design** | Designs, writes and reviews anything Peasy (screens, flows, copy, decks, audits) on the Peasy Design System. Ships with an offline copy of the design system, so it works without any extra access. |

Install **both**: the brainstormer calls peasy-design for its mockups.

---

## 1. Install

Pick the option that matches how you use Claude.

### Option A: Claude app (desktop or claude.ai), recommended for PMs and designers

1. Download both files from the [latest release](https://github.com/KeyValueSoftwareSystems/peasy-claude-marketplace/releases/latest):
   - [`peasy-brainstormer.plugin`](https://github.com/KeyValueSoftwareSystems/peasy-claude-marketplace/releases/latest/download/peasy-brainstormer.plugin)
   - [`peasy-design.plugin`](https://github.com/KeyValueSoftwareSystems/peasy-claude-marketplace/releases/latest/download/peasy-design.plugin)
2. In Claude, open **Customize → Plugins → Add plugin → Upload** and upload the first file. Repeat for the second.
3. Check that both show as enabled in **Customize → Plugins**.

> Requires a paid Claude plan (Pro, Max, Team or Enterprise). If you don't see Plugins, ask your Claude admin to allow plugins and skills.

**Admins (Team/Enterprise):** after installing, use **Publish to organization** on each plugin so everyone at Peasy gets it without uploading. Or add this repo as a GitHub plugin marketplace in your organization settings so updates arrive automatically.

### Option B: Claude Code (terminal)

```text
/plugin marketplace add KeyValueSoftwareSystems/peasy-claude-marketplace
/plugin install peasy-brainstormer@peasy-claude-marketplace
/plugin install peasy-design@peasy-claude-marketplace
```

Restart Claude Code when prompted.

---

## 2. Try it

Start a new chat and type:

> Brainstorm adding a new energy supplier to the Peasy comparison.

What happens:

1. Claude asks 1–2 short rounds of multiple-choice questions. Answer in one click, or say **"use defaults"**.
2. It plays back a short brief. Confirm or correct it.
3. It asks whether to generate a mockup. **"Yes, key screens"** makes up to 3 screens in the Peasy style.
4. You get one HTML page: the epic, its stories with acceptance criteria, Definition of Ready, open questions and the embedded mockup. Each issue has **Copy as Jira markup**.

Say **"quick"** for a single round and one screen.

More prompts:

- "Write a ticket for itsme and Google login on Peasy."
- "Design the Peasy car-insurance result page in Dutch."
- "Review this screen against the Peasy design system." (attach a screenshot)
- "Make an on-brand Peasy slide on our Q4 energy results."

Finished examples are in [`examples/`](examples/): open any `index.html` in your browser.

| Example | Shows |
|---|---|
| [`energy-supplier-prd/`](examples/energy-supplier-prd/) | Current output: Jira-style PRD with the 5-screen mockup embedded |
| [`energy-partner-ticket/`](examples/energy-partner-ticket/) | Earlier format: partner integration with failure paths and ops stories |
| [`itsme-google-login/`](examples/itsme-google-login/) | Earlier format: identity and SSO epic |

How the skill flows: [`docs/flows/`](docs/flows/) (demo, user and call flow, plus a zoomable viewer).

---

## 3. Update

- **Claude app:** download the new `.plugin` files from the [latest release](https://github.com/KeyValueSoftwareSystems/peasy-claude-marketplace/releases/latest) and upload them again. They replace the old version.
- **Claude Code:** `/plugin marketplace update peasy-claude-marketplace`

See [CHANGELOG.md](CHANGELOG.md) for what changed.

---

## 4. Good to know

- **Design system source.** peasy-design first tries the live Peasy Design System artifact on claude.ai. If you don't have access, it uses the bundled offline copy (snapshot 29 Oct 2026) automatically.
- **Font.** Mockups embed Grold Rounded Slim. For downloaded `.pptx` decks, install the font on your machine (it's in `plugins/peasy-design/skills/peasy-design/design-system/fonts/`), subject to Peasy's font licence.
- **No Jira connector yet.** The PRD is an HTML page. Use **Copy as Jira markup** per issue. Jira keys default to `PEASY-XXX` unless you give real ones.
- **French.** UI copy is Dutch first. French strings are marked `[FR: todo]` and flagged by the linter.
- **Placeholders, not guesses.** The skill never invents prices, commissions, partner deals or legal text. It writes `€ XX`, `[N]` and lists open questions instead.

### Troubleshooting

| Problem | Fix |
|---|---|
| Claude doesn't use the skill | Mention Peasy in your prompt ("a Peasy ticket for…"), or start a new chat after installing. |
| Mockup step is skipped | peasy-design isn't installed or enabled. Install both plugins. |
| Upload fails | Upload the `.plugin` file as-is. Don't unzip it. |
| Fonts look wrong in a deck | Install Grold Rounded Slim locally (see above). |

---

## For maintainers

```text
.claude-plugin/marketplace.json      marketplace manifest (both plugins)
plugins/
  peasy-brainstormer/                0.5.0
    skills/peasy-brainstormer/
      SKILL.md
      references/  peasy-context.md · pm-thinking.md · ticket-format.md
      assets/prd/  template-jira.html · build.py · prd_lint.py · example-prd.json
  peasy-design/                      1.1.0
    skills/peasy-design/
      SKILL.md
      references/  brand-rules · audit-checklist · data-and-charts · product-docs
      design-system/  tokens · components · fonts · assets · starter
examples/  docs/flows/
scripts/validate.py   checks manifests, frontmatter, versions, referenced files
scripts/package.sh    builds dist/<plugin>.plugin
.github/workflows/    CI validation; release on tag
```

**Release a change**

1. Edit the skill. Bump `version` in the plugin's `.claude-plugin/plugin.json` **and** in `.claude-plugin/marketplace.json`.
2. `python3 scripts/validate.py`
3. Add a line to `CHANGELOG.md`, commit, push.
4. `git tag vX.Y.Z && git push origin vX.Y.Z`. GitHub Actions builds both `.plugin` files and publishes the release, so the download links above always serve the latest.

**Licence.** Code is MIT ([LICENSE](LICENSE)). Peasy brand assets, fonts and examples belong to Peasy and are not licensed for reuse ([NOTICE](NOTICE)).

Maintained by KeyValue Software Systems for Peasy.
