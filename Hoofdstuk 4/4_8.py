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

score = 0

# Achtergrond, mol, gaten en score tekenen
def draw():
    achtergrond.draw()

    screen.draw.filled_circle((75, 450), 50, "black")
    screen.draw.filled_circle((225, 450), 50, "black")
    screen.draw.filled_circle((375, 450), 50, "black")
    screen.draw.filled_circle((525, 450), 50, "black")
    screen.draw.filled_circle((675, 450), 50, "black")

    mol.draw()
    
    screen.draw.text("Score: " + str(score), (550,25), color = (255, 0, 0), fontsize = 50)

pgzrun.go()