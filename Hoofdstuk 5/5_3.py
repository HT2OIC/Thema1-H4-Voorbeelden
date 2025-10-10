def update():
    global score, levens

    # Beweeg alien naar beneden
    alien.y += 10

    # Als de alien onderaan het scherm is:
    # Score verhogen en alien op een willekeurige plaats zetten
    if alien.y >= HEIGHT:
        score += 1
        alien.x = random.randrange(50, WIDTH-50, 100)
        alien.y = random.randint(-500, 0)

    # Als de alien botst met het schip:
    # Levens verlagen en alien op willekeurige plaats zetten
    if alien.colliderect(schip):
        levens -= 1
        alien.x = random.randrange(50, WIDTH-50, 100)
        alien.y = random.randint(-500, 0)

    # Beweeg schip links/rechts
    if keyboard.right and schip.x <= WIDTH-50:
        schip.x += 5
    elif keyboard.left and schip.x >= 50:
        schip.x -= 5

    # Einde spel
    if levens < 0:
        print("Game over!")