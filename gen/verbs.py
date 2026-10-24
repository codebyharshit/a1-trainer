"""A1 verb data and conjugation helpers.

Each RAW line: infinitive | english | du | er | aux | Partizip II | context#LABEL | flags
  - du / er only when irregular (vowel change etc.); otherwise computed
  - separable verbs: prefix+base, e.g. auf+stehen
  - aux: h = haben, s = sein (Perfekt)
  - context: words that follow the verb in a simple sentence, plus its structure label
  - flags: nopl = only singular subjects make sense
"""
RAW = """
machen|do / make|||h|gemacht|Sport#AKK|
spielen|play|||h|gespielt|gern Tennis#AKK|
wohnen|live|||h|gewohnt|in München#ORT|
kommen|come|||s|gekommen|aus Indien#ORT|
gehen|go|||s|gegangen|nach Hause#ORT|
lernen|learn|||h|gelernt|Deutsch#AKK|
kaufen|buy|||h|gekauft|Brot#AKK|
kochen|cook|||h|gekocht|Pasta#AKK|
trinken|drink|||h|getrunken|Kaffee#AKK|
schreiben|write|||h|geschrieben|eine E-Mail#AKK|
hören|listen to|||h|gehört|Musik#AKK|
brauchen|need|||h|gebraucht|Hilfe#AKK|
suchen|look for|||h|gesucht|eine Wohnung#AKK|
fragen|ask|||h|gefragt|den Lehrer#AKK|
finden|find|findest|findet|h|gefunden|den Schlüssel#AKK|
arbeiten|work|arbeitest|arbeitet|h|gearbeitet|bei Siemens#ORT|
warten|wait|wartest|wartet|h|gewartet|auf den Bus#ADV|
antworten|answer|antwortest|antwortet|h|geantwortet|sofort#ADV|
heißen|be called|heißt|heißt|h|geheißen|Anna#ADV|nopl
tanzen|dance|tanzt|tanzt|h|getanzt|gern Salsa#AKK|
reisen|travel|reist|reist|s|gereist|nach Spanien#ORT|
sprechen|speak|sprichst|spricht|h|gesprochen|Deutsch#AKK|
lesen|read|liest|liest|h|gelesen|die Zeitung#AKK|
sehen|see|siehst|sieht|h|gesehen|einen Film#AKK|
fahren|drive / go|fährst|fährt|s|gefahren|nach Berlin#ORT|
schlafen|sleep|schläfst|schläft|h|geschlafen|lange#ADV|
essen|eat|isst|isst|h|gegessen|Pizza#AKK|
nehmen|take|nimmst|nimmt|h|genommen|den Bus#AKK|
geben|give|gibst|gibt|h|gegeben|Tipps#AKK|
helfen|help|hilfst|hilft|h|geholfen|der Kollegin#DAT|
treffen|meet|triffst|trifft|h|getroffen|Freunde#AKK|
laufen|run|läufst|läuft|s|gelaufen|jeden Morgen#ZEIT|
tragen|wear / carry|trägst|trägt|h|getragen|eine Jacke#AKK|
waschen|wash|wäschst|wäscht|h|gewaschen|die Wäsche#AKK|
vergessen|forget|vergisst|vergisst|h|vergessen|das Passwort#AKK|
empfehlen|recommend|empfiehlst|empfiehlt|h|empfohlen|das Restaurant#AKK|
schwimmen|swim|||s|geschwommen|im See#ORT|
fliegen|fly|||s|geflogen|nach Rom#ORT|
bleiben|stay|||s|geblieben|zu Hause#ORT|
studieren|study|||h|studiert|Informatik#AKK|
telefonieren|phone|||h|telefoniert|mit Mama#DAT|
reparieren|repair|||h|repariert|das Fahrrad#AKK|
bezahlen|pay|||h|bezahlt|die Rechnung#AKK|
besuchen|visit|||h|besucht|die Oma#AKK|
verstehen|understand|||h|verstanden|die Frage#AKK|
beginnen|begin|||h|begonnen|um 9 Uhr#ZEIT|
bekommen|get / receive|||h|bekommen|eine Nachricht#AKK|
erzählen|tell|||h|erzählt|eine Geschichte#AKK|
verkaufen|sell|||h|verkauft|das Auto#AKK|
bringen|bring|||h|gebracht|den Kuchen#AKK|
denken|think|||h|gedacht|oft an Indien#ADV|
kennen|know (a person/place)|||h|gekannt|den Weg#AKK|
auf+stehen|get up|||s|aufgestanden|um 7 Uhr#ZEIT|
ein+kaufen|go shopping|||h|eingekauft|am Samstag#ZEIT|
an+rufen|call (phone)|||h|angerufen|die Mutter#AKK|
fern+sehen|watch TV|siehst|sieht|h|ferngesehen|am Abend#ZEIT|
ab+holen|pick up|||h|abgeholt|das Paket#AKK|
an+fangen|start|fängst|fängt|h|angefangen|um 8 Uhr#ZEIT|
auf+räumen|tidy up|||h|aufgeräumt|die Küche#AKK|
mit+kommen|come along|||s|mitgekommen|heute#ZEIT|
aus+gehen|go out|||s|ausgegangen|am Freitag#ZEIT|
zu+machen|close|||h|zugemacht|das Fenster#AKK|
auf+machen|open|||h|aufgemacht|die Tür#AKK|
ein+laden|invite|lädst|lädt|h|eingeladen|die Kollegen#AKK|
an+kommen|arrive|||s|angekommen|um 10 Uhr#ZEIT|
ab+fahren|depart|fährst|fährt|s|abgefahren|um 6 Uhr#ZEIT|
zurück+kommen|come back|||s|zurückgekommen|morgen#ZEIT|
mit+bringen|bring along|||h|mitgebracht|Wein#AKK|
um+steigen|change trains|||s|umgestiegen|in Augsburg#ORT|
aus+steigen|get off|||s|ausgestiegen|am Marienplatz#ORT|
ein+steigen|get on|||s|eingestiegen|vorne#ORT|
an+ziehen|put on|||h|angezogen|den Mantel#AKK|
frühstücken|have breakfast|||h|gefrühstückt|um 7 Uhr#ZEIT|
duschen|shower|||h|geduscht|am Morgen#ZEIT|
putzen|clean|||h|geputzt|das Bad#AKK|
zeigen|show|||h|gezeigt|den Weg#AKK|
glauben|believe|||h|geglaubt|das nicht#ADV|
lachen|laugh|||h|gelacht|viel#ADV|
malen|paint|||h|gemalt|ein Bild#AKK|
wandern|hike|||s|gewandert|in den Bergen#ORT|
fotografieren|take photos|||h|fotografiert|gern#ADV|
mieten|rent|||h|gemietet|eine Wohnung#AKK|
sagen|say|||h|gesagt|die Wahrheit#AKK|
bestellen|order|||h|bestellt|eine Pizza#AKK|
erklären|explain|||h|erklärt|die Grammatik#AKK|
feiern|celebrate|||h|gefeiert|den Geburtstag#AKK|
sitzen|sit|||h|gesessen|im Garten#ORT|
stehen|stand|||h|gestanden|an der Tür#ORT|
liegen|lie (be lying)|||h|gelegen|im Bett#ORT|
singen|sing|||h|gesungen|ein Lied#AKK|
gewinnen|win|||h|gewonnen|das Spiel#AKK|
verlieren|lose|||h|verloren|den Schlüssel#AKK|
wiederholen|repeat|||h|wiederholt|die Wörter#AKK|
packen|pack|||h|gepackt|den Koffer#AKK|
rauchen|smoke|||h|geraucht|nicht#NEG|
benutzen|use|||h|benutzt|das Handy#AKK|
aus+füllen|fill in|||h|ausgefüllt|das Formular#AKK|
auf+wachen|wake up|||s|aufgewacht|um 6 Uhr#ZEIT|
ein+schlafen|fall asleep|schläfst|schläft|s|eingeschlafen|spät#ZEIT|
um+ziehen|move house|||s|umgezogen|nach Köln#ORT|
los+fahren|set off|fährst|fährt|s|losgefahren|um 8 Uhr#ZEIT|
zu+hören|listen|||h|zugehört|gut#ADV|
aus+sehen|look (appearance)|siehst|sieht|h|ausgesehen|müde#ADJ|
"""
PRON = ["ich", "du", "er", "wir", "ihr", "sie"]
CAP = {"ich": "Ich", "du": "Du", "er": "Er", "wir": "Wir", "ihr": "Ihr", "sie": "Sie"}
PRON_EN = {"ich": "ich (I)", "du": "du (you, informal)", "er": "er/sie/es (he/she/it)",
           "wir": "wir (we)", "ihr": "ihr (you all)", "sie": "sie/Sie (they / formal you)"}


def parse():
    verbs = []
    for line in RAW.strip().splitlines():
        inf, en, du, er, aux, p2, ctx, flags = (line.split("|") + [""] * 8)[:8]
        pre, base = inf.split("+") if "+" in inf else ("", inf)
        ctx_text, ctx_lab = ctx.split("#")
        verbs.append(dict(inf=inf.replace("+", ""), base=base, pre=pre, en=en, du_irr=du, er_irr=er,
                          aux=aux, p2=p2, ctx=ctx_text, ctx_lab=ctx_lab, flags=[f for f in flags.split(",") if f]))
    return verbs


def stem(base):
    return base[:-1] if base.endswith(("eln", "ern")) else base[:-2]


def kind(v):
    """Why the verb is special in the present tense (for explanations)."""
    s = stem(v["base"])
    if v["du_irr"] and ("ä" in v["du_irr"] or "ä" in v["er_irr"]):
        return "a→ä"
    if v["du_irr"] and v["base"] not in ("finden", "arbeiten", "warten", "antworten", "heißen", "tanzen", "reisen"):
        return "e→i/ie"
    if s.endswith(("t", "d")):
        return "-t/-d stem"
    if s.endswith(("s", "ß", "z")):
        return "s-sound stem"
    return "regular"


def forms(v):
    b = v["base"]; s = stem(b)
    ins = s.endswith(("t", "d"))
    ss = s.endswith(("s", "ß", "z", "x"))
    f = {"ich": s + "e", "du": s + ("est" if ins else ("t" if ss else "st")), "er": s + ("et" if ins else "t"),
         "wir": b, "ihr": s + ("et" if ins else "t"), "sie": b}
    if v["du_irr"]: f["du"] = v["du_irr"]
    if v["er_irr"]: f["er"] = v["er_irr"]
    return f


def imperative(v):
    f = forms(v); s = stem(v["base"]); k = kind(v)
    if k == "e→i/ie":
        d = f["du"]
        du = d[:-1] if s.endswith(("s", "ß")) else (d[:-2] if d.endswith("st") else d[:-1])
    elif k == "-t/-d stem" or v["base"].endswith(("ern", "eln")):
        du = s + "e"
    else:
        du = s
    return {"du": du, "ihr": f["ihr"], "Sie": v["base"]}


SEIN = dict(ich="bin", du="bist", er="ist", wir="sind", ihr="seid", sie="sind")
HABEN = dict(ich="habe", du="hast", er="hat", wir="haben", ihr="habt", sie="haben")
WAR = dict(ich="war", du="warst", er="war", wir="waren", ihr="wart", sie="waren")
HATTE = dict(ich="hatte", du="hattest", er="hatte", wir="hatten", ihr="hattet", sie="hatten")
MODALS = {
    "können": dict(en="can", ich="kann", du="kannst", er="kann", wir="können", ihr="könnt", sie="können"),
    "müssen": dict(en="must / have to", ich="muss", du="musst", er="muss", wir="müssen", ihr="müsst", sie="müssen"),
    "wollen": dict(en="want to", ich="will", du="willst", er="will", wir="wollen", ihr="wollt", sie="wollen"),
    "dürfen": dict(en="may / be allowed to", ich="darf", du="darfst", er="darf", wir="dürfen", ihr="dürft", sie="dürfen"),
    "sollen": dict(en="should / be supposed to", ich="soll", du="sollst", er="soll", wir="sollen", ihr="sollt", sie="sollen"),
    "möchten": dict(en="would like", ich="möchte", du="möchtest", er="möchte", wir="möchten", ihr="möchtet", sie="möchten"),
}
