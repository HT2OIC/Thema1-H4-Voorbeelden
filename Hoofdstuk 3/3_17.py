antwoord = input("Wie schilderde de Mona Lisa?")

# Controleren op kernwoord
if "leonardo" in antwoord.lower():
    print("Proficiat! Je hebt de vraag juist beantwoord!")
else:
    print("Jammer! Het juiste antwoord was: Leonardo da Vinci")