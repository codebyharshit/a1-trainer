"""Template-based question generators. Each function appends to core.QUESTIONS."""
from .core import add, choose, pick, R
from .verbs import parse, forms, imperative, kind, stem, PRON, CAP, PRON_EN, SEIN, HABEN, WAR, HATTE, MODALS
from .nouns import N, g
from . import topics

VERBS = parse()
VB = {v["inf"]: v for v in VERBS}
SUBJ = {"ich": ["Ich"], "du": ["Du"], "er": ["Er", "Anna", "Mein Bruder", "Herr Weber", "Sie (she)"], "wir": ["Wir", "Mein Mann und ich"],
        "ihr": ["Ihr"], "sie": ["Sie", "Die Kinder", "Tom und Lisa", "Meine Eltern"]}
def subj(p):
    return R.choice(SUBJ[p])
FORM_NAME = {"ich": "ich-form", "du": "du-form", "er": "er/sie/es-form", "wir": "wir-form", "ihr": "ihr-form", "sie": "sie/Sie-form"}


def form_why(f, target_p):
    """Explain each wrong conjugated form by naming which person it belongs to."""
    why = {}
    for p in PRON:
        if f[p] != f[target_p] and f[p] not in why:
            same = [q for q in PRON if f[q] == f[p]]
            why[f[p]] = f"'{f[p]}' is the {' / '.join(FORM_NAME[q] for q in same)}. For {PRON_EN[target_p]} you need '{f[target_p]}'."
    return why


# ---------- 1. verb endings ----------
def verb_endings():
    regular = [v for v in VERBS if not v["pre"] and kind(v) in ("regular", "-t/-d stem", "s-sound stem")]
    irregular = [v for v in VERBS if not v["pre"] and kind(v) in ("e→i/ie", "a→ä")]
    for v in regular:
        ps = list(PRON)
        if "nopl" in v["flags"]:
            ps = ["ich", "du", "er"]
        for p in ps:
            f = forms(v)
            opts = [f[p]] + pick([x for x in set(f.values()) if x != f[p]], 2)
            extra = {"-t/-d stem": " The stem ends in -t/-d, so an extra -e- is added: du " + f["du"] + ", er " + f["er"] + ".",
                     "s-sound stem": " The stem ends in an s-sound, so du only adds -t: du " + f["du"] + "."}.get(kind(v), "")
            add("verb", [[subj(p), "S"], ["{" + f[p] + "}", "V"], [v["ctx"] + ".", v["ctx_lab"]]],
                opts, f"{v['inf']} ({v['en']}) → {p} {f[p]}." + extra, form_why(f, p), note=v["inf"])
    for v in irregular:
        for p in ["du", "er"]:
            f = forms(v)
            reg = stem(v["base"]) + ("st" if p == "du" else "t")
            opts = list(dict.fromkeys([f[p], reg, f["ihr"], f["ich"], f["wir"]]))[:3]
            why = form_why(f, p)
            why[reg] = f"'{reg}' would be the regular form — but {v['inf']} changes its vowel ({kind(v)}) in the du and er/sie/es forms: du {f['du']}, er {f['er']}."
            add("verb_irr", [[subj(p), "S"], ["{" + f[p] + "}", "V"], [v["ctx"] + ".", v["ctx_lab"]]],
                opts, f"{v['inf']} is a {kind(v)} verb: du {f['du']}, er/sie/es {f['er']} — but ihr {f['ihr']}, wir {f['wir']}.", why, note=v["inf"])
    # vowel change does NOT happen in ich / wir / ihr
    for v, p in [(v, p) for v in irregular for p in ["ich", "wir", "ihr", "sie"]]:
        f = forms(v)
        wrong = {"ich": f["er"][:-1] + "e", "wir": f["er"][:-1] + "en", "ihr": f["er"], "sie": f["er"][:-1] + "en"}[p]
        if wrong == f["er"]: wrong = f["du"]
        add("verb_irr", [[subj(p), "S"], ["{" + f[p] + "}", "V"], [v["ctx"] + ".", v["ctx_lab"]]],
            list(dict.fromkeys([f[p], wrong, f["er"]])), f"The vowel change of {v['inf']} only happens in du and er/sie/es. {p} {f[p]} keeps the normal vowel.",
            {wrong: (f"'{wrong}' is the du-form." if wrong == f["du"] else f"No vowel change for '{p}' — only du and er/sie/es change."), f["er"]: f"'{f['er']}' is the er/sie/es-form."})


def sein_haben():
    ctx_s = {"ich": "müde", "du": "sehr nett", "er": "Arzt", "wir": "Kollegen", "ihr": "zu spät", "sie": "aus Spanien"}
    lab_s = {"ich": "ADJ", "du": "ADJ", "er": "NOM", "wir": "NOM", "ihr": "ADJ", "sie": "ORT"}
    ctx_h = {"ich": "Hunger", "du": "heute Zeit", "er": "zwei Kinder", "wir": "einen Hund", "ihr": "ein Auto", "sie": "keine Zeit"}
    for p in PRON:
        add("seinhaben", [[CAP[p] if p != "er" else "Sie (she)", "S"], ["{" + SEIN[p] + "}", "V"], [ctx_s[p] + ".", lab_s[p]]],
            [SEIN[p]] + pick([x for x in set(SEIN.values()) if x != SEIN[p]] + ["sein", "seit"], 2),
            f"sein: ich bin · du bist · er/sie/es ist · wir sind · ihr seid · sie/Sie sind.", form_why(SEIN, p) | {"sein": "'sein' is the infinitive — it must be conjugated.", "seit": "'seit' (with t) is a preposition meaning 'since'. ihr seid (with d)."})
        add("seinhaben", [[CAP[p] if p != "er" else "Er", "S"], ["{" + HABEN[p] + "}", "V"], [ctx_h[p] + ".", "AKK"]],
            [HABEN[p]] + pick([x for x in set(HABEN.values()) if x != HABEN[p]] + ["habst", "habet"], 2),
            "haben: ich habe · du hast · er/sie/es hat · wir haben · ihr habt · sie/Sie haben. du and er drop the b.",
            form_why(HABEN, p) | {"habst": "No b in the du-form: du hast.", "habet": "Not a form. ihr habt."})


# ---------- 2. yes/no questions & word order ----------
def janein():
    items = [("Du", "spielst", "gern Tennis", "AKK"), ("Sie", "arbeiten", "am Wochenende", "ZEIT"), ("Er", "liest", "gern Romane", "AKK"),
             ("Du", "hast", "heute Abend Zeit", "ZEIT"), ("Ihr", "fahrt", "am Freitag nach Berlin", "ORT"), ("Sie", "ist", "Ärztin", "NOM"),
             ("Du", "kommst", "aus Indien", "ORT"), ("Sie", "sprechen", "Englisch", "AKK"), ("Ihr", "wohnt", "in Hamburg", "ORT"),
             ("Er", "trinkt", "keinen Kaffee", "AKK"), ("Du", "bist", "müde", "ADJ"), ("Sie", "haben", "eine Frage", "AKK")]
    for s, v, rest, lab in items:
        sl = s if s in ("Sie",) else s.lower()
        correct = f"{v.capitalize()}#V1 / {sl}#S / {rest}?#{lab}"
        choose("janein", f"Make a yes/no question: „{s} {v} {rest}.“", correct,
               [f"{v.capitalize()} {rest} {sl}?", f"{s} {rest} {v}?"] + ([f"{v.capitalize()} {rest.split()[0]} {sl} {' '.join(rest.split()[1:])}?"] if len(rest.split()) > 1 else []),
               "Yes/no question: the verb jumps to position 1, the subject follows directly. Everything else stays in place.",
               {f"{v.capitalize()} {rest} {sl}?": "The subject must come directly after the verb.", f"{s} {rest} {v}?": "In questions the verb doesn't go to the end — it goes to position 1.", f"{v.capitalize()} {rest.split()[0]} {sl} {' '.join(rest.split()[1:])}?": "Nothing may stand between the verb and the subject in a yes/no question."},
               note="German has no helper verb like English 'do' — the main verb itself moves to the front.")
    stmts = [("Heute", "ZEIT", "gehe", "ich", "ins Kino", "ORT"), ("Am Montag", "ZEIT", "habe", "ich", "frei", "ADV"),
             ("Morgen", "ZEIT", "fährt", "er", "nach Köln", "ORT"), ("In München", "ORT", "wohnen", "wir", "seit drei Jahren", "ZEIT"),
             ("Am Wochenende", "ZEIT", "spiele", "ich", "Tischtennis", "AKK"), ("Um 8 Uhr", "ZEIT", "beginnt", "der Kurs", "", ""),
             ("Jetzt", "ZEIT", "lerne", "ich", "Deutsch", "AKK"), ("Im Sommer", "ZEIT", "reisen", "wir", "nach Italien", "ORT"),
             ("Danach", "ADV", "trinken", "wir", "einen Kaffee", "AKK"), ("Den Film", "AKK", "finde", "ich", "super", "ADJ"),
             ("Abends", "ZEIT", "kocht", "mein Mann", "", ""), ("Leider", "ADV", "habe", "ich", "keine Zeit", "AKK"),
             ("Am Abend", "ZEIT", "sieht", "sie", "fern", "PRE"), ("Zuerst", "ADV", "frühstücke", "ich", "", ""), ("Dann", "ADV", "gehe", "ich", "zur Arbeit", "ORT")]
    for p1, l1, v, s, rest, lr in stmts:
        tail = f" / {rest}.#{lr}" if rest else ""
        spec = f"{p1}#{l1} / {v}#V / {s}#S" + (tail if rest else ".#")
        if not rest:
            spec = f"{p1}#{l1} / {v}#V / {s}.#S"
        r = (" " + rest) if rest else ""
        choose("satzbau", "Which sentence is correct?", spec,
               [f"{p1} {s} {v}{r}.", (f"{s[0].upper() + s[1:]} {p1[0].lower() + p1[1:]} {v}{r}." if l1 != "AKK" else f"{p1} {s} {r.strip()} {v}.")],
               f"Verb in position 2! '{p1}' takes position 1, so the verb '{v}' comes next and the subject '{s}' moves behind it.",
               {f"{p1} {s} {v}{r}.": f"Subject before the verb puts the verb in position 3. After '{p1}' the verb must come next.", (f"{s[0].upper() + s[1:]} {p1[0].lower() + p1[1:]} {v}{r}." if l1 != "AKK" else f"{p1} {s} {r.strip()} {v}."): "The verb must be the 2nd element — here it comes too late."},
               note="English puts the subject before the verb (Today I go …). German keeps the verb in position 2 and moves the subject.")


# ---------- 3. articles & plural ----------
RULE_EXPL = {
 "-ung": "nouns ending in -ung are always die", "-heit": "-heit is always die", "-keit": "-keit is always die", "-schaft": "-schaft is always die",
 "-ion": "-ion is always die", "-tät": "-tät is always die", "-ik": "-ik is die", "-ie": "-ie is die", "-ei": "-ei is die", "-ur": "-ur is die",
 "-e": "about 90% of nouns ending in -e are die", "-chen": "-chen (diminutive) is always das", "-um": "-um is das", "-ment": "-ment is das",
 "-ma": "-ma is das", "-o": "nouns ending in -o are usually das", "Ge-": "Ge- nouns are usually das", "-in": "-in marks a female person → die",
 "male": "male people and animals are der", "female": "female people are die", "day": "days of the week are der", "month": "months are der",
 "season": "seasons are der", "weather": "weather words are der", "direction": "compass directions are der", "-en": "nouns ending in -en (not verbs) are usually der",
 "-er": "nouns in -er for people/tools are usually der", "compound": "in a compound, the LAST part decides the article", "-ling": "-ling is der",
 "-ismus": "-ismus is der", "-or": "-or is der", "-kunft": "-kunft is die", "-nis": "-nis is usually das", "-zeug": "-zeug is das", "verb": "an infinitive used as a noun is das",
 "foreign": "English/French loanwords are often das", "daytime": "parts of the day are der", "-enz": "-enz is die", "-age": "-age is die", "-a": "-a is usually die",
}
def artikel(dic):
    pool = [d for d in dic if d["t"] and d["r"] in RULE_EXPL and d["r"] not in ("two genders",)]
    R.shuffle(pool)
    frames = [("Wo ist {A} {N}?", "W|V|S"), ("{A} {N} ist neu.", "S|V|ADJ"), ("{A} {N} ist hier.", "S|V|ORT"), ("Wie findest du {a} {N}?", "")]
    used = 0
    for d in pool:
        if used >= 160: break
        a = d["a"]; n = d["n"]
        rule = RULE_EXPL[d["r"]] + (f" ({d['x'].replace('← ', 'last part: ')})" if d["x"] else "") + "."
        why = {o: f"Not {o}: {n} is {a} — {RULE_EXPL[d['r']]}." for o in ("der", "die", "das") if o != a}
        if d["r"] == "compound": why = {o: f"Look at the last part: {d['x'].replace('← ', '')} → so {a} {n}." for o in ("der", "die", "das") if o != a}
        fr = used % 3
        if fr == 0: segs = [["Wo", "W"], ["ist", "V"], ["{" + a + "} " + n + "?", "S"]]
        elif fr == 1: segs = [["{" + a.capitalize() + "} " + n, "S"], ["ist", "V"], ["neu.", "ADJ"]]
        else: segs = [["{" + a.capitalize() + "} " + n, "S"], ["ist", "V"], ["hier.", "ORT"]]
        opts = ["der", "die", "das"] if fr == 0 else ["Der", "Die", "Das"]
        corr = a if fr == 0 else a.capitalize()
        opts = [corr] + [o for o in opts if o != corr]
        why = {(k if fr == 0 else k.capitalize()): v for k, v in why.items()}
        add("artikel", segs, opts, f"{a} {n} ({d['e']}): {rule}", why, note=f"{a} {n}")
        used += 1
    # plural article always die
    for n in pick([x for x in N.values() if x["p"] not in ("–",) and x["a"] != "die"], 20):
        add("artikel", [["{Die} " + n["p"], "S"], ["sind", "V"], ["neu.", "ADJ"]], ["Die", n["a"].capitalize(), "Den"],
            f"Plural nouns always take die — even if the singular is {n['a']} {n['n']}.",
            {n["a"].capitalize(): f"{n['a']} is only for the singular ({n['a']} {n['n']}). Plural is always die {n['p']}.", "Den": "den is masculine Akkusativ (or Dativ plural). Here it's the subject in the plural → die."})


def plural_type(sg, pl):
    if pl == sg: return "no change"
    if pl.endswith("s") and pl[:-1] == sg: return "-s"
    if pl.endswith("en") or pl.endswith("n") and pl[:-1] == sg: return "-(e)n"
    if pl.endswith("er"): return "-er (+ umlaut)"
    if pl.endswith("e"): return "-e" + (" + umlaut" if pl[:-1] != sg else "")
    if pl[:len(sg)] != sg: return "umlaut"
    return "other"

def fake_plurals(sg, pl, a):
    cands = [sg + "s", sg + "en" if not sg.endswith("e") else sg + "n", sg + "e", sg + "er", sg]
    um = sg.replace("a", "ä", 1).replace("o", "ö", 1).replace("u", "ü", 1) if any(c in sg for c in "aou") else sg
    cands += [um + "e", um + "er"]
    out = []
    for c in cands:
        if c != pl and c not in out:
            out.append(c)
    R.shuffle(out)
    return out[:2]

def plural():
    pool = [x for x in N.values() if x["p"] not in ("–",)]
    for n in pool:
        typ = plural_type(n["n"], n["p"])
        wrong = fake_plurals(n["n"], n["p"], n["a"])
        hint = {"der": "Short der-words often take -e (sometimes with umlaut).", "das": "Short das-words often take -er + umlaut.", "die": "Most die-words take -(e)n."}[n["a"]]
        add("plural", [["ein " + n["n"] if n["a"] != "die" else "eine " + n["n"], "NOM"], ["→ zwei {" + n["p"] + "}", "NOM"]],
            ["die " + n["p"]] + ["die " + w for w in wrong], f"{n['a']} {n['n']} → die {n['p']} (type: {typ}). {hint}",
            {"die " + w: f"'{w}' isn't the plural. The plural of {n['n']} is {n['p']} — type {typ}. You have to learn the plural with each noun." for w in wrong},
            prompt=f"Plural of {n['a']} {n['n']} ({n['e']}):", note=f"{n['a']} {n['n']}, die {n['p']}")


# ---------- 4. ein / kein ----------
def einkein():
    pool = list(N.values())
    for n in pool:
        e = "eine" if n["a"] == "die" else "ein"
        add("einkein", [["Das", "S"], ["ist", "V"], ["{" + e + "} " + n["n"] + ".", "NOM"]], [e, "eine" if e == "ein" else "ein", "einen"],
            f"{n['a']} {n['n']} → {e}. ein for der and das, eine for die. After sein it's Nominativ, so no -en.",
            {"einen": "einen is Akkusativ (masculine). After 'Das ist' you need Nominativ → " + e + ".",
             ("eine" if e == "ein" else "ein"): f"{n['n']} is {n['a']} → {e}."}, note=f"{n['a']} {n['n']}")
    pairs = [("Bus", "Straßenbahn"), ("Auto", "Taxi"), ("U-Bahn", "Zug"), ("Park", "Garten"), ("Bahnhof", "Hotel"), ("Kirche", "Museum"),
             ("Tasche", "Rucksack"), ("Hund", "Katze"), ("Buch", "Wörterbuch"), ("Jacke", "Mantel"), ("Tisch", "Schrank"), ("Laptop", "Handy")]
    for a, b in pairs:
        na, nb = N[a], N[b]
        k = "keine" if na["a"] == "die" else "kein"
        e = "eine" if nb["a"] == "die" else "ein"
        add("einkein", [["Nein, das", "S"], ["ist", "V"], ["{" + k + "} " + a + ".", "NEG"], ["Das ist " + e + " " + b + ".", ""]],
            [k, "nicht ein" if k == "kein" else "nicht eine", "keine" if k == "kein" else "kein"],
            f"Negate a noun with kein: ein → kein, eine → keine. {a} is {na['a']} → {k}.",
            {"nicht ein": "German doesn't say 'nicht ein' — use kein.", "nicht eine": "German doesn't say 'nicht eine' — use keine.",
             "keine": f"{a} is {na['a']}, not die → kein.", "kein": f"{a} is die → keine."},
            prompt=f"Ist das {'eine' if na['a']=='die' else 'ein'} {a}? – Nein, das ist ___ {a}. Das ist {e} {b}.")
    nicht = [("Das ist {nicht} teuer.", "ADJ", "adjective"), ("Ich komme heute {nicht}.", "V", "verb"), ("Er spielt {nicht} gern Fußball.", "ADV", "activity"),
             ("Wir haben {keine} Zeit.", "AKK", "noun (die Zeit)"), ("Ich habe {keinen} Hunger.", "AKK", "noun (der Hunger, Akkusativ)"),
             ("Sie hat {keine} Kinder.", "AKK", "plural noun"), ("Das Essen schmeckt {nicht}.", "V", "verb"), ("Der Kaffee ist {nicht} heiß.", "ADJ", "adjective"),
             ("Ich trinke {keinen} Alkohol.", "AKK", "noun (der Alkohol)"), ("Er wohnt {nicht} in Berlin.", "ORT", "place"), ("Hast du {kein} Handy?", "AKK", "noun (das Handy)"),
             ("Ich verstehe das {nicht}.", "V", "verb")]
    for s, lab, what in nicht:
        corr = s[s.index("{") + 1:s.index("}")]
        opts = [corr] + [x for x in ["nicht", "kein", "keine", "keinen"] if x != corr][:2]
        if corr == "nicht": opts = ["nicht", "kein", "keine"]
        add("einkein", [[s, ""]], opts, f"Negating a {what} → {corr}. kein/keine/keinen negate nouns (that would have ein or no article); nicht negates everything else.",
            {o: ("nicht negates verbs, adjectives, places — but this negates a noun → " + corr + ".") if o == "nicht" else (f"kein-words go before nouns. Here you negate a {what} → nicht." if corr == "nicht" else f"Wrong ending: the noun is {what} → {corr}.") for o in opts[1:]})


# ---------- 5. imperative ----------
def imperativ():
    vs = [v for v in VERBS if v["base"] not in ("heißen", "passieren", "kennen", "bekommen", "verlieren", "gewinnen", "liegen", "sitzen", "wiederholen")
          and v["inf"] not in ("ankommen", "aussehen", "einschlafen", "aufwachen", "kommen", "abfahren", "umsteigen")]
    for v, who in [(v, w) for v in vs for w in ("du", "ihr", "Sie")]:
        im = imperative(v); f = forms(v)
        pre = v["pre"]
        ctx = v["ctx"]
        if who == "du":
            corr = im["du"].capitalize()
            wrong = [f["du"].capitalize(), (f["du"].capitalize() + " du") if not pre else f["du"].capitalize()]
            if kind(v) == "a→ä": wrong = [f["du"].capitalize(), f["du"][:-2].capitalize() if f["du"].endswith("st") else f["du"][:-1].capitalize()]
            if kind(v) == "e→i/ie": wrong = [f["du"].capitalize(), (stem(v["base"])).capitalize()]
            rule = f"du-imperative: du {f['du']} → drop -st and du → {im['du']}!" + (" The a→ä change does NOT happen in the imperative." if kind(v) == "a→ä" else "") + (" The e→i/ie change stays." if kind(v) == "e→i/ie" else "")
        elif who == "ihr":
            corr = im["ihr"].capitalize(); wrong = [f["ihr"].capitalize() + " ihr", im["du"].capitalize()]
            rule = f"ihr-imperative = ihr-form without ihr: ihr {f['ihr']} → {im['ihr'].capitalize()}!"
        else:
            corr = v["base"].capitalize() + " Sie"; wrong = ["Sie " + v["base"], im["du"].capitalize()]
            rule = f"Sie-imperative: infinitive + Sie, verb first → {v['base'].capitalize()} Sie …!"
        tail = (" " + ctx) + ((" " + pre) if pre else "") + "!"
        if pre and who == "du": wrong.append(pre.capitalize() + im["du"])
        wrong = list(dict.fromkeys(w for w in wrong if w != corr))
        segs = [["{" + corr + "}", "IMP"], [ctx, v["ctx_lab"] if v["ctx_lab"] != "DAT" else "DAT"]] + ([[pre + "!", "PRE"]] if pre else [])
        if not pre: segs[-1][0] += "!"
        why = {}
        for w in wrong:
            if pre and w.lower().startswith(pre): why[w] = f"The prefix '{pre}' separates and goes to the end: {corr} … {pre}!"
            elif " du" in w or " ihr" in w: why[w] = "No pronoun in du/ihr imperatives — just the verb."
            elif w.startswith("Sie "): why[w] = "That's a statement (Sie + verb). The imperative puts the verb first: " + corr + "."
            elif w.lower() == f["du"]: why[w] = f"'{w}' is the normal du-form. For the imperative drop the -st: {im['du']}!"
            elif who == "Sie": why[w] = f"'{w}' is the du-imperative. For Sie: {corr} …!"
            elif who == "ihr": why[w] = f"'{w}' is the du-imperative. For ihr use the ihr-form: {corr}!"
            else: why[w] = f"Not correct for {who}. → {corr}"
        add("imp", segs, [corr] + wrong[:2], rule + (f" The prefix '{pre}' goes to the end." if pre else ""), why,
            prompt=f"({who}, {v['inf']}) ___ {ctx}{(' ' + pre) if pre else ''}!", note=f"{v['inf']} – {v['en']}")
    for who, corr, wr in [("du", "Sei", ["Bist", "Seid"]), ("ihr", "Seid", ["Sei", "Seit"]), ("Sie", "Seien Sie", ["Sind Sie", "Sei"])]:
        add("imp", [["{" + corr + "}", "IMP"], ["bitte pünktlich!", "ADJ"]], [corr] + wr, "sein is irregular in the imperative: Sei! (du) · Seid! (ihr) · Seien Sie! (Sie)",
            {w: "Imperative of sein: Sei! · Seid! · Seien Sie!" for w in wr}, prompt=f"({who}, sein) ___ bitte pünktlich!")


# ---------- 6. Akkusativ ----------
AKK = {"der": ("den", "einen", "keinen"), "die": ("die", "eine", "keine"), "das": ("das", "ein", "kein")}
NOMF = {"der": ("der", "ein", "kein"), "die": ("die", "eine", "keine"), "das": ("das", "ein", "kein")}
def akkusativ():
    things = [N[x] for x in ["Apfel", "Kuchen", "Saft", "Pullover", "Rucksack", "Stuhl", "Laptop", "Schlüssel", "Mantel", "Koffer", "Tisch", "Termin", "Kühlschrank", "Spiegel",
                            "Teppich", "Löffel", "Computer", "Brief", "Film", "Tee",
                            "Tasche", "Jacke", "Lampe", "Tasse", "Uhr", "Pizza", "Tomate", "Banane", "Hose", "Fahrkarte", "Wohnung", "Brille", "Zeitung", "Kreditkarte", "Flasche",
                            "Brot", "Buch", "Handy", "Fahrrad", "Hemd", "Ticket", "Sofa", "Auto", "Regal", "Geschenk", "Wörterbuch", "Kleid", "Bett", "Bild", "Ei", "Glas", "Messer", "Foto"]]
    frames = [("Ich", "kaufe"), ("Wir", "brauchen"), ("Er", "sucht"), ("Ich", "nehme"), ("Sie", "hat"), ("Ich", "möchte"), ("Du", "siehst"), ("Wir", "haben")]
    masc = [t for t in things if t["a"] == "der"]
    rest = [t for t in things if t["a"] != "der"]
    sel = [(t, k) for t in things for k in range(3)]
    for i, (t, kind_i) in enumerate(sel):
        s, v = frames[(i * 7 + kind_i) % len(frames)]
        corr = AKK[t["a"]][kind_i]
        nom = NOMF[t["a"]][kind_i]
        opts = [corr]
        if t["a"] == "der": opts += [nom, {0: "dem", 1: "einem", 2: "keinem"}[kind_i]]
        elif t["a"] == "die": opts += [{0: "den", 1: "einen", 2: "keinen"}[kind_i], {0: "der", 1: "einer", 2: "keiner"}[kind_i]]
        else: opts += [{0: "den", 1: "einen", 2: "keinen"}[kind_i], {0: "dem", 1: "einem", 2: "keinem"}[kind_i]]
        q = "?" if s == "Du" else "."
        segs = [[s, "S"], [v, "V"], ["{" + corr + "} " + t["n"] + q, "AKK"]]
        rule = f"{t['n']} is the object (Wen/Was {v} {s.lower() if s!='Ich' else 'ich'}?) → Akkusativ. {t['a']} {t['n']} → {corr} {t['n']}." + (" Only masculine changes in the Akkusativ." if t["a"] != "der" else " Masculine: der→den, ein→einen, kein→keinen.")
        why = {}
        for o in opts[1:]:
            if o == nom and t["a"] == "der": why[o] = f"'{o}' is Nominativ (subject form). {t['n']} is the object → Akkusativ → {corr}."
            elif o.endswith("em") or o.endswith("er") and o != "der": why[o] = f"'{o}' is a Dativ form. kaufen/brauchen/haben … take the Akkusativ → {corr}."
            elif o == "der": why[o] = f"'der' here would be Dativ feminine (or Nominativ masculine). {t['n']} is die, and die stays die in the Akkusativ."
            else: why[o] = f"'{o}' is for masculine nouns only. {t['n']} is {t['a']} → {corr}."
        add("akk", segs, opts, rule, why, note=f"{t['a']} {t['n']}")
    # es gibt
    for t in pick(things, 24):
        corr = AKK[t["a"]][1]
        add("akk", [["Hier", "ORT"], ["gibt", "V"], ["es", "S"], ["{" + corr + "} " + t["n"] + ".", "AKK"]], [corr, NOMF[t["a"]][1] if t["a"] == "der" else "einen", "einem"],
            f"es gibt + Akkusativ → {corr} {t['n']}.", {"einem": "einem is Dativ.", "ein": "ein would be Nominativ here — es gibt takes Akkusativ: einen.", "einen": f"{t['n']} is {t['a']} → {corr}."})


# ---------- 7. time ----------
WORDS = {0: "null", 1: "eins", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "sieben", 8: "acht", 9: "neun", 10: "zehn", 11: "elf", 12: "zwölf"}
def hourw(h):
    h = h % 12 or 12
    return "ein" if h == 1 else WORDS[h]
def uhrzeit():
    times = [(7, 30), (8, 15), (6, 45), (9, 30), (10, 15), (11, 45), (12, 30), (2, 15), (3, 45), (4, 30), (5, 5), (7, 10), (8, 20), (9, 50), (10, 55), (1, 30), (6, 40), (11, 25)]
    for h, m in times:
        hw, nw = hourw(h).replace("ein", "eins") if m == 0 else hourw(h), hourw(h + 1)
        if hw == "ein": hw = "eins"
        if nw == "ein": nw = "eins"
        if m == 30: corr, wr = f"halb {nw}", [f"halb {hw}", f"{hw} halb"]
        elif m == 15: corr, wr = f"Viertel nach {hw}", [f"Viertel vor {hw}", f"Viertel nach {nw}"]
        elif m == 45: corr, wr = f"Viertel vor {nw}", [f"Viertel nach {nw}", f"Viertel vor {hw}"]
        elif m < 25: corr, wr = f"{WORDS.get(m, 'zwanzig')} nach {hw}", [f"{WORDS.get(m, 'zwanzig')} vor {hw}", f"{WORDS.get(m, 'zwanzig')} nach {nw}"]
        elif m == 25: corr, wr = f"fünf vor halb {nw}", [f"fünf nach halb {hw}", f"fünf vor halb {hw}"]
        else: corr, wr = f"{WORDS[60 - m] if 60 - m in WORDS else 'zwanzig'} vor {nw}", [f"{WORDS[60 - m] if 60 - m in WORDS else 'zwanzig'} nach {nw}", f"{WORDS[60 - m] if 60 - m in WORDS else 'zwanzig'} vor {hw}"]
        add("uhrzeit", [["Es", "S"], ["ist", "V"], ["{" + corr + "}.", "ZEIT"]], [corr] + wr,
            f"{h}:{m:02d} → {corr}. " + ("halb always points to the NEXT hour: half (way) to " + nw + "." if m == 30 else "nach = past, vor = to."),
            {w: ("halb counts towards the next hour — 7:30 is halb acht, not halb sieben." if "halb" in w and "vor halb" not in w and "nach halb" not in w else f"That would be a different time. {h}:{m:02d} = {corr}.") for w in wr},
            prompt=f"{h}:{m:02d} → Es ist ___. (informal)")


def zeitpraep():
    items = [("Der Kurs beginnt {um} 9 Uhr.", "um", "clock time"), ("Ich arbeite {am} Montag.", "am", "day"), ("Mein Geburtstag ist {im} Mai.", "im", "month"),
             ("{Im} Winter fahren wir Ski.", "im", "season"), ("Wir treffen uns {am} Abend.", "am", "part of the day"), ("{Am} Wochenende habe ich frei.", "am", "Wochenende"),
             ("Der Zug fährt {um} 14:30 Uhr.", "um", "clock time"), ("{Im} Sommer ist es heiß.", "im", "season"), ("Ich habe {am} 5. Juni Geburtstag.", "am", "date"),
             ("Die Praxis ist {von} 8 {bis} 12 Uhr geöffnet.", "von … bis", "from … to"), ("{Am} Vormittag lerne ich.", "am", "part of the day"),
             ("{Im} Oktober ist das Oktoberfest.", "im", "month"), ("Wir essen {um} halb eins.", "um", "clock time"), ("{In der} Nacht schlafe ich.", "in der", "exception: Nacht"),
             ("Ich komme {am} Freitag zurück.", "am", "day"), ("{Im} Frühling blühen die Blumen.", "im", "season")]
    for s, corr, what in items:
        if "von" in corr:
            opts = ["von … bis", "um … bis", "am … um"]
            seg_ = [["Die Praxis", "S"], ["ist", "V"], ["{von} 8 {bis} 12 Uhr", "ZEIT"], ["geöffnet.", "ADJ"]]
            add("zeitpraep", seg_, opts, "von … bis = from … to.", {"um … bis": "um is for a single point in time. A range is von … bis.", "am … um": "am goes with days, not clock times."},
                prompt="Die Praxis ist ___ 8 ___ 12 Uhr geöffnet.")
            continue
        base = ["um", "am", "im"] if corr in ("um", "am", "im") else ["in der", "am", "um"]
        opts = [corr] + [o for o in base if o != corr][:2]
        if s.startswith("{"): opts = [o.capitalize() if o != "in der" else "In der" for o in opts]
        rule = {"um": "um + clock time.", "am": "am + days, parts of the day, dates and Wochenende.", "im": "im + months and seasons.", "in der": "Exception: in der Nacht (not am Nacht)."}[corr]
        add("zeitpraep", [[s, "ZEIT"]], opts, f"{what} → {corr}. " + rule,
            {o: {"um": "um is only for clock times.", "am": "am is for days, dates and parts of the day.", "im": "im is for months and seasons.", "in der": "in der is only used for die Nacht."}[o.lower()] for o in opts[1:]})


ORD = {1: "ersten", 2: "zweiten", 3: "dritten", 4: "vierten", 5: "fünften", 6: "sechsten", 7: "siebten", 8: "achten", 10: "zehnten", 12: "zwölften", 15: "fünfzehnten", 19: "neunzehnten", 20: "zwanzigsten", 21: "einundzwanzigsten", 30: "dreißigsten", 31: "einunddreißigsten"}
MON = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
def datum():
    days = [1, 3, 7, 2, 20, 21, 30, 12, 15, 8, 31, 19]
    for i, d in enumerate(days):
        m = MON[(i * 5) % 12]
        corr = f"am {ORD[d]}"
        base = ORD[d][:-1]
        wrong = [f"am {base}", f"im {ORD[d]}"]
        if d == 1: wrong = ["am einsten", "am eins"]
        if d == 3: wrong = ["am dreiten", "am drei"]
        if d == 7: wrong = ["am siebenten" if False else "am siebeten", "am sieben"]
        add("datum", [["Ich", "S"], ["habe", "V"], ["{" + corr + "} " + m, "ZEIT"], ["Geburtstag.", "AKK"]], [corr] + wrong,
            f"{d}. {m} → {corr} {m}. After am the ordinal ends in -en. 1.–19.: -te(n); from 20.: -ste(n). Irregular: ersten, dritten, siebten.",
            {w: ("Irregular ordinal: 1. = erste, 3. = dritte, 7. = siebte." if d in (1, 3, 7) else ("Dates use am, not im." if w.startswith("im") else "After am the ending is -en.")) for w in wrong},
            prompt=f"Ich habe ___ {m} Geburtstag. ({d}.)")


# ---------- 8. possessives ----------
POSS = {"ich": "mein", "du": "dein", "er": "sein", "sie_f": "ihr", "wir": "unser", "ihr": "euer", "Sie": "Ihr"}
def poss_form(stem_, gender, case):
    st = "eur" if stem_ == "euer" and (gender in ("die", "pl") or (case == "akk" and gender == "der")) else stem_
    if gender == "der": return st + ("en" if case == "akk" else "")
    if gender == "das": return st
    return st + "e"
def possessiv():
    owners = [("ich", "Ich", "mein"), ("du", "Du", "dein"), ("er", "Er", "sein"), ("sie_f", "Sie (she)", "ihr"), ("wir", "Wir", "unser"), ("ihr", "Ihr", "euer"), ("Sie", "Sie (formal)", "Ihr")]
    things_nom = [N[x] for x in ["Bruder", "Vater", "Schwester", "Mutter", "Kind", "Auto", "Wohnung", "Laptop", "Handy", "Tasche", "Sohn", "Büro"]]
    for i, (o, t) in enumerate([(o, t) for o in owners for t in things_nom]):
        who, label, st = o
        corr = poss_form(st, t["a"], "nom")
        corr_c = corr.capitalize() if who == "Sie" else corr
        wrong = list({poss_form(st, "die", "nom"), poss_form(st, "der", "akk"), poss_form(st, "das", "nom")} - {corr})
        if who == "Sie": wrong = [w.capitalize() for w in wrong][:1] + [corr.lower()] if True else wrong
        wrong = [w for w in wrong if w != corr_c][:2]
        add("poss", [["Das", "S"], ["ist", "V"], ["{" + corr_c + "} " + t["n"] + ".", "NOM"]], [corr_c] + wrong,
            f"{who.replace('_f','')} → {st}. {t['n']} is {t['a']} → {corr_c} (Nominativ). Endings like ein: -e for die and plural, no ending for der/das in the Nominativ." + (" Formal Ihr always has a capital I." if who == "Sie" else ""),
            {w: (f"'{w}' has the -e ending for die/plural; {t['n']} is {t['a']}." if w.endswith("e") else (f"'{w}' is masculine Akkusativ. After 'Das ist' it's Nominativ." if w.endswith("en") else ("Formal 'Ihr' needs a capital I." if w == corr.lower() and who == "Sie" else f"Not right for {t['a']} {t['n']}."))) for w in wrong},
            prompt=f"({label}) Das ist ___ {t['n']}.", note=f"{t['a']} {t['n']}")
    akk_things = [N[x] for x in ["Schlüssel", "Pullover", "Laptop", "Koffer", "Rucksack", "Bruder", "Freund", "Mantel"]]
    akk_all = akk_things + [N[x] for x in ["Jacke", "Handy", "Brille", "Fahrrad"]]
    for i, (o, t) in enumerate([(o, t) for o in owners for t in akk_all]):
        who, label, st = o
        corr = poss_form(st, t["a"], "akk"); corr_c = corr.capitalize() if who == "Sie" else corr
        nomf = poss_form(st, t["a"], "nom")
        wrong = [x for x in dict.fromkeys([nomf, poss_form(st, "die", "nom"), st + "em", poss_form(st, "der", "akk")]) if x != corr][:2]
        if who == "Sie": wrong = [w.capitalize() for w in wrong]
        subj = {"ich": "Ich suche", "du": "Suchst du", "er": "Er sucht", "sie_f": "Sie sucht", "wir": "Wir suchen", "ihr": "Sucht ihr", "Sie": "Suchen Sie"}[who]
        q = "?" if subj.split()[0] in ("Suchst", "Sucht", "Suchen") else "."
        add("poss", [[subj, "S"], ["{" + corr_c + "} " + t["n"] + q, "AKK"]], [corr_c] + wrong,
            f"suchen + Akkusativ. {t['a']} {t['n']} → {corr_c} {t['n']}." + (" Masculine Akkusativ: -en." if t["a"] == "der" else " die/das don't change in the Akkusativ.") + (" euer loses its e before an ending: euren, eure." if st == "euer" else ""),
            {w: (f"'{w}' is the Nominativ form. {t['n']} is the object → Akkusativ." if w.lower() == nomf.lower() else ("-em is a Dativ ending." if w.endswith("em") else f"Wrong ending for {t['a']} {t['n']}.")) for w in wrong},
            prompt=f"({label}) {subj} ___ {t['n']}{q}", note=f"{t['a']} {t['n']}")
    for st, who, pl in [("unser", "wir", "Kinder"), ("euer", "ihr", "Eltern"), ("ihr", "sie (they)", "Freunde"), ("mein", "ich", "Eltern")]:
        corr = poss_form(st, "pl", "nom")
        add("poss", [["Wo", "W"], ["sind", "V"], ["{" + corr + "} " + pl + "?", "S"]], [corr, st, st + "en"],
            f"Plural → -e: {corr} {pl}." + (" euer drops its e: eure." if st == "euer" else ""), {st: "No ending only for der/das (Nominativ). Plural takes -e.", st + "en": "-en is masculine Akkusativ."},
            prompt=f"({who}) Wo sind ___ {pl}?")


# ---------- 9. modal verbs ----------
def modal():
    ctxs = {"können": [("gut Deutsch", "sprechen", "AKK"), ("sehr gut", "kochen", "ADV")], "müssen": [("heute lange", "arbeiten", "ZEIT"), ("morgen früh", "aufstehen", "ZEIT")],
            "wollen": [("ein Auto", "kaufen", "AKK"), ("im Sommer nach Spanien", "fahren", "ORT")], "dürfen": [("hier nicht", "parken", "ORT"), ("heute länger", "bleiben", "ZEIT")],
            "sollen": [("viel Wasser", "trinken", "AKK"), ("mehr Sport", "machen", "AKK")], "möchten": [("einen Kaffee", "trinken", "AKK"), ("ins Kino", "gehen", "ORT")]}
    for m, f in MODALS.items():
        for p, (c, inf, lab) in [(p, c) for p in PRON for c in ctxs[m]]:
            corr = f[p]
            wrong = [x for x in {f[q] for q in PRON} - {corr}]
            R.shuffle(wrong)
            fake = (corr + "t") if p in ("ich", "er") and not corr.endswith("e") else None
            if fake: wrong = [fake] + wrong
            wrong = list(dict.fromkeys(w for w in wrong if w != corr))
            add("modal", [[CAP[p], "S"], ["{" + corr + "}", "MV"], [c, lab], [inf + ".", "INF"]], [corr] + wrong[:2],
                f"{m} ({MODALS[m]['en']}): ich {f['ich']} · du {f['du']} · er {f['er']} · wir {f['wir']} · ihr {f['ihr']} · sie {f['sie']}. ich and er have no ending.",
                {w: ("ich and er/sie/es forms of modal verbs have NO -t: er " + f["er"] + "." if w == fake else f"'{w}' is the {' / '.join(FORM_NAME[q] for q in PRON if f[q]==w)}.") for w in wrong[:2]},
                prompt=f"{CAP[p]} ___ {c} {inf}. ({m})", note=m)
    order = [("Ich", "kann", "gut", "schwimmen", "ADV"), ("Wir", "müssen", "morgen früh", "aufstehen", "ZEIT"), ("Er", "will", "nach Berlin", "fahren", "ORT"),
             ("Du", "darfst", "hier nicht", "rauchen", "ORT"), ("Ihr", "sollt", "die Hausaufgaben", "machen", "AKK"), ("Sie", "möchte", "einen Tee", "trinken", "AKK"),
             ("Ich", "muss", "heute einkaufen", "", "ZEIT"), ("Wir", "können", "am Samstag", "kommen", "ZEIT"), ("Kannst", "du", "mir", "helfen", "DAT")]
    for s, mv, mid, inf, lab in order:
        if s == "Kannst":
            choose("modal", "Which question is correct?", "Kannst#V1 / du#S / mir#DAT / helfen?#INF", ["Kannst du helfen mir?", "Kannst helfen du mir?"],
                   "Modal verb first (yes/no question), infinitive at the end: Kannst du mir helfen?",
                   {"Kannst du helfen mir?": "The infinitive goes to the very END — after 'mir'.", "Kannst helfen du mir?": "The subject comes right after the modal; the infinitive goes to the end."}); continue
        if not inf:
            choose("modal", "Which sentence is correct?", f"{s}#S / {mv}#MV / heute#ZEIT / einkaufen.#INF", ["Ich muss einkaufen heute.", "Ich muss heute kaufe ein."],
                   "With a modal verb the separable verb stays together at the end: einkaufen.",
                   {"Ich muss einkaufen heute.": "The infinitive goes to the very end, after 'heute'.", "Ich muss heute kaufe ein.": "After a modal verb the 2nd verb is an unconjugated infinitive — and separable verbs don't split: einkaufen."}); continue
        choose("modal", "Which sentence is correct?", f"{s}#S / {mv}#MV / {mid}#{lab} / {inf}.#INF",
               [f"{s} {mv} {inf} {mid}.", f"{s} {inf} {mv} {mid}."],
               f"Satzklammer: the modal verb '{mv}' is in position 2, the infinitive '{inf}' goes to the END.",
               {f"{s} {mv} {inf} {mid}.": "The infinitive must be at the very end, not right after the modal.", f"{s} {inf} {mv} {mid}.": "The modal verb is the conjugated verb → position 2."})


# ---------- 10. separable verbs ----------
def trennbar():
    sep = [v for v in VERBS if v["pre"]]
    for v in sep:
        f = forms(v); p = R.choice(["ich", "er", "wir", "du"])
        conj = f[p]
        s = CAP[p]
        if p == "du":
            spec = f"{conj.capitalize()}#V1 / du#S / {v['ctx']}#{v['ctx_lab']} / {v['pre']}?#PRE"
            wrong = [f"{v['pre'].capitalize()}{conj} du {v['ctx']}?", f"{conj.capitalize()} {v['pre']} du {v['ctx']}?"]
            pr = f"Make a question with du + {v['inf']} ({v['en']}) + „{v['ctx']}“:"
        else:
            spec = f"{s}#S / {conj}#V / {v['ctx']}#{v['ctx_lab']} / {v['pre']}.#PRE"
            wrong = [f"{s} {v['pre']}{conj} {v['ctx']}.", f"{s} {conj} {v['pre']} {v['ctx']}."]
            pr = f"{v['inf']} ({v['en']}) — which sentence is correct?"
        choose("trenn", pr, spec, wrong,
               f"{v['inf']} is separable: the verb '{conj}' takes position {'1' if p=='du' else '2'}, the prefix '{v['pre']}' goes to the very END.",
               {wrong[0]: "The prefix separates in the present tense — it doesn't stay attached.", wrong[1]: "The prefix goes to the END of the sentence, not right after the verb."})
    for inf, ok in [("anfangen", True), ("verstehen", False), ("aufräumen", True), ("bezahlen", False), ("einladen", True), ("bekommen", False), ("fernsehen", True), ("erzählen", False), ("mitbringen", True), ("verkaufen", False)]:
        if not ok: continue
        insep = R.choice(["verstehen", "bezahlen", "bekommen", "erzählen", "verkaufen", "besuchen"])
        insep2 = R.choice([x for x in ["vergessen", "empfehlen", "beginnen", "verstehen", "bezahlen"] if x != insep])
        add("trenn", [["{" + inf + "}", "V"]], [inf, insep, insep2], f"{inf} is separable ({inf[:2] if inf[:3] not in ('auf','mit','ein','fer') else inf[:3]}- comes off). be-, ver-, er-, ent-, emp- never separate.",
            {insep: f"{insep} starts with an inseparable prefix (be-/ver-/er-/emp-/beg-).", insep2: f"{insep2} doesn't separate."}, prompt="Which verb is separable?")


# ---------- 11. pronouns ----------
def pronomen():
    akk = [("Ich liebe {dich}.", "dich", ["dir", "du"], "du", "lieben + Akkusativ"), ("Ich sehe {ihn}.", "ihn", ["ihm", "er"], "er", "sehen + Akkusativ"),
           ("Das Geschenk ist für {dich}.", "dich", ["dir", "du"], "du", "für + Akkusativ"), ("Ich rufe {Sie} morgen an.", "Sie", ["Ihnen", "Ihr"], "Sie", "anrufen + Akkusativ"),
           ("Besuchst du {uns}?", "uns", ["wir", "unser"], "wir", "besuchen + Akkusativ"), ("Ich kenne {sie} gut.", "sie", ["ihr", "ihnen"], "sie (she)", "kennen + Akkusativ"),
           ("Wir holen {euch} ab.", "euch", ["ihr", "euer"], "ihr", "abholen + Akkusativ"), ("Er fragt {mich}.", "mich", ["mir", "ich"], "ich", "fragen + Akkusativ"),
           ("Ohne {dich} gehe ich nicht.", "dich", ["dir", "du"], "du", "ohne + Akkusativ"), ("Kannst du {mich} hören?", "mich", ["mir", "ich"], "ich", "hören + Akkusativ")]
    dat = [("Kannst du {mir} helfen?", "mir", ["mich", "ich"], "ich", "helfen + Dativ"), ("Die Jacke gefällt {mir}.", "mir", ["mich", "mein"], "ich", "gefallen + Dativ"),
           ("Wie geht es {dir}?", "dir", ["dich", "du"], "du", "Wie geht es …? + Dativ"), ("Der Pullover passt {ihm} nicht.", "ihm", ["ihn", "er"], "er", "passen + Dativ"),
           ("Ich danke {Ihnen}.", "Ihnen", ["Sie", "Ihr"], "Sie", "danken + Dativ"), ("Gehört das Buch {dir}?", "dir", ["dich", "dein"], "du", "gehören + Dativ"),
           ("Das Essen schmeckt {uns}.", "uns", ["wir", "unser"], "wir", "schmecken + Dativ"), ("Ich gebe {ihr} das Buch.", "ihr", ["sie", "ihn"], "sie (she)", "geben + Dativ (person) + Akkusativ (thing)"),
           ("Ich komme mit {euch}.", "euch", ["ihr", "euer"], "ihr", "mit + Dativ"), ("Wie geht es {ihnen}?", "ihnen", ["sie", "ihr"], "sie (they)", "Dativ plural: ihnen"),
           ("Steht mir die Farbe? – Ja, sie steht {dir} gut.", "dir", ["dich", "du"], "du", "stehen (to suit) + Dativ"), ("Ich helfe {ihm} gern.", "ihm", ["ihn", "er"], "er", "helfen + Dativ")]
    for lst, case in [(akk, "AKK"), (dat, "DAT")]:
        for s, corr, wr, who, why_ in lst:
            add("pron", [[s, case]], [corr] + wr, f"{why_} → {who} becomes '{corr}'. " + ("Akkusativ: mich, dich, ihn, sie, es, uns, euch, sie/Sie." if case == "AKK" else "Dativ: mir, dir, ihm, ihr, ihm, uns, euch, ihnen/Ihnen."),
                {w: (f"'{w}' is Nominativ (subject form)." if w in ("ich", "du", "er", "wir", "Sie") and w != corr else
                     f"'{w}' is {'Dativ' if case=='AKK' else 'Akkusativ'} — {why_}." if w in ("mir", "dir", "ihm", "Ihnen", "mich", "dich", "ihn", "ihnen", "sie", "ihr", "uns", "euch") else
                     f"'{w}' is a possessive article (my/your …), not a pronoun.") for w in wr},
                prompt=s.replace("{" + corr + "}", "___") + f" ({who})")


def praeteritum():
    ctx = [("Gestern", "krank", "war"), ("Letzte Woche", "in Berlin", "war"), ("Am Wochenende", "keine Zeit", "hatte"), ("Gestern", "Geburtstag", "hatte"),
           ("Letztes Jahr", "in Spanien", "war"), ("Gestern Abend", "müde", "war"), ("Am Montag", "einen Termin", "hatte"), ("Früher", "einen Hund", "hatte")]
    for i, ((t, c, verb), p) in enumerate([(c, p) for c in ctx for p in PRON]):
        tbl = WAR if verb == "war" else HATTE
        pres = SEIN if verb == "war" else HABEN
        corr = tbl[p]
        other = HATTE if verb == "war" else WAR
        wr = [pres[p], other[p]]
        s = p if p != "sie" else "sie"
        add("praet", [[t, "ZEIT"], ["{" + corr + "}", "V"], [s, "S"], [c + ".", "ADJ" if verb == "war" and c in ("krank", "müde") else ("ORT" if verb == "war" else "AKK")]],
            [corr] + wr, f"Past of {'sein' if verb=='war' else 'haben'}: ich {tbl['ich']} · du {tbl['du']} · er {tbl['er']} · wir {tbl['wir']} · ihr {tbl['ihr']} · sie {tbl['sie']}.",
            {pres[p]: f"'{pres[p]}' is present tense. '{t}' is in the past → {corr}.", other[p]: f"'{other[p]}' is the past of {'haben' if verb=='war' else 'sein'}. Here you need {'sein' if verb=='war' else 'haben'}."},
            prompt=f"{t} ___ {s} {c}.")


# ---------- 12. Dativ prepositions ----------
DAT_ART = {"der": "dem", "das": "dem", "die": "der"}
def dativ():
    items = [("Ich fahre mit", ["Bus", "Zug", "Auto", "Fahrrad", "U-Bahn", "Straßenbahn", "Taxi"], "mit + Dativ (transport)"),
             ("Ich gehe mit", ["Freund", "Kollegin", "Kind", "Schwester", "Bruder"], "mit + Dativ (with someone)"),
             ("Ich wohne bei", ["Freund", "Freundin", "Kollegin", "Mutter", "Vater"], "bei + Dativ (at someone's place)"),
             ("Er kommt aus", ["Büro", "Supermarkt", "Kino", "Apotheke", "Küche"], "aus + Dativ (out of / from inside)"),
             ("Wir sprechen mit", ["Arzt", "Ärztin", "Kollegin", "Kind"], "mit + Dativ")]
    for pre, ns, rule in items:
        for nn in ns:
            n = N[nn]; corr = DAT_ART[n["a"]]
            opts = [corr, n["a"], "den" if n["a"] != "die" else "dem"]
            add("dativ", [["{" + pre.split()[0] + "}", "S"], [pre.split()[1], "V"], [pre.split()[2] + " {" + corr + "} " + nn + ".", "DAT"]][1:] if False else
                [[pre.split()[0], "S"], [pre.split()[1], "V"], [pre.split()[2] + " {" + corr + "} " + nn + ".", "DAT"]],
                list(dict.fromkeys(opts)), f"{rule}. {n['a']} {nn} → {corr} {nn}. Dativ: der/das → dem, die → der.",
                {o: (f"'{o}' is the Nominativ. After {pre.split()[2]} you always need Dativ → {corr}." if o == n["a"] else (f"'dem' is Dativ for der/das — {nn} is die → der." if o == "dem" else f"'{o}' is Akkusativ. {pre.split()[2]} always takes Dativ.")) for o in opts[1:]},
                note=f"{n['a']} {nn}")
    zu = [("Arzt", "zum"), ("Bank", "zur"), ("Bahnhof", "zum"), ("Post", "zur"), ("Apotheke", "zur"), ("Supermarkt", "zum"), ("Arbeit", "zur"), ("Kino", "zum"), ("Schule", "zur"), ("Hotel", "zum")]
    for nn, corr in zu:
        add("dativ", [["Ich", "S"], ["gehe", "V"], ["{" + corr + "} " + nn + ".", "ORT"]], [corr, "zur" if corr == "zum" else "zum", "zu"],
            f"zu + Dativ: zu dem → zum (der/das), zu der → zur (die). {N[nn]['a']} {nn} → {corr}.",
            {"zur": f"zur = zu der, for die-nouns. {nn} is {N[nn]['a']} → zum.", "zum": f"zum = zu dem, for der/das. {nn} is die → zur.", "zu": "With a noun you need the article: zu + dem/der → zum/zur."})
    mix = [("Ich komme {aus} Indien.", "aus", ["von", "nach"], "aus + country/city = origin"), ("Ich fahre {nach} Berlin.", "nach", ["zu", "in"], "nach + cities/countries (no article)"),
           ("Ich arbeite {bei} Buycycle.", "bei", ["mit", "zu"], "bei + company"), ("Ich gehe jetzt {nach} Hause.", "nach", ["zu", "im"], "nach Hause = going home"),
           ("Ich bin {zu} Hause.", "zu", ["nach", "bei"], "zu Hause = at home"), ("Ich komme gerade {von} der Arbeit.", "von", ["aus", "bei"], "von = coming from (a person/activity/place)"),
           ("Ich wohne {seit} drei Jahren hier.", "seit", ["vor", "für"], "seit + Dativ = since / for (still true now)"), ("Ich gehe {zu} meiner Oma.", "zu", ["nach", "bei"], "zu + person"),
           ("Er fährt {mit} dem Rad.", "mit", ["bei", "von"], "mit + transport"), ("Wir treffen uns {beim} Bäcker.", "beim", ["zum", "bei"], "bei dem → beim (location)"),
           ("Ich komme {vom} Arzt.", "vom", ["von", "zum"], "von dem → vom"), ("Spielst du mit den {Kindern}?", "Kindern", ["Kinder", "Kindes"], "Dativ plural: den + noun + -n")]
    for s, corr, wr, rule in mix:
        add("dativ", [[s, "DAT" if "dem" in s or "der " in s or "Kindern" in s else "ORT"]], [corr] + wr, rule + ".",
            {w: f"Not '{w}': {rule}." for w in wr})


def wechsel():
    wo_verbs = [("liegt", "Das Buch"), ("steht", "Die Lampe"), ("hängt", "Das Bild"), ("ist", "Die Katze"), ("sitzt", "Der Junge"), ("liegt", "Der Schlüssel")]
    wohin_verbs = [("lege", "das Buch"), ("stelle", "die Lampe"), ("hänge", "das Bild"), ("lege", "den Schlüssel"), ("stelle", "die Flasche"), ("setze", "das Kind")]
    places = [("auf", "Tisch"), ("auf", "Sofa"), ("unter", "Bett"), ("neben", "Tür"), ("an", "Wand"), ("vor", "Fenster"), ("hinter", "Schrank"), ("in", "Küche"), ("über", "Sofa"), ("in", "Regal"), ("auf", "Stuhl"), ("neben", "Lampe")]
    AK = {"der": "den", "die": "die", "das": "das"}
    for i, (prep, nn) in enumerate([]):  # replaced by curated scenes in more.wechsel
        n = N[nn]
        v, subj = wo_verbs[i % len(wo_verbs)]
        corr = DAT_ART[n["a"]]; ak = AK[n["a"]]
        cform = corr; aform = ak
        if prep == "in" and n["a"] != "die": cform, aform = "im", "ins"
        if prep == "an" and n["a"] != "die": cform, aform = "am", "ans"
        rest = f"{prep} {corr} {nn}" if cform == corr else f"{cform} {nn}"
        opts = list(dict.fromkeys([cform, aform] + [x for x in [n["a"], "den", "dem", "der"] if x not in (cform, aform)]))[:3]
        q_rest = f"{prep} ___ {nn}" if cform == corr else f"___ {nn}"
        add("wechsel", [[subj, "S"], [v, "V"], [(f"{prep} {{{cform}}} {nn}." if cform == corr else f"{{{cform}}} {nn}."), "ORT"]], list(dict.fromkeys(opts)),
            f"Wo? ({v} = position, no movement) → Dativ: {prep} + {n['a']} {nn} → {rest}.",
            {aform: f"'{aform}' is Akkusativ — that's for Wohin? (movement). {v} describes a position → Dativ.", n["a"]: "That's the Nominativ. After a preposition you need Dativ (Wo?) or Akkusativ (Wohin?).",
             "den": "den is Akkusativ masculine (Wohin?).", "der": f"der would be Dativ feminine — {nn} is {n['a']}." , "dem": f"dem is Dativ for der/das — {nn} is die → der."}, prompt=f"{subj} {v} {q_rest}.")
        v2, obj = wohin_verbs[i % len(wohin_verbs)]
        add("wechsel", [["Ich", "S"], [v2, "V"], [obj, "AKK"], [(f"{prep} {{{aform}}} {nn}." if aform == ak else f"{{{aform}}} {nn}."), "ORT"]], list(dict.fromkeys([aform, cform] + [x for x in [n["a"], "dem", "den", "der"] if x not in (cform, aform)]))[:3],
            f"Wohin? ({v2} = movement to a place) → Akkusativ: {prep} + {n['a']} {nn} → {(prep + ' ' + ak) if aform == ak else aform} {nn}.",
            {cform: f"'{cform}' is Dativ — that's for Wo? (position). {v2} is a movement → Akkusativ.", n["a"]: "That's Nominativ. After the preposition: Akkusativ for movement.", "dem": "dem is Dativ (Wo?).", "den": f"den is for der-nouns — {nn} is {n['a']}.", "der": "der is Dativ feminine (Wo?) — for movement use Akkusativ."},
            prompt=f"Ich {v2} {obj} {(prep + ' ___') if aform == ak else '___'} {nn}.")
    for s, corr, wr in [("Ich gehe heute {ins} Kino.", "ins", ["im", "in"]), ("Ich bin {im} Kino.", "im", ["ins", "in das"]), ("Wir fahren {in die} Stadt.", "in die", ["in der", "im"]), ("Wir wohnen {in der} Stadt.", "in der", ["in die", "im"]),
                        ("Ich gehe {in den} Park.", "in den", ["im", "in dem"]), ("Die Kinder spielen {im} Park.", "im", ["in den", "ins"])]:
        add("wechsel", [[s, "ORT"]], [corr] + wr, "gehen/fahren (Wohin?) → Akkusativ: ins, in die, in den · sein/wohnen/spielen (Wo?) → Dativ: im, in der, im.",
            {w: ("Akkusativ is for movement (Wohin?)." if w in ("ins", "in die", "in den") else "Dativ is for position (Wo?).") if w not in ("in",) else "You need the article: in + das = ins / in + dem = im." for w in wr})


# ---------- 13. Perfekt ----------
def perfekt():
    for v in VERBS:
        p2 = v["p2"]; base = v["base"]; s = stem(base)
        reg = ("ge" + s + "t") if not v["pre"] else (v["pre"] + "ge" + s + "t")
        irr = ("ge" + base) if not v["pre"] else (v["pre"] + "ge" + base)
        wrong = [x for x in dict.fromkeys([reg, irr, "ge" + p2 if not p2.startswith("ge") else p2[2:], p2[:-1] + ("en" if p2.endswith("t") else "t"), p2 + "et" if p2.endswith("t") else p2[:-2] + "t"]) if x != p2]
        why_typ = ("-ieren verbs take no ge-." if base.endswith("ieren") else
                   "be-/ver-/er-/emp-/beg- verbs take no ge-." if base.startswith(("be", "ver", "er", "emp")) and not v["pre"] else
                   "Separable: ge- goes between prefix and stem." if v["pre"] else
                   "Regular verb: ge- + stem + -t." if p2 == reg else "Irregular verb: ge- … -en (often with a vowel change). Learn it with the verb.")
        if base in ("bringen", "denken", "kennen"): why_typ = "Mixed verb: vowel change like irregular verbs, but -t like regular ones."
        R.shuffle(wrong)
        add("perf_p2", [["{" + p2 + "}", "P2"]], [p2] + wrong[:2], f"{v['inf']} → {p2}. {why_typ}",
            {w: ("No ge- here: " + why_typ if w.startswith("ge") and not p2.startswith("ge") and not v["pre"] else
                 "ge- must go between prefix and stem: " + p2 if v["pre"] and not w.startswith(v["pre"] + "ge") else
                 f"{v['inf']} is {'irregular (-en)' if p2.endswith('en') else 'regular (-t)'} → {p2}.") for w in wrong[:2]},
            prompt=f"Partizip II of {v['inf']} ({v['en']}):", note=f"{v['inf']} – hat/ist {p2}")
    for v, p in [(v, p) for v in VERBS for p in R.sample(PRON, 2)]:
        aux = (SEIN if v["aux"] == "s" else HABEN)[p]
        other = (HABEN if v["aux"] == "s" else SEIN)[p]
        add("perf_aux", [[CAP[p], "S"], ["{" + aux + "}", "HV"], [v["ctx"], v["ctx_lab"]], [v["p2"] + ".", "P2"]],
            [aux, other, (WAR if v["aux"] == "s" else HATTE)[p]],
            f"{v['inf']} takes {'sein (movement A→B / change of state / bleiben)' if v['aux']=='s' else 'haben (most verbs)'} → {CAP[p]} {aux} {v['ctx']} {v['p2']}.",
            {other: (f"{v['inf']} is movement from A to B (or bleiben/change) → sein." if v["aux"] == "s" else f"Only movement A→B, change of state and bleiben/sein take sein. {v['inf']} takes haben."),
             (WAR if v["aux"] == "s" else HATTE)[p]: "That's Präteritum. The Perfekt uses the PRESENT of haben/sein + Partizip II."},
            prompt=f"{CAP[p]} ___ {v['ctx']} {v['p2']}.", note=f"{v['inf']} → {'ist' if v['aux']=='s' else 'hat'} {v['p2']}")
    for v in [x for x in VERBS if x["aux"] == "h" and x["ctx_lab"] in ("AKK",)]:
        choose("perf_aux", "Which sentence is correct?", f"Ich#S / habe#HV / gestern#ZEIT / {v['ctx']}#AKK / {v['p2']}.#P2",
               [f"Ich habe {v['p2']} gestern {v['ctx']}.", f"Ich habe gestern {v['p2']} {v['ctx']}."],
               "Perfekt = Satzklammer: haben/sein in position 2, Partizip II at the very END.",
               {f"Ich habe {v['p2']} gestern {v['ctx']}.": "The Partizip II goes to the end, not after haben.", f"Ich habe gestern {v['p2']} {v['ctx']}.": "Unlike English, the object comes BEFORE the Partizip II."})


def welcher():
    items = [("Pullover", "der"), ("Jacke", "die"), ("Hemd", "das"), ("Mantel", "der"), ("Hose", "die"), ("Kleid", "das"), ("Tasche", "die"), ("Rucksack", "der"),
             ("Film", "der"), ("Lampe", "die"), ("Buch", "das"), ("Stuhl", "der"), ("Uhr", "die"), ("Sofa", "das"), ("Laptop", "der"), ("Brille", "die"), ("Fahrrad", "das"), ("Koffer", "der")]
    for nn, a in items:
        nom = {"der": "dieser", "die": "diese", "das": "dieses"}[a]
        add("welcher", [["{" + nom.capitalize() + "} " + nn, "S"], ["gefällt", "V"], ["mir.", "DAT"]], [nom.capitalize()] + [x.capitalize() for x in ["dieser", "diese", "dieses"] if x != nom],
            f"dies- has the same endings as der/die/das: der → dieser, die → diese, das → dieses. {nn} is {a}.", {x.capitalize(): f"{x} goes with {'der' if x.endswith('r') else 'die' if x.endswith('e') else 'das'}-nouns. {nn} is {a} → {nom}." for x in ["dieser", "diese", "dieses"] if x != nom}, prompt=f"___ {nn} gefällt mir.", note=f"{a} {nn}")
        wq = {"der": "Welcher", "die": "Welche", "das": "Welches"}[a]
        add("welcher", [["{" + wq + "} " + nn, "S"], ["gefällt", "V"], ["dir?", "DAT"]], [wq] + [x for x in ["Welcher", "Welche", "Welches"] if x != wq],
            f"welch- like der/die/das: welcher (der), welche (die), welches (das). {nn} is {a}.", {x: f"{x} goes with {'der' if x.endswith('r') else 'die' if x.endswith('e') else 'das'}-nouns. {nn} is {a} → {wq}." for x in ["Welcher", "Welche", "Welches"] if x != wq}, prompt=f"___ {nn} gefällt dir?")
        akk = {"der": "diesen", "die": "diese", "das": "dieses"}[a]
        add("welcher", [["Ich", "S"], ["nehme", "V"], ["{" + akk + "} " + nn + ".", "AKK"]], [akk] + [x for x in ["dieser", "diesen", "dieses", "diese"] if x != akk][:2],
            f"nehmen + Akkusativ: only masculine changes → diesen. {nn} is {a} → {akk}.",
            {"dieser": "dieser is Nominativ masculine. Object → Akkusativ: diesen." if a == "der" else f"{nn} isn't masculine.", "diesen": f"diesen is only for masculine nouns. {nn} is {a}.",
             "dieses": f"dieses is for das-nouns. {nn} is {a}.", "diese": f"diese is for die/plural. {nn} is {a}."}, prompt=f"Ich nehme ___ {nn}.")


ZW = ["", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
TENS = {2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig", 6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"}
TEEN = {11: "elf", 12: "zwölf", 13: "dreizehn", 14: "vierzehn", 15: "fünfzehn", 16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn"}
def numword(n):
    if n in TEEN: return TEEN[n]
    if n < 10: return {1: "eins"}.get(n, ZW[n])
    if n == 10: return "zehn"
    if n == 100: return "hundert"
    t, o = divmod(n, 10)
    return TENS[t] if o == 0 else ZW[o] + "und" + TENS[t]
def zahlen():
    for n in [16, 17, 30, 70, 60, 21, 47, 74, 35, 53, 68, 86, 99, 31, 76, 67, 12, 11, 100, 41]:
        corr = numword(n)
        wrong = set()
        if n in (16, 60): wrong |= {"sechszehn" if n == 16 else "sechszig", "sechzig" if n == 16 else "sechzehn"}
        if n in (17, 70): wrong |= {"siebenzehn" if n == 17 else "siebenzig", "siebzig" if n == 17 else "siebzehn"}
        if n == 30: wrong |= {"dreizig", "dreizehn"}
        if 20 < n < 100 and n % 10:
            t, o = divmod(n, 10)
            wrong.add(TENS[t] + ("eins" if o == 1 else ZW[o]))
            if o != t and o >= 2: wrong.add(numword(o * 10 + t))
            if o == 1: wrong.add("einsund" + TENS[t])
            if o == t: wrong.add(TENS[t] + "und" + ZW[o])
        if n == 12: wrong |= {"zweizehn", "zwanzig"}
        if n == 11: wrong |= {"einszehn", "zehneins"}
        if n == 100: wrong |= {"zehnzig", "einhunderte"}
        if n in (76, 67):
            t, o = divmod(n, 10)
            wrong.add(("sechs" if o == 6 else "sieben") + "und" + ("siebenzig" if t == 7 else "sechszig"))
        w = list(wrong - {corr})[:2]
        if n in (11, 12): rule = f"{n} = {corr}. 11 and 12 are their own words (like English eleven, twelve)."
        elif n == 100: rule = "100 = hundert (or einhundert). No ending."
        elif 20 < n < 100 and n % 10: rule = f"{n} = {corr}: ones first ({numword(n % 10).replace('eins','ein')}) + und + tens ({TENS[n // 10]}), one word." + (" 1 becomes ein- in compounds." if n % 10 == 1 else "")
        else: rule = f"{n} = {corr}. Watch the spelling: sechzehn/sechzig and siebzehn/siebzig drop letters, dreißig has ß."
        def nwhy(x):
            if n in (11, 12): return f"{n} is simply '{corr}'."
            if n == 100: return "Just 'hundert'."
            if "und" not in x and n > 20 and n % 10: return "German says the ones FIRST, then und, then the tens: " + corr + "."
            if x.startswith("eins"): return "1 becomes ein- in compounds: einund…"
            if "sechs" in x and ("zehn" in x or "zig" in x) and "und" not in x: return "sechs drops its s: sechzehn, sechzig."
            if "sieben" in x and ("zehn" in x or "zig" in x) and "und" not in x: return "sieben drops -en: siebzehn, siebzig."
            if "siebenzig" in x or "sechszig" in x: return "Only the ones keep the full form; the tens shorten: sechzig, siebzig."
            if x == "dreizig": return "30 is dreißig — the only tens with ß."
            return f"That's a different number. {n} = {corr}."
        add("zahlen", [["{" + corr + "}", ""]], [corr] + w, rule, {x: nwhy(x) for x in w},
            prompt=f"{n} =")


def run_all(dic):
    verb_endings(); sein_haben(); janein(); artikel(dic); plural(); einkein(); imperativ(); akkusativ(); zeitpraep()
    possessiv(); modal(); trennbar(); pronomen(); praeteritum(); dativ(); wechsel(); perfekt(); welcher(); zahlen()
