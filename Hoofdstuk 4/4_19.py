import pgzrun

mol = Actor("whacamole_mol")

def draw():
    mol.draw()
    
def on_mouse_down(pos):
    if mol.collidepoint(pos):
        update_score(True)
    else:
        update_score(False)


def update_score(raak):
    if raak:
        print("Aaah!")
    else:
        print("Je hebt me gemist!")

pgzrun.go()