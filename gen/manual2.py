"""More hand-written questions (second batch) for topics that don't template well.
Same spec format as manual.py: segments separated by ' / ', each 'text#LABEL'. {answer} marks the gap."""
from .core import add, choose


def G(t, spec, opts, rule, why):
    add(t, spec, opts, rule, why)


def S(t, text, lab, opts, rule, why):
    """Gap question that is a single labelled segment."""
    add(t, [[text, lab]], opts, rule, why)


def C(t, prompt, spec, wrong, rule):
    """Word-order question: wrong is a list of (sentence, why)."""
    choose(t, prompt, spec, [w for w, _ in wrong], rule, {w: y for w, y in wrong})


WHY_W = {
 "Wo": "Wo asks for a position (In München). ", "Woher": "Woher asks for an origin (Aus Indien). ", "Wohin": "Wohin asks for a direction (Nach Berlin). ",
 "Wann": "Wann asks for a point in time (um 9 Uhr). ", "Wie lange": "Wie lange asks for a duration (zwei Stunden). ", "Wie oft": "Wie oft asks how often (zweimal pro Woche). ",
 "Wie viel": "Wie viel is for prices, the time and things you can't count. ", "Wie viele": "Wie viele is for countable plurals. ",
 "Wer": "Wer asks for the subject (Nominativ). ", "Wen": "Wen = Akkusativ (whom). ", "Wem": "Wem = Dativ (to whom). ",
 "Was": "Was asks for a thing/activity. ", "Wie": "Wie asks how. ", "Wie alt": "Wie alt asks for age. ",
 "Welcher": "welcher is for der-nouns. ", "Welche": "welche is for die-nouns and the plural. ", "Welches": "welches is for das-nouns. ",
 "Was für ein": "was für ein asks what kind of (der/das). ", "Was für eine": "was für eine is for die-nouns. ", "Warum": "Warum asks why. ",
}


def wfragen():
    W = [
     ("{Wo}#W / ist#V / die Toilette?#S", ["Wo", "Wohin", "Woher"], "Wo = where (position).", "Da hinten links."),
     ("{Woher}#W / kommt#V / Frau Kaya?#S", ["Woher", "Wo", "Wohin"], "Woher = where from → answer with aus.", "Aus der Türkei."),
     ("{Wohin}#W / geht#V / ihr#S / heute Abend?#ZEIT", ["Wohin", "Wo", "Woher"], "Wohin = where to → in + Akkusativ (ins Kino).", "Ins Kino."),
     ("{Wann}#W / hast#V / du#S / Geburtstag?#AKK", ["Wann", "Wie lange", "Wo"], "Wann = when (a point in time).", "Am 3. Mai."),
     ("{Wie lange}#W / wohnst#V / du#S / schon hier?#ORT", ["Wie lange", "Wann", "Wie oft"], "Wie lange = how long (duration).", "Seit zwei Jahren."),
     ("{Wie oft}#W / spielt#V / ihr#S / Fußball?#AKK", ["Wie oft", "Wie lange", "Wann"], "Wie oft = how often.", "Zweimal pro Woche."),
     ("{Wer}#W / kommt#V / heute#ZEIT / zur Party?#ORT", ["Wer", "Wen", "Wem"], "Wer = who (the subject).", "Paul und Lisa."),
     ("{Wen}#W / fragst#V / du?#S", ["Wen", "Wem", "Wer"], "fragen + Akkusativ → Wen?", "Den Lehrer."),
     ("{Wem}#W / gibst#V / du#S / das Geschenk?#AKK", ["Wem", "Wen", "Wer"], "The receiver is Dativ → Wem?", "Meiner Schwester."),
     ("{Was}#W / trinkst#V / du?#S", ["Was", "Wer", "Wie"], "Was = what.", "Einen Tee."),
     ("{Wie}#W / geht#V / es#S / dir?#DAT", ["Wie", "Was", "Wo"], "Wie geht es dir? = How are you?", "Gut, danke."),
     ("{Wie viel}#W / kosten#V / die Äpfel?#S", ["Wie viel", "Wie viele", "Was"], "Price → wie viel.", "2 Euro das Kilo."),
     ("{Wie viele}#W / Kinder#AKK / haben#V / Sie?#S", ["Wie viele", "Wie viel", "Wie oft"], "Countable plural → wie viele.", "Drei."),
     ("{Warum}#W / kommst#V / du#S / nicht?#NEG", ["Warum", "Wann", "Wie"], "Warum = why.", "Ich bin krank."),
     ("{Welcher}#W / Bus#S / fährt#V / zum Bahnhof?#ORT", ["Welcher", "Welche", "Welches"], "welch- = which; der Bus → welcher.", "Die Linie 58."),
     ("{Welches}#W / Buch#AKK / liest#V / du?#S", ["Welches", "Welcher", "Welche"], "welch- = which; das Buch → welches.", "Harry Potter."),
     ("{Wie alt}#W / ist#V / dein Sohn?#S", ["Wie alt", "Wie viel", "Wie lange"], "Age → Wie alt?", "Sechs."),
     ("{Was für ein}#W / Auto#AKK / hast#V / du?#S", ["Was für ein", "Was für eine", "Welcher"], "was für ein = what kind of; das Auto → ein.", "Einen VW Golf."),
     ("{Wo}#W / arbeitet#V / deine Frau?#S", ["Wo", "Wohin", "Wann"], "Wo = where (position).", "Im Krankenhaus."),
     ("{Wohin}#W / fliegt#V / ihr#S / im Sommer?#ZEIT", ["Wohin", "Wo", "Woher"], "Wohin = where to.", "Nach Portugal."),
     ("{Woher}#W / kennst#V / du#S / Tom?#AKK", ["Woher", "Wo", "Wann"], "Woher kennst du …? = How (from where) do you know …?", "Aus dem Deutschkurs."),
     ("{Wann}#W / fährt#V / der Zug#S / ab?#PRE", ["Wann", "Wie lange", "Wohin"], "Wann = when.", "Um 10.15 Uhr."),
     ("{Wie lange}#W / dauert#V / die Fahrt?#S", ["Wie lange", "Wann", "Wie oft"], "dauern + Wie lange? (duration).", "Drei Stunden."),
     ("{Was}#W / ist#V / dein Beruf?#S", ["Was", "Wer", "Wie"], "Was ist dein Beruf? = What's your job?", "Ich bin Ingenieurin."),
     ("{Wie}#W / schreibt#V / man#S / das?#AKK", ["Wie", "Was", "Wo"], "Spelling: Wie schreibt man das?", "M-Ü-L-L-E-R."),
     ("{Wen}#W / besucht#V / ihr#S / am Sonntag?#ZEIT", ["Wen", "Wem", "Wer"], "besuchen + Akkusativ → Wen?", "Unsere Großeltern."),
     ("{Wem}#W / gefällt#V / der Film#S / nicht?#NEG", ["Wem", "Wen", "Wer"], "gefallen + Dativ → Wem?", "Meinem Vater."),
     ("{Wie viel}#W / Uhr ist es?#S", ["Wie viel", "Wie viele", "Wann"], "The time: Wie viel Uhr ist es? / Wie spät ist es?", "Zehn nach drei."),
     ("{Warum}#W / bist#V / du#S / so müde?#ADJ", ["Warum", "Wie", "Wo"], "Warum = why.", "Ich habe schlecht geschlafen."),
     ("{Welche}#W / Farbe#AKK / magst#V / du?#S", ["Welche", "Welcher", "Welches"], "die Farbe → welche.", "Blau."),
     ("{Was}#W / machen#V / Sie#S / beruflich?#ADV", ["Was", "Wie", "Wer"], "Was machen Sie beruflich? = What do you do for a living?", "Ich bin Lehrer."),
     ("{Wie oft}#W / fährt#V / der Bus?#S", ["Wie oft", "Wie lange", "Wann"], "Wie oft = how often.", "Alle zehn Minuten."),
    ]
    for spec, opts, rule, ans in W:
        add("wfrage", spec, opts, f"Answer: „{ans}“ → {rule}", {o: WHY_W.get(o, "") + f"The answer „{ans}“ needs {opts[0]}." for o in opts[1:]},
            prompt="___ " + " ".join(p.split("#")[0] for p in spec.split(" / ")[1:]) + " – " + ans)


def moegen():
    MOG = "mögen: ich mag · du magst · er/sie/es mag · wir mögen · ihr mögt · sie/Sie mögen."
    G("moegen", "Wir#S / {mögen}#V / Kaffee.#AKK", ["mögen", "mag", "mögt"], MOG, {"mag": "mag is the ich- / er-form.", "mögt": "mögt is the ihr-form."})
    G("moegen", "{Mögt}#V1 / ihr#S / Fußball?#AKK", ["Mögt", "Mögen", "Magt"], MOG, {"Mögen": "Mögen is the wir/sie/Sie-form.", "Magt": "The vowel only changes in the singular: ihr mögt."})
    G("moegen", "Meine Schwester#S / {mag}#V / Hunde.#AKK", ["mag", "mögen", "magt"], MOG + " er/sie/es has no -t.", {"mögen": "Meine Schwester = sie (singular) → mag.", "magt": "No -t: sie mag (like ich mag)."})
    G("moegen", "Meine Eltern#S / {mögen}#V / Jazz.#AKK", ["mögen", "mag", "mögt"], MOG, {"mag": "Meine Eltern = sie (plural) → mögen.", "mögt": "mögt is the ihr-form."})
    G("moegen", "Du#S / {magst}#V / Schokolade, oder?#AKK", ["magst", "mögst", "magt"], MOG, {"mögst": "Singular forms use a: du magst.", "magt": "du needs -st: magst."})
    G("moegen", "{Mögen}#V1 / Sie#S / Fisch?#AKK", ["Mögen", "Mag", "Mögt"], MOG, {"Mag": "Mag is ich/er. Formal Sie → Mögen.", "Mögt": "Mögt is ihr (informal plural)."})
    G("moegen", "Ihr#S / {mögt}#V / keine Tomaten?#AKK", ["mögt", "mögen", "magt"], MOG, {"mögen": "mögen is wir/sie. ihr → mögt.", "magt": "Plural forms keep ö: ihr mögt."})
    G("moegen", "Ich#S / {möchte}#V / bitte#ADV / ein Glas Wasser.#AKK", ["möchte", "mag", "möchten"], "A polite wish right now → ich möchte.",
      {"mag": "mögen = to like in general, not 'I'd like (now)'.", "möchten": "möchten is wir/sie. ich → möchte."})
    G("moegen", "{Möchtest}#V1 / du#S / ein Stück Kuchen?#AKK", ["Möchtest", "Möchte", "Möchtet"], "Offering something: Möchtest du …? (du-form).",
      {"Möchte": "Möchte is ich/er. du → möchtest.", "Möchtet": "Möchtet is the ihr-form."})
    G("moegen", "Ich#S / {mag}#V / meine Kollegen.#AKK", ["mag", "möchte", "mage"], "Liking people/things in general → mögen: ich mag.",
      {"möchte": "möchte is a wish right now — you like your colleagues in general → mag.", "mage": "ich mag has no -e."})
    G("moegen", "Was#AKK / {möchtest}#V / du#S / zum Geburtstag?#ZEIT", ["möchtest", "magst", "möchtet"], "A wish → möchten: Was möchtest du zum Geburtstag?",
      {"magst": "mögen = general taste, not a wish.", "möchtet": "möchtet is the ihr-form."})
    G("moegen", "Mein Bruder#S / {möchte}#MV / Arzt#NOM / werden.#INF", ["möchte", "mag", "möchtet"], "möchte + infinitive at the end = would like to.",
      {"mag": "mögen + infinitive isn't used for wishes at A1 → möchte.", "möchtet": "möchtet is the ihr-form."})
    G("moegen", "Wir#S / {möchten}#V / zwei Kaffee, bitte.#AKK", ["möchten", "möchtet", "mögen"], "Ordering → möchten: wir möchten.",
      {"möchtet": "möchtet is the ihr-form.", "mögen": "mögen = to like in general. Ordering is a wish → möchten."})
    G("moegen", "Ich#S / trinke#V / gern Tee, aber Kaffee trinke ich {lieber}.#ADV", ["lieber", "gerner", "mehr gern"], "gern → <b>lieber</b> → am liebsten (irregular).",
      {"gerner": "gern is irregular: gern → lieber.", "mehr gern": "German doesn't say 'mehr gern' → lieber."})
    G("moegen", "Ich#S / fahre#V / {lieber}#ADV / Fahrrad als Bus.#AKK", ["lieber", "gerner", "am liebsten"], "Comparing two things → lieber (… als …).",
      {"gerner": "There is no 'gerner'. gern → lieber.", "am liebsten": "am liebsten = the most of all. With two things (… als …) → lieber."})
    G("moegen", "Nudeln mag ich, Reis mag ich lieber, aber {am liebsten}#ADV / esse#V / ich#S / Pizza.#AKK", ["am liebsten", "lieber", "gern"], "gern → lieber → <b>am liebsten</b> (the favourite).",
      {"lieber": "lieber was already used for Reis — the top favourite is am liebsten.", "gern": "gern is the lowest level. The favourite → am liebsten."})
    G("moegen", "Was#AKK / isst#V / du#S / {am liebsten}?#ADV", ["am liebsten", "am liebste", "am gernsten"], "Favourite → am liebsten.",
      {"am liebste": "After am the form ends in -en: am liebsten.", "am gernsten": "gern is irregular: am liebsten."})
    G("moegen", "Ich#S / spiele#V / {nicht gern}#NEG / Golf.#AKK", ["nicht gern", "gern nicht", "kein gern"], "Negating gern → nicht gern (nicht comes before gern).",
      {"gern nicht": "nicht goes before gern: nicht gern.", "kein gern": "kein only negates nouns."})
    G("moegen", "In meiner Stadt#ORT / {gibt es}#V / viele Parks.#AKK", ["gibt es", "es gibt", "sind es"], "there is/are → es gibt. After something in position 1: gibt es.",
      {"es gibt": "Verb in position 2: 'In meiner Stadt' is position 1 → gibt es.", "sind es": "German says es gibt for 'there are'."})
    G("moegen", "Nein,#ADV / hier#ORT / {gibt es kein}#V / Café.#AKK", ["gibt es kein", "ist kein", "gibt es nicht"], "es gibt + kein: Hier gibt es kein Café.",
      {"ist kein": "'there is no' → es gibt kein …", "gibt es nicht": "Negate the noun with kein, not nicht."})


def konnektoren():
    K = [
     ("Ich habe Hunger, {denn}#KON / ich#S / habe#HV / heute#ZEIT / nichts gegessen.#P2", ["denn", "aber", "oder"], "denn = because.", {"aber": "No contrast here.", "oder": "Not a choice."}),
     ("Wir gehen ins Kino {oder}#KON / wir#S / bleiben#V / zu Hause.#ORT", ["oder", "denn", "aber"], "oder = or → two options.", {"denn": "Staying home isn't the reason for the cinema.", "aber": "This is a choice, not a contrast."}),
     ("Anna spricht Englisch {und}#KON / sie#S / lernt#V / Deutsch.#AKK", ["und", "denn", "oder"], "und = and → adding information.", {"denn": "Learning German isn't the reason she speaks English.", "oder": "Both are true — not a choice."}),
     ("Das Wetter ist schlecht, {aber}#KON / wir#S / gehen#V / spazieren.#INF", ["aber", "denn", "oder"], "Bad weather but we go anyway → aber (contrast).", {"denn": "Going for a walk isn't the reason for the weather.", "oder": "Not a choice."}),
     ("Ich nehme den Bus, {denn}#KON / mein Auto#S / ist#V / kaputt.#ADJ", ["denn", "oder", "und"], "The broken car is the reason → denn.", {"oder": "Not a choice.", "und": "The second part explains the first → denn."}),
     ("Trinkst du Wein {oder}#KON / Bier?#AKK", ["oder", "aber", "denn"], "A choice → oder.", {"aber": "aber = but.", "denn": "denn = because."}),
     ("Ich bin müde, {aber}#KON / ich#S / muss#MV / noch#ADV / arbeiten.#INF", ["aber", "denn", "oder"], "Tired but still have to work → aber.", {"denn": "Having to work isn't the reason for being tired here — it's a contrast.", "oder": "Not a choice."}),
     ("Er kocht {und}#KON / sie#S / deckt#V / den Tisch.#AKK", ["und", "denn", "oder"], "Two things happening → und.", {"denn": "Setting the table isn't the reason he cooks.", "oder": "Both happen — not a choice."}),
     ("Ich gehe zum Arzt, {denn}#KON / ich#S / habe#V / Fieber.#AKK", ["denn", "aber", "oder"], "Fever is the reason → denn.", {"aber": "No contrast.", "oder": "Not a choice."}),
     ("Die Wohnung ist klein, {aber}#KON / sie#S / ist#V / billig.#ADJ", ["aber", "denn", "oder"], "Negative + positive → aber.", {"denn": "Being cheap isn't why it's small.", "oder": "Not a choice."}),
     ("Kommst du mit {oder}#KON / hast#V / du#S / keine Zeit?#AKK", ["oder", "denn", "aber"], "Two alternatives in a question → oder. The second part is a yes/no question, so its verb comes first.", {"denn": "Not a reason.", "aber": "Not a contrast."}),
     ("Ich lerne viel, {denn}#KON / ich#S / habe#V / bald#ZEIT / eine Prüfung.#AKK", ["denn", "aber", "oder"], "The exam is the reason → denn.", {"aber": "No contrast.", "oder": "Not a choice."}),
     ("Der Pullover ist schön, {aber}#KON / er#S / ist#V / zu teuer.#ADJ", ["aber", "und", "denn"], "Positive + negative → aber.", {"und": "und joins similar facts; schön and zu teuer contrast.", "denn": "zu teuer isn't the reason it's schön."}),
     ("Am Samstag kaufe ich ein {und}#KON / am Sonntag#ZEIT / besuche#V / ich#S / meine Eltern.#AKK", ["und", "denn", "oder"], "und = and. After und, a time word can take position 1 — then the verb, then the subject.", {"denn": "Visiting parents isn't the reason for shopping.", "oder": "Both happen — not a choice."}),
     ("Ich trinke abends keinen Kaffee, {denn}#KON / ich#S / kann#MV / dann#ZEIT / nicht schlafen.#INF", ["denn", "aber", "oder"], "Not sleeping is the reason → denn.", {"aber": "No contrast — it's a reason.", "oder": "Not a choice."}),
    ]
    for spec, opts, rule, why in K:
        G("konnektor", spec, opts, rule + " und/aber/oder/denn are 'position 0' — they don't change word order.", why)
    END = "The verb went to the end — that only happens after weil/dass (A2). After und/aber/oder/denn: normal order, verb in position 2."
    INV = "The connector doesn't take position 1 — the subject (or a time word) does, then the verb."
    ORD = "After und/aber/oder/denn the clause has normal word order: the conjugated verb is in position 2 (the connector is position 0)."
    O = [
     ("Ich lerne Deutsch, ___ (denn · ich · möchte · in Deutschland arbeiten)", "denn#KON / ich#S / möchte#MV / in Deutschland#ORT / arbeiten.#INF",
      [("denn ich in Deutschland arbeiten möchte.", END), ("denn möchte ich in Deutschland arbeiten.", INV)]),
     ("Es regnet, ___ (aber · wir · spielen · Fußball)", "aber#KON / wir#S / spielen#V / Fußball.#AKK",
      [("aber spielen wir Fußball.", INV), ("aber wir Fußball spielen.", END)]),
     ("Ich esse kein Fleisch, ___ (denn · ich · bin · Vegetarier)", "denn#KON / ich#S / bin#V / Vegetarier.#NOM",
      [("denn ich Vegetarier bin.", END), ("denn bin ich Vegetarier.", INV)]),
     ("Wir fahren mit dem Zug ___ (oder · wir · nehmen · das Auto)", "oder#KON / wir#S / nehmen#V / das Auto?#AKK",
      [("oder nehmen wir das Auto?", INV), ("oder wir das Auto nehmen?", END)]),
     ("Ich arbeite bis 17 Uhr ___ (und · dann · gehe · ich · ins Fitnessstudio)", "und#KON / dann#ZEIT / gehe#V / ich#S / ins Fitnessstudio.#ORT",
      [("und dann ich gehe ins Fitnessstudio.", "'dann' is in position 1, so the verb must come next, then the subject: dann gehe ich."), ("und dann ich ins Fitnessstudio gehe.", END)]),
     ("Sie möchte kommen, ___ (aber · sie · hat · keine Zeit)", "aber#KON / sie#S / hat#V / keine Zeit.#AKK",
      [("aber sie keine Zeit hat.", END), ("aber hat sie keine Zeit.", INV)]),
     ("Ich bleibe heute zu Hause, ___ (denn · morgen · habe · ich · einen Test)", "denn#KON / morgen#ZEIT / habe#V / ich#S / einen Test.#AKK",
      [("denn morgen ich habe einen Test.", "'morgen' is in position 1, so the verb comes next: morgen habe ich."), ("denn ich morgen einen Test habe.", END)]),
     ("Er spielt Gitarre ___ (und · seine Frau · singt)", "und#KON / seine Frau#S / singt.#V",
      [("und singt seine Frau.", INV), ("und seine Frau singen.", "seine Frau = sie (singular) → singt.")]),
     ("Der Film war lang, ___ (aber · er · war · sehr gut)", "aber#KON / er#S / war#V / sehr gut.#ADJ",
      [("aber war er sehr gut.", INV), ("aber er sehr gut war.", END)]),
     ("Ich rufe dich an, ___ (denn · ich · brauche · deine Hilfe)", "denn#KON / ich#S / brauche#V / deine Hilfe.#AKK",
      [("denn ich deine Hilfe brauche.", END), ("denn brauche ich deine Hilfe.", INV)]),
    ]
    for p, spec, wrong in O:
        C("konnektor", p, spec, wrong, ORD)


def man_wer():
    MAN = "man always takes the er/sie/es form of the verb."
    for spec, opts, why in [
        ("In der Bibliothek#ORT / {muss}#MV / man#S / leise sein.#INF", ["muss", "müssen", "musst"], {"müssen": "man is grammatically singular → muss.", "musst": "musst is the du-form."}),
        ("Im Kurs#ORT / {spricht}#V / man#S / Deutsch.#AKK", ["spricht", "sprechen", "sprecht"], {"sprechen": "man takes the er-form → spricht.", "sprecht": "sprecht is the ihr-form."}),
        ("Wo#W / {kann}#MV / man#S / hier#ORT / Brot kaufen?#INF", ["kann", "können", "kannst"], {"können": "man is singular → kann.", "kannst": "kannst is the du-form."}),
        ("Im Museum#ORT / {darf}#MV / man#S / nicht#NEG / fotografieren.#INF", ["darf", "dürfen", "darfst"], {"dürfen": "man is singular → darf.", "darfst": "darfst is the du-form."}),
        ("Wie#W / {schreibt}#V / man#S / Ihren Namen?#AKK", ["schreibt", "schreiben", "schreibst"], {"schreiben": "man takes the er-form → schreibt.", "schreibst": "schreibst is the du-form."}),
        ("In Bayern#ORT / {trinkt}#V / man#S / viel Bier.#AKK", ["trinkt", "trinken", "trinkst"], {"trinken": "man is singular → trinkt.", "trinkst": "trinkst is the du-form."}),
        ("Was#AKK / {macht}#V / man#S / am Wochenende#ZEIT / in München?#ORT", ["macht", "machen", "machst"], {"machen": "man takes the er-form → macht.", "machst": "machst is the du-form."}),
    ]:
        G("man_wer", spec, opts, MAN, why)
    G("man_wer", "Hier#ORT / spricht#V / {man}#S / Englisch.#AKK", ["man", "Mann", "mann"], "man (small m, one n) = people in general. der Mann = a man.",
      {"Mann": "der Mann (capital, double n) is a male person. 'People in general' → man.", "mann": "'mann' isn't a German word."})
    WW = "Wer? = subject (Nominativ) · Wen? = Akkusativ object · Wem? = Dativ object."
    for spec, opts, rule, why in [
        ("{Wer}#W / hat#HV / das Fenster#AKK / aufgemacht?#P2", ["Wer", "Wen", "Wem"], "Asking for the subject → Wer?", {"Wen": "das Fenster is the object; you ask for the subject → Wer.", "Wem": "Wem asks for a Dativ object."}),
        ("{Wen}#W / siehst#V / du?#S", ["Wen", "Wem", "Wer"], "sehen + Akkusativ → Wen?", {"Wem": "sehen takes Akkusativ, not Dativ.", "Wer": "du is the subject already."}),
        ("{Wem}#W / dankst#V / du?#S", ["Wem", "Wen", "Wer"], "danken + Dativ → Wem?", {"Wen": "danken takes Dativ.", "Wer": "du is the subject already."}),
        ("{Wer}#W / wohnt#V / hier?#ORT", ["Wer", "Wen", "Wem"], "Asking for the subject → Wer?", {"Wen": "Wen is Akkusativ. The person who lives here is the subject.", "Wem": "Wem is Dativ."}),
        ("{Wen}#W / lädst#V / du#S / zur Party#ORT / ein?#PRE", ["Wen", "Wem", "Wer"], "einladen + Akkusativ → Wen?", {"Wem": "einladen takes Akkusativ.", "Wer": "du is the subject already."}),
        ("{Wem}#W / gefällt#V / das Bild?#S", ["Wem", "Wen", "Wer"], "gefallen + Dativ → Wem?", {"Wen": "gefallen takes Dativ: Das Bild gefällt mir.", "Wer": "das Bild is the subject."}),
        ("{Wen}#W / liebst#V / du?#S", ["Wen", "Wem", "Wer"], "lieben + Akkusativ → Wen?", {"Wem": "lieben takes Akkusativ.", "Wer": "du is the subject already."}),
        ("{Wem}#W / gehören#V / die Schuhe?#S", ["Wem", "Wen", "Wer"], "gehören + Dativ → Wem?", {"Wen": "gehören takes Dativ.", "Wer": "die Schuhe is the subject — you ask for the owner (Dativ)."}),
    ]:
        G("man_wer", spec, opts, rule + " " + WW, why)


def zeitdativ():
    Z = [
     ("Ich habe {vor} einer Stunde gegessen.", ["vor", "seit", "in"], "Finished in the past + ago → vor + Dativ.", {"seit": "seit = still going on now.", "in": "in = in the future."}),
     ("{Seit} zwei Monaten habe ich ein Fahrrad.", ["Seit", "Vor", "In"], "Started in the past and still true → seit + Dativ.", {"Vor": "vor = ago (a finished event).", "In": "in = in the future."}),
     ("{In} drei Tagen fliege ich nach Indien.", ["In", "Vor", "Seit"], "In the future → in + Dativ.", {"Vor": "vor = ago (past).", "Seit": "seit = since (still going)."}),
     ("{Nach} der Schule spielen die Kinder Fußball.", ["Nach", "Seit", "Ab"], "After → nach + Dativ.", {"Seit": "seit = since; it doesn't fit a daily routine.", "Ab": "ab = from … on (a start date)."}),
     ("Ich bin seit {einer} Woche krank.", ["einer", "eine", "einem"], "seit + Dativ: die Woche → einer Woche.", {"eine": "eine is Nominativ/Akkusativ. After seit → Dativ: einer.", "einem": "einem is for der/das. die Woche → einer."}),
     ("Vor {einem} Monat bin ich umgezogen.", ["einem", "einen", "ein"], "vor + Dativ: der Monat → einem Monat.", {"einen": "einen is Akkusativ. vor (time) takes Dativ.", "ein": "ein is Nominativ. After vor → Dativ: einem."}),
     ("Nach {dem} Frühstück gehe ich joggen.", ["dem", "den", "der"], "nach + Dativ: das Frühstück → dem Frühstück.", {"den": "den is Akkusativ masculine.", "der": "der is Dativ for die-nouns. das Frühstück → dem."}),
     ("Vor {der} Arbeit bringe ich die Kinder zur Schule.", ["der", "die", "den"], "vor + Dativ: die Arbeit → der Arbeit.", {"die": "die is Nominativ/Akkusativ. Dativ of die → der.", "den": "den is masculine Akkusativ or Dativ plural."}),
     ("In {einer} Stunde beginnt der Film.", ["einer", "eine", "einem"], "in (time) + Dativ: die Stunde → einer Stunde.", {"eine": "After in (time) → Dativ: einer.", "einem": "einem is for der/das. die Stunde → einer."}),
     ("Ich wohne seit fünf {Monaten} in München.", ["Monaten", "Monate", "Monat"], "Dativ plural adds -n: seit fünf Monaten.", {"Monate": "Dativ plural needs -n: Monaten.", "Monat": "fünf = plural."}),
     ("Vor drei {Wochen} war ich im Urlaub.", ["Wochen", "Woche", "Wochenen"], "Dativ plural: Wochen already ends in -n, so nothing is added.", {"Woche": "drei = plural → Wochen.", "Wochenen": "Plurals already ending in -n get no extra -n."}),
     ("Ich bin {seit} 2020 in Deutschland.", ["seit", "vor", "ab"], "Since 2020 and still here → seit.", {"vor": "vor needs a time span (vor drei Jahren), not a year.", "ab": "ab = from … on, for a start in the future."}),
     ("Ich bin {vor} zwei Jahren nach Deutschland gekommen.", ["vor", "seit", "in"], "A finished event in the past (Perfekt) → vor = ago.", {"seit": "seit is for something still going on, not a finished arrival.", "in": "in = in the future."}),
     ("{Ab} nächster Woche habe ich Urlaub.", ["Ab", "Seit", "Vor"], "Start in the future → ab (from … on).", {"Seit": "seit is for something that started in the past.", "Vor": "vor = before / ago."}),
     ("Das Geschäft hat von 8 {bis} 20 Uhr geöffnet.", ["bis", "ab", "seit"], "von … bis = from … until.", {"ab": "ab can't close a range — von … bis.", "seit": "seit = since."}),
     ("Ich warte schon {seit} einer halben Stunde!", ["seit", "vor", "für"], "Still waiting now → seit (+ schon).", {"vor": "vor = ago (finished).", "für": "German uses seit here, not für."}),
     ("Wir sehen uns {in} zwei Wochen.", ["in", "vor", "seit"], "In the future → in.", {"vor": "vor = ago.", "seit": "seit = since."}),
     ("Wie lange lernst du schon Deutsch? – {Seit} acht Monaten.", ["Seit", "Vor", "Für"], "Still learning now → seit + Dativ.", {"Vor": "vor = ago (finished).", "Für": "German uses seit for 'for' + time up to now."}),
     ("Wann bist du nach München gekommen? – {Vor} einem Jahr.", ["Vor", "Seit", "In"], "When (in the past)? → vor = ago.", {"Seit": "seit answers 'how long', not 'when'.", "In": "in = in the future."}),
     ("Wann ist die Prüfung? – {In} einem Monat.", ["In", "Vor", "Seit"], "In the future → in + Dativ.", {"Vor": "vor = ago (past).", "Seit": "seit = since."}),
    ]
    for text, opts, rule, why in Z:
        S("zeitdativ", text, "ZEIT", opts, rule, why)


def alltag():
    AL = [
     ("At the supermarket you can't find the milk:", "Entschuldigung, wo finde ich die Milch?", [("Entschuldigung, wo ist Milch finden?", "Two verbs (ist + finden) — use one: Wo finde ich …? or Wo ist …?"), ("Wo Milch, bitte?", "A question needs a verb in position 2.")], "Wo finde ich …? / Wo ist …?"),
     ("The cashier asks: „Zahlen Sie bar oder mit Karte?“", "Mit Karte, bitte.", [("Mit der Bar, bitte.", "bar = in cash; die Bar is a pub."), ("Ich zahle mit Geld Karte.", "Geld Karte isn't German. → mit Karte or bar.")], "bar = cash · mit Karte = by card."),
     ("At the bakery: „Sonst noch etwas?“ You don't want more:", "Nein, danke. Das ist alles.", [("Ja, danke. Das ist alles.", "Ja would mean you want more."), ("Nein, bitte. Das ist alle.", "'Nein, danke' declines; 'alle' means all (people) → Das ist alles.")], "Sonst noch etwas? = Anything else? → Nein, danke. Das ist alles."),
     ("In a clothes shop you need another size:", "Haben Sie die Hose auch in Größe 38?", [("Haben Sie die Hose auch in Nummer 38?", "Clothes sizes are Größe."), ("Gibt die Hose in 38?", "es gibt needs es — and here you ask the seller: Haben Sie …?")], "Größe = size. Haben Sie das auch in Größe …?"),
     ("You want to try on a jacket:", "Kann ich die Jacke anprobieren?", [("Kann ich die Jacke probieren an?", "After a modal verb the separable verb stays together at the end: anprobieren."), ("Kann ich die Jacke versuchen?", "versuchen = to attempt. Clothes → anprobieren.")], "anprobieren = to try on (clothes)."),
     ("In a restaurant, ordering:", "Ich nehme die Tomatensuppe, bitte.", [("Ich bekomme die Tomatensuppe nehmen.", "Two verbs that don't belong together. → Ich nehme … / Ich hätte gern …"), ("Ich will haben Tomatensuppe.", "Rude and wrong word order (haben would go to the end).")], "Ordering: Ich nehme … / Ich hätte gern … / Ich möchte …"),
     ("You want to see the menu:", "Die Speisekarte, bitte.", [("Das Menü, bitte.", "das Menü is a set meal, not the list of dishes."), ("Die Rechnung, bitte.", "die Rechnung = the bill.")], "die Speisekarte = the menu · die Rechnung = the bill."),
     ("The waiter asks: „Hat es geschmeckt?“", "Ja, sehr gut, danke!", [("Ja, ich habe geschmeckt.", "es (the food) tasted, not you."), ("Ja, es war sehr lecker gegessen.", "Mixing two structures. → Ja, es war sehr lecker.")], "Hat es geschmeckt? – Ja, sehr gut / Ja, sehr lecker, danke!"),
     ("The bill is 18,50 €. You give 20 € and want no change back:", "Stimmt so.", [("Das ist richtig so viel.", "Not a set phrase. → Stimmt so."), ("Behalten Sie die Rest.", "der Rest → Behalten Sie den Rest.")], "Tipping: Stimmt so. = Keep the change."),
     ("At the doctor's reception:", "Ich habe um 10 Uhr einen Termin bei Dr. Weber.", [("Ich habe um 10 Uhr eine Verabredung mit Dr. Weber.", "Verabredung is a date with friends. Doctor → Termin."), ("Ich bin um 10 Uhr Termin.", "You HAVE an appointment: Ich habe einen Termin.")], "einen Termin haben bei + doctor."),
     ("„Ihre Versichertenkarte, bitte.“ You hand it over:", "Hier, bitte.", [("Danke schön, bitte.", "You're giving, not receiving → Hier, bitte."), ("Hier sind Sie.", "That's English ('here you are'). German: Hier, bitte. / Bitte schön.")], "Handing something over: Hier, bitte. / Bitte schön."),
     ("The doctor asks: „Wo tut es weh?“", "Mein Rücken tut weh.", [("Mein Rücken macht weh.", "The verb is wehtun: … tut weh."), ("Ich tue Rücken weh.", "The body part is the subject: Mein Rücken tut weh.")], "Body part + tut weh / tun weh: Mein Kopf tut weh."),
     ("You call in sick at work:", "Ich bin krank und kann heute nicht kommen.", [("Ich bin krank und kann heute nicht zu kommen.", "No zu after a modal verb."), ("Ich habe krank und komme nicht.", "krank sein: Ich bin krank.")], "Ich bin krank. Ich kann heute nicht kommen."),
     ("At the pharmacy:", "Haben Sie etwas gegen Kopfschmerzen?", [("Haben Sie etwas für Kopfschmerzen gegen?", "gegen goes before the noun: etwas gegen Kopfschmerzen."), ("Ich möchte Kopfschmerzen, bitte.", "That means you WANT a headache!")], "Medicine: etwas gegen + problem (gegen Husten, gegen Fieber)."),
     ("At the Bürgeramt you want to register your new address:", "Ich möchte mich anmelden.", [("Ich möchte mich anmachen.", "anmachen = to switch on / to chat someone up!"), ("Ich möchte mich einschreiben Wohnung.", "einschreiben = enrol (university). Address → anmelden.")], "sich anmelden = to register (address, course)."),
     ("An official asks: „Wie ist Ihr Familienname?“", "Mein Familienname ist Sharma.", [("Ich heiße Familie Sharma.", "Familie means family, not surname."), ("Mein Familienname heißt Sharma.", "A name 'ist', a person 'heißt': Mein Name ist … / Ich heiße …")], "Familienname / Nachname = surname · Vorname = first name."),
     ("On a form, „Familienstand“ asks for:", "ledig / verheiratet / geschieden", [("männlich / weiblich", "That's Geschlecht (sex)."), ("Straße / Hausnummer", "That's the Adresse.")], "Familienstand = marital status: ledig (single), verheiratet, geschieden."),
     ("You call about a flat:", "Ist die Wohnung noch frei?", [("Ist die Wohnung noch kostenlos?", "kostenlos = free of charge. Available → frei."), ("Hat die Wohnung noch frei?", "frei sein: Ist … noch frei?")], "frei = available (flat, seat) · kostenlos = free of charge."),
     ("Asking about the rent:", "Wie hoch ist die Miete?", [("Wie viel ist die Miete hoch?", "Either Wie hoch ist … ? or Wie viel kostet …? — not both."), ("Was kostet die Miete warm hoch?", "Mixed-up phrase. → Wie hoch ist die Warmmiete?")], "Wie hoch ist die Miete? / Was kostet die Wohnung?"),
     ("What is the „Warmmiete“?", "Die Miete mit Nebenkosten (Heizung, Wasser …).", [("Die Miete im Sommer.", "warm here means heating included, not the season."), ("Die Miete ohne Heizung.", "That's the Kaltmiete.")], "Kaltmiete = rent only · Warmmiete = rent + Nebenkosten."),
     ("On the phone you want to speak to Mr Braun:", "Kann ich bitte Herrn Braun sprechen?", [("Kann ich bitte mit Herr Braun reden zu?", "No zu, and mit + Dativ: mit Herrn Braun."), ("Ist Herr Braun sprechen?", "Two verbs, no structure. → Kann ich … sprechen?")], "Kann ich bitte Herrn / Frau … sprechen?"),
     ("On the phone the person you want isn't there. The secretary says:", "Er ist leider nicht da. Kann ich etwas ausrichten?", [("Er ist leider nicht da. Kann ich etwas sagen?", "That means 'Can I say something?' → etwas ausrichten = pass on a message."), ("Er ist nicht. Möchten Sie warten?", "sein needs more: Er ist nicht da.")], "nicht da = not here · etwas ausrichten = take a message."),
     ("You dialled the wrong number:", "Entschuldigung, ich habe mich verwählt.", [("Entschuldigung, ich habe falsch gerufen.", "rufen = to shout. Wrong number → sich verwählen."), ("Entschuldigung, die Nummer ist kaputt.", "The number isn't broken — you dialled wrong.")], "Ich habe mich verwählt. = I dialled the wrong number."),
     ("„Wie komme ich zum Bahnhof?“ You answer:", "Gehen Sie hier rechts und dann immer geradeaus.", [("Gehen rechts Sie und dann geradeaus.", "Sie-imperative: verb + Sie together at the start."), ("Du gehen rechts und dann geradeaus.", "du needs gehst — and a stranger gets Sie.")], "Directions: Sie-imperative — Gehen Sie … / Nehmen Sie …"),
     ("Asking whether it's far:", "Ist das weit von hier?", [("Ist das lang von hier?", "Distance → weit. lang is for length/time."), ("Wie weit ist das hier von?", "von needs its noun: von hier.")], "weit = far · nah = near."),
     ("At the ticket machine you ask someone:", "Entschuldigung, wie funktioniert der Automat?", [("Entschuldigung, wie arbeitet der Automat?", "Machines funktionieren; people arbeiten."), ("Wie geht der Automat funktioniert?", "Two verbs mixed. → Wie funktioniert …?")], "Wie funktioniert das? = How does it work?"),
     ("At the station you ask which platform:", "Von welchem Gleis fährt der Zug nach Hamburg?", [("Von welcher Gleis fährt der Zug nach Hamburg?", "das Gleis → von + Dativ: welchem."), ("Wo fährt der Zug nach Hamburg ab von?", "Mixed structure. → Von welchem Gleis …? / Wo fährt … ab?")], "das Gleis = platform track. von + Dativ → von welchem Gleis."),
     ("„Der Zug hat zehn Minuten Verspätung.“ This means:", "Der Zug kommt zehn Minuten später.", [("Der Zug fährt zehn Minuten früher.", "Verspätung = delay, not early."), ("Der Zug fällt aus.", "ausfallen = cancelled.")], "die Verspätung = delay · ausfallen = to be cancelled."),
     ("Buying a return ticket:", "Einmal Köln hin und zurück, bitte.", [("Einmal Köln hin und her, bitte.", "hin und her = back and forth (moving around). Ticket → hin und zurück."), ("Einmal Köln zurück und hin, bitte.", "Fixed order: hin und zurück.")], "hin und zurück = return · einfach = one way."),
     ("Small talk about the weather:", "Heute ist es aber kalt!", [("Heute hat es aber kalt!", "Weather: es ist kalt (not hat)."), ("Heute bin ich aber kalt!", "Ich bin kalt = I'm a cold person. Feeling → Mir ist kalt.")], "Weather: Es ist kalt / warm / windig."),
     ("You feel cold:", "Mir ist kalt.", [("Ich bin kalt.", "Ich bin kalt describes your personality (unfriendly)."), ("Ich habe kalt.", "That's French/Spanish style. German: Mir ist kalt.")], "Feeling: Mir ist kalt / warm / schlecht (Dativ)."),
     ("The forecast says sun all day:", "Morgen scheint die Sonne.", [("Morgen sonnt es.", "There is no 'es sonnt'. → Die Sonne scheint / Es ist sonnig."), ("Morgen ist die Sonne scheinen.", "Two verbs mixed: Die Sonne scheint.")], "Die Sonne scheint. Es regnet. Es schneit. Es ist sonnig."),
     ("Asking about hobbies:", "Was machst du in deiner Freizeit?", [("Was machst du in deiner freien Zeit Hobby?", "Hobby doesn't fit at the end."), ("Was ist dein Freizeit?", "die Freizeit → deine Freizeit — and you ask what someone does.")], "die Freizeit = free time. Was machst du gern?"),
     ("Saying you like reading:", "Ich lese gern.", [("Ich mag gern lesen.", "At A1: verb + gern → Ich lese gern."), ("Ich gern lese.", "The verb is in position 2: Ich lese gern.")], "Liking an activity: verb + gern."),
     ("Inviting a friend to your party:", "Hast du am Samstag Zeit? Ich mache eine Party.", [("Hast du am Samstag Zeit? Ich habe eine Party gemacht.", "That's the past — an invitation is about the future."), ("Bist du Samstag Zeit? Ich mache Party.", "Zeit haben: Hast du Zeit? — and eine Party.")], "Hast du am … Zeit? = Are you free on …?"),
     ("Suggesting the cinema:", "Wollen wir zusammen ins Kino gehen?", [("Wollen wir zusammen ins Kino gegangen?", "After a modal: infinitive (gehen), not Partizip."), ("Wir wollen zusammen gehen Kino?", "Infinitive at the end, and ins Kino.")], "Suggestion: Wollen wir …? / Gehen wir …? / Hast du Lust, …?"),
     ("Agreeing a meeting point:", "Treffen wir uns um acht vor dem Kino?", [("Treffen wir um acht vor dem Kino uns?", "uns comes right after the subject: Treffen wir uns …"), ("Wir treffen uns um acht vor das Kino?", "Position (Wo?) → Dativ: vor dem Kino.")], "sich treffen: Treffen wir uns …? Wo? → vor dem Kino."),
     ("Your friend asks „Kommst du mit?“ You can't:", "Tut mir leid, ich kann leider nicht.", [("Tut mir leid, ich kann nicht leider gehen.", "leider goes before nicht: leider nicht."), ("Es tut mich leid, ich kann nicht.", "Dativ: Es tut mir leid.")], "Tut mir leid / Leider kann ich nicht."),
     ("Someone asks where you are from:", "Ich komme aus Indien, aus Delhi.", [("Ich komme von Indien, von Delhi.", "Origin (countries/cities) → aus."), ("Ich bin aus Indien von Delhi kommen.", "Two verbs mixed. → Ich komme aus … / Ich bin aus …")], "Origin: aus + country/city."),
     ("Asking how long someone has lived here:", "Wie lange wohnst du schon hier?", [("Seit wann lange wohnst du hier?", "Either Seit wann …? or Wie lange …? — not both."), ("Wie lange du wohnst schon hier?", "Verb in position 2, right after the W-word.")], "Wie lange …? / Seit wann …? + schon."),
     ("Introducing yourself to a new colleague:", "Hallo, ich bin Priya. Ich arbeite im Marketing.", [("Hallo, ich bin Priya. Ich arbeite als Marketing.", "als + job title (als Designerin). Department → im Marketing."), ("Hallo, mein Name heißt Priya, ich bin Marketing.", "Mein Name ist … / Ich heiße … — and you aren't a department.")], "arbeiten als + job · arbeiten in/im + department or bei + company."),
     ("Saying your profession:", "Ich bin Ingenieur von Beruf.", [("Ich bin ein Ingenieur von Beruf.", "No article with professions: Ich bin Ingenieur."), ("Ich arbeite Ingenieur.", "arbeiten needs als: Ich arbeite als Ingenieur.")], "Jobs: Ich bin Lehrerin. / Ich arbeite als Lehrerin. (no ein!)"),
     ("Asking a colleague for help:", "Kannst du mir bitte kurz helfen?", [("Kannst du mich bitte kurz helfen?", "helfen + Dativ → mir."), ("Hilfst du mich kurz?", "helfen + Dativ → mir.")], "helfen + Dativ: Kannst du mir helfen?"),
     ("You need to leave work early:", "Darf ich heute früher gehen? Ich habe einen Arzttermin.", [("Muss ich heute früher gehen? Ich habe einen Arzttermin.", "Muss ich …? asks if you are forced to. Permission → Darf ich …?"), ("Darf ich heute früher gehen? Ich habe eine Arztverabredung.", "Doctor → Termin, not Verabredung.")], "Asking for permission → Darf ich …?"),
     ("Informal email to your friend Sara, opening:", "Liebe Sara,", [("Sehr geehrte Sara,", "Too formal for a friend."), ("Lieber Sara,", "Lieber for men, Liebe for women.")], "Informal: Liebe (f) / Lieber (m) + first name, · Hallo …,"),
     ("Informal email, ending:", "Viele Grüße, Tom", [("Mit freundlichen Grüßen, dein Tom", "Formal closing with informal 'dein' — doesn't match."), ("Viel Gruß, Tom", "Plural: Viele Grüße.")], "Informal: Viele Grüße / Liebe Grüße. Formal: Mit freundlichen Grüßen."),
     ("Formal email to Mr Klein, opening:", "Sehr geehrter Herr Klein,", [("Sehr geehrte Herr Klein,", "Herr is masculine → geehrter."), ("Sehr geehrter Klein,", "You need Herr / Frau before the surname.")], "Sehr geehrter Herr … · Sehr geehrte Frau …"),
     ("Formal email, asking for information:", "Können Sie mir bitte Informationen schicken?", [("Können Sie mich bitte Informationen schicken?", "schicken: the person is Dativ → mir."), ("Sie können mir bitte Informationen schicken?", "A request is a yes/no question: modal verb first.")], "Polite request: Können Sie mir bitte …?"),
     ("Someone says „Entschuldigung!“ after bumping into you:", "Kein Problem!", [("Gleichfalls!", "gleichfalls = same to you (for wishes)."), ("Gesundheit!", "Gesundheit is for sneezing.")], "Kein Problem! / Macht nichts! / Schon gut!"),
     ("Leaving a friend you'll see tomorrow:", "Tschüss, bis morgen!", [("Auf Wiederhören, bis morgen!", "Auf Wiederhören is only on the phone."), ("Tschüss, bis gestern!", "gestern = yesterday.")], "Tschüss! Bis morgen / bis später / bis bald!"),
     ("Meeting someone formally for the first time:", "Freut mich, Sie kennenzulernen.", [("Freut mich, Sie zu kennen lernen.", "kennenlernen is one verb; zu goes inside: kennenzulernen."), ("Ich freue Sie kennenzulernen.", "Fixed phrase: (Es) freut mich …")], "Freut mich! / Freut mich, Sie kennenzulernen."),
     ("You want someone to speak more slowly:", "Können Sie bitte langsamer sprechen?", [("Können Sie bitte mehr langsam sprechen?", "Comparative with -er: langsamer, not mehr langsam."), ("Sprechen Sie bitte langsam mehr?", "Wrong order and form → langsamer.")], "langsam → langsamer (comparative)."),
     ("You want to know what a word means:", "Was bedeutet das Wort „Termin“?", [("Was meint das Wort „Termin“ bedeuten?", "One verb: Was bedeutet …?"), ("Wie bedeutet das Wort „Termin“?", "Meaning → Was bedeutet …?")], "Was bedeutet …? / Was heißt … auf Englisch?"),
    ]
    for p, corr, wrong, rule in AL:
        add("alltag", [[corr, ""]], [corr] + [w for w, _ in wrong], rule, {w: y for w, y in wrong}, prompt=p, mode="choose")


def adjektiv():
    FIND = "finden + Akkusativ: der → ihn, die → sie, das → es, plural → sie. The adjective after it has no ending."
    for text, opts, why in [
        ("Wie findest du den Film? – Ich finde {ihn} super.", ["ihn", "er", "es"], {"er": "er is Nominativ. finden takes Akkusativ → ihn.", "es": "der Film is masculine → ihn."}),
        ("Wie findest du die Wohnung? – Ich finde {sie} sehr schön.", ["sie", "ihn", "es"], {"ihn": "ihn is for der-nouns. die Wohnung → sie.", "es": "es is for das-nouns. die Wohnung → sie."}),
        ("Wie findest du das Hotel? – Ich finde {es} zu teuer.", ["es", "ihn", "er"], {"ihn": "ihn is for der-nouns. das Hotel → es.", "er": "er is masculine Nominativ."}),
        ("Wie findest du die Schuhe? – Ich finde {sie} toll.", ["sie", "es", "ihn"], {"es": "die Schuhe is plural → sie.", "ihn": "Plural → sie."}),
    ]:
        S("adjektiv", text, "AKK", opts, FIND, why)
    NOEND = "After sein (or finden) the adjective takes <b>no ending</b>."
    for text, opts in [("Mein Zimmer ist {klein}.", ["klein", "kleine", "kleines"]), ("Die Kinder sind {müde}.", ["müde", "müden", "müdes"]),
                       ("Das Wetter ist heute {schön}.", ["schön", "schönes", "schöne"]), ("Ich finde den Kurs {interessant}.", ["interessant", "interessanten", "interessiert"])]:
        S("adjektiv", text, "ADJ", opts, NOEND, {w: ("interessiert = interested (a person). The course is interessant." if w == "interessiert" else "Endings only appear BEFORE a noun (ein kleines Zimmer). After sein/finden: no ending.") for w in opts[1:]})
    S("adjektiv", "Die Suppe ist {zu} salzig. Ich kann sie nicht essen.", "ADJ", ["zu", "zu viel", "viel"], "zu + adjective = too (negative).",
      {"zu viel": "zu viel goes with nouns (zu viel Salz). Before an adjective → zu.", "viel": "viel doesn't intensify adjectives. → sehr / zu."})
    S("adjektiv", "Das Restaurant ist {sehr} gut. Wir gehen oft hin.", "ADJ", ["sehr", "zu", "viel"], "sehr = very (positive or neutral). zu = too (negative).",
      {"zu": "zu gut sounds like a problem. Positive → sehr.", "viel": "viel isn't used before adjectives like gut → sehr."})
    OPP = "Learn adjectives in opposite pairs."
    for text, opts, pair in [("Die Straße ist nicht laut, sie ist {ruhig}.", ["ruhig", "leer", "langsam"], "laut ↔ ruhig"),
                             ("Der Test war nicht schwer, er war {leicht}.", ["leicht", "schnell", "kurz"], "schwer ↔ leicht"),
                             ("Der Koffer ist nicht leicht, er ist {schwer}.", ["schwer", "groß", "voll"], "leicht ↔ schwer (weight)"),
                             ("Die Jacke ist nicht sauber, sie ist {schmutzig}.", ["schmutzig", "nass", "kaputt"], "sauber ↔ schmutzig"),
                             ("Die Antwort ist nicht falsch, sie ist {richtig}.", ["richtig", "gut", "fertig"], "falsch ↔ richtig")]:
        S("adjektiv", text, "ADJ", opts, f"{pair}. {OPP}", {w: f"'{w}' isn't the opposite here. {pair}." for w in opts[1:]})
    S("adjektiv", "Wie ist das Wetter? – Es ist {sonnig}.", "ADJ", ["sonnig", "Sonne", "sonnt"], "Weather adjectives: sonnig, windig, regnerisch, bewölkt.",
      {"Sonne": "die Sonne is a noun. Es ist + adjective → sonnig.", "sonnt": "There's no verb 'sonnen' for weather. → Es ist sonnig / Die Sonne scheint."})


def modal_meaning():
    M = [
     ("Morgen ist Sonntag.# / Ich#S / {muss}#MV / nicht#NEG / arbeiten.#INF", ["muss", "darf", "kann"], "muss nicht = don't have to (no obligation).", {"darf": "darf nicht = not allowed. On Sunday you just don't have to.", "kann": "kann nicht = unable."}),
     ("Hier ist ein Krankenhaus.# / Man#S / {darf}#MV / hier#ORT / nicht#NEG / laut sein.#INF", ["darf", "muss", "will"], "darf nicht = not allowed.", {"muss": "muss nicht = don't have to — but here it's forbidden.", "will": "wollen = want."}),
     ("Ich#S / {kann}#MV / gut#ADV / schwimmen.#INF", ["kann", "darf", "soll"], "können = ability (can).", {"darf": "dürfen = permission.", "soll": "sollen = someone else's advice/order."}),
     ("Der Arzt sagt,# / ich#S / {soll}#MV / mehr Wasser#AKK / trinken.#INF", ["soll", "will", "darf"], "sollen = advice or instruction from another person.", {"will": "wollen = your own wish. Here it's the doctor's advice.", "darf": "dürfen = permission."}),
     ("Mein Fuß tut weh.# / Ich#S / {kann}#MV / nicht#NEG / laufen.#INF", ["kann", "muss", "will"], "können = (physically) able.", {"muss": "muss nicht = don't have to.", "will": "will nicht = don't want to — but the problem is the foot."}),
     ("Im Bus#ORT / {muss}#MV / man#S / eine Fahrkarte#AKK / haben.#INF", ["muss", "darf", "will"], "müssen = obligation.", {"darf": "dürfen = permission. A ticket is required → muss.", "will": "wollen = want."}),
     ("Ich#S / {möchte}#V / bitte#ADV / einen Tee.#AKK", ["möchte", "will", "muss"], "Polite wish → möchte.", {"will": "Ich will … sounds rude when ordering.", "muss": "müssen = obligation."}),
     ("Mein Sohn#S / {will}#MV / Pilot#NOM / werden.#INF / Das ist sein Traum.#", ["will", "soll", "darf"], "wollen = a strong personal wish or plan.", {"soll": "sollen = someone else wants it.", "darf": "dürfen = permission."}),
     ("Kinder#S / {müssen}#MV / in Deutschland#ORT / zur Schule gehen.#INF", ["müssen", "dürfen", "wollen"], "Schulpflicht → müssen (obligation).", {"dürfen": "dürfen = permission. School is compulsory → müssen.", "wollen": "wollen = want."}),
     ("Du#S / {musst}#MV / das Formular#AKK / nicht heute#NEG / abgeben.#INF / Freitag ist auch okay.#", ["musst", "darfst", "kannst"], "musst nicht = don't have to.", {"darfst": "darfst nicht = not allowed — but Friday is okay, so there's no ban.", "kannst": "kannst nicht = unable."}),
     ("Entschuldigung,# / {darf}#MV / ich#S / hier#ORT / parken?#INF", ["darf", "muss", "will"], "Asking permission → Darf ich …?", {"muss": "Muss ich …? = Am I obliged to …?", "will": "Will ich …? asks about your own wish."}),
     ("Wo#W / {kann}#MV / man#S / hier#ORT / gut essen?#INF", ["kann", "muss", "darf"], "können = possibility (where is it possible).", {"muss": "müssen = obligation.", "darf": "dürfen = permission."}),
     ("{Kannst}#MV / du#S / mir#DAT / bitte das Salz geben?#INF", ["Kannst", "Musst", "Sollst"], "Polite request → Kannst du …? / Können Sie …?", {"Musst": "Musst du …? = Do you have to …?", "Sollst": "Sollst du …? = Are you supposed to …?"}),
     ("Wir#S / {sollen}#MV / die Hausaufgaben#AKK / bis Montag#ZEIT / machen.#INF / Das sagt die Lehrerin.#", ["sollen", "wollen", "dürfen"], "sollen = instruction from another person (the teacher).", {"wollen": "wollen = our own wish.", "dürfen": "dürfen = permission."}),
     ("Im Flugzeug#ORT / {darf}#MV / man#S / nicht rauchen.#INF", ["darf", "muss", "will"], "darf nicht = forbidden.", {"muss": "muss nicht = don't have to.", "will": "wollen = want."}),
    ]
    for spec, opts, rule, why in M:
        G("modal", spec, opts, rule + " (muss nicht ≠ darf nicht!)", why)


def einkein():
    KR = "kein/keine/keinen negate nouns with ein or no article. nicht negates verbs, adjectives, places and nouns with der/die/das or mein/dein …"
    for text, lab, opts, why in [
        ("Ich habe {kein} Auto.", "AKK", ["kein", "nicht", "keinen"], {"nicht": "Nouns with ein / no article → kein.", "keinen": "keinen is for der-nouns. das Auto → kein."}),
        ("Wir haben {keinen} Garten.", "AKK", ["keinen", "kein", "nicht"], {"kein": "der Garten in the Akkusativ → keinen.", "nicht": "Negate a noun → kein-."}),
        ("Sie hat {keine} Geschwister.", "AKK", ["keine", "keinen", "nicht"], {"keinen": "Geschwister is plural → keine.", "nicht": "Negate a noun → kein-."}),
        ("Ich esse {kein} Fleisch.", "AKK", ["kein", "keinen", "nicht"], {"keinen": "das Fleisch → kein.", "nicht": "A noun without article → kein."}),
        ("Er trinkt {keine} Milch.", "AKK", ["keine", "kein", "nicht"], {"kein": "die Milch → keine.", "nicht": "A noun without article → kein-."}),
        ("Das ist {nicht} mein Handy.", "NEG", ["nicht", "kein", "keine"], {"kein": "With mein/dein … use nicht.", "keine": "With mein/dein … use nicht."}),
        ("Das ist {nicht} der Bus nach Augsburg.", "NEG", ["nicht", "kein", "keinen"], {"kein": "With der/die/das use nicht.", "keinen": "With der/die/das use nicht."}),
        ("Ich kenne den Mann {nicht}.", "NEG", ["nicht", "kein", "keinen"], {"kein": "den Mann has a definite article → nicht at the end.", "keinen": "den Mann has a definite article → nicht."}),
        ("Heute regnet es {nicht}.", "NEG", ["nicht", "kein", "keine"], {"kein": "You negate the verb → nicht.", "keine": "You negate the verb → nicht."}),
        ("Ich habe heute {keine} Lust.", "AKK", ["keine", "nicht", "keinen"], {"nicht": "Lust is a noun → keine.", "keinen": "die Lust → keine."}),
        ("Wir brauchen {keinen} Kühlschrank.", "AKK", ["keinen", "kein", "keine"], {"kein": "der Kühlschrank in the Akkusativ → keinen.", "keine": "keine is for die/plural."}),
        ("Das ist {keine} Katze, das ist ein Hund.", "NOM", ["keine", "nicht", "kein"], {"nicht": "eine Katze → keine Katze.", "kein": "die Katze → keine."}),
        ("Ich habe {kein} Geld.", "AKK", ["kein", "keine", "nicht"], {"keine": "das Geld → kein.", "nicht": "A noun without article → kein."}),
        ("Ich verstehe {kein} Wort.", "AKK", ["kein", "nicht", "keinen"], {"nicht": "ein Wort → kein Wort.", "keinen": "das Wort → kein."}),
        ("Wir fahren heute {nicht} mit dem Auto.", "NEG", ["nicht", "kein", "keinem"], {"kein": "mit dem Auto has a definite article → nicht.", "keinem": "With dem Auto use nicht."}),
    ]:
        S("einkein", text, lab, opts, KR, why)
    POS = "Position of nicht: at the end for the whole sentence, but <b>before</b> adjectives, places, gern, and the infinitive/Partizip at the end."
    for prompt, spec, wrong in [
        ("I'm not coming tomorrow.", "Ich#S / komme#V / morgen#ZEIT / nicht.#NEG", [("Ich nicht komme morgen.", "The verb must stay in position 2."), ("Ich komme morgen kein.", "kein only goes before nouns.")]),
        ("I don't live in Berlin.", "Ich#S / wohne#V / nicht#NEG / in Berlin.#ORT", [("Ich wohne in Berlin nicht.", "nicht goes before a place."), ("Ich wohne kein Berlin.", "kein only negates nouns with ein / no article.")]),
        ("The coffee isn't hot.", "Der Kaffee#S / ist#V / nicht#NEG / heiß.#ADJ", [("Der Kaffee ist heiß nicht.", "nicht goes before the adjective."), ("Der Kaffee ist kein heiß.", "heiß is an adjective → nicht.")]),
        ("I can't swim.", "Ich#S / kann#MV / nicht#NEG / schwimmen.#INF", [("Ich kann schwimmen nicht.", "The infinitive stays at the very end; nicht goes before it."), ("Ich nicht kann schwimmen.", "The modal must be in position 2.")]),
        ("He doesn't like dancing.", "Er#S / tanzt#V / nicht gern.#NEG", [("Er tanzt gern nicht.", "nicht goes before gern."), ("Er nicht tanzt gern.", "The verb must be in position 2.")]),
        ("I have no time today.", "Ich#S / habe#V / heute#ZEIT / keine Zeit.#AKK", [("Ich habe heute nicht Zeit.", "Zeit is a noun without article → keine Zeit."), ("Ich habe keine heute Zeit.", "keine belongs directly before its noun.")]),
    ]:
        C("einkein", f"Which sentence is correct? ({prompt})", spec, wrong, POS)


def satzbau():
    P3 = "Subject before the verb puts the verb in position 3. After the first element, the verb comes next."
    RULE = "Verb in position 2! When a time, place or object takes position 1, the subject moves <b>behind</b> the verb."
    for spec, wrong in [
        ("Morgen#ZEIT / besuche#V / ich#S / meine Oma.#AKK", [("Morgen ich besuche meine Oma.", P3), ("Morgen meine Oma ich besuche.", "The verb comes far too late — position 2!")]),
        ("Am Sonntag#ZEIT / schlafen#V / wir#S / lange.#ADV", [("Am Sonntag wir schlafen lange.", P3), ("Am Sonntag lange wir schlafen.", "The verb must be in position 2.")]),
        ("In der Küche#ORT / steht#V / ein Tisch.#S", [("In der Küche ein Tisch steht.", P3), ("Ein Tisch in der Küche steht.", "The verb must be the 2nd element.")]),
        ("Kaffee#AKK / trinke#V / ich#S / jeden Tag.#ZEIT", [("Kaffee ich trinke jeden Tag.", P3), ("Kaffee jeden Tag ich trinke.", "The verb must be in position 2.")]),
        ("Nach dem Kurs#ZEIT / gehen#V / wir#S / essen.#INF", [("Nach dem Kurs wir gehen essen.", P3), ("Nach dem Kurs essen wir gehen.", "gehen is the conjugated verb → position 2; essen goes to the end.")]),
        ("Um 7 Uhr#ZEIT / klingelt#V / der Wecker.#S", [("Um 7 Uhr der Wecker klingelt.", P3), ("Der Wecker um 7 Uhr klingelt.", "The verb must be in position 2.")]),
        ("Im Sommer#ZEIT / fahren#V / viele Leute#S / ans Meer.#ORT", [("Im Sommer viele Leute fahren ans Meer.", P3), ("Im Sommer viele Leute ans Meer fahren.", "The verb only goes to the end in subordinate clauses.")]),
        ("Gestern#ZEIT / war#V / ich#S / im Kino.#ORT", [("Gestern ich war im Kino.", P3), ("Gestern im Kino ich war.", "The verb must be in position 2.")]),
        ("Heute Abend#ZEIT / koche#V / ich#S / Pasta.#AKK", [("Heute Abend ich koche Pasta.", P3), ("Heute Abend Pasta ich koche.", "The verb must be in position 2.")]),
        ("Vielleicht#ADV / kommt#V / er#S / morgen.#ZEIT", [("Vielleicht er kommt morgen.", P3), ("Vielleicht er morgen kommt.", "The verb must be in position 2.")]),
        ("Am Wochenende#ZEIT / will#MV / ich#S / Fahrrad#AKK / fahren.#INF", [("Am Wochenende ich will Fahrrad fahren.", P3), ("Am Wochenende will ich fahren Fahrrad.", "The infinitive goes to the very end.")]),
        ("Letztes Jahr#ZEIT / habe#HV / ich#S / Deutsch#AKK / gelernt.#P2", [("Letztes Jahr ich habe Deutsch gelernt.", P3), ("Letztes Jahr habe ich gelernt Deutsch.", "The Partizip II goes to the very end.")]),
        ("Morgens#ZEIT / trinkt#V / meine Mutter#S / Tee.#AKK", [("Morgens meine Mutter trinkt Tee.", P3), ("Meine Mutter morgens Tee trinkt.", "The verb only goes to the end in subordinate clauses.")]),
        ("Hier#ORT / wohnt#V / mein Kollege.#S", [("Hier mein Kollege wohnt.", P3), ("Hier wohnen mein Kollege.", "mein Kollege is singular → wohnt.")]),
        ("Um halb neun#ZEIT / fängt#V / der Unterricht#S / an.#PRE", [("Um halb neun der Unterricht fängt an.", P3), ("Um halb neun fängt an der Unterricht.", "The prefix an goes to the very end.")]),
        ("Dieses Buch#AKK / finde#V / ich#S / langweilig.#ADJ", [("Dieses Buch ich finde langweilig.", P3), ("Dieses Buch langweilig finde ich.", "The verb must be in position 2.")]),
    ]:
        C("satzbau", "Which sentence is correct?", spec, wrong, RULE)


def janein():
    DOCH = "Answering a <b>negative</b> question: <b>doch</b> = yes (the opposite of the negative), <b>nein</b> = no, I agree with the negative. ja is only for positive questions."
    for text, opts, why in [
        ("Bist du nicht müde? – {Doch}, ich bin sehr müde.", ["Doch", "Ja", "Nein"], {"Ja": "After a negative question, a positive answer is doch.", "Nein": "Nein would mean you're not tired."}),
        ("Kommst du nicht mit? – {Doch}, ich komme mit.", ["Doch", "Ja", "Nein"], {"Ja": "After a negative question, a positive answer is doch.", "Nein": "Nein would mean you're not coming."}),
        ("Hast du keinen Hunger? – {Nein}, ich habe keinen Hunger.", ["Nein", "Doch", "Ja"], {"Doch": "doch would mean you ARE hungry.", "Ja": "ja is confusing after a negative question. Agreeing with the negative → nein."}),
        ("Wohnst du in München? – {Ja}, ich wohne in München.", ["Ja", "Doch", "Nein"], {"Doch": "doch only answers negative questions.", "Nein": "The answer is positive → ja."}),
        ("Sprechen Sie kein Deutsch? – {Doch}, ein bisschen.", ["Doch", "Ja", "Nein"], {"Ja": "Positive answer to a negative question → doch.", "Nein": "Nein would mean you speak no German."}),
        ("Trinkst du keinen Kaffee? – {Nein}, ich trinke nur Tee.", ["Nein", "Doch", "Ja"], {"Doch": "doch would mean you DO drink coffee.", "Ja": "Agreeing with a negative question → nein."}),
    ]:
        S("janein", text, "", opts, DOCH, why)
    Q = "Yes/no question: the conjugated verb goes to position 1, the subject follows. Infinitive, Partizip II or prefix stay at the very end."
    for stmt, spec, wrong in [
        ("Du kannst schwimmen.", "Kannst#V1 / du#S / schwimmen?#INF", [("Kannst schwimmen du?", "The subject comes directly after the verb; the infinitive goes to the end."), ("Können du schwimmen?", "du → kannst.")]),
        ("Ihr steht früh auf.", "Steht#V1 / ihr#S / früh#ZEIT / auf?#PRE", [("Aufsteht ihr früh?", "The prefix separates and goes to the end."), ("Steht ihr auf früh?", "The prefix goes to the very end.")]),
        ("Er muss heute arbeiten.", "Muss#V1 / er#S / heute#ZEIT / arbeiten?#INF", [("Muss er arbeiten heute?", "The infinitive goes to the very end."), ("Muss heute er arbeiten?", "The subject comes directly after the verb.")]),
        ("Sie haben ein Zimmer reserviert.", "Haben#V1 / Sie#S / ein Zimmer#AKK / reserviert?#P2", [("Haben Sie reserviert ein Zimmer?", "The Partizip II goes to the very end."), ("Haben ein Zimmer Sie reserviert?", "The subject comes directly after the verb.")]),
        ("Du rufst Lisa an.", "Rufst#V1 / du#S / Lisa#AKK / an?#PRE", [("Anrufst du Lisa?", "The prefix separates and goes to the end."), ("Rufst du an Lisa?", "The prefix goes to the very end.")]),
    ]:
        C("janein", f"Make a yes/no question: „{stmt}“", spec, wrong, Q)


def run():
    wfragen(); moegen(); konnektoren(); man_wer(); zeitdativ(); alltag(); adjektiv(); modal_meaning(); einkein(); satzbau(); janein()
