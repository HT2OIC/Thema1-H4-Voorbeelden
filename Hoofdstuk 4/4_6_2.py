score = 0

def score_aanpassen(gescoord):
    """Past score aan op basis van gescoord. Als gescoord True is +1, anders -1.
    Argumenten:
        gescoord (boolean): Gescoord / niet gescoord
    """
    global score
    
    if gescoord:
        score = score + 1
    else:
        score = score -1