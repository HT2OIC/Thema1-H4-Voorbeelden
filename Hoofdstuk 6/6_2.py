# Pokémon
# De speler verkent één zone: dorp
# Hij moet een Pokéball vinden en naar het bos gaan.
# Oefent op: 
# - beweging
# - botsingen
# - functies

import pgzrun

# Grootte van het venster
WIDTH = 1000
HEIGHT = 850

# Actoren: de speler, objecten en gebieden
dorp = Actor("pokemon_dorp")
speler = Actor("pokemon_ash")
speler.pos = (650, 260)
pokeball = Actor("pokemon_pokeball", (300, 625))
tekstveld = Rect((0, 750), (1000, 100))
deur_bos = Rect((450, 0), (100, 50))

# Tekst die onderaan het scherm verschijnt
boodschap = ""
opdracht = "Zoek een Pokéball."

def draw():
    # Teken alles op het scherm.
    screen.clear()

    draw_dorp()

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
    

def update():
    global boodschap, opdracht

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

pgzrun.go()