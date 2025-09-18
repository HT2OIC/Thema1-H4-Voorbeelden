# Extra functionaliteit aan Python toevoegen
# Zonder import kan je random niet gebruiken
import random

# Seednummer kiezen --> Alleen om te testen!
random.seed(5)

# Kommagetal (float) tussen 0.0 en 1.O (exclusief)
print(random.random())

# Geheel getal (integer) tussen 1 en 5 (inclusief)
print(random.randint(1, 5))

# Geheel getal (integer) tussen 1 en 5 (inclusief) met stapgrootte 2
# --> 1, 3, of 5
print(random.randrange(1, 5, 2))

# Willekeurig element uit de lijst
print(random.choice(["hallo", "dag", "hoi", "hey"]))