mario_snelheid_y = 0

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
        mario_snelheid_y -= 12

def verwerk_zwaartekracht():
    """Verwerkt de zwaartekracht. """
    global mario_snelheid_y

    # Zwaartekracht trekt Mario naar beneden.
    mario_snelheid_y += 0.5
    mario.y += mario_snelheid_y

    # Houd Mario op de grond. Anders zakt hij door de grond.
    if mario.y > 200:
        mario.y = 200
        mario_snelheid_y = 0