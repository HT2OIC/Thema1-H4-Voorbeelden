def teken_gaten(x_positie):
    """Tekent een zwart gat op het opgegeven coördinaat.

    Argumenten:
        x_positie (int): De x-coördinaat van het gat."""
    
    screen.draw.filled_circle((x_positie, 450), 50, "black")

def mol_positie_bepalen():
    """Bepaalt willekeurig een nieuwe x-positie voor de mol.

    Returns:
        int:  Een nieuw x-coördinaat voor de mol."""
    
    positie = random.choice([75, 225, 375, 525, 675])
    return positie