# Space Invaders
# De speler beweegt een schip en ontwijkt vallende aliens.
# Oefent op:
# - for- en while-lussen
# - lijsten doorlopen
# - functies definiëren en oproepen
# - botsingen detecteren
# - toetsenbordinput verwerken
# - werken met Actoren (positie, tekenen)
# - gebruik van random

import pgzrun
import random

# Grootte van het venster
WIDTH = 1500
HEIGHT = 1000

# Actoren: Speler (schip) en vijanden (aliens)
schip = Actor("spaceinvaders_schip")
schip.pos = (WIDTH/2, HEIGHT-50)

# Maak 5 aliens en stop ze in een lijst
alien_lijst = []

for i in range(5):
    alien = Actor("spaceinvaders_alien")
    alien.pos = (random.randrange(50, 1450, 100), random.randint(-500, 0))
    alien_lijst.append(alien)

# Score en levens
score = 0
levens = 3

# Startmechanisme met while-lus
start = input("Typ 'start' om het spel te beginnen: ")

while start.lower() != "start":
    start = input("Typ 'start' om het spel te beginnen: ")

# Schip + aliens tekenen
# Score en aantal levens tonen op het scherm
def draw():
    screen.clear()

    schip.draw()

    for alien in alien_lijst:
        alien.draw()

    screen.draw.text("Score: " + str(score), (1300,25), color=(0,255,0), fontsize=50)
    screen.draw.text("Levens: " + str(levens), (100,25), color=(0,255,0), fontsize=50)

def update():
    global score, levens, alien_lijst

    # Alle aliens: bewegen + detectie onderkant scherm + detectie botsing
    for alien in alien_lijst:
        alien.y += 10

        if alien.y >= HEIGHT:
            score += 1
            reset_alien(alien)

        if schip.colliderect(alien):
            levens -= 1
            reset_alien(alien)

    # Beweeg schip links/rechts
    if keyboard.right and schip.x <= WIDTH-50:
        schip.x += 5
    elif keyboard.left and schip.x >= 50:
        schip.x -= 5

    # Einde spel
    if levens < 0:
        print("Game over!")
        exit()

def reset_alien(alien):
    """
    Verplaatst de alien terug naar boven met een willekeurige positie.

    Argumenten:
        alien (Actor): De alien die gereset moet worden.
    """
    alien.x = random.randrange(50, WIDTH-50, 100)
    alien.y = random.randint(-500, 0)

pgzrun.go()