namen = ["Emma", "Liam", "X", "Olivia", "Noah", "Mila"]

gezocht = "Olivia"

for naam in namen:
    if naam == "X":
        # Sla ongeldige naam over
        continue

    if naam == gezocht:
        print("De gezochte naam is gevonden!")
        break

    print(naam, "is niet de juiste naam.")

else:
    print(naam, "is niet gevonden in de lijst.")
