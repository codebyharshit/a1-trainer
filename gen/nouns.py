"""Curated A1 nouns for sentence templates: (article, noun, plural, english)."""
N = {}
def _add(spec):
    for line in spec.strip().splitlines():
        a, n, p, e = [x.strip() for x in line.split("|")]
        N[n] = dict(a=a, n=n, p=p, e=e)
_add("""
der|Apfel|Äpfel|apple
der|Kuchen|Kuchen|cake
der|Käse|Käse|cheese
der|Saft|Säfte|juice
der|Kaffee|Kaffees|coffee
der|Pullover|Pullover|jumper
der|Rucksack|Rucksäcke|backpack
der|Stuhl|Stühle|chair
der|Tisch|Tische|table
der|Laptop|Laptops|laptop
der|Schlüssel|Schlüssel|key
der|Schrank|Schränke|cupboard
der|Hund|Hunde|dog
der|Bus|Busse|bus
der|Zug|Züge|train
der|Bahnhof|Bahnhöfe|station
der|Supermarkt|Supermärkte|supermarket
der|Park|Parks|park
der|Arzt|Ärzte|doctor
der|Freund|Freunde|friend
der|Kollege|Kollegen|colleague
der|Bruder|Brüder|brother
der|Vater|Väter|father
der|Sohn|Söhne|son
der|Mantel|Mäntel|coat
der|Termin|Termine|appointment
der|Kühlschrank|Kühlschränke|fridge
der|Teppich|Teppiche|carpet
der|Spiegel|Spiegel|mirror
der|Balkon|Balkone|balcony
der|Garten|Gärten|garden
der|Computer|Computer|computer
der|Koffer|Koffer|suitcase
der|Brief|Briefe|letter
der|Film|Filme|film
der|Tee|Tees|tea
der|Löffel|Löffel|spoon
die|Tasche|Taschen|bag
die|Jacke|Jacken|jacket
die|Lampe|Lampen|lamp
die|Milch|–|milk
die|Banane|Bananen|banana
die|Hose|Hosen|trousers
die|Fahrkarte|Fahrkarten|ticket
die|Wohnung|Wohnungen|flat
die|Küche|Küchen|kitchen
die|Uhr|Uhren|clock
die|Brille|Brillen|glasses
die|Zeitung|Zeitungen|newspaper
die|Kirche|Kirchen|church
die|Bank|Banken|bank
die|Post|–|post office
die|Apotheke|Apotheken|pharmacy
die|Schule|Schulen|school
die|Arbeit|Arbeiten|work
die|Mutter|Mütter|mother
die|Schwester|Schwestern|sister
die|Freundin|Freundinnen|friend (f)
die|Kollegin|Kolleginnen|colleague (f)
die|Ärztin|Ärztinnen|doctor (f)
die|Tür|Türen|door
die|Wand|Wände|wall
die|Straße|Straßen|street
die|Stadt|Städte|city
die|Katze|Katzen|cat
die|Tomate|Tomaten|tomato
die|Flasche|Flaschen|bottle
die|Tasse|Tassen|cup
die|Pizza|Pizzen|pizza
die|Reise|Reisen|trip
die|Firma|Firmen|company
die|U-Bahn|U-Bahnen|underground
die|Straßenbahn|Straßenbahnen|tram
die|Universität|Universitäten|university
die|Party|Partys|party
die|Kreditkarte|Kreditkarten|credit card
das|Brot|Brote|bread
das|Buch|Bücher|book
das|Handy|Handys|mobile phone
das|Fahrrad|Fahrräder|bike
das|Hemd|Hemden|shirt
das|Ticket|Tickets|ticket
das|Sofa|Sofas|sofa
das|Auto|Autos|car
das|Bett|Betten|bed
das|Regal|Regale|shelf
das|Fenster|Fenster|window
das|Bild|Bilder|picture
das|Zimmer|Zimmer|room
das|Kind|Kinder|child
das|Haus|Häuser|house
das|Kino|Kinos|cinema
das|Restaurant|Restaurants|restaurant
das|Hotel|Hotels|hotel
das|Büro|Büros|office
das|Museum|Museen|museum
das|Café|Cafés|café
das|Geschenk|Geschenke|present
das|Glas|Gläser|glass
das|Ei|Eier|egg
das|Wörterbuch|Wörterbücher|dictionary
das|Kleid|Kleider|dress
das|Taxi|Taxis|taxi
das|Krankenhaus|Krankenhäuser|hospital
das|Mädchen|Mädchen|girl
das|Baby|Babys|baby
das|Foto|Fotos|photo
das|Messer|Messer|knife
das|Zentrum|Zentren|centre
""")
def g(*names):
    return [N[n] for n in names]
DEF = {"der": "der", "die": "die", "das": "das", "pl": "die"}
GEN_EN = {"der": "masculine (der)", "die": "feminine (die)", "das": "neuter (das)", "pl": "plural"}
