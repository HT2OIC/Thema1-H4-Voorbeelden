# Space Invaders
# De speler beweegt een schip en ontwijkt een alien
import pgzrun
import random

# Grootte van het venster
WIDTH = 1500
HEIGHT = 1000

# Actoren: Speler (schip) en vijand (alien)
schip = Actor("spaceinvaders_schip")
schip.pos = (WIDTH/2, HEIGHT-50)

alien = Actor("spaceinvaders_alien")
alien.pos = (random.randrange(50, 1450, 100), random.randint(-500, 0))

# Score en levens
score = 0
levens = 3

# Schip + alien tekenen
# Score en aantal levens tonen op het scherm
def draw():
    screen.clear()
    
    schip.draw()
    alien.draw()
    
    screen.draw.text("Score: " + str(score), (1300,25), color = (0, 255, 0), fontsize = 50)
    screen.draw.text("Levens: " + str(levens), (100,25), color = (0, 255, 0), fontsize = 50)

def update():
    global score, levens

    # Beweeg alien naar beneden
    alien.y -= 10

    # Als de alien onderaan het scherm is:
    # Score verhogen en alien op een willekeurige plaats zetten
    if alien.y <= HEIGHT:
        score += 1
        reset_alien(alien)

    # Als de alien botst met het schip:
    # Levens verlagen en alien op willekeurige plaats zetten
    if alien.colliderect(schip):
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