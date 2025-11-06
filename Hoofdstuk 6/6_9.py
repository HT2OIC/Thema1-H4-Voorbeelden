pokemon = {"naam": "Pikachu", "type": "Elektrisch", "level": 10}

pokemon["aanval"] = "Bliksem"
print(pokemon)

pokemon.update({"ervaring": 120, "trainer": "Ash"})
print(pokemon)

pokemon.pop("type")
print(pokemon)

pokemon.clear()
print(pokemon)