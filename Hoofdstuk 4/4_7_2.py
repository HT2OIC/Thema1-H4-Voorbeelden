def on_mouse_down(pos):
    if mol.collidepoint(pos):
        print("Aaah!")
    else:
        print("Je hebt me gemist!")