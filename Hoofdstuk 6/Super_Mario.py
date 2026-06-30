# Super Mario
# Verzamel munten en ontwijk de Goomba. Je wint het spel als je tegen de vlaggenmast springt.

import pgzrun
import time
import pygame

# Grootte van het venster
WIDTH = 1920
HEIGHT = 1080
fullscreen = True

# Actoren instellen
achtergrond = 'mario_achtergrond'
mario = Actor('mario_lopen')
mario.pos = (50, 980)
goomba = Actor('mario_goomba')
goomba.pos = (1100, 985)


# Recthoeken op de plaats van het platform en de vlag
platform = Rect((520, 870), (170, 40))
vlag = Rect((WIDTH - 80, 750), (10, 200))

# Meerdere muntjes op verschillende posities plaatsen
munten_posities = [(450, 900), (600, 780), (1200, 900)]
munten = []
for pos in munten_posities:
    munt = Actor("mario_munt")
    munt.pos = pos
    munten.append(munt)

# Spelvariabelen initialiseren
spel = {
    'score': 0,
    'levens': 3
}

goomba_snelheid_x = -2
mario_snelheid_y = 0

op_platform = False

def draw():
    global fullscreen
    if fullscreen:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fullscreen = False 
    screen.clear()
    
    screen.blit(achtergrond, (0, 0))

    mario.draw()
    goomba.draw()

    for munt in munten:
        munt.draw()

    screen.draw.text(f"Score: {spel["score"]}", (10, 10), color=(255, 0, 0), fontsize=40)
    screen.draw.text(f"Levens: {spel['levens']}", (10, 50), color=(255,0,0), fontsize=40)

def update():
    beweeg_mario()
    beweeg_goomba()
    verwerk_muntjes()
    controleer_einde_spel()
    verwerk_zwaartekracht_en_platform()

def beweeg_mario():
    """Laat Mario links of rechts bewegen met behulp van de pijltjestoetsen."""
    global mario_snelheid_y, op_platform

    if keyboard.left:
        mario.x -= 4
    if keyboard.right:
        mario.x += 4

    # Nakijken of Mario op de grond staat.
    op_grond = mario.y >= 980

    # Als Mario op de grond staat wanneer op spatie is gedrukt, laten we hem springen.
    if keyboard.space and (op_grond or op_platform):
        sounds.mario_springen.play()
        mario.image = "mario_spring"
        clock.schedule_unique(mario_reset, 0.5)
        mario_snelheid_y -= 12
        op_platform = False
    
def beweeg_goomba():
    """Laat Goomba automatisch heen en weer lopen."""
    global goomba_snelheid_x
    goomba.x += goomba_snelheid_x
    if goomba.x > 1100:
        goomba_snelheid_x = -2
    elif goomba.x < 100:
        goomba_snelheid_x = 2

def verwerk_muntjes():
    """Controleert of Mario een muntje raakt en verhoogt de score."""
    for munt in munten:
        if mario.colliderect(munt):
            sounds.mario_munt.play()
            spel["score"] += 1
            munt.pos = (-50, -50)  # Muntje 'verdwijnt'

def controleer_einde_spel():
    """Controleert of het spel verloren of gewonnen is."""

    if mario.colliderect(goomba):
        spel["levens"] -= 1
        goomba.pos = (-100, -100) # Wegteleporteren om meerdere detecties te voorkomen.
        sounds.mario_verloren.play()
        
        if spel["levens"] <= 0:
            time.sleep(1)
            print(f"Game over! Score: {spel["score"]}")
            exit()
        else:
            time.sleep(0.5)
            goomba.pos = (1100, 985)
    
    if mario.colliderect(vlag):
        sounds.mario_gewonnen.play()
        time.sleep(1)
        print("Gewonnen!")
        print(f"Je behaalde {spel["score"]} punten.")
        exit()

def verwerk_zwaartekracht_en_platform():
    """Verwerkt zwaartekracht en botsing met platform of grond"""
    global mario_snelheid_y, op_platform

    # Zwaartekracht trekt Mario naar beneden.
    mario_snelheid_y += 0.5
    mario.y += mario_snelheid_y

    # Houd Mario op de grond. Anders zakt hij door de grond.
    if mario.y > 980:
        mario.y = 980
        mario_snelheid_y = 0

    # Botsing met platform.
    # Bovenkant: Mario landt op platform.
    # Onderkant: Mario botst tegen platform en komt terug op de grond.
    if mario.colliderect(platform):
        if mario_snelheid_y > 0 and mario.y < platform.top:
            mario.y = platform.top - mario.height / 2
            mario_snelheid_y = 0
            op_platform = True
        elif mario_snelheid_y < 0 and mario.y > platform.bottom:
            mario.y = platform.bottom + mario.height / 2
            mario_snelheid_y = 0


def mario_reset():
    """Reset Mario naar de lopende afbeelding."""
    mario.image = "mario_lopen"
  
pgzrun.go()