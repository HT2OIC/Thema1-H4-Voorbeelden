# Parameters weer instellen
zonnig = 1
warm = 1
regen = 0

# AND: Het is zowel zonnig als warm
if zonnig == 1 and warm == 1:
    print("Ga buiten zwemmen!")

# OR: Het is zonnig of warm
if zonnig == 1 or warm == 1:
    print("Ga buiten wandelen!")

# NOT: Het is niet warm
if not warm == 1: # of: if warm != 1:
    print("Blijf lekker binnen!")

# Combinatie: Het is zonnig of warm én het regent niet
if (zonnig == 1 or warm == 1) and not regen == 1:
    print("Ideaal weer voor een barbecue!")