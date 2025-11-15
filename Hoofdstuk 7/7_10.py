# Volledige Super Mario: Mario kan links en rechts bewegen en springen. Hij kan op een platform springen. Als je tegen de vlaggenpaal springt, win je het spel.
# Leerdoelen:
# - Gebruik van Actoren en Rectangles
# - Botsingsdetectie
# - Lijsten gebruiken
# - Zwaartekracht en springen
# - Basisgame-logica (score, winnen/verliezen)

import pgzrun
import time

# Grootte van het venster
WIDTH = 1040
HEIGHT = 260

# Actoren instellen
achtergrond = Actor("mario_achtergrond")
mario = Actor("mario_lopen")
mario.pos = (50, 200)
goomba = Actor("mario_goomba")
goomba.pos = (600, 200)

# Recthoeken op de plaats van het platform en de vlag
platform = Rect((275, 135), (100, 25))
vlag = Rect((1020, 50), (10, 100))


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
    verwerk_zwaartekracht_en_platform()

def beweeg_mario():
    """Laat Mario links of rechts bewegen met behulp van de pijltjestoetsen."""
    global mario_snelheid_y

    if keyboard.left:
        mario.x -= 4
    if keyboard.right:
        mario.x += 4

    # Nakijken of Mario op de grond staat.
    op_grond = mario.y >= 200

    # Als Mario op de grond staat wanneer op spatie is gedrukt, laten we hem springen.
    if keyboard.space and op_grond:
        sounds.mario_springen.play()
        mario_snelheid_y -= 12
    
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
            sounds.mario_munt.play()
            score += 1
            munt.pos = (-50, -50)  # Muntje 'verdwijnt'

def controleer_einde_spel():
    """Controleert of het spel verloren of gewonnen is."""

    if mario.colliderect(goomba):
        sounds.mario_verloren.play()
        time.sleep(1)
        print("Game over!")
        print(f"Je behaalde {score} punten.")
        exit()
    
    if mario.colliderect(vlag):
        sounds.mario_gewonnen.play()
        time.sleep(1)
        print("Gewonnen!")
        print(f"Je behaalde {score} punten.")
        exit()

def verwerk_zwaartekracht_en_platform():
    """Verwerkt zwaartekracht en botsing met platform of grond"""
    global mario_snelheid_y

    # Zwaartekracht trekt Mario naar beneden.
    mario_snelheid_y += 0.5
    mario.y += mario_snelheid_y

    # Houd Mario op de grond. Anders zakt hij door de grond.
    if mario.y > 200:
        mario.y = 200
        mario_snelheid_y = 0

    # Botsing met platform.
    # Bovenkant: Mario landt op platform.
    # Onderkant: Mario botst tegen platform en komt terug op de grond.
    if mario.colliderect(platform):
        if mario_snelheid_y > 0 and mario.y < platform.top:
            mario.y = platform.top - mario.height / 2
            mario_snelheid_y = 0
        elif mario_snelheid_y < 0 and mario.y > platform.bottom:
            mario.y = platform.bottom + mario.height / 2
            mario_snelheid_y = 0

    
pgzrun.go()