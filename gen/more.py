"""Extra generators: wider coverage of the grammar topics plus vocabulary topics built from the whole dictionary."""
import re
from .core import add, choose, pick, R
from .verbs import forms, kind, PRON, CAP, PRON_EN
from .nouns import N
from .generators import VERBS, form_why, subj, numword, TENS, ZW, MON, DAT_ART, RULE_EXPL, fake_plurals, plural_type

# ---------- time (every 5 minutes, informal + formal + reverse) ----------
HW = {1: "eins", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "sieben", 8: "acht", 9: "neun", 10: "zehn", 11: "elf", 12: "zwölf"}
def _h(h):
    return HW[h % 12 or 12]

def informal(h, m):
    hw, nw = _h(h), _h(h + 1)
    return {0: f"{hw} Uhr".replace("eins Uhr", "ein Uhr"), 5: f"fünf nach {hw}", 10: f"zehn nach {hw}", 15: f"Viertel nach {hw}", 20: f"zwanzig nach {hw}",
            25: f"fünf vor halb {nw}", 30: f"halb {nw}", 35: f"fünf nach halb {nw}", 40: f"zwanzig vor {nw}", 45: f"Viertel vor {nw}",
            50: f"zehn vor {nw}", 55: f"fünf vor {nw}"}[m]

def uhrzeit():
    for h in range(1, 13):
        for m in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55):
            corr = informal(h, m)
            cands = [informal(h - 1, m), informal(h, (m + 30) % 60) if m != 30 else f"halb {_h(h)}", informal(h, {5: 55, 10: 50, 15: 45, 20: 40, 25: 35, 35: 25, 40: 20, 45: 15, 50: 10, 55: 5, 30: 30}[m])]
            wr = [c for c in dict.fromkeys(cands) if c != corr][:2]
            why = {}
            for w in wr:
                if w == f"halb {_h(h)}": why[w] = f"halb points to the NEXT hour: {h}:30 is halb {_h(h + 1)} (half way to {_h(h + 1)})."
                elif "halb" in w and "halb" in corr: why[w] = f"Count from the half hour of the NEXT hour: {h}:{m:02d} → {corr}."
                else: why[w] = f"That's a different time. nach = past, vor = to. {h}:{m:02d} = {corr}."
            rule = f"{h}:{m:02d} → {corr}. " + ("halb always points to the NEXT hour." if "halb" in corr else "nach = past, vor = to (the next hour).")
            if (h * 11 + m) % 3:
                add("uhrzeit", [["Es", "S"], ["ist", "V"], ["{" + corr + "}.", "ZEIT"]], [corr] + wr, rule, why, prompt=f"{h}:{m:02d} → Es ist ___. (informal)")
            else:
                digital = f"{h}:{m:02d}"
                other = [f"{(h - 1) % 12 or 12}:{m:02d}" if "halb" in corr or "vor" in corr else f"{h % 12 + 1}:{m:02d}", f"{h}:{(60 - m) % 60:02d}" if m != 30 else f"{(h - 1) % 12 or 12}:30"]
                other = [o for o in dict.fromkeys(other) if o != digital]
                add("uhrzeit", [["Es", "S"], ["ist", "V"], [corr + ".", "ZEIT"]], [digital] + other, rule,
                    {o: f"„{corr}“ = {digital}. " + ("halb points to the next hour." if "halb" in corr else "vor = before the next hour, nach = after this hour.") for o in other},
                    prompt=f"„Es ist {corr}.“ Which time is it?", mode="choose")
    for h, m in [(7, 30), (8, 15), (13, 45), (14, 5), (16, 20), (18, 40), (19, 55), (20, 10), (21, 30), (22, 50), (6, 25), (17, 35), (12, 0), (15, 15), (23, 45)]:
        corr = f"{numword(h).replace('eins', 'ein') if h != 1 else 'ein'} Uhr" + (f" {numword(m)}" if m else "")
        wr = [informal(h, m) if m else f"{numword(h)} Uhr null", f"{numword(m)} Uhr {numword(h)}" if m else f"Uhr {numword(h)}"]
        add("uhrzeit", [["Der Zug", "S"], ["fährt", "V"], ["um {" + corr + "}.", "ZEIT"]], [corr] + wr,
            f"Formal time (train, radio, appointments): hour + Uhr + minutes, 24-hour clock: {h}:{m:02d} = {corr}.",
            {wr[0]: "That's the informal way. The station announcement uses the formal time: hours + Uhr + minutes.", wr[1]: "Formal: first the hours, then Uhr, then the minutes."},
            prompt=f"Announcement: Der Zug fährt um ___. ({h}:{m:02d})")

# ---------- dates ----------
def ordinal(d):
    return {1: "erst", 3: "dritt", 7: "siebt", 8: "acht"}.get(d) or (numword(d) + ("t" if d < 20 else "st"))

def datum():
    for d in range(1, 32):
        m = MON[(d * 7) % 12]
        if d > 29 and m == "Februar": m = "März"
        corr = f"am {ordinal(d)}en"
        if d in (1, 3, 7): wrong = [f"am {numword(d).replace('eins', 'ein')}ten" if d != 7 else "am siebenten", f"am {numword(d)}"]
        elif d < 20: wrong = [f"am {numword(d)}sten", f"im {ordinal(d)}en"]
        else: wrong = [f"am {numword(d)}ten", f"am {ordinal(d)}e"]
        if d == 7: wrong = ["am siebenten" if False else "am siebeten", "am sieben"]
        add("datum", [["Ich", "S"], ["habe", "V"], ["{" + corr + "} " + m, "ZEIT"], ["Geburtstag.", "AKK"]], [corr] + wrong,
            f"{d}. {m} → {corr} {m}. After am the ordinal ends in -en. 1.–19.: -te(n); from 20.: -ste(n). Irregular: ersten, dritten, siebten.",
            {w: ("Irregular ordinal: 1. = erste, 3. = dritte, 7. = siebte." if d in (1, 3, 7) else ("Dates use am, not im." if w.startswith("im") else
                 ("1.–19. take -te(n), not -ste(n)." if d < 20 and "sten" in w else ("From 20. on the ordinal takes -ste(n)." if "sten" not in w and w.endswith("ten") else "After am the ending is -en.")))) for w in wrong},
            prompt=f"Ich habe ___ {m} Geburtstag. ({d}.)")
    for d in (1, 2, 3, 4, 7, 10, 11, 16, 20, 23, 28, 31):
        m = MON[(d * 5) % 12]
        corr = f"der {ordinal(d)}e"
        wr = [f"der {ordinal(d)}en", f"am {ordinal(d)}en"]
        add("datum", [["Heute", "ZEIT"], ["ist", "V"], ["{" + corr + "} " + m + ".", "NOM"]], [corr] + wr,
            f"Der Wievielte ist heute? → Heute ist der {ordinal(d)}e {m}. After 'ist' the date is Nominativ: der …-e. With am (on): am …-en.",
            {wr[0]: "-en comes after am (Dativ). After 'Heute ist der …' the ending is -e.", wr[1]: "am = on (a date). 'Heute ist …' needs der + ordinal in -e."},
            prompt=f"Der Wievielte ist heute? – Heute ist ___ {m}. ({d}.)")
    seasons = [("Januar", "Winter"), ("April", "Frühling"), ("Juli", "Sommer"), ("Oktober", "Herbst"), ("Dezember", "Winter"), ("August", "Sommer"), ("Mai", "Frühling"), ("November", "Herbst")]
    for mo, se in seasons:
        others = [x for x in ["Winter", "Frühling", "Sommer", "Herbst"] if x != se][:2]
        add("datum", [["Der " + mo, "S"], ["ist", "V"], ["im {" + se + "}.", "ZEIT"]], [se] + others,
            "Seasons: der Frühling (März–Mai), der Sommer (Juni–August), der Herbst (September–November), der Winter (Dezember–Februar). All seasons and months are der.",
            {o: f"{mo} isn't in the {o}." for o in others}, prompt=f"Der {mo} ist im ___.")

# ---------- numbers ----------
def zahl_wrongs(n, corr):
    out = []
    if n < 100 and n > 20 and n % 10:
        t, o = divmod(n, 10)
        out.append(TENS[t] + "und" + (ZW[o] if o > 1 else "ein"))
        if o >= 2 and o != t: out.append(numword(o * 10 + t))
        if o == 1: out.append("einsund" + TENS[t])
    if n >= 100:
        out.append(corr.replace("hundert", "hunderte", 1) if "hundert" in corr else corr + "e")
        out.append(corr.replace("und", "", 1) if "und" in corr else corr.replace("hundert", "hundertund", 1))
    for a, b in [("sechz", "sechsz"), ("siebz", "siebenz"), ("dreißig", "dreizig"), ("zwanzig", "zweizig")]:
        if a in corr: out.append(corr.replace(a, b))
    return [w for w in dict.fromkeys(out) if w != corr]

def numword_big(n):
    if n < 100: return numword(n)
    h, r = divmod(n, 100)
    return ("ein" if h == 1 else ZW[h]) + "hundert" + (numword(r) if r else "")

def zahlen():
    nums = [13, 14, 15, 18, 19, 20, 22, 23, 25, 28, 29, 33, 36, 39, 40, 42, 44, 45, 50, 51, 55, 57, 58, 61, 63, 66, 69, 71, 72, 77, 79, 80, 81, 83, 85, 88, 90, 92, 94, 97, 98,
            101, 115, 120, 150, 199, 230, 365, 499, 725, 860, 999]
    for i, n in enumerate(nums):
        corr = numword_big(n)
        w = zahl_wrongs(n, corr)[:2]
        if len(w) < 2:
            w += [x for x in [numword_big(n + 10) if n + 10 < 1000 else "tausend", numword_big(n - 1)] if x not in w and x != corr][:2 - len(w)]
        rule = (f"{n} = {corr}. Hundreds: (ein)hundert, zweihundert … then the rest as usual: ones + und + tens. All one word." if n >= 100 else
                f"{n} = {corr}: ones first + und + tens, one word." if n > 20 and n % 10 else f"{n} = {corr}. Watch the spelling: sechzehn/sechzig, siebzehn/siebzig, dreißig.")
        def nwhy(x):
            if "sechsz" in x: return "sechs drops its s before -zehn/-zig: sechzehn, sechzig."
            if "siebenz" in x: return "sieben drops -en before -zehn/-zig: siebzehn, siebzig."
            if "dreizig" in x: return "30 = dreißig — with ß."
            if x.startswith("eins"): return "1 becomes ein- in compounds: einund…"
            if "hunderte" in x: return "No ending on hundert."
            if n > 20 and n % 10 and x.startswith(TENS.get(n // 10 % 10, "#")) and "und" in x: return "German says the ones FIRST: " + corr + "."
            return f"That's a different number. {n} = {corr}."
        if i % 2:
            add("zahlen", [["{" + corr + "}", ""]], [corr] + w, rule, {x: nwhy(x) for x in w}, prompt=f"{n} =")
        else:
            dg = [str(n)] + [str(x) for x in dict.fromkeys([int(str(n)[::-1]) if n < 100 and n % 10 else n + 10, n + 1 if n % 10 != 9 else n - 1]) if x != n]
            add("zahlen", [[corr, ""]], dg[:3], rule, {x: f"„{corr}“ = {n}. " + ("German says the ones first — einundzwanzig = 1 + 20." if x == str(n)[::-1] else "Read it again slowly.") for x in dg[1:3]},
                prompt=f"„{corr}“ =", mode="choose")
    for price, corr, wr in [("2,50 €", "zwei Euro fünfzig", ["zwei Komma fünfzig Euro", "fünfzig Euro zwei"]), ("1,99 €", "ein Euro neunundneunzig", ["eins Euro neunundneunzig", "neunundneunzig Euro eins"]),
                            ("12,80 €", "zwölf Euro achtzig", ["zwölf Euro und achtzig Cent und", "achtzig zwölf Euro"]), ("0,90 €", "neunzig Cent", ["null Euro neunzig", "neun Cent"]),
                            ("34,00 €", "vierunddreißig Euro", ["dreißigvier Euro", "vierunddreißig Euro null"])]:
        add("zahlen", [["Das", "S"], ["kostet", "V"], ["{" + corr + "}.", "AKK"]], [corr] + wr, f"Prices: euros + Euro + cents: {price} = {corr}.",
            {w: f"Prices are said as „{corr}“." for w in wr}, prompt=f"Das kostet ___. ({price})")

# ---------- personal pronouns (generated) ----------
AKKP = {"ich": "mich", "du": "dich", "er": "ihn", "sie": "sie", "es": "es", "wir": "uns", "ihr": "euch", "sie (they)": "sie", "Sie": "Sie"}
DATP = {"ich": "mir", "du": "dir", "er": "ihm", "sie": "ihr", "es": "ihm", "wir": "uns", "ihr": "euch", "sie (they)": "ihnen", "Sie": "Ihnen"}
def pronomen():
    akk_frames = [("besuche ___ morgen.", "besuchen"), ("rufe ___ heute an.", "anrufen"), ("frage ___ morgen.", "fragen"), ("hole ___ um 8 Uhr ab.", "abholen"), ("sehe ___ jeden Tag.", "sehen")]
    dat_frames = [("helfe ___ gern.", "helfen"), ("danke ___ sehr.", "danken"), ("antworte ___ morgen.", "antworten"), ("gebe ___ das Buch.", "geben"), ("schreibe ___ eine E-Mail.", "schreiben")]
    who_list = ["du", "er", "sie", "ihr", "sie (they)", "Sie", "ich", "wir"]
    for case, frames, tab, other in [("AKK", akk_frames, AKKP, DATP), ("DAT", dat_frames, DATP, AKKP)]:
        for i, who in enumerate(who_list):
            for j in (0, 1):
                fr, inf = frames[(i + j * 3) % len(frames)]
                corr = tab[who]
                subj_ = "Ich" if who not in ("ich", "wir") else "Er"
                if subj_ == "Er":
                    v = fr.split()[0]; verbs = {"besuche": "besucht", "rufe": "ruft", "frage": "fragt", "hole": "holt", "sehe": "sieht", "helfe": "hilft", "danke": "dankt", "antworte": "antwortet", "gebe": "gibt", "schreibe": "schreibt"}
                    fr = verbs[v] + fr[len(v):]
                nom = who.split()[0] if who != "Sie" else "Sie"
                wr = [w for w in dict.fromkeys([other[who], nom if nom != corr else ("ihn" if case == "DAT" else "ihm")]) if w != corr][:2]
                if len(wr) < 2: wr.append("ihnen" if corr != "ihnen" else "ihn")
                rule = f"{inf} + {'Akkusativ' if case == 'AKK' else 'Dativ'} → {who} becomes '{corr}'. " + ("Akkusativ: mich, dich, ihn, sie, es, uns, euch, sie/Sie." if case == "AKK" else "Dativ: mir, dir, ihm, ihr, ihm, uns, euch, ihnen/Ihnen.")
                why = {w: (f"'{w}' is {'Dativ' if case == 'AKK' else 'Akkusativ'} — {inf} takes the {'Akkusativ' if case == 'AKK' else 'Dativ'}." if w in other.values() else
                           f"'{w}' is the {'Akkusativ' if case == 'AKK' else 'Dativ'} of a different person. For {who}: '{corr}'." if w in tab.values() else f"'{w}' is the Nominativ (subject form).") for w in wr}
                text = f"{subj_} {fr.replace('___', '{' + corr + '}')}"
                add("pron", [[text, case]], [corr] + wr, rule, why, prompt=f"{subj_} {fr} ({who})")

# ---------- Wechselpräpositionen (curated scenes) ----------
SCENES = [("Das Buch", "liegt", "lege", "das Buch", "auf", "Tisch"), ("Die Katze", "schläft", "setze", "die Katze", "auf", "Sofa"), ("Der Koffer", "steht", "stelle", "den Koffer", "unter", "Bett"),
          ("Das Bild", "hängt", "hänge", "das Bild", "an", "Wand"), ("Die Lampe", "steht", "stelle", "die Lampe", "neben", "Bett"), ("Der Teppich", "liegt", "lege", "den Teppich", "vor", "Sofa"),
          ("Die Milch", "steht", "stelle", "die Milch", "in", "Kühlschrank"), ("Die Gläser", "stehen", "stelle", "die Gläser", "in", "Schrank"), ("Der Spiegel", "hängt", "hänge", "den Spiegel", "über", "Tisch"),
          ("Das Fahrrad", "steht", "stelle", "das Fahrrad", "vor", "Haus"), ("Die Schuhe", "stehen", "stelle", "die Schuhe", "neben", "Tür"), ("Das Handy", "liegt", "lege", "das Handy", "in", "Tasche"),
          ("Der Schlüssel", "liegt", "lege", "den Schlüssel", "unter", "Teppich"), ("Die Bücher", "stehen", "stelle", "die Bücher", "in", "Regal"), ("Die Uhr", "hängt", "hänge", "die Uhr", "an", "Wand"),
          ("Der Stuhl", "steht", "stelle", "den Stuhl", "an", "Fenster"), ("Das Auto", "steht", "stelle", "das Auto", "hinter", "Haus"), ("Die Blumen", "stehen", "stelle", "die Blumen", "auf", "Balkon"),
          ("Der Laptop", "liegt", "lege", "den Laptop", "auf", "Bett"), ("Die Jacke", "hängt", "hänge", "die Jacke", "in", "Schrank"), ("Das Foto", "steht", "stelle", "das Foto", "neben", "Lampe"),
          ("Der Hund", "liegt", "lege", "den Hund", "zwischen", "Stuhl und Tisch")]
AKK_ART = {"der": "den", "die": "die", "das": "das"}
CONTR_D = {("in", "der"): "im", ("in", "das"): "im", ("an", "der"): "am", ("an", "das"): "am"}
CONTR_A = {("in", "das"): "ins", ("an", "das"): "ans"}
def wechsel():
    for subj_, wo_v, wohin_v, obj, prep, noun in SCENES:
        if " und " in noun:
            add("wechsel", [[subj_, "S"], [wo_v, "V"], ["zwischen {dem} Stuhl und dem Tisch.", "ORT"]], ["dem", "den", "der"],
                "Wo? → Dativ. zwischen + dem Stuhl und dem Tisch.", {"den": "den is Akkusativ (Wohin?).", "der": "Stuhl is der → Dativ dem."}, prompt=f"{subj_} {wo_v} zwischen ___ Stuhl und dem Tisch.")
            continue
        a = N[noun]["a"]
        dform = CONTR_D.get((prep, a)) or f"{prep} {DAT_ART[a]}"
        aform = CONTR_A.get((prep, a)) or f"{prep} {AKK_ART[a]}"
        same = {dform, aform, f"{prep} dem" if dform in ("im", "am") else "", f"{prep} das" if aform in ("ins", "ans") else ""}
        wrong_d = [aform] + [f"{prep} {x}" for x in ("den", "der", "dem", "das") if f"{prep} {x}" not in same]
        wrong_a = [dform] + [f"{prep} {x}" for x in ("dem", "der", "den", "die") if f"{prep} {x}" not in same]
        add("wechsel", [[subj_, "S"], [wo_v, "V"], ["{" + dform + "} " + noun + ".", "ORT"]], [dform] + wrong_d[:2],
            f"Wo? ({wo_v} = position, no movement) → Dativ: {a} {noun} → {dform} {noun}.",
            {w: (f"'{w}' is Akkusativ — that's for Wohin? (movement). '{wo_v}' describes where something is → Dativ." if w == aform else f"Wrong article: {noun} is {a} → Dativ {DAT_ART[a]}.") for w in wrong_d[:2]},
            prompt=f"Wo? {subj_} {wo_v} ___ {noun}.", note=f"{a} {noun}")
        add("wechsel", [["Ich", "S"], [wohin_v, "V"], [obj, "AKK"], ["{" + aform + "} " + noun + ".", "ORT"]], [aform] + wrong_a[:2],
            f"Wohin? ({wohin_v} = putting something somewhere) → Akkusativ: {a} {noun} → {aform} {noun}.",
            {w: (f"'{w}' is Dativ — that's for Wo? (position). '{wohin_v}' is a movement → Akkusativ." if w == dform else f"Wrong article: {noun} is {a} → Akkusativ {AKK_ART[a]}.") for w in wrong_a[:2]},
            prompt=f"Wohin? Ich {wohin_v} {obj} ___ {noun}.", note=f"{a} {noun}")
    places = ["Kino", "Park", "Büro", "Restaurant", "Supermarkt", "Café", "Museum", "Hotel", "Stadt", "Küche", "Garten", "Schule", "Kirche", "Krankenhaus", "Zimmer", "Universität"]
    for i, pl in enumerate(places):
        a = N[pl]["a"]
        d = CONTR_D.get(("in", a)) or f"in {DAT_ART[a]}"
        ak = CONTR_A.get(("in", a)) or f"in {AKK_ART[a]}"
        go = ["Ich gehe", "Wir gehen", "Er geht", "Sie geht"][i % 4]
        be = ["Ich bin", "Wir sind", "Er ist", "Sie wartet"][i % 4]
        wr1 = [d] + [x for x in ("in", "in dem" if d == "im" else "in den") if x not in (d, ak)]
        add("wechsel", [[go.split()[0], "S"], [go.split()[1], "V"], ["{" + ak + "} " + pl + ".", "ORT"]], [ak] + wr1[:2],
            f"Wohin? {go.split()[1]} = movement → Akkusativ: {a} {pl} → {ak} {pl}.",
            {w: ("Dativ is for Wo? (position). This is movement → Akkusativ." if w == d else "You need the article: in + das = ins, in + den, in + die.") for w in wr1[:2]}, prompt=f"Wohin? {go} ___ {pl}.")
        wr2 = [ak] + [x for x in ("in", "in das" if ak == "ins" else "in den") if x not in (d, ak)]
        add("wechsel", [[be.split()[0], "S"], [be.split()[1], "V"], ["{" + d + "} " + pl + ".", "ORT"]], [d] + wr2[:2],
            f"Wo? {be.split()[1]} = position → Dativ: {a} {pl} → {d} {pl}.",
            {w: ("Akkusativ is for Wohin? (movement). This is a position → Dativ." if w == ak else "You need the article: in + dem = im, in + der.") for w in wr2[:2]}, prompt=f"Wo? {be} ___ {pl}.")

# ---------- Dativ prepositions (more) ----------
def dativ():
    combos = [("Ich fahre mit", ["Bus", "Zug", "Taxi", "Straßenbahn", "U-Bahn", "Fahrrad", "Auto"], "mit + Dativ"), ("Wir sprechen mit", ["Lehrer", "Ärztin", "Kollege", "Mutter", "Kind", "Freundin"], "mit + Dativ"),
              ("Ich komme aus", ["Büro", "Supermarkt", "Kirche", "Küche", "Hotel", "Schule", "Museum"], "aus + Dativ"), ("Er wohnt bei", ["Vater", "Schwester", "Freund", "Kollegin"], "bei + Dativ"),
              ("Das Geschenk ist von", ["Bruder", "Oma", "Kollegin", "Vater", "Freundin"], "von + Dativ"), ("Ich gehe nach", ["Arbeit", "Schule"], "nach + Dativ")]
    N.setdefault("Lehrer", dict(a="der", n="Lehrer", p="Lehrer", e="teacher")); N.setdefault("Oma", dict(a="die", n="Oma", p="Omas", e="grandma"))
    for pre, nouns, rule in combos:
        if "nach" in pre: continue
        words = pre.split()
        for nn in nouns:
            a = N[nn]["a"]; corr = DAT_ART[a]
            noun = nn
            opts = list(dict.fromkeys([corr, a, "den" if a != "die" else "die", "dem" if a == "die" else "der"]))
            opts = [corr] + [o for o in opts if o != corr][:2]
            why = {o: (f"'{o}' is Nominativ. After {words[-1]} always Dativ → {corr}." if o == a else f"'{o}' is Akkusativ. {words[-1]} always takes the Dativ." if o in ("den", "die") else f"Wrong gender: {nn} is {a} → {corr}.") for o in opts[1:]}
            add("dativ", [[" ".join(words[:-1]), ""], [words[-1] + " {" + corr + "} " + noun + ".", "DAT"]], opts, f"{rule}. {a} {nn} → {corr} {nn}. Dativ: der/das → dem, die → der.",
                why, prompt=f"{pre} ___ {noun}.", note=f"{a} {nn}")
    zu = [("Bäcker", "zum", "der"), ("Friseur", "zum", "der"), ("Party", "zur", "die"), ("Universität", "zur", "die"), ("Museum", "zum", "das"), ("Bahnhof", "zum", "der"),
          ("Haltestelle", "zur", "die"), ("Hotel", "zum", "das"), ("Kirche", "zur", "die"), ("Park", "zum", "der"), ("Kollegin", "zur", "die"), ("Zahnarzt", "zum", "der")]
    for nn, corr, a in zu:
        wr = ["zur" if corr == "zum" else "zum", "nach"]
        add("dativ", [["Entschuldigung, wie komme ich", ""], ["{" + corr + "} " + nn + "?", "ORT"]], [corr] + wr, f"zu + Dativ: zu dem → zum (der/das), zu der → zur (die). {a} {nn} → {corr} {nn}.",
            {wr[0]: f"{nn} is {a} → {corr}.", "nach": "nach is for cities, countries and nach Hause. To a place/person in town: zu."}, prompt=f"Entschuldigung, wie komme ich ___ {nn}?", note=f"{a} {nn}")
    plurals = [("Kinder", "Kindern"), ("Freunde", "Freunden"), ("Kollegen", "Kollegen"), ("Eltern", "Eltern"), ("Leute", "Leuten"), ("Brüder", "Brüdern")]
    for nom, dat in plurals:
        wr = [x for x in dict.fromkeys([nom + "s", nom if nom != dat else nom + "n", dat + "n"]) if x != dat][:2]
        add("dativ", [["Ich", "S"], ["spreche", "V"], ["mit den {" + dat + "}.", "DAT"]], [dat] + wr,
            "Dativ plural: den + noun + -n (if it doesn't already end in -n or -s): mit den Kindern. " + (f"{nom} already ends in -n → no extra -n." if nom == dat else ""),
            {w: ("Dativ plural adds -n: " + dat if w == nom else "Not a correct plural form.") for w in wr}, prompt=f"Ich spreche mit den ___. (die {nom})")

# ---------- separable verbs: conjugation with the prefix at the end ----------
def trennbar():
    for v in [x for x in VERBS if x["pre"]]:
        f = forms(v)
        for p in R.sample(PRON, 3):
            corr = f[p]
            wr = [v["pre"] + corr, (f["er"] if f[p] != f["er"] else f["ich"])]
            wr = [w for w in dict.fromkeys(wr) if w != corr]
            s = subj(p)
            why = {wr[0]: f"In a main clause the prefix '{v['pre']}' separates and goes to the end: {s} {corr} … {v['pre']}."}
            if len(wr) > 1: why[wr[1]] = f"Wrong person: for {PRON_EN[p]} you need '{corr}'."
            add("trenn", [[s, "S"], ["{" + corr + "}", "V"], [v["ctx"], v["ctx_lab"]], [v["pre"] + ".", "PRE"]], [corr] + wr,
                f"{v['inf']} ({v['en']}): the verb part '{corr}' is in position 2, the prefix '{v['pre']}' goes to the END.", why,
                prompt=f"{s} ___ {v['ctx']} {v['pre']}. ({v['inf']})", note=v["inf"])
        if v["inf"] in ("aussehen", "einschlafen", "aufwachen"): continue
        add("trenn", [["Ich", "S"], ["muss", "MV"], [v["ctx"], v["ctx_lab"]], ["{" + v["inf"] + "}.", "INF"]],
            [v["inf"], f"{forms(v)['ich']} {v['pre']}", f"{v['pre']} {v['base']}"],
            f"With a modal verb the separable verb stays together at the end as one word: Ich muss {v['ctx']} {v['inf']}.",
            {f"{forms(v)['ich']} {v['pre']}": "After a modal verb the second verb is an unconjugated infinitive — written as one word.", f"{v['pre']} {v['base']}": "The infinitive of a separable verb is written as ONE word: " + v["inf"] + "."},
            prompt=f"Ich muss {v['ctx']} ___. ({v['inf']})", note=v["inf"])

# ---------- yes/no questions and verb-second from the verb list ----------
def janein_satzbau():
    for v in [x for x in VERBS if not x["pre"] and "nopl" not in x["flags"]]:
        p = R.choice(["du", "Sie", "ihr"])
        f = forms(v); conj = f["sie" if p == "Sie" else p]
        s, ctx = p, v["ctx"]
        corr = f"{conj.capitalize()}#V1 / {s}#S / {ctx}?#{v['ctx_lab']}"
        w1 = f"{s.capitalize()} {conj} {ctx}?"
        w2 = f"{conj.capitalize()} {ctx} {s}?"
        choose("janein", f"Make a yes/no question: „{s.capitalize()} {conj} {ctx}.“", corr, [w1, w2],
               "Yes/no question: the verb goes to position 1 and the subject follows directly.",
               {w1: "That's a statement word order. In writing, a yes/no question puts the verb first.", w2: "The subject must come directly after the verb."})
    times = ["Heute", "Morgen", "Am Montag", "Am Wochenende", "Jetzt", "Oft", "Am Abend", "Im Sommer", "Manchmal", "Dann"]
    for i, v in enumerate([x for x in VERBS if not x["pre"] and x["ctx_lab"] != "ZEIT" and "nopl" not in x["flags"]]):
        t = times[i % len(times)]
        p = ["ich", "er", "wir", "sie"][i % 4]
        s = subj(p); f = forms(v); conj = f[p]
        sl = s if s in ("Anna", "Herr Weber", "Tom und Lisa") else s[0].lower() + s[1:]
        if s.startswith("Sie (she)"): sl = "sie"
        if s == "Sie": sl = "sie"
        corr = f"{t}#ZEIT / {conj}#V / {sl}#S / {v['ctx']}.#{v['ctx_lab']}"
        w1 = f"{t} {sl} {conj} {v['ctx']}."
        w2 = f"{t} {sl} {v['ctx']} {conj}."
        choose("satzbau", "Which sentence is correct?", corr, [w1, w2],
               f"Verb in position 2! '{t}' is position 1, so the verb '{conj}' comes next and the subject moves behind it.",
               {w1: "The subject before the verb puts the verb in position 3.", w2: "The verb goes to the end only in subordinate clauses (weil, dass …). Here it must be in position 2."})

def umlaut_last(w):
    """Umlaut the last vowel group if it is a/o/u/au (Haus → Häus, Stuhl → Stühl); None otherwise."""
    m = list(re.finditer(r"[aeiouäöüy]+", w))
    if not m or m[-1].group() not in ("a", "o", "u", "au"): return None
    x = m[-1]
    return w[:x.start()] + {"au": "äu", "a": "ä", "o": "ö", "u": "ü"}[x.group()] + w[x.end():]

def plausible_plurals(sg, pl):
    """Two wrong plurals that follow real German plural patterns for this word shape."""
    if sg.endswith("e"):
        cands = [sg + "n", sg, sg + "s"]
    elif sg.endswith(("er", "el", "en")):
        um = umlaut_last(sg[:-2])
        cands = [sg, sg + "n", sg + "s"] + ([um + sg[-2:]] if um else [])
    elif sg[-1] in "aiouy":
        cands = [sg + "s", sg + "en", sg]
    else:
        um = None if sg.endswith(("ung", "heit", "keit", "schaft", "ion", "tät", "in", "ei", "ik", "ur", "um")) else umlaut_last(sg)
        cands = [sg + "e", sg + "en", sg + "er", sg + "s"] + ([um + "e", um + "er"] if um else [])
    out = [c for c in dict.fromkeys(cands) if c != pl]
    R.shuffle(out)
    return out[:2]

# ---------- vocabulary: the whole dictionary ----------
GENDER_HINT = {"learn": "No reliable rule — learn this one with its article.", "exception": "This word breaks the usual rule — learn it.", "two genders": "This word has two genders with different meanings."}
def wortschatz(dic):
    for i, d in enumerate(dic):
        a, n, r = d["a"], d["n"], d["r"]
        reason = RULE_EXPL.get(r) or GENDER_HINT.get(r) or r
        if r == "compound" and d.get("x"): reason = f"compound — the last part decides ({d['x'].replace('← ', '')})"
        why = {o: f"Not {o}. {n} is {a}: {reason}." for o in ("der", "die", "das") if o != a}
        q = add("wort_art", [["{" + a + "} " + n, "S"]], [a] + [o for o in ("der", "die", "das") if o != a], f"<b>{a} {n}</b> ({d['e']}) — {reason}.", why,
                prompt=f"___ {n} ({d['e']})", note=(f"Plural: die {d['p']}" if d.get("p") and d["p"] not in ("–", "") else None))
        q["r"] = i
    # meaning: German → English, distractors from neighbouring frequency band with a different meaning
    for i, d in enumerate(dic):
        band = [x for x in dic[max(0, i - 60): i + 60] if x["e"] != d["e"] and x["n"] != d["n"]]
        wr = []
        for x in R.sample(band, min(len(band), 6)):
            if x["e"] not in wr and x["e"].split(",")[0] != d["e"].split(",")[0]: wr.append(x["e"])
            if len(wr) == 3: break
        q = add("wort_bed", [[f"{d['a']} {d['n']}", "S"]], [d["e"]] + wr, f"<b>{d['a']} {d['n']}</b> = {d['e']}" + (f" · plural: die {d['p']}" if d.get("p") and d["p"] not in ("–", "") else "") + ".",
                {w: f"„{w}“ is a different word." for w in wr}, prompt=f"What does „{d['a']} {d['n']}“ mean?", mode="choose")
        q["r"] = i + 6
    for i, d in enumerate(dic):
        p = d.get("p")
        if not p or p in ("–", "") or " " in p: continue
        wr = plausible_plurals(d["n"], p)
        if len(wr) < 2: continue
        typ = plural_type(d["n"], p)
        q = add("wort_pl", [["die {" + p + "}", "NOM"]], ["die " + p] + ["die " + w for w in wr], f"{d['a']} {d['n']} → die {p} (plural type: {typ}).",
                {"die " + w: f"The plural of {d['n']} is {p}." for w in wr}, prompt=f"Plural of {d['a']} {d['n']} ({d['e']}):", note=f"{d['a']} {d['n']}, die {p}")
        q["r"] = i + 30


def run_all(dic):
    uhrzeit(); datum(); zahlen(); pronomen(); wechsel(); dativ(); trennbar(); janein_satzbau(); wortschatz(dic)


# ---------- listening: hear a sentence, pick what you heard ----------
HOMOPHONES = [{"seid", "seit"}, {"isst", "ist"}, {"das", "dass"}, {"wird", "wirt"}, {"end", "ent"}, {"mahlen", "malen"}, {"viel", "fiel"}, {"wider", "wieder"}]
LISTEN_TOPICS = ["verb", "verb_irr", "seinhaben", "akk", "dativ", "wechsel", "poss", "modal", "trenn", "pron", "praet", "perf_aux", "einkein", "welcher", "akkpraep", "vergleich", "laender", "imp", "zeitpraep"]

def _sounds_same(a, b):
    a, b = a.lower(), b.lower()
    if a == b: return True
    wa, wb = a.split(), b.split()
    if len(wa) != len(wb): return False
    diff = [(x, y) for x, y in zip(wa, wb) if x != y]
    return all(any({x.strip(".,!?"), y.strip(".,!?")} == h for h in HOMOPHONES) for x, y in diff)

def listening(qs):
    """Build listening questions from clean gap questions: the app speaks the full sentence; options are the sentence with each option filled in."""
    out = []
    pool = [q for q in qs if q["t"] in LISTEN_TOPICS and q["p"].count("___") == 1 and "(" not in q["p"] and ":" not in q["p"] and "→" not in q["p"] and "–" not in q["p"]]
    R.shuffle(pool)
    per_topic = {}
    for q in pool:
        if per_topic.get(q["t"], 0) >= 30: continue
        p = re.sub(r"^(Wo\?|Wohin\?)\s+", "", q["p"])
        variants = [p.replace("___", o) for o in q["o"]]
        if len(set(v.lower() for v in variants)) < len(variants): continue
        if any(_sounds_same(variants[0], v) for v in variants[1:]): continue
        per_topic[q["t"]] = per_topic.get(q["t"], 0) + 1
        nq = add("hoeren", [list(x) for x in q["s"]], variants, q["w"] + " <i>(heard: „" + variants[0] + "“)</i>",
                 {v: f"You heard „{variants[0]}“ — not „{v}“. Listen to the word that changes: {q['o'][0]} vs {o}." for v, o in zip(variants[1:], q["o"][1:])},
                 prompt="🔊 Which sentence do you hear?", mode="choose")
        nq["au"] = variants[0]
        nq["r"] = len(out) * 6
        out.append(nq)
    # numbers and times by ear
    for i, n in enumerate([13, 30, 17, 70, 16, 60, 24, 42, 35, 53, 67, 76, 19, 90, 48, 84, 12, 20, 89, 98, 115, 250, 512, 999]):
        w = numword_big(n)
        rev = int(str(n)[::-1]) if 10 < n < 100 and n % 10 else None
        others = [x for x in dict.fromkeys([rev, n + 1 if n % 10 != 9 else n - 1, n + 10 if n < 990 else n - 10, {13: 30, 30: 13, 17: 70, 70: 17, 16: 60, 60: 16, 19: 90, 90: 19, 12: 20, 20: 12}.get(n)]) if x and x != n][:3]
        nq = add("hoeren", [[w, ""]], [str(n)] + [str(x) for x in others], f"„{w}“ = {n}. " + ("-zehn (13–19) vs -zig (20–90): listen to the ending." if n in (13, 30, 17, 70, 16, 60, 19, 90, 12, 20) else "German says the ones first: vierundzwanzig = 4 + 20."),
                 {str(x): f"You heard „{w}“ = {n}." for x in others}, prompt="🔊 Which number do you hear?", mode="choose")
        nq["au"] = w
        nq["r"] = len(out) * 6
        out.append(nq)
    for h, m in [(7, 30), (8, 15), (6, 45), (9, 30), (10, 20), (11, 40), (12, 30), (2, 15), (3, 45), (4, 55), (5, 5), (1, 30), (7, 25), (8, 35)]:
        spoken = informal(h, m)
        opts = [f"{h}:{m:02d}"] + [x for x in dict.fromkeys([f"{h % 12 + 1}:{m:02d}", f"{h}:{(60 - m) % 60:02d}", f"{(h - 1) % 12 or 12}:{m:02d}"]) if x != f"{h}:{m:02d}"][:2]
        nq = add("hoeren", [[spoken, "ZEIT"]], opts, f"„Es ist {spoken}.“ = {h}:{m:02d}. " + ("halb points to the NEXT hour." if "halb" in spoken else "nach = past, vor = to."),
                 {o: f"„{spoken}“ = {h}:{m:02d}." for o in opts[1:]}, prompt="🔊 What time is it?", mode="choose")
        nq["au"] = f"Es ist {spoken}."
        nq["r"] = len(out) * 6
        out.append(nq)
    return out
