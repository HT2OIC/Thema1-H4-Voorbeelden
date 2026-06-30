def update():
    global score, levens

    # Deelprobleem 1: Alien bewegen
    alien.y += 10

    # Als de alien onderaan het scherm is:
    # Score verhogen en alien op een willekeurige plaats zetten
    if alien.y >= HEIGHT:
        score += 1
        reset_alien(alien)

    # Als de alien botst met het schip:
    # Levens verlagen en alien op willekeurige plaats zetten
    if alien.colliderect(schip):
        levens -= 1
        reset_alien(alien)


    # Deelprobleem 2: Schip bewegen
    if keyboard.right and schip.x <= WIDTH-50:
        schip.x += 5
    elif keyboard.left and schip.x >= 50:
        schip.x -= 5


    # Deelprobleem 3: Einde spel
    if levens < 0:
        print("Game over!")
        exit()

def reset_alien(alien):
    """
    Verplaatst de alien terug naar boven met een willekeurige positie.
    Argumenten:
        alien (Actor): De alien die gereset moet worden.
    """
    alien.x = random.randrange(50, WIDTH-50, 100)
    alien.y = random.randint(-500, 0) # Negatieve y: alien start buiten scherm voor meer variatie