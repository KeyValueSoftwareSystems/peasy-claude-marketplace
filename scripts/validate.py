#!/usr/bin/env python3
"""Checks manifests, SKILL.md frontmatter, versions in sync, and that referenced files exist."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
errors = []
mk = json.loads((root / ".claude-plugin/marketplace.json").read_text())
for entry in mk["plugins"]:
    pdir = root / entry["source"]
    pj = json.loads((pdir / ".claude-plugin/plugin.json").read_text())
    if pj["name"] != entry["name"]: errors.append(f"{entry['name']}: name mismatch")
    if pj.get("version") != entry.get("version"): errors.append(f"{entry['name']}: version {pj.get('version')} != marketplace {entry.get('version')}")
    for skill in (pdir / "skills").glob("*/SKILL.md"):
        text = skill.read_text()
        m = re.match(r"---\n(.*?)\n---", text, re.S)
        if not m or "name:" not in m.group(1) or "description:" not in m.group(1):
            errors.append(f"{skill}: missing frontmatter name/description")
        for ref in set(re.findall(r"`((?:references|assets|design-system)/[^`\s<>*]+?\.[a-z]{2,5})`", text)):
            if not (skill.parent / ref).exists(): errors.append(f"{skill.relative_to(root)}: missing {ref}")
print("\n".join(errors) or "OK: marketplace, plugins and skill references valid")
sys.exit(1 if errors else 0)
