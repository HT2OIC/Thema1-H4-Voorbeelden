minimum_leeftijd_bier = 16
minimum_leeftijd_sterke_drank = 18
leeftijd = int(input("Hou oud ben je? "))

# Controleren welke drank je mag drinken
if leeftijd < minimum_leeftijd_bier:
    print("Je mag nog geen bier of sterke drank drinken!")
elif leeftijd < minimum_leeftijd_sterke_drank:
    print("Je mag bier drinken! Sterke drank mag je nog niet drinken!")
else:
    print("Je mag bier en sterke drank drinken!")