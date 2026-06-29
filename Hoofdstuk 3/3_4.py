# Vragen en verwachte antwoorden
vraag_wetenschap_natuur = "Geef het getal pi tot 5 cijfers na de komma."
antwoord_wetenschap_natuur = 3.14159

# Vraag 4 – wetenschap en natuur
# Antwoord is een kommagetal (float)
elif vraag == 4:
    antwoord = float(input(vraag_wetenschap_natuur))
    if antwoord == antwoord_wetenschap_natuur:
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juist antwoord was: ", str(antwoord_wetenschap_natuur))