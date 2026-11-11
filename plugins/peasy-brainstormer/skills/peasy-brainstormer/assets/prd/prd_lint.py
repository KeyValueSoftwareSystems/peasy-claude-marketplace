#!/usr/bin/env python3
"""PRD lint for Peasy tickets.
ERRORS  = Peasy structure missing (must fix).
WARNINGS = readability guidance for grooming (fix unless there's a reason; content freedom is allowed).
Usage: python3 prd_lint.py prd.json"""
import json, re, sys

d = json.load(open(sys.argv[1]))
E, T = d["epic"], d["tickets"]
err, warn = [], []
words = lambda s: len(str(s).split())
def soft(path, text, limit, why=""):
    n = words(text)
    if n > limit: warn.append(f"{path}: {n} words (guide ≤{limit}){' – '+why if why else ''}")

# --- Structure (Peasy Jira epic format) ---
for k in ["key", "title", "fields", "summary", "goals", "people", "scope", "dependencies", "notes"]:
    if not E.get(k): err.append(f"epic.{k} missing")
for k in ["Type", "Status", "Priority", "Assignee", "Reporter", "Created", "Updated"]:
    if k not in E.get("fields", {}): err.append(f"epic.fields.{k} missing (use TBD)")
for k in ["figma", "tdd"]:
    if k not in E: err.append(f"epic.{k} missing (use TBD)")
if not E.get("scope", {}).get("included") or not E.get("scope", {}).get("excluded"):
    err.append("epic.scope needs included + excluded")

title_rx = re.compile(r"^[A-Z][\w ]+ - [^:]+: .+")
for t in T:
    p = t.get("key", "?")
    if not title_rx.match(t.get("title", "")): err.append(f"{p}: title must be 'Vertical - Area: action'")
    if not t.get("description"): err.append(f"{p}: description missing")
    if t.get("type") == "Story":
        if not t.get("ac"): err.append(f"{p}: story has no acceptance criteria")
        for i, a in enumerate(t.get("ac", []), 1):
            for k in ["title", "given", "when", "then"]:
                if not a.get(k): err.append(f"{p} AC{i}: '{k}' missing")

# --- Readability guidance (soft) ---
soft("epic.summary", E.get("summary", ""), 45)
for i, g in enumerate(E.get("goals", []), 1): soft(f"epic.goals[{i}]", g, 15)
if len(E.get("goals", [])) > 5: warn.append("epic.goals: more than 5 – keep the top ones")
for side in ["included", "excluded"]:
    for i, x in enumerate(E.get("scope", {}).get(side, []), 1): soft(f"epic.scope.{side}[{i}]", x, 10, "scope items are labels")
for i, x in enumerate(E.get("notes", []), 1): soft(f"epic.notes[{i}]", x, 25)

for t in T:
    p = t["key"]
    soft(f"{p}.title", t["title"], 14)
    soft(f"{p}.description", t.get("description", ""), 45, "say what changes, not why")
    acs = t.get("ac", [])
    if len(acs) > 8: warn.append(f"{p}: {len(acs)} ACs – consider splitting the story")
    for i, a in enumerate(acs, 1):
        soft(f"{p} AC{i}.title", a.get("title", ""), 8)
        for k in ["given", "when"]: soft(f"{p} AC{i}.{k}", a.get(k, ""), 20)
        then = a.get("then", "")
        for j, x in enumerate(then if isinstance(then, list) else [then], 1):
            soft(f"{p} AC{i}.then[{j}]", x, 20, "one outcome per line; use a list")
        if isinstance(then, str) and re.search(r"\b(and|,)\b.*\b(and)\b", then):
            warn.append(f"{p} AC{i}.then: several outcomes in one line – split into a list or 'and'")
        if re.search(r"\b(should|might|could|ideally|etc\.?)\b", " ".join(map(str, [a.get("given"), a.get("when"), then])), re.I):
            warn.append(f"{p} AC{i}: vague word (should/might/could/ideally/etc.) – use 'must' or state the behaviour")
    for i, x in enumerate(t.get("notes", []), 1): soft(f"{p}.notes[{i}]", x, 25)

# --- Audit checks (senior dev + PM) ---
if not E.get("problem"): warn.append("epic.problem missing – state the problem, not just the solution")
mets = E.get("metrics") or []
if not mets: err.append("epic.metrics missing – add metric, baseline, target")
for i, m in enumerate(mets, 1):
    if len(m) < 3 or not m[2]: warn.append(f"epic.metrics[{i}]: needs baseline and target")
for k in ["Components", "Fix version"]:
    if k not in E.get("fields", {}): warn.append(f"epic.fields.{k} missing (use TBD)")
keys = {t["key"] for t in T}
PII = re.compile(r"\b(EAN|address|adres|consent|e-?mail|phone|personal data|payload)\b", re.I)
for t in T:
    p = t["key"]
    if t.get("type") == "Story":
        if (t.get("points") or 0) > 5: warn.append(f"{p}: {t['points']} pts – split (INVEST: Small)")
        if not t.get("moscow"): warn.append(f"{p}: no MoSCoW priority")
        blob = json.dumps(t, ensure_ascii=False)
        if PII.search(blob) and not re.search(r"privacy|gdpr", " ".join(t.get("notes", [])), re.I):
            warn.append(f"{p}: touches personal data – add a Privacy note")
        for i, a in enumerate(t.get("ac", []), 1):
            then = " ".join(a["then"]) if isinstance(a.get("then"), list) else str(a.get("then", ""))
            if re.search(r"\b(dashboard shows|works|correctly|properly|user-friendly|fast)\b", then, re.I):
                warn.append(f"{p} AC{i}: outcome not testable – state an observable result")
        for dep in t.get("depends", []):
            if dep not in keys and not re.match(r"^[A-Z]+-\d+$", dep): warn.append(f"{p}: unknown dependency {dep}")
    fr = sum(1 for r in t.get("copy", []) if len(r) < 3 or not r[2])
    if fr: warn.append(f"{p}: {fr} copy string(s) without FR (blocks release in BE)")
G = d.get("grooming", {})
for k in ["risks", "rollout", "dod"]:
    if not G.get(k): warn.append(f"grooming.{k} missing")
for i, q in enumerate(G.get("questions", []), 1):
    if len(q) < 4: warn.append(f"grooming.Q{i}: add due date and blocked tickets")
for i, q in enumerate(G.get("questions", []), 1): soft(f"grooming.Q{i}", q[0], 20)

total = sum(words(x) for x in json.dumps({"epic": E, "tickets": T}, ensure_ascii=False).split('"') if x.strip(" :,{}[]"))
print(f"PRD words (excl. grooming): ~{total}  ·  tickets: {len(T)}  ·  ACs: {sum(len(t.get('ac',[])) for t in T)}")
for e in err: print("ERROR  ", e)
for w in warn: print("WARN   ", w)
print("OK – structure matches Peasy format" if not err else f"{len(err)} structural error(s)")
sys.exit(1 if err else 0)
