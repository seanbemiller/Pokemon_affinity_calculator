def off_type_calc(type):
    # This function takes in the move's type
    # and then calculates the type resistances and weakness inside and passes
    # back a list of the offensive typing information
    # This had to be another functions as defensive and offensive resistances differ

    normal = 0
    fighting = 1
    flying = 2
    poison = 3
    ground = 4
    rock = 5
    bug = 6
    ghost = 7
    steel = 8
    fire = 9
    water = 10
    grass = 11
    electric = 12
    psychic = 13
    ice = 14
    dragon = 15
    dark = 16
    fairy = 17

    # First you get the move's from the database
    # for example:

    typechart = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if type == "normal":
        pass
    if type == "fighting":

        typechart[rock] += 1
        typechart[normal] += 1
        typechart[dark] += 1
        typechart[steel] += 1
        typechart[ice] += 1

    if type == "flying":

        typechart[fighting] += 1
        typechart[bug] += 2
        typechart[grass] += 1

    if type == "poison":

        typechart[grass] += 1
        typechart[fairy] += 1

    if type == "ground":

        typechart[poison] += 1
        typechart[rock] += 1
        typechart[steel] += 1
        typechart[fire] += 1
        typechart[electric] += 1

    if type == "rock":

        typechart[fire] += 1
        typechart[flying] += 1
        typechart[ice] += 1
        typechart[bug] += 1

    if type == "bug":

        typechart[dark] += 1
        typechart[grass] += 1
        typechart[psychic] += 1

    if type == "ghost":

        typechart[ghost] += 1
        typechart[psychic] += 1

    if type == "steel":

        typechart[fairy] += 1
        typechart[ice] += 1
        typechart[rock] += 1

    if type == "fire":

        typechart[bug] += 1
        typechart[grass] += 1
        typechart[ice] += 1
        typechart[steel] += 1

    if type == "water":

        typechart[ground] += 1
        typechart[fire] += 1
        typechart[rock] += 1

    if type == "grass":

        typechart[water] += 1
        typechart[rock] += 1
        typechart[ground] += 1

    if type == "electric":

        typechart[water] += 1
        typechart[flying] += 1

    if type == "psychic":

        typechart[fighting] += 1
        typechart[poison] += 1

    if type == "ice":

        typechart[dragon] += 1
        typechart[flying] += 1
        typechart[grass] += 1
        typechart[ground] += 1

    if type == "dragon":

        typechart[dragon] += 1

    if type == "dark":

        typechart[psychic] += 1
        typechart[ghost] += 1

    if type == "fairy":

        typechart[dragon] += 1
        typechart[dark] += 1
        typechart[fighting] += 1

    return typechart

