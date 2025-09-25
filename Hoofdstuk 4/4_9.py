def draw():
    achtergrond.draw()
    mol.draw()
    screen.draw.text("Score: " + str(score), (550,25), color = (255, 0, 0), fontsize = 50)

def update():
    teller_snelheid += 1

    if teller_snelheid >= snelheid:
        mol.x = random.choice([75, 225, 375, 525, 675])
        teller_snelheid = 0