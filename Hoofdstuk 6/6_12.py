# Pokémon
# De speler verkent drie zones: dorp, bos en arena.
# Hij moet een Pokéball vinden, een Pokémon vangen en naar de arena gaan.
# Oefent op: 
# - beweging
# - scenes
# - botsingen
# - dictionaries
# - statusbeheer
# - functies
# - f-strings

import pgzrun

# Grootte van het venster
WIDTH = 1000
HEIGHT = 850

# Actoren: de speler, objecten en gebieden
speler = Actor("pokemon_ash")
speler.pos = (650, 260)

pokeball = Actor("pokemon_pokeball", (300, 625))
pokeball.naam = "Pokéball" # We geven de actors een naam, zodat we dit als sleutel in de dictionary kunnen gebruiken.
pokemon = Actor("pokemon_pikachu", (750, 300))
pokemon.naam = "Pokémon"
voorwerp = Actor("pokemon_pokeball", (-500, -500))
voorwerp.naam = ""

tekstveld = Rect((0, 750), (1000, 100))

deur_bos = Rect((450, 0), (100, 50))
deur_arena = Rect((450, 50), (100, 50))
midden_arena = Rect((WIDTH/2 - 50, HEIGHT/2 - 100), (50, 50))

# Tekst die onderaan het scherm verschijnt
boodschap = ""
opdracht = "Zoek een Pokéball."

# Speltoestand: scene (locatie) en inventaris
scene = "dorp"  # Andere mogelijkheden: "bos", "arena", "einde"
inventaris = {
    "Pokéball": False,
    "Pokémon": False,
    "": True
}

def draw():
    # Teken alles op het scherm.
    screen.clear()

    if scene == "dorp":
        draw_dorp()
    elif scene == "bos":
        draw_bos()
    elif scene == "arena":
        draw_arena()
    elif scene == "einde":
        draw_einde()

    # Tekst tonen onderaan: opdracht en boodschap
    screen.draw.filled_rect(tekstveld, color="navy")
    screen.draw.text(boodschap, (20, 775), color = "red", fontsize = 30)
    screen.draw.text(opdracht, (20, 800), color = "white", fontsize = 30)

    # Alle items die op True staan in de inventaris op het scherm tonen.
    screen.draw.text("INVENTARIS:", (800, 770), color = "white", fontsize = 30)
    y = 800
    for item, heeft_item in inventaris.items():
        if heeft_item:
            screen.draw.text(f"- {item}", (800, y), color = "white", fontsize = 25)
            y += 25

def draw_dorp():
    """
        Elementen dorp tekenen.
    """
    screen.blit("pokemon_dorp", (0,0))
    speler.draw()
    # Voorwerp alleen tekenen als het nog niet in de inventaris zit.
    if not inventaris["Pokéball"]:
        pokeball.draw()

def draw_bos():
    """
        Elementen bos tekenen.
    """
    screen.blit("pokemon_bos", (0,0))
    speler.draw()
    if not inventaris["Pokémon"]:
        pokemon.draw()

def draw_arena():
    """
        Elementen arena tekenen.
    """
    screen.blit("pokemon_arena", (0,0))
    speler.draw()

def draw_einde():
    """
        Elementen einde tekenen.
    """
    screen.blit("pokemon_arena", (0,0))
    speler.draw()
    pokemon.draw()


def update():
    global boodschap, opdracht, scene

    # Asher met pijltjestoetsen bewegen.
    if keyboard.left:
        speler.x -= 4
    elif keyboard.right:
        speler.x += 4
    elif keyboard.up:
        speler.y -= 4
    elif keyboard.down:
        speler.y += 4
    
    # De scene_logica uitvoeren met de juiste argumenten.
    if scene == "dorp":
        scene_logica("Zoek een Pokéball.", "Ga naar het bos.", "Pokéball gevonden!", "Welkom in het bos!", pokeball, deur_bos, "bos", speler )
    elif scene == "bos":
        scene_logica("Vang een Pokémon!", "Ga naar de arena.", "Pokémon gevangen!", "Welkom in de arena!", pokemon, deur_arena, "arena", speler)
    elif scene == "arena":
        scene_logica("Ga naar het midden van de arena.", "", "Pikachu, ik kies jou!", "Einde! Druk op R om opnieuw te spelen.", voorwerp, midden_arena, "einde", pokemon)

def scene_logica(opdracht1, opdracht2, boodschap1, boodschap2, voorwerp, deur, volgende_scene, persoon):
    """
        Functie waarmee de opdracht en boodschap wordt aangepast. 
        Er wordt gecontroleerd op de botsing met een voorwerp en deur. 
        De volgende scène wordt gedefinieerd en de speler of Pikachu wordt van positie veranderd.

        argumenten:
            opdracht1, opdracht2 (str): Opdracht die getoond moet worden bij het begin en einde van de scène.
            boodschap1, boodschap2 (str): Boodschap die getoond moet worden bij het begin en einde van de scène.
            voorwerp (Actor): Voorwerp (Pokéball, Pokémon) dat verzameld moet worden.
            deur (Rect): Deur om naar de volgende scène te gaan.
            volgende_scene (str): Volgende scène. Kan bos, arena en einde bevatten.
            persoon (Actor): Asher of Pikachu die van positie veranderd moet worden.
    """
    global opdracht, boodschap, scene, inventaris

    # Opdracht1 blijft zichtbaar tot het voorwerp verzameld is.
    if not inventaris[voorwerp.naam]:
        opdracht = opdracht1
    
    if speler.colliderect(voorwerp):
        inventaris[voorwerp.naam] = True # Het voorwerp is verzameld. De waarde staat nu op True.
        boodschap = boodschap1
        opdracht = opdracht2

    elif speler.colliderect(deur) and inventaris[voorwerp.naam]:
        persoon.pos = (500, 700)
        boodschap = boodschap2
        opdracht = ""
        scene = volgende_scene

    # Als het juiste voorwerp nog niet is verzameld, mag de speler niet naar de volgende scène gaan.
    elif speler.colliderect(deur) and not inventaris[voorwerp.naam]:
        boodschap = f"Je hebt een {voorwerp.naam} nodig voor je naar {volgende_scene} kan gaan."

pgzrun.go()