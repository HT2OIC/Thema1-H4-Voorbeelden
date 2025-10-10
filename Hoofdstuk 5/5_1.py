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
alien.pos = (random.randrange(50, 1450, 100), 0)

# Score en levens
score = 0
levens = 3

# Schip + alien tekenen
# Score en aantal levens tonen op het scherm
def draw():
    schip.draw()
    alien.draw()
    
    screen.draw.text("Score: " + str(score), (1300,25), color = (0, 255, 0), fontsize = 50)
    screen.draw.text("Levens: " + str(levens), (100,25), color = (0, 255, 0), fontsize = 50)

def update():
    pass

pgzrun.go()