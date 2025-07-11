zonnig = 1
warm = 0
regen = 1

# Binnenblijven:
# - Niet zonnig
# - En niet warm of het regent
if not zonnig == 1 and not warm == 1 or regen == 1:
    print("Blijf binnen!")

# Fout bij: zonnig = 1, warm = 0 en regen = 1 --> Bij zonnig weer blijven we niet binnen!
# Fout bij: zonnig = 1, warm = 1 en regen = 1 --> Bij zonnig weer blijven we niet binnen!