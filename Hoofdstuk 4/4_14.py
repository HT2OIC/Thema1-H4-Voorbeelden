def update():
    teller_snelheid += 1

    if teller_snelheid >= snelheid:
        mol.x = mol_positie_bepalen()
        teller_snelheid = 0

def mol_positie_bepalen():
    positie = random.choice([75, 225, 375, 525, 675])
    return positie