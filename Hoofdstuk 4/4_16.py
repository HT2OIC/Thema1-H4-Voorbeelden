# Whac-a-Mole
# Spel waarin de gebruiker zo snel mogelijk op mollen moet klikken.
# Oefent op:
# - Programmeren met functies, variabelen (global, +=) en constanten
# - Werken met randomness en coördinaten
# - Introductie tot Pygame Zero: afbeeldingen, muisklik, collision, tekst

import pgzrun
import random

# Grootte van het venster
WIDTH = 750
HEIGHT = 500

# Actoren: de mol en de achtergrond
mol = Actor("whacamole_mol")
mol.pos = (75, 400)
achtergrond = Actor("whacamole_achtergrond")

# Snelheid van het spel (hoe vaak de mol van plaats verandert)
teller_snelheid = 0
snelheid = 50

score = 0

# Achtergrond, mol, gaten en score tekenen
def draw():
    achtergrond.draw()

    teken_gaten(75)
    teken_gaten(225)
    teken_gaten(375)
    teken_gaten(525)
    teken_gaten(675)

    mol.draw()
    
    screen.draw.text("Score: " + str(score), (550,25), color = (255, 0, 0), fontsize = 50)

# Laat de mol op een andere positie verschijnen volgens de ingestelde snelheid.
def update():
    global teller_snelheid

    teller_snelheid += 1

    if teller_snelheid >= snelheid:
        mol.x = mol_positie_bepalen()
        teller_snelheid = 0

def teken_gaten(x_positie):
    """Tekent een zwart gat op het opgegeven coördinaat.

    Argumenten:
        x_positie (int): De x-coördinaat van het gat."""
    
    screen.draw.filled_circle((x_positie, 450), 50, "black")


def mol_positie_bepalen():
    """Bepaalt willekeurig een nieuwe x-positie voor de mol.

    Return:
        int:  Een nieuw x-coördinaat voor de mol."""
    
    positie = random.choice([75, 225, 375, 525, 675])
    return positie

pgzrun.go()