"""A1 vocabulary beyond nouns: verbs, adjectives/adverbs and function words, with meaning questions.

VERBS: infinitive | english | er-form (present) | Perfekt
ADJS / PHRASES: word | english | opposite (optional)
Lists are in learning order: the most basic words come first.
"""
import random, re
from .core import add

VERBS = """
sein|be|ist|ist gewesen
haben|have|hat|hat gehabt
heißen|be called|heißt|hat geheißen
kommen|come|kommt|ist gekommen
wohnen|live (reside)|wohnt|hat gewohnt
sprechen|speak|spricht|hat gesprochen
machen|do, make|macht|hat gemacht
gehen|go, walk|geht|ist gegangen
lernen|learn|lernt|hat gelernt
arbeiten|work|arbeitet|hat gearbeitet
spielen|play|spielt|hat gespielt
trinken|drink|trinkt|hat getrunken
essen|eat|isst|hat gegessen
kaufen|buy|kauft|hat gekauft
fahren|drive, ride, go (by vehicle)|fährt|ist gefahren
lesen|read|liest|hat gelesen
schreiben|write|schreibt|hat geschrieben
hören|hear, listen to|hört|hat gehört
sehen|see|sieht|hat gesehen
verstehen|understand|versteht|hat verstanden
fragen|ask|fragt|hat gefragt
antworten|answer|antwortet|hat geantwortet
sagen|say|sagt|hat gesagt
brauchen|need|braucht|hat gebraucht
suchen|look for|sucht|hat gesucht
finden|find|findet|hat gefunden
nehmen|take|nimmt|hat genommen
geben|give|gibt|hat gegeben
kennen|know (be familiar with)|kennt|hat gekannt
wissen|know (a fact)|weiß|hat gewusst
können|can, be able to|kann|hat gekonnt
müssen|must, have to|muss|hat gemusst
wollen|want|will|hat gewollt
dürfen|may, be allowed to|darf|hat gedurft
sollen|should, be supposed to|soll|hat gesollt
mögen|like|mag|hat gemocht
möchten|would like|möchte|–
kochen|cook|kocht|hat gekocht
schlafen|sleep|schläft|hat geschlafen
bleiben|stay|bleibt|ist geblieben
leben|live (be alive)|lebt|hat gelebt
lieben|love|liebt|hat geliebt
bezahlen|pay|bezahlt|hat bezahlt
kosten|cost|kostet|hat gekostet
zahlen|pay (the bill)|zahlt|hat gezahlt
öffnen|open|öffnet|hat geöffnet
schließen|close, shut|schließt|hat geschlossen
beginnen|begin|beginnt|hat begonnen
enden|end|endet|hat geendet
helfen|help|hilft|hat geholfen
danken|thank|dankt|hat gedankt
treffen|meet|trifft|hat getroffen
besuchen|visit|besucht|hat besucht
warten|wait|wartet|hat gewartet
laufen|run, walk|läuft|ist gelaufen
fliegen|fly|fliegt|ist geflogen
reisen|travel|reist|ist gereist
schwimmen|swim|schwimmt|ist geschwommen
tanzen|dance|tanzt|hat getanzt
singen|sing|singt|hat gesungen
malen|paint|malt|hat gemalt
studieren|study (at university)|studiert|hat studiert
telefonieren|be on the phone|telefoniert|hat telefoniert
fotografieren|take photos|fotografiert|hat fotografiert
reparieren|repair|repariert|hat repariert
buchstabieren|spell|buchstabiert|hat buchstabiert
wiederholen|repeat|wiederholt|hat wiederholt
erklären|explain|erklärt|hat erklärt
erzählen|tell (a story)|erzählt|hat erzählt
bekommen|get, receive|bekommt|hat bekommen
vergessen|forget|vergisst|hat vergessen
verkaufen|sell|verkauft|hat verkauft
vermieten|rent out|vermietet|hat vermietet
mieten|rent|mietet|hat gemietet
bestellen|order|bestellt|hat bestellt
empfehlen|recommend|empfiehlt|hat empfohlen
schmecken|taste|schmeckt|hat geschmeckt
gefallen|be pleasing to (like)|gefällt|hat gefallen
gehören|belong to|gehört|hat gehört
passen|fit, suit|passt|hat gepasst
stehen|stand|steht|hat gestanden
liegen|lie (be lying)|liegt|hat gelegen
sitzen|sit|sitzt|hat gesessen
hängen|hang|hängt|hat gehangen
stellen|put (upright)|stellt|hat gestellt
legen|lay, put (flat)|legt|hat gelegt
setzen|seat, put|setzt|hat gesetzt
bringen|bring|bringt|hat gebracht
holen|fetch, get|holt|hat geholt
tragen|carry, wear|trägt|hat getragen
waschen|wash|wäscht|hat gewaschen
putzen|clean|putzt|hat geputzt
duschen|shower|duscht|hat geduscht
frühstücken|have breakfast|frühstückt|hat gefrühstückt
wandern|hike|wandert|ist gewandert
feiern|celebrate|feiert|hat gefeiert
lachen|laugh|lacht|hat gelacht
weinen|cry|weint|hat geweint
glauben|believe|glaubt|hat geglaubt
denken|think|denkt|hat gedacht
meinen|mean, think (have an opinion)|meint|hat gemeint
hoffen|hope|hofft|hat gehofft
zeigen|show|zeigt|hat gezeigt
benutzen|use|benutzt|hat benutzt
packen|pack|packt|hat gepackt
rauchen|smoke|raucht|hat geraucht
regnen|rain|regnet|hat geregnet
schneien|snow|schneit|hat geschneit
scheinen|shine|scheint|hat geschienen
werden|become|wird|ist geworden
passieren|happen|passiert|ist passiert
gewinnen|win|gewinnt|hat gewonnen
verlieren|lose|verliert|hat verloren
schicken|send|schickt|hat geschickt
senden|send (a message)|sendet|hat gesendet
dauern|last, take (time)|dauert|hat gedauert
parken|park|parkt|hat geparkt
grillen|barbecue|grillt|hat gegrillt
joggen|jog|joggt|ist gejoggt
surfen|surf|surft|hat gesurft
chatten|chat (online)|chattet|hat gechattet
übersetzen|translate|übersetzt|hat übersetzt
unterschreiben|sign|unterschreibt|hat unterschrieben
verdienen|earn|verdient|hat verdient
vereinbaren|arrange (an appointment)|vereinbart|hat vereinbart
versuchen|try|versucht|hat versucht
wechseln|change, exchange|wechselt|hat gewechselt
wünschen|wish|wünscht|hat gewünscht
ziehen|pull|zieht|hat gezogen
drücken|push, press|drückt|hat gedrückt
rufen|call, shout|ruft|hat gerufen
springen|jump|springt|ist gesprungen
fallen|fall|fällt|ist gefallen
sterben|die|stirbt|ist gestorben
heiraten|marry|heiratet|hat geheiratet
gratulieren|congratulate|gratuliert|hat gratuliert
schenken|give (as a present)|schenkt|hat geschenkt
einladen|invite|lädt ein|hat eingeladen
anrufen|call (on the phone)|ruft an|hat angerufen
aufstehen|get up|steht auf|ist aufgestanden
einkaufen|go shopping|kauft ein|hat eingekauft
anfangen|start|fängt an|hat angefangen
aufhören|stop|hört auf|hat aufgehört
aufmachen|open|macht auf|hat aufgemacht
zumachen|close|macht zu|hat zugemacht
mitkommen|come along|kommt mit|ist mitgekommen
mitbringen|bring along|bringt mit|hat mitgebracht
mitnehmen|take along|nimmt mit|hat mitgenommen
abholen|pick up|holt ab|hat abgeholt
abfahren|depart|fährt ab|ist abgefahren
ankommen|arrive|kommt an|ist angekommen
aussteigen|get off|steigt aus|ist ausgestiegen
einsteigen|get on|steigt ein|ist eingestiegen
umsteigen|change (trains)|steigt um|ist umgestiegen
aufräumen|tidy up|räumt auf|hat aufgeräumt
fernsehen|watch TV|sieht fern|hat ferngesehen
ausgehen|go out|geht aus|ist ausgegangen
zurückkommen|come back|kommt zurück|ist zurückgekommen
anziehen|put on (clothes)|zieht an|hat angezogen
ausziehen|take off (clothes)|zieht aus|hat ausgezogen
umziehen|move (house)|zieht um|ist umgezogen
ausfüllen|fill in (a form)|füllt aus|hat ausgefüllt
ankreuzen|tick (a box)|kreuzt an|hat angekreuzt
aussehen|look (appearance)|sieht aus|hat ausgesehen
einschlafen|fall asleep|schläft ein|ist eingeschlafen
aufwachen|wake up|wacht auf|ist aufgewacht
anmachen|switch on|macht an|hat angemacht
ausmachen|switch off|macht aus|hat ausgemacht
vorstellen|introduce|stellt vor|hat vorgestellt
zuhören|listen|hört zu|hat zugehört
weggehen|go away, leave|geht weg|ist weggegangen
losfahren|set off|fährt los|ist losgefahren
spazieren gehen|go for a walk|geht spazieren|ist spazieren gegangen
Rad fahren|cycle|fährt Rad|ist Rad gefahren
Ski fahren|ski|fährt Ski|ist Ski gefahren
kennenlernen|get to know|lernt kennen|hat kennengelernt
sich freuen|be happy, look forward|freut sich|hat sich gefreut
sich waschen|wash (oneself)|wäscht sich|hat sich gewaschen
sich anziehen|get dressed|zieht sich an|hat sich angezogen
sich ausruhen|rest|ruht sich aus|hat sich ausgeruht
sich treffen|meet (each other)|trifft sich|hat sich getroffen
sich vorstellen|introduce oneself|stellt sich vor|hat sich vorgestellt
sich setzen|sit down|setzt sich|hat sich gesetzt
sich beeilen|hurry|beeilt sich|hat sich beeilt
sich fühlen|feel|fühlt sich|hat sich gefühlt
sich interessieren|be interested|interessiert sich|hat sich interessiert
sich entschuldigen|apologise|entschuldigt sich|hat sich entschuldigt
sich anmelden|register, sign up|meldet sich an|hat sich angemeldet
sich duschen|take a shower|duscht sich|hat sich geduscht
klingeln|ring (a bell)|klingelt|hat geklingelt
lächeln|smile|lächelt|hat gelächelt
mitmachen|join in|macht mit|hat mitgemacht
nennen|name, call|nennt|hat genannt
leihen|lend, borrow|leiht|hat geliehen
lassen|let, leave|lässt|hat gelassen
bitten|ask (for), request|bittet|hat gebeten
sammeln|collect|sammelt|hat gesammelt
schauen|look|schaut|hat geschaut
ändern|change|ändert|hat geändert
kontrollieren|check|kontrolliert|hat kontrolliert
markieren|mark|markiert|hat markiert
notieren|note down|notiert|hat notiert
ordnen|put in order|ordnet|hat geordnet
korrigieren|correct|korrigiert|hat korrigiert
ergänzen|complete, add|ergänzt|hat ergänzt
zuordnen|match|ordnet zu|hat zugeordnet
üben|practise|übt|hat geübt
wählen|choose, dial|wählt|hat gewählt
"""

ADJS = """
gut|good|schlecht
schlecht|bad|gut
groß|big, tall|klein
klein|small, short|groß
neu|new|alt
alt|old|jung
jung|young|alt
schön|beautiful, nice|hässlich
hässlich|ugly|schön
teuer|expensive|billig
billig|cheap|teuer
günstig|good value, inexpensive|
lang|long|kurz
kurz|short (length)|lang
schnell|fast|langsam
langsam|slow|schnell
heiß|hot|kalt
warm|warm|kalt
kalt|cold|warm
früh|early|spät
spät|late|früh
richtig|right, correct|falsch
falsch|wrong|richtig
leicht|easy, light|schwer
schwer|difficult, heavy|leicht
einfach|simple|kompliziert
kompliziert|complicated|einfach
voll|full|leer
leer|empty|voll
laut|loud|leise
leise|quiet|laut
hell|bright, light|dunkel
dunkel|dark|hell
nah|near|weit
weit|far|nah
hoch|high|niedrig
niedrig|low|hoch
dick|fat, thick|dünn
dünn|thin|dick
gesund|healthy|krank
krank|ill, sick|gesund
müde|tired|wach
wach|awake|müde
glücklich|happy|traurig
traurig|sad|glücklich
froh|glad|
zufrieden|satisfied|unzufrieden
böse|angry, evil|
nett|nice, kind|unfreundlich
freundlich|friendly|unfreundlich
unfreundlich|unfriendly|freundlich
lustig|funny|langweilig
langweilig|boring|interessant
interessant|interesting|langweilig
toll|great|
super|super|
prima|great, excellent|
wichtig|important|unwichtig
möglich|possible|unmöglich
frei|free, available|besetzt
besetzt|occupied, busy|frei
geöffnet|open|geschlossen
geschlossen|closed|geöffnet
offen|open|geschlossen
sauber|clean|schmutzig
schmutzig|dirty|sauber
ruhig|quiet, calm|laut
lecker|tasty|
süß|sweet|sauer
sauer|sour, annoyed|süß
salzig|salty|
scharf|spicy, sharp|mild
fertig|ready, finished|
bereit|ready, prepared|
pünktlich|punctual|unpünktlich
ledig|single|verheiratet
verheiratet|married|ledig
geschieden|divorced|
ganz|whole, quite|
genau|exact, exactly|
gleich|same, right away|
verschieden|different|gleich
allein|alone|zusammen
fremd|foreign, strange|
privat|private|
kaputt|broken|
nass|wet|trocken
trocken|dry|nass
sonnig|sunny|
windig|windy|
bewölkt|cloudy|
neblig|foggy|
rot|red|
blau|blue|
grün|green|
gelb|yellow|
schwarz|black|weiß
weiß|white|schwarz
grau|grey|
braun|brown|
orange|orange|
rosa|pink|
lila|purple|
bunt|colourful|
hungrig|hungry|satt
satt|full (not hungry)|hungrig
durstig|thirsty|
heute|today|
morgen|tomorrow|gestern
gestern|yesterday|morgen
jetzt|now|
bald|soon|
später|later|früher
früher|earlier, in the past|später
oft|often|selten
selten|rarely|oft
manchmal|sometimes|
immer|always|nie
nie|never|immer
schon|already|noch nicht
noch|still|
wieder|again|
gerade|just (now)|
sofort|immediately|
morgens|in the mornings|abends
abends|in the evenings|morgens
nachmittags|in the afternoons|
täglich|daily|
zuerst|first|zuletzt
dann|then|
danach|afterwards|vorher
vorher|before(hand)|danach
hier|here|dort
dort|there|hier
da|there|
links|left|rechts
rechts|right|links
geradeaus|straight on|
oben|up, upstairs|unten
unten|down, downstairs|oben
vorne|at the front|hinten
hinten|at the back|vorne
draußen|outside|drinnen
drinnen|inside|draußen
überall|everywhere|
viel|much, a lot|wenig
wenig|little, not much|viel
viele|many|wenige
alle|all, everyone|
etwas|something|nichts
nichts|nothing|etwas
alles|everything|nichts
mehr|more|weniger
genug|enough|
sehr|very|
zu|too (much)|
ziemlich|quite, rather|
fast|almost|
nur|only|
auch|also, too|
"""

PHRASES = """
ja|yes|
nein|no|
doch|yes (contradicting a negative)|
bitte|please, you're welcome|
danke|thank you|
vielleicht|maybe|
leider|unfortunately|
zusammen|together|
getrennt|separately|
gern|gladly, with pleasure|
lieber|rather, preferably|
am liebsten|most of all|
natürlich|of course|
sicher|sure, certainly|
wirklich|really|
eigentlich|actually|
also|so, well|
übrigens|by the way|
zum Beispiel|for example|
nicht|not|
kein|no, not a|
und|and|
aber|but|
oder|or|
denn|because|
wer|who|
was|what|
wo|where|
woher|where from|
wohin|where to|
wann|when|
wie|how|
warum|why|
wie viel|how much|
wie viele|how many|
wie lange|how long|
wie oft|how often|
welcher|which|
mit|with|
ohne|without|
für|for|
von|from, of|
nach|after, to (a city)|
bei|at (someone's place)|
seit|since|
bis|until|
gegen|against, around (time)|
durch|through|
um|at (clock time), around|
zwischen|between|
neben|next to|
hinter|behind|
über|over, above|
unter|under|
Entschuldigung|excuse me, sorry|
Tschüss|bye|
Auf Wiedersehen|goodbye|
Guten Morgen|good morning|
Gute Nacht|good night|
Herzlich willkommen|welcome|
Viel Glück|good luck|
Gute Besserung|get well soon|
Alles Gute|all the best|
"""

R = random.Random(2024)
# words close enough in meaning that they must never be offered as the "wrong" option against each other
SIMILAR = [{"heiß", "warm"}, {"ruhig", "leise"}, {"offen", "geöffnet"}, {"toll", "super", "prima", "gut"}, {"froh", "glücklich"},
           {"nett", "freundlich"}, {"günstig", "billig"}, {"bereit", "fertig"}, {"böse", "sauer"}, {"da", "dort"}, {"neu", "jung"}]
def similar(a, b):
    return any(a in g and b in g for g in SIMILAR)
STOP = {"a", "an", "the", "to", "be", "of", "at", "in", "on", "up", "not", "(a", "(by", "(with", "(at", "(as", "(an", "(be", "someone's"}


def parse(block, cols):
    out = []
    for line in block.strip().splitlines():
        parts = (line.split("|") + [""] * cols)[:cols]
        out.append([p.strip() for p in parts])
    return out


def tokens(gloss):
    """Content words of an English gloss, for detecting overlapping meanings."""
    words = re.findall(r"[a-z']+", gloss.lower())
    return {w for w in words if w not in STOP and len(w) > 1}


def distractors(entry, pool, key_gloss, key_answer, k=3):
    """Pick k other entries whose meaning (and answer text) doesn't overlap with the target."""
    own = tokens(key_gloss(entry))
    chosen, used = [], set(own)
    cands = [e for e in pool if e is not entry]
    R.shuffle(cands)
    for c in cands:
        t = tokens(key_gloss(c))
        if t & used or key_answer(c) == key_answer(entry) or key_answer(c) in [key_answer(x) for x in chosen]:
            continue
        chosen.append(c); used |= t
        if len(chosen) == k:
            break
    return chosen


def run():
    verbs = parse(VERBS, 4)
    words = parse(ADJS, 3) + parse(PHRASES, 3)
    rank = 0

    # ---------- verbs ----------
    for i, (inf, en, er, perf) in enumerate(verbs):
        forms = f"er {er}" + (f" · {perf}" if perf and perf != "–" else "")
        rule = f"<b>{inf}</b> = {en} · {forms}"
        near = verbs[max(0, i - 50): i + 50]
        ds = distractors(verbs[i], near, lambda e: e[1], lambda e: e[1])
        q = add("wort_verb", [[inf, ""]], [en] + [d[1] for d in ds], rule,
                {d[1]: f"„{d[1]}“ is {d[0]}." for d in ds}, prompt=f"What does „{inf}“ mean?", mode="choose")
        q["r"] = rank; rank += 1
        if i % 2 == 0:
            ds = distractors(verbs[i], near, lambda e: e[1], lambda e: e[0])
            q = add("wort_verb", [[inf, ""]], [inf] + [d[0] for d in ds], rule,
                    {d[0]: f"„{d[0]}“ means {d[1]}." for d in ds}, prompt=f"How do you say „to {en}“ in German?", mode="choose")
            q["r"] = rank + 3; rank += 1

    # ---------- adjectives, adverbs, function words ----------
    rank = 0
    for i, (w, en, opp) in enumerate(words):
        rule = f"<b>{w}</b> = {en}" + (f" · opposite: {opp}" if opp else "")
        near = words[max(0, i - 60): i + 60]
        ds = distractors(words[i], near, lambda e: e[1], lambda e: e[1])
        q = add("wort_adj", [[w, ""]], [en] + [d[1] for d in ds], rule,
                {d[1]: f"„{d[1]}“ is {d[0]}." for d in ds}, prompt=f"What does „{w}“ mean?", mode="choose")
        q["r"] = rank; rank += 1
        if i % 2 == 0:
            ds = distractors(words[i], near, lambda e: e[1], lambda e: e[0])
            q = add("wort_adj", [[w, ""]], [w] + [d[0] for d in ds], rule,
                    {d[0]: f"„{d[0]}“ means {d[1]}." for d in ds}, prompt=f"How do you say „{en}“ in German?", mode="choose")
            q["r"] = rank + 3; rank += 1
        if opp:
            pool = [e for e in parse(ADJS, 3) if e[0] not in (w, opp)]
            R.shuffle(pool)
            wr = []
            for e in pool:
                if e[2] == w or similar(e[0], opp) or similar(e[0], w): continue
                if e[0] not in wr and not (tokens(e[1]) & tokens(en)) and not (tokens(e[1]) & tokens(dict((x[0], x[1]) for x in parse(ADJS, 3)).get(opp, "#"))):
                    wr.append(e[0])
                if len(wr) == 3:
                    break
            gloss = {e[0]: e[1] for e in parse(ADJS, 3)}
            q = add("wort_adj", [[f"{w} ↔ {opp}", ""]], [opp] + wr, f"<b>{w}</b> ({en}) ↔ <b>{opp}</b> ({gloss.get(opp, '')}). Learn adjectives in opposite pairs.",
                    {x: f"„{x}“ means {gloss[x]}, not the opposite of {w}." for x in wr}, prompt=f"Opposite of „{w}“?", mode="choose")
            q["r"] = rank + 8; rank += 1
