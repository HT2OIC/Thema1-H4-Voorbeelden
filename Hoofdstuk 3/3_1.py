# Trivial Pursuit
# Stelt een vraag en controleert het antwoord.

import random

print("Welkom bij Trivial Pursuit!")

# Vragen en verwachte antwoorden
vraag_aardrijkskunde = "Welke planeet staat bekend als de rode planeet?"
vraag_kunst_literatuur= "Wie schilderde de Mona Lisa?"

antwoord_aardrijkskunde = "Mars"
antwoord_kunst_literatuur = "Leonardo da Vinci"

# Willekeurig vraagnummer kiezen (1 tem 5)
vraag = random.randint(1, 5)