# Super Mario
# Vereenvoudigde Super Mario: Mario beweegt links en rechts met de pijltjestoetsen, Goomba beweegt automatisch, er is botsingsdetectie met de munten en Goomba.
import pgzrun
import time

# Grootte van het venster
WIDTH = 1040
HEIGHT = 260

# Actoren instellen
achtergrond = 'mario_achtergrond'
mario = Actor('mario_lopen')
mario.pos = (50, 200)
goomba = Actor('mario_goomba')
goomba.pos = (600, 200)

# Meerdere muntjes op verschillende posities plaatsen
munten_posities = [(300, 200), (325, 100), (800, 200)]
munten = []
for pos in munten_posities:
    munt = Actor('mario_munt')
    munt.pos = pos
    munten.append(munt)

# Spelstatus in een dictionary
spel = {
    'score': 0,
    'levens': 3
}

# Spelvariabelen initialiseren
goomba_snelheid_x = -2

def draw():
    screen.clear()

    screen.blit(achtergrond, (0, 0))

    mario.draw()
    goomba.draw()

    for munt in munten:
        munt.draw()
        
    screen.draw.text(f"Score: {spel['score']}", (10, 10), color=(255,0,0), fontsize=40)
    screen.draw.text(f"Levens: {spel['levens']}", (10, 50), color=(255,0,0), fontsize=40)

def update():
    beweeg_mario()
    beweeg_goomba()
    verwerk_muntjes()
    controleer_einde_spel()

def beweeg_mario():
    """Laat Mario links of rechts bewegen met de pijltjestoetsen."""
    if keyboard.left:
        mario.x -= 4
    if keyboard.right:
        mario.x += 4

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
    for munt in munten:
        if mario.colliderect(munt):
            spel['score'] += 1
            munt.pos = (-50, -50)

def controleer_einde_spel():
    """Controleert of het spel verloren is."""
    if mario.colliderect(goomba):
        spel["levens"] -= 1
        goomba.pos = (-100, -100) # Wegteleporteren om meerdere detecties te voorkomen.

        if spel["levens"] <= 0:
            time.sleep(1)
            print(f"Game over! Score: {spel["score"]}")
            exit()
        else:
            time.sleep(0.5)
            goomba.pos = (600, 200)

pgzrun.go()