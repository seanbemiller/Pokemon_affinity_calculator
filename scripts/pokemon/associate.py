#writes out.json that combines pokemon.json and moveset and adds nulls for missing atributes
import json

out = open("./outfile.json", 'a')
with open('./pokemon.json') as pokedex:
	with open('./moveset.txt') as movelist:
		data = json.load(pokedex)
		for pokemon in data:
			nameToMatch = pokemon.get("name").lower()
			movelist.seek(0)
			while True:
				line = movelist.readline()
				if not line:
					break
				if nameToMatch == line.split(':')[0]:
					if "type2" not in pokemon:
						pokemon["type2"] = None
					if "ability2" not in pokemon:
						pokemon["ability2"] = None
					if "ability3" not in pokemon:
						pokemon["ability3"] = None
					lineafter = line.split(":")
					pokemon['moveset'] = lineafter[1].strip()
					# print(pokemon)
					out.write(json.dumps(pokemon) + "\n")
