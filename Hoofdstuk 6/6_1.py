# Super Mario
# Verzamel munten en ontwijk de Goomba. Je wint het spel als je tegen de vlaggenmast springt.
import pgzrun

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
    'levens': 3,
    'actief': True
}

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
    pass

pgzrun.go()