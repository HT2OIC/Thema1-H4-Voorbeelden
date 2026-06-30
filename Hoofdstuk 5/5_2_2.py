getal = 0

while getal < 10:
    getal += 1

    if getal == 2:
        print("Mijn lievelinsgetal is:", getal)
        continue

    print("Getal is:", getal)
    
    if getal == 5:
        print("Getal is 5, stop de loop.")
        break

else:
    print("De while-loop is normaal geëindigd.")