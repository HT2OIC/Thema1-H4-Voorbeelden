# Whac-a-Mole
# Spel waarin de gebruiker zo snel mogelijk op mollen moet klikken.
# Oefent op:
# - Programmeren met functies, variabelen (global, +=) en constanten
# - Werken met randomness en coördinaten
# - Introductie tot Pygame Zero: afbeeldingen, muisklik, collision, tekst

import pgzrun

# Grootte van het venster
WIDTH = 750
HEIGHT = 500

# Actoren: de mol en de achtergrond
mol = Actor("whacamole_mol")
achtergrond = Actor("whacamole_achtergrond")

# Achtergrond en mol tekenen
def draw():
    achtergrond.draw()
    mol.draw()

pgzrun.go()