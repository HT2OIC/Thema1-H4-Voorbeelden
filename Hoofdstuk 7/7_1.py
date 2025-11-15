# Vereenvoudigde Super Mario: Mario beweegt links en rechts met de pijltjestoetsen, Goomba beweegt automatisch, er is botsingsdetectie met de munten en Goomba.
# Leerdoelen:
# - Gebruik van Actoren
# - Botsingsdetectie
# - Lijsten gebruiken

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

# Score initialiseren
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
    pass

pgzrun.go()