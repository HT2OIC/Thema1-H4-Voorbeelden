import pgzrun

WIDTH = 750
HEIGHT = 500

mol = Actor("whacamole_mol")
achtergrond = Actor("whacamole_achtergrond")

def draw():
    achtergrond.draw()
    mol.draw()

pgzrun.go()