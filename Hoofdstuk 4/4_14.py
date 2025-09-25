teller_snelheid = 0
snelheid = 50

def update():
    global teller_snelheid

    teller_snelheid += 1

    if teller_snelheid >= snelheid:
        mol.x = mol_positie_bepalen()
        teller_snelheid = 0