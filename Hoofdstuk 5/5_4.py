# Maak 5 aliens en stop ze in een lijst
alien_lijst = []

for _ in range(5):
    alien = Actor("spaceinvaders_alien")
    alien.pos = (random.randrange(50, 1450, 100), random.randint(-500, 0))
    alien_lijst.append(alien)

def draw():
        # De 5 aliens tekenen
    for alien in alien_lijst:
        alien.draw()

def update():
    global score, levens, alien_lijst

        # Deelprobleem 1: Aliens bewegen
        # Alle aliens: bewegen + detectie onderkant scherm + detectie botsing
    for alien in alien_lijst:
        alien.y += 10

        if alien.y >= HEIGHT:
            score += 1
            reset_alien(alien)

        if schip.colliderect(alien):
            levens -= 1
            reset_alien(alien)