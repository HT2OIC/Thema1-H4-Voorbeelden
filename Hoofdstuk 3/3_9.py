minimum_leeftijd = 16
leeftijd = int(input("Hou oud ben je? "))

# Controleren of je bier mag drinken.
if leeftijd < minimum_leeftijd:
    print("Je mag nog geen bier drinken!")