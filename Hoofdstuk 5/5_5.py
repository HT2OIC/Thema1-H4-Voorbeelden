def reset_alien(alien):
    """
    Verplaatst de alien terug naar boven met een willekeurige positie.

    Argumenten:
        alien (Actor): De alien die gereset moet worden.
    """
    alien.x = random.randrange(50, WIDTH-50, 100)
    alien.y = random.randint(-500, 0)