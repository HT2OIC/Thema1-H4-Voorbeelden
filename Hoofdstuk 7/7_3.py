# Volledige Super Mario: Mario kan links en rechts bewegen en springen. Hij kan op een platform springen. Als je tegen de vlaggenpaal springt, win je het spel.
# Leerdoelen:
# - Gebruik van Actoren en Rectangles
# - Botsingsdetectie
# - Lijsten gebruiken
# - Zwaartekracht en springen
# - Basisgame-logica (score, winnen/verliezen)

import pgzrun

# Grootte van het venster
WIDTH = 1040
HEIGHT = 260

# Actoren instellen
achtergrond = Actor("mario_achtergrond")
mario = Actor("mario_lopen")
mario.pos = (50, 200)
goomba = Actor("mario_goomba")
goomba.pos = (600, 200)

# Meerdere muntjes op verschillende posities plaatsen
munten_posities = [(300, 200), (325, 100), (800, 200)]
munten = []
for pos in munten_posities:
    munt = Actor("mario_munt")
    munt.pos = pos
    munten.append(munt)

# Spelvariabelen initialiseren
goomba_snelheid_x = -2
mario_snelheid_y = 0
score = 0

def draw():
    screen.clear()
    
    achtergrond.draw()

    mario.draw()
    goomba.draw()

    for munt in munten:
        munt.draw()

    screen.draw.text(f"Score: {score}", (10, 10), color=(255, 0, 0), fontsize=40)

def update():
    beweeg_mario()
    beweeg_goomba()
    verwerk_muntjes()
    controleer_einde_spel()

def beweeg_mario():
    """Laat Mario links of rechts bewegen met behulp van de pijltjestoetsen."""
    global mario_snelheid_y

    if keyboard.left:
        mario.x -= 4
    if keyboard.right:
        mario.x += 4

    # Als op de spatie is gedrukt, laten we Mario springen.
    if keyboard.space:
        mario_snelheid_y -= 12

    mario.y += mario_snelheid_y
    
def beweeg_goomba():
    """Laat Goomba automatisch heen en weer lopen."""
    global goomba_snelheid_x
    goomba.x += goomba_snelheid_x
    if goomba.x > 600:
        goomba_snelheid_x = -2
    elif goomba.x < 100:
        goomba_snelheid_x = 2

def verwerk_muntjes():
    """Controleert of Mario een muntje raakt en verhoogt de score."""
    global score
    for munt in munten:
        if mario.colliderect(munt):
            score += 1
            munt.pos = (-50, -50)  # Muntje 'verdwijnt'

def controleer_einde_spel():
    """Controleert of het spel verloren is."""
    if mario.colliderect(goomba):
        print("Game over!")
        print(f"Je behaalde {score} punten.")
        exit()
    
pgzrun.go()