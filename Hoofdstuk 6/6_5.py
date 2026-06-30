import time

def beweeg_mario():
    """Laat Mario links of rechts bewegen met behulp van de pijltjestoetsen."""
    # Als Mario op de grond staat wanneer op spatie is gedrukt, laten we hem springen.
    if keyboard.space and op_grond:
        sounds.mario_springen.play()
        mario.image = "mario_spring"
        clock.schedule_unique(mario_reset, 0.5)
        mario_snelheid_y -= 12


def mario_reset():
    """Reset Mario naar de lopende afbeelding."""
    mario.image = "mario_lopen"


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