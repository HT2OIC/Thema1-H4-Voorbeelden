spel = {
    "speler1": {"naam": "Mario", "leven": 3},
    "speler2": {"naam": "Luigi", "leven": 5}
}

print(spel["speler1"])              # {'naam': 'Mario', 'leven': 3}
print(spel["speler1"]["naam"])      # Mario

spel["speler2"]["leven"] -= 1