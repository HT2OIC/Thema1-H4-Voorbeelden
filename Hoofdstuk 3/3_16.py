antwoord = input("Wie schilderde de Mona Lisa?")

# Hoofdletterongevoelig controleren
if antwoord.lower() == "Leonardo da Vinci".lower():
    print("Proficiat! Je hebt de vraag juist beantwoord!")
else:
    print("Jammer! Het juiste antwoord was: Leonardo da Vinci")