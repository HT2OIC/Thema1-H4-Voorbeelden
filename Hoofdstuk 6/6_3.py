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
dorp = Actor("pokemon_dorp")
bos = Actor("pokemon_bos")
arena = Actor("pokemon_arena")
speler = Actor("pokemon_ash")
speler.pos = (650, 260)
pokeball = Actor("pokemon_pokeball", (300, 625))
pokemon = Actor("pokemon_pikachu", (750, 300))
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
    dorp.draw()
    speler.draw()
    pokeball.draw()

def draw_bos():
    """
        Elementen bos tekenen.
    """
    bos.draw()
    speler.draw()
    pokemon.draw()

def draw_arena():
    """
        Elementen arena tekenen.
    """
    arena.draw()
    speler.draw()

def draw_einde():
    """
        Elementen einde tekenen.
    """
    arena.draw()
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
    
    # Nakijken of Asher een Pokéball heeft gevonden of het bos binnenwandelt.
    if speler.colliderect(pokeball):
        boodschap = "Pokéball gevonden!"
        opdracht = "Ga naar het bos."
    elif speler.colliderect(deur_bos):
        speler.pos = (500, 750)
        boodschap = "Welkom in het bos!"
        opdracht = ""
        scene = "bos"

pgzrun.go()