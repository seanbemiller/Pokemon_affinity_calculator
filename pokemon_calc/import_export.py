def exporter():
    # first we need to get the info from the pokemon
    # ideally we get a list of each pokemon and we repeat the
    # process 6 times to correctly format all of them
    # ex:
    name = "bulbasaur"
    ability = "overgrowth"
    item = "life orb"
    nature = "jolly"
    move1 = "fire punch"
    move2 = "thunder punch"
    move3 = "ice punch"
    move4 = "earthquake"

    exportedString = ""
    exportedString += name + " @ " + item + "\n"
    exportedString += "Ability: " + ability + '\n'
    exportedString += nature + " Nature" + '\n'
    exportedString += "- " + move1 + '\n'
    exportedString += "- " + move2 + '\n'
    exportedString += "- " + move3 + '\n'
    exportedString += "- " + move4 + '\n'

    print(exportedString)

def importer(PokemonTeam):
    pass