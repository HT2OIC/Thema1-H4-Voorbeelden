score = 0

# Achtergrond, mol, gaten en score tekenen
def draw():
    achtergrond.draw()

    screen.draw.filled_circle((75, 450), 50, "black")
    screen.draw.filled_circle((225, 450), 50, "black")
    screen.draw.filled_circle((375, 450), 50, "black")
    screen.draw.filled_circle((525, 450), 50, "black")
    screen.draw.filled_circle((675, 450), 50, "black")

    mol.draw()
    
    screen.draw.text("Score: " + str(score), (550,25), color = (255, 0, 0), fontsize = 50)