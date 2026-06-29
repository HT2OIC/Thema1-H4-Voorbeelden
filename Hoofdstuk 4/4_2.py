# Actoren: de mol en de achtergrond
mol = Actor("whacamole_mol")
mol.x = 75
mol.y = 400
achtergrond = Actor("whacamole_achtergrond")

# Achtergrond en mol tekenen
def draw():
    achtergrond.draw()
    mol.draw()