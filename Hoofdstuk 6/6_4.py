def update():
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

def controleer_einde_spel():
    """Controleert of het spel verloren of gewonnen is."""
        
    if mario.colliderect(vlag):
        print("Gewonnen!")
        print(f"Je behaalde {score} punten.")
        exit()