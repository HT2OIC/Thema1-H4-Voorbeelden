# Vraag 1 – aardrijkskunde
# Hoofdletterongevoelig vergelijken (.lower())
if vraag == 1:
    antwoord = input(vraag_aardrijkskunde)
    if antwoord.lower() == antwoord_aardrijkskunde.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_aardrijkskunde)

# Vraag 2 – sport en ontspanning
# Antwoord is correct als 1 van 2 opties overeenkomt (or)
elif vraag == 2:
    antwoord = input(vraag_sport_ontspanning)
    if antwoord.lower() == antwoord_sport_ontspanning_mogelijkheid1.lower() or antwoord.lower() == antwoord_sport_ontspanning_mogelijkheid2.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! Het juiste antwoord was:", antwoord_sport_ontspanning_mogelijkheid1, "of: ", antwoord_sport_ontspanning_mogelijkheid2)

# Vraag 3 – amusement
# Antwoord is correct als beide kernwoorden voorkomen (and + in)
elif vraag == 3:
    antwoord = input(vraag_amusement)
    if antwoord_amusement_kernwoord1.lower() in antwoord.lower() and antwoord_amusement_kernwoord2.lower() in antwoord.lower():
        print("Proficiat! Je hebt de vraag juist beantwoord.")
    else:
        print("Jammer! In je antwoord moesten zeker de kernwoorden: ", antwoord_amusement_kernwoord1, "en:", antwoord_amusement_kernwoord2, "staan.")