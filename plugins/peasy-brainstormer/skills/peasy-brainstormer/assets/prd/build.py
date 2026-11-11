#!/usr/bin/env python3
"""Build a self-contained Peasy PRD (Jira-style issue view).

  python3 build.py prd.json [mockup.html] > <kebab-title>-prd.html

- prd.json      : the PRD content (schema: references/prd-format.md)
- mockup.html   : optional local mockup from peasy-design; embedded in the file.
                  Screens are found by a leading text "Scherm N" (or "Screen N");
                  stories link to them with "mock": "Scherm N".
If the mockup is a claude.ai Design artifact instead, omit mockup.html and set
"mockup": {"url": "<artifact url>"} in prd.json.
"""
import base64, json, os, sys

here = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(here, "template-jira.html"), encoding="utf-8").read()
data = json.load(open(sys.argv[1], encoding="utf-8"))

# Silences uncaught errors in the embedded mockup (clean console in viewers).
QUIET = "<script>addEventListener('error',function(e){e.preventDefault()},true);addEventListener('unhandledrejection',function(e){e.preventDefault()});</script>"
# Deep-link contract: parent posts {scherm:N} or URL has #scherm-N → scroll to screen N.
DEEPLINK = """<script>/* PRD deep-link: #scherm-N or postMessage({scherm:N}) */
(function(){function go(x){var h=x||location.hash.slice(1);if(!h)return;var n=h.replace('scherm-','');
var el=[].slice.call(document.querySelectorAll('body *')).find(function(e){var t=e.textContent.trim(),m=t.match(/^(Scherm|Screen)\\s*(\\d+)/);return e.children.length===0&&m&&m[2]===n});
if(el){var s=el.closest('section')||el.parentElement;s.scrollIntoView({block:'start'});}}
addEventListener('hashchange',function(){go()});addEventListener('message',function(e){if(e.data&&e.data.scherm){go('scherm-'+e.data.scherm);}});
addEventListener('load',function(){setTimeout(function(){go()},400)});})();</script>"""

b64 = ""
if len(sys.argv) > 2:
    mock = open(sys.argv[2], encoding="utf-8").read()
    if QUIET not in mock:
        mock = mock.replace("<head>", "<head>" + QUIET, 1) if "<head>" in mock else QUIET + mock
    if "PRD deep-link" not in mock:
        mock = mock.replace("</body>", DEEPLINK + "</body>") if "</body>" in mock else mock + DEEPLINK
    b64 = base64.b64encode(mock.encode("utf-8")).decode()
    data.setdefault("mockup", {})["file"] = data.get("mockup", {}).get("file") or os.path.basename(sys.argv[2])
elif not (data.get("mockup") or {}).get("url"):
    data.pop("mockup", None)

out = tpl.replace("__PRD_JSON__", json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")).replace("__MOCKUP_B64__", b64)
sys.stdout.write(out)
