# Wanneer de speler klikt: controleer of hij de mol raakt.
def on_mouse_down(pos):
    if mol.collidepoint(pos):
        update_score(True)
    else:
        update_score(False)

def update_score(raak):
    """Past de score aan en geeft feedback op basis van of de mol werd geraakt of niet.
    Argumenten:
       raak (boolean): Is de mol geraakt? 
        """
    global score
    if raak:
        score += 1
        print("Aaah!")
    else:
        score -= 1
        print("Je hebt me gemist!")