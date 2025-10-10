# Space Invaders
# De speler beweegt een schip en ontwijkt 5 aliens

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

actor1 = Actor("spaceinvaders_alien")
actor1.x = random.randrange(50, 1450, 100)
actor1.y = random.randint(-500, 0)
alien_lijst.append(actor1)

actor2 = Actor("spaceinvaders_alien")
actor2.x = random.randrange(50, 1450, 100)
actor2.y = random.randint(-500, 0)
alien_lijst.append(actor2)

actor3 = Actor("spaceinvaders_alien")
actor3.x = random.randrange(50, 1450, 100)
actor3.y = random.randint(-500, 0)
alien_lijst.append(actor3)

actor4 = Actor("spaceinvaders_alien")
actor4.x = random.randrange(50, 1450, 100)
actor4.y = random.randint(-500, 0)
alien_lijst.append(actor4)

actor5 = Actor("spaceinvaders_alien")
actor5.x = random.randrange(50, 1450, 100)
actor5.y = random.randint(-500, 0)
alien_lijst.append(actor5)

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

    alien_lijst[0].draw()
    alien_lijst[1].draw()
    alien_lijst[2].draw()
    alien_lijst[3].draw()
    alien_lijst[4].draw()

    screen.draw.text("Score: " + str(score), (1300,25), color=(0,255,0), fontsize=50)
    screen.draw.text("Levens: " + str(levens), (100,25), color=(0,255,0), fontsize=50)

def update():
    global score, levens

    # Alien 0: bewegen + detectie onderkant scherm + detectie botsing
    alien_lijst[0].y += 10

    if alien_lijst[0].y >= HEIGHT:
        score += 1
        reset_alien(alien_lijst[0])

    if schip.colliderect(alien_lijst[0]):
        levens -= 1
        reset_alien(alien_lijst[0])

    # Alien 1: bewegen + detectie onderkant scherm + detectie botsing
    alien_lijst[1].y += 10

    if alien_lijst[1].y >= HEIGHT:
        score += 1
        reset_alien(alien_lijst[1])

    if schip.colliderect(alien_lijst[1]):
        levens -= 1
        reset_alien(alien_lijst[1])

    # Alien 2: bewegen + detectie onderkant scherm + detectie botsing
    alien_lijst[2].y += 10

    if alien_lijst[2].y >= HEIGHT:
        score += 1
        reset_alien(alien_lijst[2])

    if schip.colliderect(alien_lijst[2]):
        levens -= 1
        reset_alien(alien_lijst[2])

    # Alien 3: bewegen + detectie onderkant scherm + detectie botsing
    alien_lijst[3].y += 10

    if alien_lijst[3].y >= HEIGHT:
        score += 1
        reset_alien(alien_lijst[3])

    if schip.colliderect(alien_lijst[3]):
        levens -= 1
        reset_alien(alien_lijst[3])

    # Alien 4: bewegen + detectie onderkant scherm + detectie botsing
    alien_lijst[4].y += 10

    if alien_lijst[4].y >= HEIGHT:
        score += 1
        reset_alien(alien_lijst[4])

    if schip.colliderect(alien_lijst[4]):
        levens -= 1
        reset_alien(alien_lijst[4])

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