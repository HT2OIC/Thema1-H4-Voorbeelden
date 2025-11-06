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
pokemon = Actor("pokemon_pikachu", (750, 300))
voorwerp = Actor("pokemon_pokeball", (-500, -500))

tekstveld = Rect((0, 750), (1000, 100))

deur_bos = Rect((450, 0), (100, 50))
deur_arena = Rect((450, 50), (100, 50))
midden_arena = Rect((WIDTH/2 - 50, HEIGHT/2 - 100), (50, 50))

# Tekst die onderaan het scherm verschijnt
boodschap = ""
opdracht = "Zoek een Pokéball."

# Speltoestand: scene (locatie)
scene = "dorp"  # Andere mogelijkheden: "bos", "arena", "einde"

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

def draw_dorp():
    """
        Elementen dorp tekenen.
    """
    screen.blit("pokemon_dorp", (0,0))
    speler.draw()
    pokeball.draw()

def draw_bos():
    """
        Elementen bos tekenen.
    """
    screen.blit("pokemon_bos", (0,0))
    speler.draw()
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
    global opdracht, boodschap, scene

    opdracht = opdracht1
    
    if speler.colliderect(voorwerp):
        boodschap = boodschap1
        opdracht = opdracht2

    elif speler.colliderect(deur):
        persoon.pos = (500, 700)
        boodschap = boodschap2
        opdracht = ""
        scene = volgende_scene

pgzrun.go()