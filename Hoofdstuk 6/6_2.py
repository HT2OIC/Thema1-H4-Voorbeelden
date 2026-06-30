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