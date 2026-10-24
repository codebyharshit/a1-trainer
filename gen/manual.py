"""Hand-written questions for topics that don't template well.
Spec format: segments separated by ' / ', each 'text#LABEL'. {answer} marks the gap."""
from .core import add, choose

def M(t, spec, opts, rule, why=None, prompt=None):
    add(t, spec, opts, rule, why or {}, prompt=prompt)

def run():
    # ---------- W-Fragen ----------
    W = [
     ("{Wo}#W / wohnst#V / du?#S", ["Wo", "Woher", "Wohin"], "– In München. Wo = where (position).", "In München."),
     ("{Woher}#W / kommst#V / du?#S", ["Woher", "Wo", "Wohin"], "– Aus Indien. Woher = where from → answer with aus.", "Aus Indien."),
     ("{Wohin}#W / fährst#V / du#S / am Wochenende?#ZEIT", ["Wohin", "Wo", "Woher"], "– Nach Berlin. Wohin = where to → answer with nach/zu/in + Akk.", "Nach Berlin."),
     ("{Wann}#W / beginnt#V / der Kurs?#S", ["Wann", "Wie lange", "Wo"], "– Um 9 Uhr. Wann = when (a point in time).", "Um 9 Uhr."),
     ("{Wie lange}#W / dauert#V / der Film?#S", ["Wie lange", "Wann", "Wie viel"], "– Zwei Stunden. Wie lange = how long (duration).", "Zwei Stunden."),
     ("{Wer}#W / ist#V / das?#S", ["Wer", "Was", "Wen"], "– Das ist Frau Müller. Wer = who (Nominativ).", "Das ist Frau Müller."),
     ("{Was}#W / machst#V / du#S / am Wochenende?#ZEIT", ["Was", "Wer", "Wie"], "– Ich spiele Tennis. Was = what.", "Ich spiele Tennis."),
     ("{Wie}#W / heißen#V / Sie?#S", ["Wie", "Was", "Wer"], "– Ich heiße Anna. German says 'How are you called?' → Wie.", "Ich heiße Anna."),
     ("{Wie viel}#W / kostet#V / der Kaffee?#S", ["Wie viel", "Wie viele", "Wann"], "– 3 Euro. Price / uncountable amount → wie viel.", "3 Euro."),
     ("{Wie viele}#W / Geschwister#AKK / hast#V / du?#S", ["Wie viele", "Wie viel", "Welche"], "– Zwei. Countable things in the plural → wie viele.", "Zwei."),
     ("{Warum}#W / lernst#V / du#S / Deutsch?#AKK", ["Warum", "Wie", "Wann"], "– Weil ich in München wohne. Warum = why.", "Weil ich in München wohne."),
     ("{Welche}#W / Sprachen#AKK / sprichst#V / du?#S", ["Welche", "Welcher", "Was"], "– Hindi und Englisch. welch- = which; plural → welche.", "Hindi und Englisch."),
     ("{Wie alt}#W / bist#V / du?#S", ["Wie alt", "Wie viel", "Wann"], "– 28. Age: Wie alt bist du?", "28."),
     ("{Wen}#W / besuchst#V / du?#S", ["Wen", "Wem", "Wer"], "– Meinen Bruder. Wen = whom (Akkusativ): besuchen + Akk.", "Meinen Bruder."),
     ("{Wem}#W / hilfst#V / du?#S", ["Wem", "Wen", "Wer"], "– Meiner Mutter. Wem = to whom (Dativ): helfen + Dat.", "Meiner Mutter."),
     ("{Wie spät}#W / ist#V / es?#S", ["Wie spät", "Wann", "Wie lange"], "– Halb drei. Asking the time: Wie spät ist es? / Wie viel Uhr ist es?", "Halb drei."),
     ("{Wo}#W / arbeiten#V / Sie?#S", ["Wo", "Wohin", "Woher"], "– Bei Buycycle. Wo = where (position).", "Bei Buycycle."),
     ("{Wie oft}#W / gehst#V / du#S / ins Fitnessstudio?#ORT", ["Wie oft", "Wie lange", "Wann"], "– Dreimal pro Woche. Wie oft = how often.", "Dreimal pro Woche."),
    ]
    for spec, opts, rule, ans in W:
        why = {
         "Wo": "Wo asks for a position (In München). ", "Woher": "Woher asks for an origin (Aus Indien). ", "Wohin": "Wohin asks for a direction (Nach Berlin). ",
         "Wann": "Wann asks for a point in time (um 9 Uhr). ", "Wie lange": "Wie lange asks for a duration (zwei Stunden). ", "Wie viel": "Wie viel is for prices and things you can't count. ",
         "Wie viele": "Wie viele is for countable plurals. ", "Wer": "Wer asks for the subject (Nominativ). ", "Wen": "Wen = Akkusativ (whom). ", "Wem": "Wem = Dativ (to whom). ",
         "Was": "Was asks for a thing/activity. ", "Wie": "Wie asks how. ", "Welcher": "welcher is for der-nouns in the singular. ", "Welche": "welche is for die-nouns and the plural. ",
        }
        rule = rule.split(". ", 1)[1] if rule.startswith("–") else rule
        add("wfrage", spec, opts, f"Answer: „{ans}“ → {rule}", {o: why.get(o, "") + f"The answer „{ans}“ needs {opts[0]}." for o in opts[1:]},
            prompt="___ " + " ".join(p.split("#")[0] for p in spec.split(" / ")[1:]) + " – " + ans)

    # ---------- sein + Adjektiv ----------
    A = [("klein", "groß", ["alt", "billig"]), ("neu", "alt", ["klein", "laut"]), ("billig", "teuer", ["schön", "neu"]), ("leise", "laut", ["leer", "kalt"]),
         ("hässlich", "schön", ["teuer", "nah"]), ("leer", "voll", ["leise", "kurz"]), ("niedrig", "hoch", ["kurz", "alt"]), ("kalt", "warm", ["leise", "lang"]),
         ("kurz", "lang", ["klein", "jung"]), ("weit", "nah", ["voll", "hoch"]), ("jung", "alt", ["neu", "kurz"]), ("langsam", "schnell", ["leise", "spät"]),
         ("spät", "früh", ["langsam", "kurz"]), ("dunkel", "hell", ["kalt", "leise"]), ("schlecht", "gut", ["billig", "leer"])]
    for opp, adj, wr in A:
        add("adjektiv", [["Der Bus", "S"], ["ist", "V"], ["nicht " + adj + ", er ist {" + opp + "}.", "ADJ"]], [opp] + wr,
            f"{adj} ↔ {opp}. After sein the adjective has no ending. Learn adjectives in opposite pairs.",
            {w: f"'{w}' isn't the opposite of {adj}." + (" (alt ↔ neu for things, alt ↔ jung for people.)" if w in ("alt", "neu", "jung") else "") for w in wr},
            prompt=f"Opposite: Der Bus ist nicht {adj}, er ist ___.")
    for s, corr, wr in [("Die Wohnung ist {groß}.", "groß", ["große", "großen"]), ("Die Häuser sind {alt}.", "alt", ["alte", "alten"]), ("Das Essen ist {lecker}.", "lecker", ["leckeres", "leckere"]),
                        ("Der Kaffee ist {zu} heiß.", "zu", ["sehr zu", "so"]), ("München ist {sehr} schön.", "sehr", ["viel", "zu viel"])]:
        add("adjektiv", [[s, "ADJ"]], [corr] + wr, "After sein the adjective takes NO ending. sehr = very, zu = too (negative: zu teuer).",
            {w: ("Endings only appear when the adjective stands BEFORE a noun (eine große Wohnung). After sein: no ending." if w.endswith(("e", "en", "es")) and corr not in ("zu", "sehr") else
                 ("sehr = very; zu = too." if corr in ("zu", "sehr") else "")) for w in wr})

    # ---------- mögen / möchten / gern / es gibt ----------
    G = [("Ich {möchte}#V / einen Kaffee, bitte.#AKK", ["möchte", "mag", "will"], "A polite wish right now → möchte.", {"mag": "mögen = to like in general, not 'I'd like now'.", "will": "will (wollen) sounds rude when ordering."}),
         ("Ich {mag}#V / keine Tomaten.#AKK", ["mag", "möchte", "mage"], "General like/dislike → mögen: ich mag.", {"möchte": "möchte is a wish right now, not a general taste.", "mage": "mögen: ich mag (no -e)."}),
         ("{Magst}#V1 / du#S / Katzen?#AKK", ["Magst", "Möchtest", "Mögst"], "General liking → mögen: du magst.", {"Möchtest": "That asks if you want cats right now.", "Mögst": "mögen changes its vowel: du magst."}),
         ("Ich#S / {schwimme gern}#V", ["schwimme gern", "mag schwimmen", "gern schwimme"], "Liking an activity → verb + gern.", {"mag schwimmen": "At A1, activities use gern: Ich schwimme gern.", "gern schwimme": "The verb is in position 2; gern comes after it."}),
         ("{Möchten}#V1 / Sie#S / etwas trinken?#AKK", ["Möchten", "Mögen", "Wollen"], "Polite offer → Möchten Sie …?", {"Mögen": "Mögen Sie …? asks about general taste.", "Wollen": "Wollen Sie …? is too direct for a polite offer."}),
         ("Er#S / {mag}#V / seine Arbeit.#AKK", ["mag", "möchte", "magt"], "mögen: er mag (same as ich, no -t).", {"möchte": "He likes his job in general → mag.", "magt": "No -t: er mag."}),
         ("Was#AKK / {möchten}#V / Sie#S / essen?#INF", ["möchten", "mögen", "möchtet"], "In a restaurant: Was möchten Sie essen?", {"mögen": "mögen = general taste.", "möchtet": "möchtet is the ihr-form."}),
         ("Hier#ORT / {gibt es}#V / einen Supermarkt.#AKK", ["gibt es", "ist es", "es gibt"], "there is/are → es gibt + Akkusativ. After 'Hier' the verb comes 2nd: Hier gibt es …", {"ist es": "German uses es gibt for 'there is'.", "es gibt": "Verb in position 2: after Hier → gibt es."}),
         ("{Gibt es}#V1 / hier#ORT / eine Apotheke?#AKK", ["Gibt es", "Ist hier", "Es gibt"], "Is there …? → Gibt es …?", {"Ist hier": "'there is' = es gibt.", "Es gibt": "In a yes/no question the verb comes first: Gibt es …?"}),
         ("Wir#S / {essen}#V / gern#ADV / Pizza.#AKK", ["essen", "mögen essen", "gern essen"], "Liking food as an activity → verb + gern.", {"mögen essen": "Use gern, or simply: Wir mögen Pizza.", "gern essen": "The verb is in position 2, gern follows."})]
    for spec, opts, rule, why in G:
        add("moegen", spec, opts, rule, why)

    # ---------- Konnektoren ----------
    K = [("Ich bleibe zu Hause, {denn}#KON / ich#S / bin#V / krank.#ADJ", ["denn", "aber", "oder"], "denn = because. Verb stays in position 2 after denn.", {"aber": "aber = but (contrast).", "oder": "oder = or (alternative)."}),
         ("Ich mag Tee, {aber}#KON / ich#S / mag#V / keinen Kaffee.#AKK", ["aber", "denn", "oder"], "aber = but → a contrast.", {"denn": "denn gives a reason.", "oder": "oder offers an alternative."}),
         ("Möchtest du Tee {oder}#KON / Kaffee?#AKK", ["oder", "aber", "und"], "oder = or → a choice.", {"aber": "aber = but.", "und": "und = and — but this is a choice."}),
         ("Ich wohne in München {und}#KON / ich#S / arbeite#V / bei Buycycle.#ORT", ["und", "aber", "denn"], "und = and → adding information.", {"aber": "There's no contrast here.", "denn": "The second part isn't a reason."}),
         ("Ich lerne Deutsch, {denn}#KON / ich#S / wohne#V / in Deutschland.#ORT", ["denn", "oder", "aber"], "denn = because.", {"oder": "Not a choice.", "aber": "Not a contrast."}),
         ("Das Hotel ist schön, {aber}#KON / es#S / ist#V / teuer.#ADJ", ["aber", "und", "denn"], "Positive + negative → aber.", {"und": "und joins two similar facts. Here they contrast.", "denn": "teuer isn't the reason why it's schön."}),
         ("Kommst du heute {oder}#KON / morgen?#ZEIT", ["oder", "und", "denn"], "oder = choice between two options.", {"und": "und = both.", "denn": "denn = because."})]
    for spec, opts, rule, why in K:
        add("konnektor", spec, opts, rule + " und/aber/oder/denn are 'position 0' — they don't change word order.", why)
    for p, corr, wr in [("Ich gehe nicht ins Kino, …", "denn ich habe keine Zeit.", ["denn ich keine Zeit habe.", "denn habe ich keine Zeit."]),
                        ("Ich koche heute, …", "aber morgen essen wir im Restaurant.", ["aber morgen wir essen im Restaurant.", "aber wir morgen essen im Restaurant."]),
                        ("Er spielt Fußball …", "und sie spielt Tennis.", ["und spielt sie Tennis.", "und sie Tennis spielt."]),
                        ("Ich trinke Kaffee, …", "denn ich bin müde.", ["denn bin ich müde.", "denn ich müde bin."])]:
        spec = corr.split(" ", 1)
        add("konnektor", [[p + " " + spec[0], "KON"], [spec[1], ""]], [corr] + wr, "After und/aber/oder/denn the clause has normal word order: the conjugated verb is in position 2 (denn doesn't count as a position).",
            {w: ("The verb went to the end — that only happens after weil/dass (A2). After denn: normal order." if w.endswith(("habe.", "bin.", "spielt.")) else "Inversion is wrong here: the connector doesn't take position 1 — the subject (or time) does, then the verb.") for w in wr},
            prompt=p + " ___")

    # ---------- man / Wer Wen Wem ----------
    MW = [("Hier#ORT / {darf}#MV / man#S / nicht#NEG / rauchen.#INF", ["darf", "dürfen", "dürft"], "man always takes the er/sie/es form: man darf.", {"dürfen": "man is singular → er-form: darf.", "dürft": "dürft is the ihr-form."}),
          ("In Deutschland#ORT / {isst}#V / man#S / viel Brot.#AKK", ["isst", "essen", "esst"], "man + er-form: man isst.", {"essen": "Although man means 'people', the verb is singular.", "esst": "esst is the ihr-form."}),
          ("Wie#W / {sagt}#V / man#S / das#AKK / auf Deutsch?#ADV", ["sagt", "sagen", "sagst"], "man + er-form: Wie sagt man …?", {"sagen": "man takes the singular er-form.", "sagst": "sagst is the du-form."}),
          ("Hier#ORT / {kann}#MV / man#S / gut#ADV / essen.#INF", ["kann", "können", "kannst"], "man + er-form: man kann.", {"können": "man is grammatically singular.", "kannst": "kannst is the du-form."}),
          ("{Wer}#W / hat#V / angerufen?#P2", ["Wer", "Wen", "Wem"], "Asking for the subject → Wer?", {"Wen": "Wen asks for the Akkusativ object.", "Wem": "Wem asks for the Dativ object."}),
          ("{Wen}#W / hast#HV / du#S / getroffen?#P2", ["Wen", "Wer", "Wem"], "treffen + Akkusativ → Wen?", {"Wer": "du is the subject already — the person you met is the object.", "Wem": "treffen takes the Akkusativ, not Dativ."}),
          ("{Wem}#W / gehört#V / das Handy?#S", ["Wem", "Wen", "Wer"], "gehören + Dativ → Wem?", {"Wen": "gehören takes Dativ.", "Wer": "das Handy is the subject — you're asking for the owner (Dativ)."}),
          ("{Wem}#W / schenkst#V / du#S / die Blumen?#AKK", ["Wem", "Wen", "Wer"], "The person you give something to → Dativ → Wem?", {"Wen": "die Blumen is already the Akkusativ. The receiver is Dativ.", "Wer": "du is the subject."}),
          ("{Wen}#W / rufst#V / du#S / an?#PRE", ["Wen", "Wem", "Wer"], "anrufen + Akkusativ → Wen rufst du an?", {"Wem": "anrufen takes Akkusativ (unlike English 'call to').", "Wer": "du is the subject."})]
    for spec, opts, rule, why in MW:
        add("man_wer", spec, opts, rule, why)

    # ---------- time prepositions + Dativ ----------
    Z = [("Ich war {vor}#ZEIT / zwei Wochen in Paris.", ["vor", "seit", "in"], "Past event + ago → vor + Dativ.", {"seit": "seit = something still continuing now.", "in": "in = in the future."}),
         ("Ich lerne {seit}#ZEIT / einem Jahr Deutsch.", ["seit", "vor", "für"], "Started in the past and still going → seit + Dativ.", {"vor": "vor = ago (finished).", "für": "German uses seit here, not für."}),
         ("{Nach}#ZEIT / der Arbeit gehe ich ins Fitnessstudio.", ["Nach", "Vor", "Seit"], "After → nach + Dativ.", {"Vor": "vor = before.", "Seit": "seit = since."}),
         ("{In}#ZEIT / einer Woche habe ich Urlaub.", ["In", "Vor", "Seit"], "In the future → in + Dativ.", {"Vor": "vor = ago (past).", "Seit": "seit = since (still going)."}),
         ("{Vor}#ZEIT / dem Essen wasche ich die Hände.", ["Vor", "Nach", "Seit"], "Before → vor + Dativ.", {"Nach": "nach = after.", "Seit": "seit = since."}),
         ("Der Kurs geht {bis}#ZEIT / Freitag.", ["bis", "seit", "vor"], "until → bis (no article with days).", {"seit": "seit = since.", "vor": "vor = before / ago."}),
         ("{Ab}#ZEIT / Montag arbeite ich wieder.", ["Ab", "Seit", "Bis"], "from … on (future start) → ab.", {"Seit": "seit is for something that started in the past.", "Bis": "bis = until."}),
         ("Ich wohne seit drei {Jahren}#ZEIT / hier.", ["Jahren", "Jahre", "Jahr"], "seit + Dativ plural → noun gets -n: drei Jahren.", {"Jahre": "Dativ plural adds -n: Jahren.", "Jahr": "drei = plural."}),
         ("Vor zwei {Tagen}#ZEIT / war ich krank.", ["Tagen", "Tage", "Tag"], "vor + Dativ plural → Tagen.", {"Tage": "Dativ plural adds -n: Tagen.", "Tag": "zwei = plural."}),
         ("Wir treffen uns {in}#ZEIT / zehn Minuten.", ["in", "nach", "vor"], "In 10 minutes (from now) → in.", {"nach": "nach + time span is 'after', usually about the past.", "vor": "vor = ago."})]
    for spec, opts, rule, why in Z:
        add("zeitdativ", spec, opts, rule, why)

    # ---------- Alltag ----------
    AL = [("Someone asks: „Wie geht es Ihnen?“", "Danke, gut. Und Ihnen?", ["Ich bin 30 Jahre alt.", "Ich heiße gut."], "Answer and ask back with the same form: Und Ihnen? (formal) / Und dir? (informal)."),
          ("End of a phone call:", "Auf Wiederhören!", ["Gute Nacht!", "Herzlich willkommen!"], "On the phone: Auf Wiederhören (hear). Auf Wiedersehen is face to face."),
          ("You answer the phone at work:", "Firma Weber, Anna Schmidt, guten Tag.", ["Hallo, wer ist da?", "Ja?"], "In Germany you answer business calls with company + full name + greeting."),
          ("A tourist asks for the way. You say:", "Gehen Sie geradeaus und dann links.", ["Ich gehe geradeaus und links.", "Geradeaus Sie gehen links."], "Directions = Sie-imperative: verb first."),
          ("In a restaurant you want to pay:", "Ich möchte bitte bezahlen.", ["Ich will zahlen jetzt.", "Ich bezahle möchte."], "Polite: möchte + infinitive at the end. Also common: Zahlen, bitte!"),
          ("The waiter asks: „Zusammen oder getrennt?“ You pay only for yourself:", "Getrennt, bitte.", ["Zusammen, bitte.", "Allein, bitte."], "getrennt = separately; zusammen = together."),
          ("At the doctor: „Was fehlt Ihnen?“", "Ich habe Kopfschmerzen.", ["Ich fehle Kopf.", "Mein Kopf hat Schmerzen gern."], "Was fehlt Ihnen? = What's wrong? → Ich habe … (Kopf-/Bauch-/Halsschmerzen)."),
          ("Compliment: That jacket looks good on you.", "Die Jacke steht Ihnen gut.", ["Die Jacke ist Ihnen gut.", "Die Jacke gefällt Ihnen gut."], "stehen + Dativ = to suit someone. gefallen = to like."),
          ("Declining an invitation politely:", "Das geht leider nicht.", ["Das geht leider ja.", "Nein, ich gehe nicht gern."], "leider = unfortunately. Das geht leider nicht = I'm afraid that doesn't work."),
          ("Accepting an invitation:", "Gern! Wann denn?", ["Gern habe ich.", "Ja, ich bin gern."], "Gern! / Sehr gern! / Das klingt gut!"),
          ("It's raining:", "Es regnet.", ["Er regnet.", "Das regnet."], "Weather always uses es: Es regnet, es schneit, es ist kalt."),
          ("At the hotel reception:", "Ich habe ein Zimmer reserviert.", ["Ich habe ein Zimmer gereserviert.", "Ich bin ein Zimmer reserviert."], "Perfekt of -ieren verbs: no ge-. reservieren takes haben."),
          ("Your colleague sneezes. You say:", "Gesundheit!", ["Guten Appetit!", "Prost!"], "Gesundheit! = bless you."),
          ("Before eating together:", "Guten Appetit!", ["Prost!", "Mahlzeit gut!"], "Guten Appetit! (In Bavarian offices you'll also hear Mahlzeit! around lunchtime.)"),
          ("At the bakery:", "Ich hätte gern zwei Brötchen, bitte.", ["Ich will zwei Brötchen.", "Gib mir zwei Brötchen."], "Polite ordering: Ich hätte gern … / Ich möchte …"),
          ("In a shop: you're just looking.", "Danke, ich schaue nur.", ["Danke, ich gucke nichts.", "Nein, ich kaufe nicht."], "Ich schaue nur / Ich sehe mich nur um = I'm just looking."),
          ("You didn't understand. You say:", "Wie bitte? Können Sie das wiederholen?", ["Was? Nochmal!", "Ich nicht verstehe."], "Polite: Wie bitte? Können Sie das bitte wiederholen / langsamer sprechen?"),
          ("You're late for a meeting:", "Entschuldigung, ich bin zu spät.", ["Sorry, ich habe spät.", "Entschuldigung, ich bin spät."], "zu spät = too late / late (for an appointment)."),
          ("Asking a stranger the time:", "Entschuldigung, wie spät ist es?", ["Was ist die Zeit?", "Wie viel Zeit ist es?"], "Wie spät ist es? / Wie viel Uhr ist es?"),
          ("At the train station:", "Eine Fahrkarte nach Augsburg, bitte.", ["Ein Ticket für Augsburg fahren.", "Ich will Augsburg."], "nach + city. Hin und zurück = return; einfach = one way."),
          ("You want to make a doctor's appointment:", "Ich möchte einen Termin vereinbaren.", ["Ich will einen Termin machen jetzt.", "Ich möchte eine Verabredung."], "Termin = appointment (doctor, office). Verabredung = date / meeting with friends."),
          ("Introducing yourself formally:", "Darf ich mich vorstellen? Ich bin Anna Schmidt.", ["Ich vorstelle mich: Anna.", "Mein Name heißt Anna."], "Mein Name ist … / Ich heiße … / Ich bin … (not 'Mein Name heißt')."),
          ("Ending a formal email:", "Mit freundlichen Grüßen", ["Liebe Grüße", "Tschüss"], "Formal: Mit freundlichen Grüßen. Informal: Viele Grüße / Liebe Grüße."),
          ("Starting a formal email to an unknown person:", "Sehr geehrte Damen und Herren,", ["Hallo Leute,", "Liebe Damen und Herren,"], "Formal opening: Sehr geehrte Damen und Herren, / Sehr geehrte Frau Müller,"),
          ("Your friend says: „Ich habe morgen eine Prüfung.“", "Viel Glück!", ["Gute Besserung!", "Herzlichen Glückwunsch!"], "Viel Glück / Viel Erfolg = good luck. Gute Besserung = get well soon."),
          ("Your colleague is ill:", "Gute Besserung!", ["Viel Spaß!", "Gesundheit!"], "Gute Besserung! = get well soon."),
          ("It's your friend's birthday:", "Alles Gute zum Geburtstag!", ["Gute Besserung!", "Viel Glück zum Geburtstag!"], "Alles Gute zum Geburtstag! / Herzlichen Glückwunsch!"),
          ("Leaving the office on Friday:", "Schönes Wochenende!", ["Gute Nacht!", "Guten Appetit!"], "Schönes Wochenende! – Danke, gleichfalls! (you too)"),
          ("Someone says „Schönen Tag noch!“ You reply:", "Danke, gleichfalls!", ["Bitte schön!", "Gern geschehen!"], "gleichfalls = the same to you."),
          ("Someone thanks you. You reply:", "Gern geschehen!", ["Gleichfalls!", "Danke!"], "Bitte! / Gern geschehen! / Kein Problem!")]
    for p, corr, wr, rule in AL:
        why = {w: "Not natural German here. " + rule for w in wr}
        add("alltag", [[corr, ""]], [corr] + wr, rule, why, prompt=p, mode="choose")
