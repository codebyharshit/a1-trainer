"""Hand-written questions, part 3: Akkusativ prepositions, comparison, countries & languages,
Dativ possessives, ja/nein/doch, more sein/haben and more time prepositions."""
import re
from .core import add, choose


def Q(t, spec, opts, rule, why, prompt=None):
    add(t, spec, opts, rule, why, prompt=prompt)


def C(t, prompt, corr, wrong, rule, why):
    """Choose-type question whose options are whole phrases (no sentence structure to show)."""
    add(t, [[corr, ""]], [corr] + wrong, rule, why, prompt=prompt, mode="choose")


# ---------------------------------------------------------------- Akkusativ prepositions
AKK_RULE = "<b>für, ohne, durch, gegen, um, bis</b> always take the <b>Akkusativ</b>. Only masculine changes: der → <b>den</b>, ein/mein → <b>einen/meinen</b>. Pronouns: mich, dich, ihn, sie, es, uns, euch, sie/Sie."

def akkpraep():
    W_DAT = "is a Dativ form. {p} always takes the Akkusativ."
    W_NOM = "is the Nominativ (no ending). {p} + Akkusativ → masculine needs -en."
    items = [
        ("Das Geschenk ist / für {meinen} Bruder.#AKK", ["meinen", "meinem", "mein"], "für", "der Bruder"),
        ("Ich kaufe Blumen / für {meine} Mutter.#AKK", ["meine", "meiner", "meinen"], "für", "die Mutter"),
        ("Ich gehe / ohne {meinen} Schirm.#AKK", ["meinen", "meinem", "mein"], "ohne", "der Schirm"),
        ("Wir gehen / durch {den} Park.#AKK", ["den", "dem", "der"], "durch", "der Park"),
        ("Das Auto fährt / gegen {einen} Baum.#AKK", ["einen", "einem", "ein"], "gegen", "der Baum"),
        ("Wir sitzen / um {den} Tisch.#AKK", ["den", "dem", "der"], "um", "der Tisch"),
        ("Die Apotheke ist / um {die} Ecke.#AKK", ["die", "der", "den"], "um", "die Ecke"),
        ("Wir fahren / durch {die} Stadt.#AKK", ["die", "der", "den"], "durch", "die Stadt"),
        ("Ich spiele heute / gegen {meinen} Bruder Tennis.#AKK", ["meinen", "meinem", "mein"], "gegen", "der Bruder"),
        ("Der Zug fährt / durch {den} Tunnel.#AKK", ["den", "dem", "der"], "durch", "der Tunnel"),
        ("Ich arbeite / für {eine} Firma in München.#AKK", ["eine", "einer", "einen"], "für", "die Firma"),
        ("Er macht das / für {seine} Kinder.#AKK", ["seine", "seinen", "seinem"], "für", "die Kinder (plural)"),
        ("Ohne {meine} Brille#AKK / sehe ich nichts.", ["meine", "meiner", "meinen"], "ohne", "die Brille"),
        ("Wir gehen / um {das} Haus.#AKK", ["das", "dem", "den"], "um", "das Haus"),
        ("Ich brauche ein Medikament / gegen {den} Husten.#AKK", ["den", "dem", "der"], "gegen", "der Husten"),
        ("Danke / für {den} Tipp!#AKK", ["den", "dem", "der"], "für", "der Tipp"),
        ("Danke / für {die} Einladung!#AKK", ["die", "der", "den"], "für", "die Einladung"),
        ("Vielen Dank / für {das} Geschenk!#AKK", ["das", "dem", "den"], "für", "das Geschenk"),
        ("Fährst du / ohne {deinen} Mann / in Urlaub?#AKK", ["deinen", "deinem", "dein"], "ohne", "der Mann"),
        ("Kommst du / ohne {deine} Kinder?#AKK", ["deine", "deinen", "deinem"], "ohne", "die Kinder (plural)"),
        ("Er läuft / durch {das} Zimmer.#AKK", ["das", "dem", "den"], "durch", "das Zimmer"),
        ("Ich lerne / für {die} Prüfung.#AKK", ["die", "der", "den"], "für", "die Prüfung"),
        ("Ich kaufe einen Pullover / für {ein} Kind.#AKK", ["ein", "einem", "einen"], "für", "das Kind"),
        ("Ich kaufe ein Geschenk / für {meinen} Freund.#AKK", ["meinen", "meinem", "mein"], "für", "der Freund"),
        ("Wir gehen / durch {den} Wald.#AKK", ["den", "dem", "der"], "durch", "der Wald"),
    ]
    for spec, opts, p, noun in items:
        corr = opts[0]
        why = {}
        for w in opts[1:]:
            if w == "der" and noun.startswith("der"):
                why[w] = f"'der' is the Nominativ. {p} + Akkusativ → masculine der becomes {corr}."
            elif w.endswith("em") or w.endswith("er"):
                why[w] = f"'{w}' " + W_DAT.format(p=p) + f" {noun} → {corr}."
            elif w in ("mein", "dein", "sein", "ein") and noun.startswith("der"):
                why[w] = f"'{w}' " + W_NOM.format(p=p) + f" → {corr}."
            else:
                why[w] = f"Wrong ending for {noun}. {p} + Akkusativ → {corr}."
        Q("akkpraep", spec, opts,
          f"{p} + Akkusativ: {noun} → {corr}. " + AKK_RULE, why)

    pron = [
        ("Ich habe heute Zeit / für {dich}.#AKK", ["dich", "dir", "du"], "du"),
        ("Ich fahre nicht / ohne {euch}.#AKK", ["euch", "ihr", "eure"], "ihr"),
        ("Ist der Brief / für {mich}?#AKK", ["mich", "mir", "ich"], "ich"),
        ("Der Kaffee ist / für {Sie}.#AKK", ["Sie", "Ihnen", "Ihr"], "Sie"),
        ("Ich habe nichts / gegen {ihn}.#AKK", ["ihn", "ihm", "er"], "er"),
        ("Das Geschenk ist / für {uns}.#AKK", ["uns", "wir", "unser"], "wir"),
        ("Wir gehen nicht / ohne {sie}.#AKK", ["sie", "ihnen", "ihr"], "sie, they"),
    ]
    for spec, opts, who in pron:
        corr = opts[0]
        why = {}
        for w in opts[1:]:
            if w in ("dir", "mir", "ihm", "Ihnen", "ihnen"): why[w] = f"'{w}' is Dativ. für/ohne/gegen take the Akkusativ → {corr}."
            elif w in ("du", "ich", "er", "wir", "ihr") : why[w] = f"'{w}' is the Nominativ (subject form). After a preposition: Akkusativ → {corr}."
            else: why[w] = f"'{w}' is a possessive article (your/our …), not a pronoun."
        Q("akkpraep", spec, opts, f"Pronoun after für/ohne/gegen → Akkusativ: {who} → {corr}. " + AKK_RULE, why,
          prompt=" ".join(re.sub(r"\{.*?\}", "___", part.split("#")[0]) for part in spec.split(" / ")) + f" ({who})")

    choice = [
        ("Das Geschenk ist {für}#ADV / meine Oma.#AKK", ["für", "ohne", "durch"], "für = for (someone).",
         {"ohne": "ohne = without — a present 'without grandma' makes no sense.", "durch": "durch = through (a place)."}),
        ("Der Bus fährt {durch}#ADV / die Stadt.#AKK", ["durch", "für", "ohne"], "durch = through.",
         {"für": "für = for (someone/something).", "ohne": "ohne = without."}),
        ("Die Bank ist gleich {um}#ADV / die Ecke.#AKK", ["um", "durch", "für"], "um die Ecke = around the corner.",
         {"durch": "durch die Ecke = through the corner — not possible.", "für": "für = for."}),
        ("Ich bleibe {bis}#ZEIT / Freitag in Berlin.", ["bis", "um", "durch"], "bis = until. With days and times no article: bis Freitag, bis 8 Uhr.",
         {"um": "um is for clock times (um 8 Uhr).", "durch": "durch = through (a place)."}),
        ("Der Laden ist {bis}#ZEIT / 20 Uhr geöffnet.", ["bis", "für", "durch"], "bis = until.",
         {"für": "für = for.", "durch": "durch = through."}),
        ("Ich trinke Kaffee {ohne}#ADV / Zucker – ich mag es nicht süß.", ["ohne", "für", "gegen"], "ohne = without.",
         {"für": "für = for — doesn't fit with 'I don't like it sweet'.", "gegen": "gegen = against."}),
        ("Ich komme {ohne}#ADV / meinen Mann – er ist krank.", ["ohne", "für", "durch"], "ohne = without.",
         {"für": "für meinen Mann = for my husband — but he's ill and stays at home.", "durch": "durch = through."}),
        ("Der Bus kommt {um}#ZEIT / 7:15 Uhr.", ["um", "am", "im"], "um + clock time.",
         {"am": "am is for days and dates.", "im": "im is for months and seasons."}),
    ]
    for spec, opts, rule, why in choice:
        Q("akkpraep", spec, opts, rule + " " + AKK_RULE, why)

    C("akkpraep", "„Ich komme gegen 8 Uhr.“ means …", "I'll come at about 8 o'clock.", ["I'll come exactly at 8 o'clock.", "I'll come against 8 o'clock."],
      "gegen + time = approximately, around. um 8 Uhr = exactly at 8.",
      {"I'll come exactly at 8 o'clock.": "Exactly at 8 = um 8 Uhr. gegen = about.", "I'll come against 8 o'clock.": "With times, gegen means 'around / about', not 'against'."})

    # contrast with Dativ prepositions
    contrast = [
        ("Ich gehe / mit {meinem} Freund / ins Kino.", ["meinem", "meinen", "mein"], "mit + Dativ: der Freund → mit meinem Freund. Compare: für meinen Freund (Akkusativ).",
         {"meinen": "meinen is Akkusativ — that's for für/ohne. mit always takes Dativ.", "mein": "No ending = Nominativ. mit + Dativ → meinem."}),
        ("Ich spreche / mit {ihm}.#DAT", ["ihm", "ihn", "er"], "mit + Dativ: er → ihm. Compare: für ihn (Akkusativ).",
         {"ihn": "ihn is Akkusativ — für ihn, ohne ihn. mit takes Dativ.", "er": "er is the Nominativ."}),
        ("Ich habe ein Geschenk / für {ihn}.#AKK", ["ihn", "ihm", "er"], "für + Akkusativ: er → ihn. Compare: mit ihm (Dativ).",
         {"ihm": "ihm is Dativ — mit ihm, bei ihm. für takes Akkusativ.", "er": "er is the Nominativ."}),
        ("{Für}#W / wen ist das Geschenk?", ["Für", "Mit", "Bei"], "für + wen (Akkusativ). Mit/bei would need wem (Dativ).",
         {"Mit": "mit takes Dativ: Mit wem …?", "Bei": "bei takes Dativ: Bei wem …?"}),
        ("Für {wen}#W / ist das Geschenk?", ["wen", "wem", "wer"], "für + Akkusativ → wen.",
         {"wem": "wem is Dativ (mit wem?). für takes Akkusativ.", "wer": "wer is Nominativ."}),
        ("Mit {wem}#W / gehst du ins Kino?", ["wem", "wen", "wer"], "mit + Dativ → wem. Compare: für wen (Akkusativ).",
         {"wen": "wen is Akkusativ (für wen?). mit takes Dativ.", "wer": "wer is Nominativ."}),
        ("Das ist ein Geschenk / {für} meine Schwester.#AKK", ["für", "mit", "bei"], "Meaning decides: a present is FOR someone → für + Akkusativ (meine Schwester).",
         {"mit": "mit = with.", "bei": "bei = at someone's place."}),
    ]
    for spec, opts, rule, why in contrast:
        Q("akkpraep", spec, opts, rule, why)


# ---------------------------------------------------------------- comparison
VG_RULE = "Comparative: adjective + <b>-er</b> (+ als). Superlative: <b>am …-sten</b>. Short words with a/o/u often get an umlaut: alt → älter, groß → größer. Irregular: gern – lieber – am liebsten · gut – besser – am besten · viel – mehr – am meisten · hoch – höher – am höchsten."

def vergleich():
    items = [
        ("Ich trinke gern Kaffee, / aber {lieber} Tee.", ["lieber", "gerner", "mehr gern"], {"gerner": "gern is irregular: gern – lieber – am liebsten.", "mehr gern": "German doesn't use 'mehr' to build comparatives. gern → lieber."}),
        ("Am {liebsten}#ADV / trinke ich Saft.", ["liebsten", "gernsten", "lieber"], {"gernsten": "gern is irregular: am liebsten.", "lieber": "After am you need the superlative -sten: am liebsten."}),
        ("Was machst du / {am liebsten}?#ADV", ["am liebsten", "am gernsten", "lieber am"], {"am gernsten": "gern – lieber – am liebsten.", "lieber am": "Superlative = am + liebsten."}),
        ("Ich trinke lieber Tee / {als} Kaffee.", ["als", "wie", "dann"], {"wie": "wie is for equality (so … wie). After a comparative (lieber, größer …) use als.", "dann": "dann = then."}),
        ("Paul ist so groß / {wie} Max.", ["wie", "als", "wann"], {"als": "als comes after a comparative (größer als). With so … wie use wie.", "wann": "wann = when (question word)."}),
        ("Anna ist größer / {als} ihr Bruder.", ["als", "wie", "so"], {"wie": "größer is a comparative → als.", "so": "so … wie is for equality, and so needs the base form."}),
        ("Der Zug ist {schneller}#ADJ / als der Bus.", ["schneller", "schnell", "schnellster"], {"schnell": "Before als you need the comparative: schneller.", "schnellster": "That's a superlative form — and you're comparing two things → schneller."}),
        ("Mein Opa ist {älter}#ADJ / als meine Oma.", ["älter", "alter", "mehr alt"], {"alter": "alt gets an umlaut: älter.", "mehr alt": "German adds -er instead of 'mehr': älter."}),
        ("Berlin ist {größer}#ADJ / als München.", ["größer", "großer", "mehr groß"], {"großer": "groß gets an umlaut: größer.", "mehr groß": "Comparative = -er: größer."}),
        ("Das Wetter ist heute {besser}#ADJ / als gestern.", ["besser", "guter", "mehr gut"], {"guter": "gut is irregular: gut – besser – am besten.", "mehr gut": "gut → besser."}),
        ("Wer spricht / {am besten}#ADV / Deutsch?", ["am besten", "am gutesten", "am bessersten"], {"am gutesten": "gut is irregular: am besten.", "am bessersten": "The superlative is am besten — no double ending."}),
        ("Ich esse {mehr}#ADV / Obst als früher.", ["mehr", "viel", "vieler"], {"viel": "Before als you need the comparative: viel → mehr.", "vieler": "viel is irregular: viel – mehr – am meisten."}),
        ("Wer hat / {am meisten}#ADV / Geld?", ["am meisten", "am vielsten", "am mehrsten"], {"am vielsten": "viel – mehr – am meisten.", "am mehrsten": "viel – mehr – am meisten."}),
        ("Der Mantel ist {teurer}#ADJ / als die Jacke.", ["teurer", "teuerer", "mehr teuer"], {"teuerer": "teuer drops the e: teurer.", "mehr teuer": "Comparative = -er: teurer."}),
        ("Im Winter ist es {kälter}#ADJ / als im Sommer.", ["kälter", "kalter", "mehr kalt"], {"kalter": "kalt gets an umlaut: kälter.", "mehr kalt": "Comparative = -er: kälter."}),
        ("Im Sommer ist es {wärmer}#ADJ / als im Frühling.", ["wärmer", "warmer", "mehr warm"], {"warmer": "warm gets an umlaut: wärmer.", "mehr warm": "Comparative = -er: wärmer."}),
        ("Mein Bruder ist {jünger}#ADJ / als ich.", ["jünger", "junger", "mehr jung"], {"junger": "jung gets an umlaut: jünger.", "mehr jung": "Comparative = -er: jünger."}),
        ("Das Hotel ist {billiger}#ADJ / als die Pension.", ["billiger", "billig", "billigster"], {"billig": "Before als you need the comparative: billiger.", "billigster": "You compare two things → comparative billiger."}),
        ("In der Stadt ist das Fahrrad / {am schnellsten}.#ADV", ["am schnellsten", "am schnellen", "am schneller"], {"am schnellen": "Superlative: am + -sten.", "am schneller": "Superlative: am schnellsten."}),
        ("Mein Handy ist nicht so neu / {wie} dein Handy.", ["wie", "als", "wann"], {"als": "(nicht) so … wie — als only after a comparative.", "wann": "wann = when."}),
        ("Ich spiele lieber Fußball / {als} Tennis.", ["als", "wie", "oder"], {"wie": "lieber is a comparative → als.", "oder": "oder = or. Comparing → als."}),
        ("Er arbeitet {mehr}#ADV / als ich.", ["mehr", "viel", "vieler"], {"viel": "Before als: comparative mehr.", "vieler": "viel – mehr – am meisten."}),
        ("Lisa singt gut, / aber Tom singt {besser}.#ADV", ["besser", "guter", "gutter"], {"guter": "gut – besser – am besten.", "gutter": "gut – besser – am besten."}),
        ("Welche Farbe magst du / {am liebsten}?#ADV", ["am liebsten", "am liebste", "am lieber"], {"am liebste": "The superlative ends in -sten: am liebsten.", "am lieber": "am + superlative: am liebsten."}),
        ("Der Turm ist {höher}#ADJ / als das Haus.", ["höher", "hocher", "hoher"], {"hocher": "hoch is irregular: hoch – höher – am höchsten (the c disappears).", "hoher": "hoch → höher (with umlaut, no c)."}),
        ("Die Wohnung ist {kleiner}#ADJ / als das Haus.", ["kleiner", "kleinerer", "mehr klein"], {"kleinerer": "Just one -er: kleiner.", "mehr klein": "Comparative = -er: kleiner."}),
        ("Heute ist es so kalt / {wie} gestern.", ["wie", "als", "so"], {"als": "so … wie for equality.", "so": "so … wie — the second word is wie."}),
        ("Mein Auto ist {langsamer}#ADJ / als dein Auto.", ["langsamer", "langsammer", "mehr langsam"], {"langsammer": "Just add -er: langsamer.", "mehr langsam": "Comparative = -er."}),
        ("Ich fahre lieber mit dem Fahrrad / {als} mit dem Auto.", ["als", "wie", "denn"], {"wie": "After lieber → als.", "denn": "denn = because."}),
        ("Er läuft {schneller}#ADV / als ich.", ["schneller", "schnell", "am schnellsten"], {"schnell": "Before als: comparative schneller.", "am schnellsten": "The superlative doesn't go with als."}),
        ("Mein Bruder ist genauso alt / {wie} ich.", ["wie", "als", "wann"], {"als": "genauso … wie = just as … as.", "wann": "wann = when."}),
        ("Die Kirche ist {älter}#ADJ / als das Rathaus.", ["älter", "alter", "ältester"], {"alter": "alt gets an umlaut: älter.", "ältester": "Comparing two things → älter."}),
        ("Wer ist / {am ältesten}#ADV / in deiner Familie?", ["am ältesten", "am älter", "am altesten"], {"am älter": "Superlative: am ältesten.", "am altesten": "alt keeps the umlaut: am ältesten."}),
        ("Ich mag Hunde, / aber Katzen mag ich {lieber}.", ["lieber", "mehr gern", "gerner"], {"mehr gern": "gern → lieber.", "gerner": "gern is irregular: lieber."}),
        ("Was isst du lieber, / Fisch {oder} Fleisch?", ["oder", "als", "wie"], {"als": "In a question with two choices you need oder.", "wie": "wie is for equality."}),
    ]
    for spec, opts, why in items:
        Q("vergleich", spec, opts, VG_RULE, why)
    forms = [
        ("gern", "gern – lieber – am liebsten", ["gern – gerner – am gernsten", "gern – mehr gern – am meisten gern"]),
        ("gut", "gut – besser – am besten", ["gut – guter – am gutesten", "gut – besser – am bessersten"]),
        ("viel", "viel – mehr – am meisten", ["viel – vieler – am vielsten", "viel – mehr – am mehrsten"]),
        ("groß", "groß – größer – am größten", ["groß – großer – am großesten", "groß – größer – am größesten"]),
        ("alt", "alt – älter – am ältesten", ["alt – alter – am altesten", "alt – älter – am ältsten"]),
        ("hoch", "hoch – höher – am höchsten", ["hoch – hocher – am hochsten", "hoch – höcher – am höchesten"]),
        ("klein", "klein – kleiner – am kleinsten", ["klein – kleiner – am kleinesten", "klein – mehr klein – am meisten klein"]),
        ("jung", "jung – jünger – am jüngsten", ["jung – junger – am jungsten", "jung – jünger – am jüngesten"]),
    ]
    for adj, corr, wr in forms:
        C("vergleich", f"Comparison of „{adj}“:", corr, wr, VG_RULE, {w: f"Not correct. The forms are: {corr}." for w in wr})
    choose("vergleich", "Which sentence is correct?", "Ich#S / trinke#V / lieber#ADV / Tee.#AKK", ["Ich lieber trinke Tee.", "Ich trinke gerner Tee."],
           "lieber is an adverb after the verb; the verb stays in position 2.",
           {"Ich lieber trinke Tee.": "The verb must be in position 2.", "Ich trinke gerner Tee.": "gern → lieber, not gerner."})
    choose("vergleich", "Which sentence is correct?", "Am liebsten#ADV / esse#V / ich#S / Pizza.#AKK", ["Am liebsten ich esse Pizza.", "Am liebsten ich Pizza esse."],
           "Am liebsten takes position 1 → verb in position 2, subject after it.",
           {"Am liebsten ich esse Pizza.": "After 'Am liebsten' the verb comes next.", "Am liebsten ich Pizza esse.": "The verb never goes to the end in a main clause."})


# ---------------------------------------------------------------- countries, languages, nationalities
LAND_RULE = "Most countries have no article: <i>aus/in Deutschland, nach Spanien</i>. Countries with an article: <b>die Schweiz, die Türkei</b> (in der / in die / aus der), <b>der Iran</b> (im / in den / aus dem), plural <b>die USA, die Niederlande</b> (in den / in die / aus den). With an article you go <b>in</b> + Akkusativ, not nach."

def laender():
    items = [
        ("Mein Kollege kommt / {aus} Italien.#ORT", ["aus", "von", "nach"], {"von": "Origin from a country or city → aus.", "nach": "nach = to (direction)."}),
        ("Wir fahren im Sommer / {nach} Spanien.#ORT", ["nach", "in", "zu"], {"in": "Countries without an article: nach Spanien (direction).", "zu": "zu is for people and places in town, not countries."}),
        ("Ich wohne / {in} Deutschland.#ORT", ["in", "nach", "aus"], {"nach": "nach = to (movement). Wo? → in.", "aus": "aus = from (origin)."}),
        ("Sie kommt / {aus der} Türkei.#ORT", ["aus der", "aus", "aus die"], {"aus": "die Türkei has an article → aus der Türkei.", "aus die": "aus takes Dativ: die → der."}),
        ("Wir fahren / {in die} Schweiz.#ORT", ["in die", "nach", "in der"], {"nach": "Countries with an article: in + Akkusativ → in die Schweiz.", "in der": "in der = Wo? (Dativ). For direction use Akkusativ: in die."}),
        ("Er wohnt / {in der} Schweiz.#ORT", ["in der", "in die", "in"], {"in die": "in die = Wohin? (movement). Wo? → in der Schweiz.", "in": "die Schweiz needs its article: in der Schweiz."}),
        ("Meine Tante lebt / {in den} USA.#ORT", ["in den", "in die", "in"], {"in die": "in die USA = direction. Wo? → Dativ plural: in den USA.", "in": "die USA (plural) needs its article: in den USA."}),
        ("Ich fliege / {in die} USA.#ORT", ["in die", "nach", "in den"], {"nach": "With an article: in + Akkusativ → in die USA.", "in den": "in den USA = Wo? (Dativ). Direction → in die."}),
        ("Er kommt / {aus dem} Iran.#ORT", ["aus dem", "aus", "aus den"], {"aus": "der Iran has an article → aus dem Iran.", "aus den": "der Iran is singular → aus dem."}),
        ("Wir fahren / {in die} Niederlande.#ORT", ["in die", "nach", "in den"], {"nach": "die Niederlande (plural, with article) → in die Niederlande.", "in den": "in den = Wo? (Dativ plural). Direction → in die."}),
        ("Sie wohnt / {in den} Niederlanden.#ORT", ["in den", "in die", "in der"], {"in die": "Wo? → Dativ plural: in den Niederlanden.", "in der": "die Niederlande is plural → in den."}),
        ("Ich komme / {aus den} USA.#ORT", ["aus den", "aus die", "aus"], {"aus die": "aus + Dativ: die USA → aus den USA.", "aus": "die USA needs its article."}),
        ("Wir fahren / {nach} Österreich.#ORT", ["nach", "in", "zu"], {"in": "Direction to a country without article → nach.", "zu": "zu isn't used with countries."}),
        ("Lisa wohnt / {in} Wien.#ORT", ["in", "nach", "zu"], {"nach": "nach = to (movement). Wo? → in.", "zu": "zu = to (a person/place)."}),
        ("Ich fahre morgen / {nach} Hamburg.#ORT", ["nach", "in", "zu"], {"in": "Direction to a city → nach.", "zu": "Cities take nach."}),
        ("Ich war letztes Jahr / {in der} Türkei.#ORT", ["in der", "in die", "nach"], {"in die": "war = Wo? → Dativ: in der Türkei.", "nach": "nach = to. And die Türkei needs in + article."}),
        ("Wir machen Urlaub / {in} Italien.#ORT", ["in", "nach", "zu"], {"nach": "Urlaub machen = Wo? → in Italien.", "zu": "zu isn't used with countries."}),
        ("Ich komme / {aus} Berlin, / aber ich wohne in München.", ["aus", "von", "in"], {"von": "Origin (city/country) → aus.", "in": "in = where you are now. Origin → aus."}),
        ("Wo liegt Hamburg? – / {Im} Norden / von Deutschland.#ORT", ["Im", "In", "Am"], {"In": "der Norden has an article → im (in dem) Norden.", "Am": "am is for days/dates. Compass directions: im Norden, im Süden …"}),
        ("München liegt / {im} Süden.#ORT", ["im", "am", "in"], {"am": "Compass directions: im Süden.", "in": "der Süden needs its article: im Süden."}),
        ("Er fährt zu seiner Familie / {nach} Polen.#ORT", ["nach", "in", "zu"], {"in": "Direction, country without article → nach.", "zu": "zu seiner Familie is already there — the country takes nach."}),
        ("Ich bin / {in} Kanada / geboren.", ["in", "aus", "nach"], {"aus": "geboren in = born in.", "nach": "nach = to."}),
        ("{Die} Schweiz#S / ist sehr schön.", ["Die", "Der", "Das"], {"Der": "It's die Schweiz.", "Das": "It's die Schweiz."}),
        ("{Die} USA#S / sind sehr groß.", ["Die", "Der", "Das"], {"Der": "die USA is plural.", "Das": "die USA is plural (sind)."}),
        ("{Woher}#W / kommen Sie? – Aus Polen.", ["Woher", "Wo", "Wohin"], {"Wo": "Wo asks for a position. The answer 'Aus Polen' → Woher.", "Wohin": "Wohin asks for a direction (nach …)."}),
    ]
    for spec, opts, why in items:
        Q("laender", spec, opts, LAND_RULE, why)

    nat = [
        ("Ben kommt aus Deutschland. / Er ist {Deutscher}.", "", ["Deutscher", "Deutsch", "Deutschländer"], "A German man: Er ist Deutscher. A German woman: Sie ist Deutsche.",
         {"Deutsch": "Deutsch (capital D) is the language.", "Deutschländer": "Not a word."}),
        ("Anna kommt aus Deutschland. / Sie ist {Deutsche}.", "", ["Deutsche", "Deutscherin", "Deutsch"], "A German woman: Sie ist Deutsche (no -in).",
         {"Deutscherin": "Deutsch is special: der Deutsche / die Deutsche — no -in.", "Deutsch": "Deutsch is the language."}),
        ("Raj kommt aus Indien. / Er ist {Inder}.", "", ["Inder", "Indier", "Indisch"], "Indien → der Inder, die Inderin. Language: Hindi (and many more).",
         {"Indier": "The nationality is Inder.", "Indisch": "indisch is the adjective (indisches Essen)."}),
        ("Priya kommt aus Indien. / Sie ist {Inderin}.", "", ["Inderin", "Inder", "Indisch"], "Women: nationality + -in → Inderin.",
         {"Inder": "Inder is the man. A woman → Inderin.", "Indisch": "indisch is an adjective."}),
        ("Carlos kommt aus Spanien. / Er ist {Spanier}.", "", ["Spanier", "Spanisch", "Spaner"], "Spanien → der Spanier, die Spanierin, language: Spanisch.",
         {"Spanisch": "Spanisch is the language.", "Spaner": "The nationality is Spanier."}),
        ("Maria kommt aus Spanien. / Sie ist {Spanierin}.", "", ["Spanierin", "Spanier", "Spanisch"], "A Spanish woman → Spanierin.",
         {"Spanier": "Spanier is a man.", "Spanisch": "Spanisch is the language."}),
        ("Marco kommt aus Italien. / Er ist {Italiener}.", "", ["Italiener", "Italienisch", "Italier"], "Italien → der Italiener, die Italienerin, language: Italienisch.",
         {"Italienisch": "Italienisch is the language.", "Italier": "The nationality is Italiener."}),
        ("Giulia kommt aus Italien. / Sie ist {Italienerin}.", "", ["Italienerin", "Italiener", "Italienisch"], "An Italian woman → Italienerin.",
         {"Italiener": "Italiener is a man.", "Italienisch": "Italienisch is the language."}),
        ("Pierre kommt aus Frankreich. / Er ist {Franzose}.", "", ["Franzose", "Französer", "Französisch"], "Frankreich → der Franzose, die Französin, language: Französisch.",
         {"Französer": "The nationality is Franzose.", "Französisch": "Französisch is the language."}),
        ("Claire kommt aus Frankreich. / Sie ist {Französin}.", "", ["Französin", "Franzosin", "Französisch"], "A French woman → Französin (with ö).",
         {"Franzosin": "With umlaut: Französin.", "Französisch": "Französisch is the language."}),
        ("Mehmet kommt aus der Türkei. / Er ist {Türke}.", "", ["Türke", "Türker", "Türkisch"], "die Türkei → der Türke, die Türkin, language: Türkisch.",
         {"Türker": "The nationality is Türke.", "Türkisch": "Türkisch is the language."}),
        ("Ayşe kommt aus der Türkei. / Sie ist {Türkin}.", "", ["Türkin", "Türkerin", "Türkisch"], "A Turkish woman → Türkin.",
         {"Türkerin": "The nationality is Türkin.", "Türkisch": "Türkisch is the language."}),
        ("John kommt aus England. / Er ist {Engländer}.", "", ["Engländer", "Englisch", "Engländerin"], "England → der Engländer, die Engländerin, language: Englisch.",
         {"Englisch": "Englisch is the language.", "Engländerin": "Engländerin is a woman."}),
        ("Emma kommt aus England. / Sie ist {Engländerin}.", "", ["Engländerin", "Engländer", "Englisch"], "An English woman → Engländerin.",
         {"Engländer": "Engländer is a man.", "Englisch": "Englisch is the language."}),
    ]
    for spec, _, opts, rule, why in nat:
        Q("laender", spec, opts, rule + " Nationalities after sein have no article: Er ist Spanier.", why)

    lang = [
        ("In Spanien spricht man / {Spanisch}.#AKK", ["Spanisch", "Spanier", "Spanien"], {"Spanier": "Spanier is a person.", "Spanien": "Spanien is the country."}),
        ("In Frankreich spricht man / {Französisch}.#AKK", ["Französisch", "Franzose", "Frankreich"], {"Franzose": "Franzose is a person.", "Frankreich": "Frankreich is the country."}),
        ("In Österreich spricht man / {Deutsch}.#AKK", ["Deutsch", "Deutscher", "Österreicher"], {"Deutscher": "Deutscher is a person.", "Österreicher": "Österreicher is a person from Austria."}),
        ("In der Türkei spricht man / {Türkisch}.#AKK", ["Türkisch", "Türke", "Türkei"], {"Türke": "Türke is a person.", "Türkei": "die Türkei is the country."}),
        ("In Italien spricht man / {Italienisch}.#AKK", ["Italienisch", "Italiener", "Italien"], {"Italiener": "Italiener is a person.", "Italien": "Italien is the country."}),
        ("In Brasilien spricht man / {Portugiesisch}.#AKK", ["Portugiesisch", "Spanisch", "Brasilien"], {"Spanisch": "Brazil's language is Portuguese.", "Brasilien": "Brasilien is the country."}),
    ]
    for spec, opts, why in lang:
        Q("laender", spec, opts, "Languages end in -isch (Spanisch, Englisch) — except Deutsch. People: der Spanier / die Spanierin. Country: Spanien.", why)

    caps = [
        ("Die Hauptstadt von Deutschland ist / {Berlin}.", ["Berlin", "München", "Hamburg"]),
        ("Die Hauptstadt von Österreich ist / {Wien}.", ["Wien", "Salzburg", "Graz"]),
        ("Die Hauptstadt der Schweiz ist / {Bern}.", ["Bern", "Zürich", "Genf"]),
    ]
    for spec, opts in caps:
        Q("laender", spec, opts, "D-A-CH capitals: Berlin (Deutschland), Wien (Österreich), Bern (die Schweiz).", {o: f"{o} is a big city, but not the capital." for o in opts[1:]})
    choose("laender", "Which sentence is correct?", "Deutschland#S / liegt#V / in Europa.#ORT", ["Das Deutschland liegt in Europa.", "Der Deutschland liegt in Europa."],
           "Most countries (Deutschland, Spanien, Indien …) are used without an article.",
           {"Das Deutschland liegt in Europa.": "No article with Deutschland.", "Der Deutschland liegt in Europa.": "No article with Deutschland."})


# ---------------------------------------------------------------- Dativ possessives
POSS_RULE = "Possessive articles in the Dativ take the same endings as ein: <b>-em</b> (der/das: meinem Bruder) · <b>-er</b> (die: meiner Mutter) · <b>-en</b> + noun -n (plural: meinen Kindern). euer → eurem / eurer / euren."
BASES = ("mein", "dein", "sein", "ihr", "Ihr", "unser", "euer")

def poss_dativ():
    items = [
        ("Ich gehe / mit {meinem} Bruder / ins Kino.", ["meinem", "meinen", "meiner"], "mit", "der Bruder"),
        ("Ich wohne / bei {meiner} Mutter.#DAT", ["meiner", "meinem", "meine"], "bei", "die Mutter"),
        ("Wir spielen / mit {unseren} Kindern.#DAT", ["unseren", "unserem", "unsere"], "mit", "die Kinder (plural)"),
        ("Er geht / zu {seiner} Freundin.#DAT", ["seiner", "seinem", "seine"], "zu", "die Freundin"),
        ("Das Buch ist / von {eurem} Lehrer.#DAT", ["eurem", "euren", "euer"], "von", "der Lehrer"),
        ("Das Auto / gehört / {deinem} Vater.#DAT", ["deinem", "deinen", "deiner"], "gehören", "der Vater"),
        ("Sie telefoniert / mit {ihrer} Schwester.#DAT", ["ihrer", "ihrem", "ihre"], "mit", "die Schwester"),
        ("Ich helfe / {meiner} Oma.#DAT", ["meiner", "meine", "meinem"], "helfen", "die Oma"),
        ("Wir fahren / mit {unserem} Auto.#DAT", ["unserem", "unseren", "unser"], "mit", "das Auto"),
        ("Kommst du / mit {deiner} Familie?#DAT", ["deiner", "deinem", "deine"], "mit", "die Familie"),
        ("Er wohnt / bei {seinen} Eltern.#DAT", ["seinen", "seinem", "seine"], "bei", "die Eltern (plural)"),
        ("Wie geht es / {Ihrer} Frau?#DAT", ["Ihrer", "Ihre", "Ihrem"], "Wie geht es …?", "die Frau"),
        ("Ich gebe / {meinem} Sohn / das Geld.", ["meinem", "meinen", "meiner"], "geben (to someone)", "der Sohn"),
        ("Sie schreibt / {ihrem} Freund / eine E-Mail.", ["ihrem", "ihren", "ihrer"], "schreiben (to someone)", "der Freund"),
        ("Gehört das Handy / {eurer} Tochter?#DAT", ["eurer", "eurem", "eure"], "gehören", "die Tochter"),
        ("Ich spreche / mit {unserem} Chef.#DAT", ["unserem", "unseren", "unser"], "mit", "der Chef"),
        ("Seit {meinem} Urlaub#ZEIT / bin ich fit.", ["meinem", "meinen", "meiner"], "seit", "der Urlaub"),
        ("Wir essen / bei {unserer} Tante.#DAT", ["unserer", "unserem", "unsere"], "bei", "die Tante"),
        ("Er kommt / aus {seinem} Büro.#DAT", ["seinem", "seinen", "seiner"], "aus", "das Büro"),
        ("Ich fahre / mit {meinem} Fahrrad.#DAT", ["meinem", "meinen", "mein"], "mit", "das Fahrrad"),
        ("Die Tasche / gehört / {meiner} Kollegin.#DAT", ["meiner", "meinem", "meine"], "gehören", "die Kollegin"),
        ("Sprecht ihr / mit {euren} Nachbarn?#DAT", ["euren", "eurem", "eure"], "mit", "die Nachbarn (plural)"),
        ("Sie spielt / mit {ihrem} Hund.#DAT", ["ihrem", "ihren", "ihr"], "mit", "der Hund"),
        ("Wir gratulieren / {unserem} Opa.#DAT", ["unserem", "unseren", "unser"], "gratulieren", "der Opa"),
        ("Er wohnt / mit {seiner} Frau / in Köln.", ["seiner", "seine", "seinem"], "mit", "die Frau"),
        ("Was schenkst du / {deiner} Schwester?#DAT", ["deiner", "deine", "deinem"], "schenken (to someone)", "die Schwester"),
        ("Das Foto ist / von {meinen} Großeltern.#DAT", ["meinen", "meinem", "meine"], "von", "die Großeltern (plural)"),
        ("Ich gehe / mit {meinen} Freunden / ins Café.", ["meinen", "meinem", "meine"], "mit", "die Freunde (plural)"),
        ("Bist du zufrieden / mit {deinem} Job?#DAT", ["deinem", "deinen", "deiner"], "mit", "der Job"),
        ("Ich danke / {Ihrem} Team.#DAT", ["Ihrem", "Ihren", "Ihr"], "danken", "das Team"),
    ]
    for spec, opts, trig, noun in items:
        corr = opts[0]
        why = {}
        for w in opts[1:]:
            if w in BASES: why[w] = f"No ending = Nominativ (der/das). {trig} needs the Dativ → {corr}."
            elif w.endswith("em"): why[w] = f"-em is Dativ for der/das nouns. {noun} → {corr}."
            elif w.endswith("er") and w not in BASES: why[w] = f"-er is Dativ for die nouns. {noun} → {corr}."
            elif w.endswith("en"): why[w] = f"-en is masculine Akkusativ (or Dativ plural). {noun} in the Dativ → {corr}."
            elif w.endswith("e"): why[w] = f"-e is Nominativ/Akkusativ (die or plural). {trig} needs the Dativ → {corr}."
            else: why[w] = f"{noun} → {corr}."
        Q("poss", spec, opts, f"{trig} + Dativ: {noun} → {corr}. " + POSS_RULE, why)


# ---------------------------------------------------------------- ja / nein / doch
JND_RULE = "<b>ja</b> = yes to a positive question · <b>nein</b> = no · <b>doch</b> = YES to a <b>negative</b> question (one with nicht/kein): <i>Kommst du nicht? – Doch!</i>"

def janein_doch():
    items = [
        ("Kommst du heute nicht mit?", "{Doch}, ich komme mit.", ["Doch", "Ja", "Nein"]),
        ("Hast du keine Zeit?", "{Doch}, ich habe Zeit.", ["Doch", "Ja", "Nein"]),
        ("Hast du keine Zeit?", "{Nein}, ich habe keine Zeit.", ["Nein", "Doch", "Kein"]),
        ("Kommst du mit?", "{Ja}, ich komme mit.", ["Ja", "Doch", "Nein"]),
        ("Sprichst du Deutsch?", "{Ja}, ein bisschen.", ["Ja", "Doch", "Nein"]),
        ("Bist du denn nicht müde?", "{Doch}, ich bin sehr müde.", ["Doch", "Ja", "Nein"]),
        ("Bist du nicht müde?", "{Nein}, ich bin nicht müde.", ["Nein", "Doch", "Nicht"]),
        ("Magst du keinen Kaffee?", "{Doch}, ich trinke gern Kaffee.", ["Doch", "Ja", "Nein"]),
        ("Wohnst du nicht in Berlin?", "{Nein}, ich wohne in Hamburg.", ["Nein", "Doch", "Nicht"]),
        ("Arbeitest du heute?", "{Nein}, ich habe heute frei.", ["Nein", "Doch", "Ja"]),
        ("Hast du kein Auto?", "{Doch}, ich habe ein Auto.", ["Doch", "Ja", "Nein"]),
        ("Ist das nicht dein Handy?", "{Doch}, das ist mein Handy.", ["Doch", "Ja", "Nein"]),
        ("Ist das dein Handy?", "{Ja}, das ist mein Handy.", ["Ja", "Doch", "Nein"]),
        ("Gehst du nicht zur Party?", "{Doch}, ich gehe hin.", ["Doch", "Ja", "Nein"]),
        ("Kannst du nicht schwimmen?", "{Doch}, ich kann gut schwimmen.", ["Doch", "Ja", "Nein"]),
        ("Hast du Hunger?", "{Nein}, ich habe keinen Hunger.", ["Nein", "Doch", "Kein"]),
    ]
    for q, a, opts in items:
        corr = opts[0]
        neg = " nicht" in " " + q or " kein" in q
        why = {}
        for w in opts[1:]:
            if w == "Ja": why[w] = ("The question is negative (nicht/kein). To say YES to a negative question German uses doch, not ja." if corr == "Doch" else "ja would be a 'yes' — but the answer that follows is negative → nein.")
            elif w == "Doch": why[w] = ("doch contradicts a negative question — but the answer agrees: it's negative → nein." if neg else "doch is only for answering a NEGATIVE question. This question is positive.")
            elif w == "Nein": why[w] = "nein would be a 'no' — but the answer that follows is positive."
            else: why[w] = f"'{w}' isn't an answer word. Use ja, nein or doch."
        Q("janein", [[q + " –", ""], [a, ""]], opts, JND_RULE, why)


# ---------------------------------------------------------------- sein & haben
PERS = {"bin": "ich", "bist": "du", "ist": "er/sie/es", "sind": "wir / sie / Sie", "seid": "ihr",
        "habe": "ich", "hast": "du", "hat": "er/sie/es", "haben": "wir / sie / Sie", "habt": "ihr"}
SEINF = {"bin", "bist", "ist", "sind", "seid"}

def sein_haben_more():
    items = [
        ("Ich {bin} 30 Jahre alt.", ["bin", "habe", "ist"], "Age uses sein: Ich bin 30 (Jahre alt)."),
        ("{Bist} du müde?", ["Bist", "Hast", "Ist"], "Feelings/states with adjectives → sein: müde, krank, glücklich."),
        ("Er {ist} krank.", ["ist", "hat", "bist"], "sein + adjective: krank, müde, verheiratet."),
        ("Wir {sind} verheiratet.", ["sind", "haben", "seid"], "Family status uses sein: verheiratet, ledig, geschieden."),
        ("Ihr {seid} sehr nett.", ["seid", "seit", "sind"], "sein + adjective."),
        ("Meine Eltern {sind} im Urlaub.", ["sind", "haben", "ist"], "Where someone is → sein."),
        ("Herr Weber {ist} Lehrer.", ["ist", "hat", "sind"], "Jobs: sein + job, no article: Er ist Lehrer."),
        ("Das {ist} mein Bruder.", ["ist", "sind", "hat"], "Das ist + one person/thing."),
        ("Das {sind} meine Kinder.", ["sind", "ist", "haben"], "Das sind + plural."),
        ("Wo {seid} ihr?", ["seid", "sind", "habt"], "sein: ihr seid."),
        ("Ich {bin} ledig.", ["bin", "habe", "ist"], "Family status uses sein."),
        ("Heute {ist} es kalt.", ["ist", "hat", "sind"], "Weather: es ist kalt / warm / sonnig."),
        ("Tom und Lisa {sind} aus Polen.", ["sind", "ist", "seid"], "Two people = plural → sind."),
        ("Ich {habe} Durst.", ["habe", "bin", "hast"], "Hunger, Durst, Zeit, Fieber, Kopfschmerzen are nouns → haben."),
        ("Er {hat} Kopfschmerzen.", ["hat", "ist", "habt"], "Pain/illness as a noun → haben: Kopfschmerzen, Fieber, eine Erkältung."),
        ("{Hast} du morgen Zeit?", ["Hast", "Bist", "Habst"], "Zeit haben = to have time."),
        ("Wir {haben} keine Kinder.", ["haben", "sind", "habt"], "haben + Akkusativ."),
        ("Ihr {habt} Glück!", ["habt", "seid", "haben"], "Glück haben = to be lucky."),
        ("Meine Eltern {haben} ein Haus in Spanien.", ["haben", "sind", "hat"], "haben + Akkusativ: ein Haus."),
        ("Anna {hat} Fieber.", ["hat", "ist", "habt"], "Fieber haben."),
        ("Ich {habe} Angst vor Hunden.", ["habe", "bin", "hat"], "Angst haben = to be afraid."),
        ("Du {hast} recht.", ["hast", "bist", "habst"], "recht haben = to be right."),
        ("Heute {habe} ich Geburtstag.", ["habe", "bin", "hat"], "Geburtstag haben = to have one's birthday."),
        ("Sie {ist} sehr glücklich.", ["ist", "hat", "sind"], "sein + adjective."),
        ("Mein Sohn {hat} eine Erkältung.", ["hat", "ist", "haben"], "eine Erkältung haben (a cold)."),
        ("Wir {haben} Urlaub.", ["haben", "sind", "habt"], "Urlaub haben = to be on holiday."),
        ("Ich {bin} Student.", ["bin", "habe", "ist"], "Job/status: Ich bin Student (no article)."),
        ("Er {hat} einen Bruder.", ["hat", "ist", "habt"], "haben + Akkusativ: einen Bruder."),
        ("Das Zimmer {hat} einen Balkon.", ["hat", "ist", "sind"], "haben + Akkusativ: einen Balkon."),
        ("Die Wohnung {ist} hell.", ["ist", "hat", "sind"], "sein + adjective."),
        ("Bist du verheiratet? – Nein, ich {bin} geschieden.", ["bin", "habe", "ist"], "Family status uses sein."),
        ("Wie alt {bist} du?", ["bist", "hast", "ist"], "Age: Wie alt bist du?"),
        ("Ihr {seid} heute so still.", ["seid", "habt", "sind"], "sein + adjective."),
    ]
    for spec, opts, reason in items:
        corr = opts[0].lower()
        why = {}
        for w in opts[1:]:
            wl = w.lower()
            if wl == "seit": why[w] = "seit (with t) is a preposition meaning 'since'. ihr seid (with d)."
            elif wl == "habst": why[w] = "haben drops the b: du hast."
            elif (wl in SEINF) != (corr in SEINF): why[w] = f"'{w}' is a form of {'sein' if wl in SEINF else 'haben'}. {reason}"
            else: why[w] = f"'{w}' is the {PERS[wl]}-form. Here you need '{opts[0]}'."
        Q("seinhaben", [[spec, ""]], opts, reason + " sein: bin, bist, ist, sind, seid, sind · haben: habe, hast, hat, haben, habt, haben.", why)
    C("seinhaben", "You feel cold. You say:", "Mir ist kalt.", ["Ich habe kalt.", "Ich bin kalt."],
      "Feeling cold/warm: Mir ist kalt / warm (Dativ). 'Ich bin kalt' means you are a cold (unfriendly) person.",
      {"Ich habe kalt.": "German doesn't use haben here: Mir ist kalt.", "Ich bin kalt.": "That means 'I am a cold person'. Mir ist kalt = I feel cold."})
    choose("seinhaben", "Which sentence is correct?", "Ich#S / bin#V / 30 Jahre alt.#ADJ", ["Ich habe 30 Jahre.", "Ich habe 30 Jahre alt."],
           "Age uses sein: Ich bin 30 Jahre alt (or: Ich bin 30).",
           {"Ich habe 30 Jahre.": "Unlike Spanish/French, German uses sein for age.", "Ich habe 30 Jahre alt.": "Age uses sein: Ich bin … Jahre alt."})


# ---------------------------------------------------------------- time prepositions
ZP_WHY = {"um": "um is only for clock times.", "am": "am is for days, dates, parts of the day and Wochenende.", "im": "im is for months, seasons and im Jahr ….",
          "in der": "in der is only used with die Nacht.", "in": "Months/seasons need the article: im (= in dem).", "ab": "ab = from … on.", "seit": "seit = since (still going on).",
          "vor": "vor = before / ago."}
ZP_RULE = "<b>um</b> + clock time · <b>am</b> + day, date, part of the day, Wochenende · <b>im</b> + month, season, im Jahr … · <b>in der</b> Nacht · <b>von … bis</b> · <b>ab</b> = from … on · <b>gegen</b> = about. Years alone take no preposition: <i>Ich bin 1995 geboren.</i>"

def zeitpraep_more():
    items = [
        "Ich stehe {um} 6 Uhr auf.|um,am,im", "{Am} Dienstag habe ich Deutschkurs.|Am,Um,Im", "{Am} Morgen trinke ich Kaffee.|Am,Im,Um",
        "{Am} Nachmittag gehe ich spazieren.|Am,Im,Um", "{Am} Mittag esse ich in der Kantine.|Am,Um,Im", "Ich arbeite oft {in der} Nacht.|in der,am,im",
        "Wir fahren {im} August in Urlaub.|im,am,um", "{Im} Herbst regnet es oft.|Im,Am,In", "Mein Sohn ist {im} Januar geboren.|im,am,um",
        "Die Party ist {am} Samstag.|am,im,um", "Der Film beginnt {um} Viertel nach acht.|um,am,im", "Wir treffen uns {am} 3. Oktober.|am,im,um",
        "{Im} Jahr 2020 bin ich nach Deutschland gekommen.|Im,In,Am", "Was machst du {am} Wochenende?|am,im,um", "Ich rufe dich {am} Abend an.|am,im,um",
        "{Um} wie viel Uhr beginnt der Kurs?|Um,Am,Im", "Der Arzt hat {am} Mittwochnachmittag geschlossen.|am,im,um", "{Im} Dezember ist Weihnachten.|Im,Am,Um",
        "Ich habe {im} März Urlaub.|im,am,um", "Der Unterricht endet {um} 12:30 Uhr.|um,am,im", "{Am} Freitagabend gehe ich aus.|Am,Im,Um",
        "Wir frühstücken {am} Sonntag zusammen.|am,im,um", "{Im} Sommer 2023 war ich in Italien.|Im,Am,In", "Wann hast du Geburtstag? – {Im} April.|Im,Am,Um",
        "Wann hast du Geburtstag? – {Am} 12. April.|Am,Im,Um", "Wann kommt der Bus? – {Um} 8:10 Uhr.|Um,Am,Im", "Die Geschäfte sind {am} Sonntag geschlossen.|am,im,um",
        "Der Supermarkt ist {ab} 7 Uhr geöffnet.|ab,seit,vor", "Ich komme {gegen} 8 Uhr – nicht genau um 8.|gegen,um,am",
    ]
    for line in items:
        spec, opts = line.split("|")
        opts = opts.split(",")
        why = {}
        for w in opts[1:]:
            k = w.lower()
            if opts[0] == "gegen" and k == "um": why[w] = "um = exactly at. The sentence says 'not exactly at 8' → gegen (about)."
            else: why[w] = ZP_WHY.get(k, "")
        Q("zeitpraep", [[spec, "ZEIT"]], opts, ZP_RULE, why)
    for spec, prompt, corr, wr in [
        ("Ich arbeite {von} Montag {bis} Freitag.", "Ich arbeite ___ Montag ___ Freitag.", "von … bis", ["am … bis", "um … bis"]),
        ("Das Geschäft ist {von} 9 {bis} 18 Uhr geöffnet.", "Das Geschäft ist ___ 9 ___ 18 Uhr geöffnet.", "von … bis", ["um … bis", "ab … um"]),
        ("Ich lerne jeden Tag {von} 7 {bis} 8 Uhr.", "Ich lerne jeden Tag ___ 7 ___ 8 Uhr.", "von … bis", ["um … um", "am … bis"]),
        ("Der Termin ist {am} Donnerstag {um} 10 Uhr.", "Der Termin ist ___ Donnerstag ___ 10 Uhr.", "am … um", ["um … am", "im … um"]),
    ]:
        add("zeitpraep", [[spec, "ZEIT"]], [corr] + wr, ZP_RULE,
            {w: ("A time span = von … bis." if corr == "von … bis" else "Day → am, clock time → um.") for w in wr}, prompt=prompt)
    choose("zeitpraep", "Which sentence is correct?", "Ich#S / bin#V / 1995#ZEIT / geboren.#P2", ["Ich bin in 1995 geboren.", "Ich bin am 1995 geboren."],
           "A year on its own takes no preposition: 1995. Or: im Jahr 1995.",
           {"Ich bin in 1995 geboren.": "'in 1995' is English. German: 1995 or im Jahr 1995.", "Ich bin am 1995 geboren.": "am is for days and dates, not years."})


def run():
    akkpraep(); vergleich(); laender(); poss_dativ(); janein_doch(); sein_haben_more(); zeitpraep_more()
