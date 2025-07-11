# Trivial Pursuit
# Spel waarin de gebruiker een willekeurige quizvraag beantwoordt.
# Oefent op:
# - input
# - condities
# - datatypes
# - logica

import random

print("Welkom bij Trivial Pursuit!")

# Vragen en verwachte antwoorden
vraag_aardrijkskunde = "Welke planeet staat bekend als de rode planeet?"
vraag_kunst_literatuur= "Wie schilderde de Mona Lisa?"

antwoord_aardrijkskunde = "Mars"
antwoord_kunst_literatuur = "Leonardo da Vinci"

# Eén van de 2 vragen stellen en het antwoord controleren.
vraag = random.randint(1, 2)

# Vraag 1 – aardrijkskunde
if vraag == 1:
    antwoord = input(vraag_aardrijkskunde)
    if antwoord == antwoord_aardrijkskunde:
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_aardrijkskunde)

# Vraag 2 – kunst en literatuur
elif vraag == 2:
    antwoord = input(vraag_kunst_literatuur)
    if antwoord == antwoord_kunst_literatuur:
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_kunst_literatuur)