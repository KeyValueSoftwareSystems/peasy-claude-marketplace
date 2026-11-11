# Peasy skills for Claude

Two Claude skills that take a Peasy feature from rough idea to a Jira-ready epic with an on-brand mockup. Built by [KeyValue](https://www.keyvalue.systems) for the Peasy team.

- **peasy-brainstormer**: turns a one-line idea into a Jira-style PRD (epic + stories with acceptance criteria).
- **peasy-design**: designs, writes and reviews Peasy screens, flows, copy and decks on the Peasy Design System.

Install both. The brainstormer uses peasy-design for its mockups.

---

## Install

### Claude app (desktop or claude.ai)

1. Open **Customize → Plugins**. On the right side, choose **Add marketplace**.
2. Paste this link:
   ```text
   https://github.com/KeyValueSoftwareSystems/peasy-claude-marketplace
   ```
3. Install **peasy-brainstormer** and **peasy-design**.

Needs a paid Claude plan. If you don't see Plugins, ask your Claude admin to allow plugins.

### Claude Code

Paste this into Claude Code:

```text
Install the Peasy plugins: add the marketplace KeyValueSoftwareSystems/peasy-claude-marketplace, then install peasy-brainstormer and peasy-design from it.
```

Restart Claude Code when it's done.

---

## Try it

Start a new chat and type:

> Brainstorm adding a new energy supplier to the Peasy comparison.

Claude asks a few quick questions, plays back a brief, offers a mockup, then gives you one HTML page with the epic and stories. Say **"quick"** for a shorter run.

More to try:

- "Write a ticket for itsme and Google login on Peasy."
- "Design the Peasy car-insurance result page in Dutch."
- "Review this screen against the Peasy design system." (attach a screenshot)

See finished results in [`examples/`](examples/).

---

## Update

- **Claude app:** in **Customize → Plugins**, turn on **Sync automatically** or use **Check for updates**.
- **Claude Code:** ask it to "update the Peasy plugins".

What changed: [CHANGELOG.md](CHANGELOG.md).

---

## Good to know

- **Placeholders, not guesses.** It never invents prices, partner deals or legal text. It writes `€ XX` and lists open questions instead.
- **Dutch first.** French strings are marked `[FR: todo]`.
- **No Jira connector yet.** Use **Copy as Jira markup** on each issue.
- **Works offline.** peasy-design uses the live Peasy Design System if you have access, otherwise a bundled copy.

| Problem | Fix |
|---|---|
| Claude doesn't use the skill | Mention Peasy in your prompt, or start a new chat after installing. |
| Mockup step is skipped | Install and enable peasy-design too. |
| Fonts look wrong in a deck | Install Grold Rounded Slim from `plugins/peasy-design/skills/peasy-design/design-system/fonts/`. |

---

## For maintainers

1. Edit the skill. Bump `version` in the plugin's `.claude-plugin/plugin.json` and in `.claude-plugin/marketplace.json`.
2. Run `python3 scripts/validate.py`.
3. Add a line to `CHANGELOG.md`, commit, push.
4. `git tag vX.Y.Z && git push origin vX.Y.Z`. GitHub Actions validates and publishes the release.

Code is MIT ([LICENSE](LICENSE)). Peasy brand assets, fonts and examples belong to Peasy ([NOTICE](NOTICE)). Maintained by KeyValue Software Systems.
