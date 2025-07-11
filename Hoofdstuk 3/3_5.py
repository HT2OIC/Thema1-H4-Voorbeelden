# Quizvraag over aardrijkskunde
# De speler moet de hoofdstad van Frankrijk invullen.
# Oefent op:
# - input
# - condities
# - stringvergelijking

# Vraag over aardrijkskunde
vraag_hoofdstad_frankrijk = "Wat is de hoofdstad van Frankrijk?"
antwoord_hoofdstad_frankrijk = "Parijs"

# Vraag stellen aan de gebruiker
antwoord_gebruiker = input(vraag_hoofdstad_frankrijk)

# Controleren of het antwoord juist is
if antwoord_gebruiker == antwoord_hoofdstad_frankrijk:
    print("Juist!")
else:
    print("Fout!")