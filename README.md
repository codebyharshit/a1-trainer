# A1 Trainer (Netzwerk neu A1)

One self-contained web page with four parts:

- **Quiz** – ~11,000 questions: 31 grammar topics (all 12 chapters) plus article, meaning and plural
  questions for every dictionary noun. „Weiter lernen“ is adaptive: new material in course order (a topic
  counts as solid after ~20 questions at 80%+), misses come back 3–5 questions later, known questions come
  back as spaced reviews (5 min → 1 → 3 → 7 → 16 → 35 days). Progress is saved after every answer and a
  reload resumes on the same question. Every question stores
  the correct sentence split into labelled parts (Subjekt, Verb · Pos. 2, Akkusativ, …), a rule,
  and an explanation for every wrong option.
- **Listening, writing, speaking** – listening questions use the browser's German voice; tick „Writing practice“
  to type answers to gap questions; after every answer „Hear it“ reads the sentence and „Say it“ checks your
  pronunciation (speech recognition: Chrome/Edge/Safari).
- **Fehler** – your saved mistakes (account storage when opened in Claude, otherwise the browser).
- **Wörterbuch** – 2,622 frequent nouns with article, plural, meaning and the reason for the article,
  plus an article quiz.
- **Grammatik** – every topic's lesson, your accuracy, and per-topic practice.

## Build

    python3 build.py        # -> dist/a1-trainer.html (+ dist/index.html), dist/questions.json

No dependencies beyond Python 3.

## Layout

    data/dictionary.json   nouns: n=noun a=article e=english p=plural r=reason x=note t=topic
    gen/topics.py          topics (course order), lessons, structure labels
    gen/verbs.py           A1 verbs + conjugation / imperative helpers
    gen/nouns.py           curated A1 nouns used in sentence templates
    gen/generators.py      template generators (verbs, articles, Akkusativ, Dativ, Perfekt …)
    gen/more.py            wider generators (time, dates, numbers, pronouns, Wechselpräp., …) + vocabulary topics
    gen/manual.py          hand-written questions (W-questions, connectors, everyday phrases …)
    gen/manual2.py         more hand-written questions
    gen/manual3.py         Akkusativ prepositions, comparison, countries, Dativ possessives, doch …
    gen/wordlist.py        A1 verbs, adjectives and small words (meaning, opposite)
    gen/core.py            question format + helpers
    web/template.html      the app (vanilla JS, no build step)

## Adding questions

Hand-written questions use a tiny spec: segments separated by ` / `, each `text#LABEL`,
and `{…}` marks the gap. Options list the correct answer first; `why` explains wrong options.

    add("akk", "Ich#S / kaufe#V / {einen} Apfel.#AKK", ["einen", "ein", "einem"],
        "der Apfel → einen Apfel (Akkusativ).",
        {"ein": "ein is Nominativ.", "einem": "einem is Dativ."})

Labels: S, V, V1, IMP, MV, HV, INF, P2, PRE, AKK, DAT, NOM, ZEIT, ORT, W, ADJ, KON, NEG, ADV.

## Saved data (when opened in Claude)

Collection `data/users/<you>` (or localStorage `a1trainer-v1` in a plain browser): `q_<id>` quiz mistakes,
`a_<hash>` article mistakes, `stats`, `p_<topic>` per-question progress `{qid: [box, dueMinute, seen, right, lastMinute]}`,
and `meta` (answers per day, the question currently on screen).
Each mistake keeps the prompt, your answers, the correct answer, the rule, how often you got it
wrong, and whether it's learned (2 right answers in a row).

Dictionary sources: Wiktionary (via kaikki.org, CC BY-SA) for gender/plural/meaning,
OpenSubtitles frequency list (hermitdave/FrequencyWords) and the Leipzig Corpora word list
for ranking. Article reasons are computed from suffix/compound rules and hand-checked for A1 words.
