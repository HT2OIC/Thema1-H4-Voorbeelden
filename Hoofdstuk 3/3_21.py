# Vraag en verwacht antwoord
vraag_kunst_literatuur= "Wie schilderde de Mona Lisa?"
antwoord_kunst_literatuur = "Leonardo da Vinci"


antwoord = input(vraag_kunst_literatuur)
# Antwoord debuggen - Wat zit er in de variabelen?
print("DEBUG: juist antwoord =", antwoord_kunst_literatuur)
print("DEBUG: antwoord =", antwoord)

# Antwoord controleren
if antwoord == antwoord_kunst_literatuur:
    print("Proficiat! Je hebt de vraag juist beantwoord.")
else:
    print("Jammer! Het juiste antwoord was:", antwoord_kunst_literatuur)