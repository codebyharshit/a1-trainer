"""Build the A1 trainer: generate all questions and inline everything into one HTML page.
Usage: python3 build.py  ->  dist/a1-trainer.html and dist/questions.json"""
import json, os
from gen import core, generators, manual, more, topics

ROOT = os.path.dirname(os.path.abspath(__file__))
dic = json.load(open(os.path.join(ROOT, "data", "dictionary.json")))
generators.run_all(dic)
more.run_all(dic)
manual.run()
import importlib
for mod in ("manual2", "manual3", "wordlist"):
    try:
        importlib.import_module("gen." + mod).run()
    except ModuleNotFoundError as e:
        if e.name != "gen." + mod: raise
        print(f"(skipping gen/{mod}.py – not found)")
seen, qs = set(), []
for q in core.QUESTIONS:
    if q["id"] in seen or len(q["o"]) < 2: continue
    seen.add(q["id"]); qs.append(q)
qs += [q for q in more.listening(qs) if q["id"] not in seen]
order = {k: i for i, k in enumerate(topics.TOPIC_KEYS)}
qs.sort(key=lambda q: order[q["t"]])
os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
json.dump(qs, open(os.path.join(ROOT, "dist", "questions.json"), "w"), ensure_ascii=False, indent=1)
tpl = open(os.path.join(ROOT, "web", "template.html")).read()
def js(x): return json.dumps(x, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (tpl.replace("/*__QUESTIONS__*/[]", js(qs))
           .replace("/*__TOPICS__*/[]", js([list(t) for t in topics.TOPICS]))
           .replace("/*__LABELS__*/{}", js(topics.LABELS))
           .replace("/*__DICT__*/[]", js(dic)))
open(os.path.join(ROOT, "dist", "a1-trainer.html"), "w").write(html)
print(f"{len(qs)} questions · {len(dic)} nouns · {len(html)//1024} KB")
