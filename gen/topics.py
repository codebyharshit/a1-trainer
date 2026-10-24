"""Topics (in course order) with a short lesson shown when an answer is wrong."""
TOPICS = [
 ("verb", "Verb endings (Präsens)", "K1–2",
  "Remove -en from the infinitive to get the stem, then add: ich <b>-e</b> · du <b>-st</b> · er/sie/es <b>-t</b> · wir <b>-en</b> · ihr <b>-t</b> · sie/Sie <b>-en</b>. "
  "Stems ending in -t/-d add an extra -e- (du arbeit<b>e</b>st). Stems ending in an s-sound (s, ß, z) only add -t for du (du heiß<b>t</b>). "
  "Don't confuse du (-st) with ihr (-t)."),
 ("verb_irr", "Vowel-changing verbs", "K2",
  "Some verbs change their vowel <b>only</b> in the du and er/sie/es forms: e→i (sprechen → du spr<b>i</b>chst), e→ie (lesen → du l<b>ie</b>st), a→ä (fahren → du f<b>ä</b>hrst). "
  "ich, wir, ihr and sie keep the normal vowel: ich spreche, ihr sprecht. Learn these verbs with their er-form: fahren, er fährt."),
 ("seinhaben", "sein & haben", "K1–2",
  "sein: bin, bist, ist, sind, seid, sind. haben: habe, ha<b>st</b>, ha<b>t</b>, haben, habt, haben — haben loses the b in du and er/sie/es. "
  "These two are completely irregular, so they have to be memorised."),
 ("wfrage", "W-questions", "K1, 12",
  "W-word in position 1, verb in position 2, then the subject: <i>Wo wohnst du?</i> "
  "wo = where (place) · woher = where from · wohin = where to · wann = when · wer = who · wen = whom (Akk) · wem = to whom (Dat) · was = what · wie = how · wie viel = how much · wie viele = how many · warum = why · welch- = which."),
 ("janein", "Yes/no questions & word order", "K2",
  "In a yes/no question the verb moves to <b>position 1</b>, the subject follows: <i>Du spielst Tennis → Spielst du Tennis?</i> "
  "German has no helper 'do'. In normal statements the verb is always in position 2."),
 ("artikel", "der · die · das", "K2–3",
  "Every noun has a gender, and you must learn it with the noun. Reliable clues: -ung, -heit, -keit, -schaft, -ion → die · -chen, -lein → das · most nouns in -e → die · "
  "days, months, seasons, weather → der · Ge- words → mostly das · compounds take the article of the <b>last</b> part (das Kranken<b>haus</b>)."),
 ("plural", "Plural", "K2",
  "The plural article is always <b>die</b>. There are five plural types: no change (der Lehrer → die Lehrer) · -(e)n (die Lampe → die Lampen) · -e, often with umlaut (der Stuhl → die Stühle) · "
  "-er with umlaut (das Haus → die Häuser) · -s for foreign words and words ending in a vowel (das Auto → die Autos)."),
 ("einkein", "ein / kein / nicht", "K3",
  "ein (der/das) · eine (die) · no article in the plural. Negate a noun with <b>kein</b>: works exactly like ein (kein, keine; plural keine). "
  "Negate a verb, adjective or the whole statement with <b>nicht</b>: <i>Das ist nicht teuer. Ich komme nicht.</i>"),
 ("adjektiv", "sein + adjective", "K3",
  "After sein, an adjective takes <b>no ending</b>: <i>Der Turm ist hoch. Die Häuser sind alt.</i> Learn adjectives in opposite pairs (groß – klein, alt – neu/jung, teuer – billig)."),
 ("imp", "Imperative", "K3, 8",
  "<b>Sie:</b> infinitive + Sie, verb first (<i>Kommen Sie!</i>). <b>du:</b> du-form without -st and without du (<i>du kommst → Komm!</i>); e→i/ie stays (<i>Nimm! Lies!</i>), but a→ä does <b>not</b> (<i>Fahr!</i>). "
  "<b>ihr:</b> ihr-form without ihr (<i>Kommt!</i>). sein: Sei! · Seid! · Seien Sie! Separable prefixes go to the end: <i>Ruf mich an!</i>"),
 ("akk", "Akkusativ", "K4",
  "The direct object (what you buy, see, need, have …) is in the Akkusativ. <b>Only masculine changes:</b> der → <b>den</b>, ein → <b>einen</b>, kein → <b>keinen</b>, mein → <b>meinen</b>. "
  "die, das and the plural stay the same. Ask 'Wen oder was?' to find it. es gibt + Akkusativ."),
 ("moegen", "mögen / möchten / gern", "K4",
  "<b>mögen</b> = to like (in general): <i>Ich mag Kaffee.</i> <b>möchten</b> = would like (a wish now, polite): <i>Ich möchte einen Kaffee.</i> "
  "For activities use verb + <b>gern</b>: <i>Ich schwimme gern.</i> (not 'Ich mag schwimmen' at A1)."),
 ("uhrzeit", "Telling the time", "K5",
  "Informal: <i>Viertel nach</i> (quarter past), <i>Viertel vor</i> (quarter to), <i>halb</i> counts towards the <b>next</b> hour: 7:30 = halb acht. "
  "5/10/20 minutes: <i>fünf nach acht, zehn vor acht, zwanzig nach acht</i>. Formal (train, radio): <i>acht Uhr dreißig</i>."),
 ("zeitpraep", "am / um / im / von … bis", "K5–6",
  "<b>um</b> + clock time (um 8 Uhr) · <b>am</b> + days, parts of the day, dates, Wochenende (am Montag, am Abend, am 3. Mai) · <b>im</b> + months and seasons (im Mai, im Winter) · "
  "<b>von … bis</b> = from … to · Exception: <i>in der Nacht</i>."),
 ("datum", "Dates & ordinal numbers", "K6",
  "Ordinals: 1.–19. add -te (der zweite, der vierte) with three irregular ones: der <b>erste</b>, der <b>dritte</b>, der <b>siebte</b>. From 20.: -ste (der zwanzigste). "
  "With am the ending is -en: <i>am ersten Mai, am dritten Oktober</i>."),
 ("poss", "Possessive articles", "K5",
  "ich → mein · du → dein · er/es → sein · sie → ihr · wir → unser · ihr → euer · sie (they) → ihr · Sie → Ihr. "
  "They take the same endings as ein/kein: <b>-e</b> for die and plural (meine Mutter, meine Eltern), <b>-en</b> for masculine Akkusativ (meinen Bruder). euer drops its e before endings: eu<b>re</b> Kinder."),
 ("modal", "Modal verbs", "K5, 8",
  "können (can), müssen (must), wollen (want), dürfen (may), sollen (should – someone else's advice), möchten (would like). "
  "ich and er forms are identical and have no ending (ich kann, er kann). The modal is in position 2, the second verb goes to the <b>end</b> as an infinitive: <i>Ich <b>kann</b> gut Deutsch <b>sprechen</b>.</i> "
  "Trap: <i>muss nicht</i> = don't have to · <i>darf nicht</i> = not allowed."),
 ("trenn", "Separable verbs", "K6",
  "Prefixes like an-, auf-, aus-, ein-, mit-, ab-, zu-, fern-, zurück- split off and go to the <b>end</b> of the sentence: <i>Ich <b>stehe</b> um 7 Uhr <b>auf</b>.</i> "
  "With a modal verb the verb stays together at the end: <i>Ich muss früh aufstehen.</i> be-, ver-, er-, ent-, emp- never separate."),
 ("pron", "Personal pronouns (Akk & Dat)", "K6, 11",
  "Nominativ: ich, du, er, sie, es, wir, ihr, sie/Sie · Akkusativ: <b>mich, dich, ihn</b>, sie, es, uns, euch, sie/Sie · Dativ: <b>mir, dir, ihm, ihr, ihm</b>, uns, euch, <b>ihnen/Ihnen</b>. "
  "Akkusativ after für, ohne and verbs like sehen, lieben, besuchen, anrufen. Dativ after helfen, danken, gefallen, passen, gehören, schmecken and in <i>Wie geht es dir?</i>"),
 ("praet", "war & hatte (Präteritum)", "K6",
  "For the past of sein and haben, Germans normally use the Präteritum: ich <b>war</b>, du warst, er war, wir waren, ihr wart, sie waren · ich <b>hatte</b>, du hattest, er hatte, wir hatten, ihr hattet, sie hatten. "
  "ich and er forms are the same."),
 ("konnektor", "und / aber / oder / denn", "K7, 12",
  "These four connectors join two main clauses and do <b>not</b> change the word order: the verb stays in position 2 after them. "
  "und = and · aber = but · oder = or · denn = because. <i>Ich bleibe zu Hause, <b>denn</b> ich bin krank.</i>"),
 ("dativ", "Dativ & prepositions", "K7, 12",
  "Dativ articles: der → <b>dem</b> · das → <b>dem</b> · die → <b>der</b> · plural → <b>den</b> + -n on the noun (mit den Kinder<b>n</b>). ein → einem / einer. "
  "Always Dativ after: <b>aus, bei, mit, nach, seit, von, zu</b>. Contractions: zu dem = zum, zu der = zur, bei dem = beim, von dem = vom. "
  "nach + cities/countries, zu + people and places, bei + people/companies."),
 ("wechsel", "Wo? or Wohin? (Wechselpräpositionen)", "K9",
  "in, an, auf, unter, über, vor, hinter, neben, zwischen take <b>Dativ for Wo?</b> (position: liegen, stehen, hängen, sein) and <b>Akkusativ for Wohin?</b> (movement: legen, stellen, hängen, gehen). "
  "<i>Das Buch liegt auf <b>dem</b> Tisch. Ich lege das Buch auf <b>den</b> Tisch.</i> in dem = im, in das = ins, an dem = am."),
 ("perf_p2", "Perfekt: Partizip II", "K10–11",
  "Regular: <b>ge-</b> stem <b>-t</b> (gemacht, gearbeitet). Irregular: <b>ge-</b> … <b>-en</b>, often with a vowel change (getrunken, geschrieben). "
  "No ge- for verbs in <b>-ieren</b> (studiert) and with <b>be-, ver-, er-, ent-, emp-</b> (bezahlt, verstanden). Separable: ge goes in the middle (ein<b>ge</b>kauft, auf<b>ge</b>standen)."),
 ("perf_aux", "Perfekt: haben or sein?", "K10",
  "Most verbs use <b>haben</b>. Use <b>sein</b> for movement from A to B (gehen, fahren, fliegen, kommen, laufen, reisen, aufstehen) and change of state (werden, passieren) plus <b>sein</b> and <b>bleiben</b>. "
  "haben/sein is in position 2, the Partizip II goes to the <b>end</b>: <i>Ich <b>bin</b> nach Berlin <b>gefahren</b>.</i>"),
 ("welcher", "welcher? / dieser", "K11",
  "welch- and dies- take the same endings as der/die/das: dies<b>er</b> (der) · dies<b>e</b> (die, plural) · dies<b>es</b> (das) · Akkusativ masculine dies<b>en</b>. "
  "<i>Welcher Pullover? – Dieser hier.</i>"),
 ("zahlen", "Numbers", "K1–2",
  "21–99: ones first + und + tens, one word: drei<b>und</b>zwanzig. 1 → <b>ein</b>- in compounds (einundzwanzig). Tens: zwanzig, <b>dreißig</b> (ß!), vierzig, fünfzig, <b>sechzig</b>, <b>siebzig</b>, achtzig, neunzig. "
  "16 = sechzehn, 17 = siebzehn (the s / -en drop)."),
 ("satzbau", "Word order: verb in position 2", "K2, 7",
  "In a statement the conjugated verb is <b>always in position 2</b>. Position 1 can be the subject, a time, a place or an object. If something else is in position 1, the subject moves <b>behind</b> the verb: "
  "<i>Heute <b>gehe</b> ich ins Kino. Am Montag <b>habe</b> ich frei.</i>"),
 ("man_wer", "man · Wer? Wen? Wem?", "K12",
  "<b>man</b> = 'one / people in general', always with the er/sie/es verb form: <i>Hier darf man nicht rauchen.</i> "
  "Wer? asks for the subject (Nominativ) · Wen? for the Akkusativ object · Wem? for the Dativ object."),
 ("zeitdativ", "Time prepositions with Dativ", "K12",
  "<b>vor</b> = ago / before (vor zwei Tagen, vor dem Essen) · <b>seit</b> = since / for (still going on: seit drei Jahren) · <b>nach</b> = after (nach der Arbeit) · <b>in</b> = in (future: in einer Woche) · "
  "<b>ab</b> = from … on (ab Montag) · <b>bis</b> = until (bis Freitag, with no article). Dativ after vor, seit, nach, in."),
 ("akkpraep", "Akkusativ prepositions", "K4, 8",
  "<b>für, ohne, durch, gegen, um</b> (and bis) are always followed by the <b>Akkusativ</b>: <i>für den Chef, ohne meinen Bruder, durch die Stadt, gegen die Wand, um den See</i>. "
  "Pronouns too: für <b>dich</b>, ohne <b>ihn</b>. Memory trick: <b>FUDGO</b> – für, um, durch, gegen, ohne. Compare: mit, bei, zu, von, aus, nach, seit always take the Dativ."),
 ("vergleich", "Comparison: lieber, besser, als", "K7, 9",
  "gern → <b>lieber</b> → <b>am liebsten</b> · gut → <b>besser</b> → <b>am besten</b> · viel → <b>mehr</b> → <b>am meisten</b>. Regular: adjective + <b>-er</b> / <b>am …-sten</b> (schnell → schneller → am schnellsten); short words often add an umlaut (alt → älter, groß → größer, jung → jünger). "
  "Different: comparative + <b>als</b> (<i>Tee ist billiger als Kaffee</i>). The same: <b>so … wie</b> (<i>Er ist so alt wie ich</i>)."),
 ("laender", "Countries, languages, nationalities", "K1, 6",
  "Most countries have no article: <i>aus Spanien, in Spanien, nach Spanien</i>. Some take one, and then you need it in every case: <b>die Schweiz, die Türkei, die USA (pl.), die Niederlande (pl.), der Iran</b> → <i>aus der Schweiz, in der Schweiz (Wo?), in die Schweiz (Wohin?), in den USA</i>. "
  "Languages are written with a capital letter and no article: <i>Ich spreche Deutsch und Hindi.</i> Nationalities have a male and a female form: der Spanier / die Spanierin, der Deutsche / die Deutsche."),
 ("alltag", "Everyday situations", "K1–12",
  "Fixed phrases for real situations: greetings, phone calls, shops, restaurants, the doctor, directions, invitations. Learn them as whole chunks — you don't need to build them from grammar."),
]
VOCAB = [
 ("wort_art", "Vocabulary: der · die · das", "Wortschatz",
  "Every noun from the dictionary, most frequent first. Learn the article together with the noun — the reason tells you which rule applies (ending, meaning, compound) or that it simply has to be learned."),
 ("wort_bed", "Vocabulary: meanings", "Wortschatz",
  "What does the word mean? Words come in frequency order, so the ones you meet most often in real German come first."),
 ("wort_pl", "Vocabulary: plurals", "Wortschatz",
  "The plural has to be learned with each noun. Typical patterns: die-words → -(e)n · der-words → -e (often with umlaut) · short das-words → -er + umlaut · -er/-el/-en words → no change · foreign words and words ending in a vowel → -s."),
]
VOCAB += [
 ("wort_verb", "Vocabulary: verbs", "Wortschatz",
  "The A1 verbs with their meaning, the er-form (to see vowel changes) and the Perfekt (hat or ist + Partizip II)."),
 ("wort_adj", "Vocabulary: adjectives & small words", "Wortschatz",
  "Adjectives, adverbs and the small words that hold sentences together (leider, vielleicht, schon, noch …). Learn adjectives in opposite pairs."),
 ("hoeren", "Listening", "Hören",
  "Listen and pick what you heard. Pay attention to endings (den/dem, -e/-en, -st/-t) and vowels (a/ä, u/ü) — in spoken German they carry the grammar. Play it again as often as you like; the slow button helps."),
]
TOPICS += VOCAB
TOPIC_KEYS = [t[0] for t in TOPICS]

LABELS = {
 "S":   ("Subjekt", "Nominativ – who/what does the action. Ask: Wer? Was?"),
 "V":   ("Verb · Pos. 2", "The conjugated verb. In statements and W-questions it is always the 2nd element."),
 "V1":  ("Verb · Pos. 1", "In yes/no questions and imperatives the verb comes first."),
 "IMP": ("Imperativ · Pos. 1", "Command form, always first in the sentence."),
 "MV":  ("Modalverb · Pos. 2", "können, müssen, wollen, dürfen, sollen, möchten – conjugated in position 2."),
 "HV":  ("Hilfsverb · Pos. 2", "haben or sein in the Perfekt, conjugated in position 2."),
 "INF": ("Infinitiv · Ende", "With a modal verb the 2nd verb goes to the end, unconjugated."),
 "P2":  ("Partizip II · Ende", "The Perfekt participle goes to the very end."),
 "PRE": ("Präfix · Ende", "The prefix of a separable verb goes to the very end."),
 "AKK": ("Akkusativ", "Direct object. Ask: Wen? Was? – der → den, ein → einen."),
 "DAT": ("Dativ", "Indirect object or after a Dativ preposition. Ask: Wem? – der/das → dem, die → der."),
 "NOM": ("Nominativ (nach sein)", "After sein / heißen the noun stays in the Nominativ: Das ist ein Hund."),
 "ZEIT":("Zeit", "When? – time expressions."),
 "ORT": ("Ort / Richtung", "Where? Where from? Where to?"),
 "W":   ("Fragewort · Pos. 1", "Question word, always first in a W-question."),
 "ADJ": ("Adjektiv", "Describes something. After sein: no ending."),
 "KON": ("Konnektor · Pos. 0", "und, aber, oder, denn – stand between two clauses and don't count as a position."),
 "NEG": ("Negation", "nicht or kein."),
 "ADV": ("Angabe", "Extra information: how, how often, with whom …"),
}
