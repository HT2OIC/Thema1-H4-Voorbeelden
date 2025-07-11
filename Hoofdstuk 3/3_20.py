# Trivial Pursuit
# Spel waarin de gebruiker een willekeurige quizvraag beantwoordt.
# Oefent op:
# - input
# - condities
# - datatypes
# - logische operatoren (and, or, not) 
# - stringfuncties

import random

print("Welkom bij Trivial Pursuit!")

# Vragen en verwachte antwoorden (soms exact, soms met kernwoorden)
vraag_aardrijkskunde = "Welke planeet staat bekend als de rode planeet?"
vraag_kunst_literatuur= "Wie schilderde de Mona Lisa?"
vraag_sport_ontspanning = "Hoe wordt de sport synchroonzwemmen nog genoemd?"
vraag_amusement = "Wat gebeurt in Harry Potter en de Steen Der Wijzen?"
vraag_wetenschap_natuur = "Geef het getal pi tot 5 cijfers na de komma."

antwoord_aardrijkskunde = "Mars"
antwoord_kunst_literatuur = "Leonardo da Vinci"
antwoord_sport_ontspanning_mogelijkheid1 = "kunstzwemmen"
antwoord_sport_ontspanning_mogelijkheid2 = "waterballet"
antwoord_amusement_kernwoord1 = "steen"
antwoord_amusement_kernwoord2 = "Voldemort"
antwoord_wetenschap_natuur = 3.14159

# Eén van de 5 vragen stellen en het antwoord controleren.
vraag = random.randint(1, 5)

# Vraag 1 – aardrijkskunde
# Hoofdletterongevoelig vergelijken (via .lower())
if vraag == 1:
    antwoord = input(vraag_aardrijkskunde)
    if antwoord.lower() == antwoord_aardrijkskunde.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_aardrijkskunde)

# Vraag 2 – kunst en literatuur
# Hoofdletterongevoelig vergelijken (via .lower())
elif vraag == 2:
    antwoord = input(vraag_kunst_literatuur)
    if antwoord.lower() == antwoord_kunst_literatuur.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_kunst_literatuur)

# Vraag 3 – sport en ontspanning
# Antwoord is correct als 1 van 2 opties overeenkomt (via or)
elif vraag == 3:
    antwoord = input(vraag_sport_ontspanning)
    if antwoord.lower() == antwoord_sport_ontspanning_mogelijkheid1.lower() or antwoord.lower() == antwoord_sport_ontspanning_mogelijkheid2.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_sport_ontspanning_mogelijkheid1, "of: ", antwoord_sport_ontspanning_mogelijkheid2)

# Vraag 4 – amusement
# Antwoord is correct als beide kernwoorden voorkomen (via and + in)
elif vraag == 4:
    antwoord = input(vraag_amusement)
    if antwoord_amusement_kernwoord1.lower() in antwoord.lower() and antwoord_amusement_kernwoord2.lower() in antwoord.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! In je antwoord moesten zeker de kernwoorden: ", antwoord_amusement_kernwoord1, "en:", antwoord_amusement_kernwoord2, "staan.")

# Vraag 5 – wetenschap en natuur
# Antwoord is een kommagetal (float)
elif vraag == 5:
    antwoord = float(input(vraag_wetenschap_natuur))
    if antwoord == antwoord_wetenschap_natuur:
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juist antwoord was: ", str(antwoord_wetenschap_natuur))