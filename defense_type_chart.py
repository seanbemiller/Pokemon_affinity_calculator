def def_type_calc(type1, type2):
    # This function takes in the pokemon's types, gets the typing from the database
    # and then calculates the type resistances and weakness inside and passes
    # back a list of the defensive typing information

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

    # First you get the pokemon types from the database
    # for example:

    typechart = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if type1 == "normal":
        typechart[fighting] -= 1

        typechart[ghost] += 1
    if type1 == "fighting":
        typechart[flying] -= 1
        typechart[psychic] -= 1
        typechart[fairy] -= 1

        typechart[rock] += 1
        typechart[bug] += 1
        typechart[dark] += 1
    if type1 == "flying":
        typechart[rock] -= 1
        typechart[electric] -= 1
        typechart[ice] -= 1

        typechart[fighting] += 1
        typechart[ground] += 1
        typechart[grass] += 1
        typechart[bug] += 1

    if type1 == "poison":
        typechart[psychic] -= 1
        typechart[ground] -= 1

        typechart[fighting] += 1
        typechart[grass] += 1
        typechart[bug] += 1
        typechart[fairy] += 1
        typechart[poison] += 1

    if type1 == "ground":
        typechart[grass] -= 1
        typechart[water] -= 1
        typechart[ice] -= 1

        typechart[poison] += 1
        typechart[rock] += 1

    if type1 == "rock":
        typechart[fighting] -= 1
        typechart[grass] -= 1
        typechart[ground] -= 1
        typechart[steel] -= 1
        typechart[water] -= 1

        typechart[fire] += 1
        typechart[flying] += 1
        typechart[normal] += 1
        typechart[poison] += 1

    if type1 == "bug":
        typechart[rock] -= 1
        typechart[flying] -= 1
        typechart[fire] -= 1

        typechart[fighting] += 1
        typechart[grass] += 1
        typechart[ground] += 1

    if type1 == "ghost":
        typechart[ghost] -= 1
        typechart[dark] -= 1

        typechart[normal] += 1
        typechart[fighting] += 1
        typechart[bug] += 1
        typechart[poison] += 1

    if type1 == "steel":
        typechart[fighting] -= 1
        typechart[fire] -= 1
        typechart[ground] -= 1

        typechart[bug] += 1
        typechart[dragon] += 1
        typechart[fairy] += 1
        typechart[flying] += 1
        typechart[grass] += 1
        typechart[ice] += 1
        typechart[normal] += 1
        typechart[psychic] += 1
        typechart[rock] += 1
        typechart[steel] += 1
        typechart[poison] += 1
    if type1 == "fire":
        typechart[water] -= 1
        typechart[rock] -= 1
        typechart[ground]-= 1

        typechart[bug] += 1
        typechart[fairy] += 1
        typechart[fire] += 1
        typechart[grass] += 1
        typechart[ice] += 1
        typechart[steel] += 1

    if type1 == "water":
        typechart[grass] -= 1
        typechart[electric] -= 1

        typechart[ice] += 1
        typechart[fire] += 1
        typechart[steel] += 1
        typechart[water] += 1

    if type1 == "grass":
        typechart[fire] -= 1
        typechart[flying] -= 1
        typechart[bug] -= 1
        typechart[ice] -= 1
        typechart[poison] -= 1

        typechart[water] += 1
        typechart[grass] += 1
        typechart[electric] += 1
        typechart[ground] += 1

    if type1 == "electric":
        typechart[ground] -= 1

        typechart[electric] += 1
        typechart[flying] += 1
        typechart[steel] += 1

    if type1 == "psychic":
        typechart[bug] -= 1
        typechart[dark] -= 1
        typechart[ghost] -= 1

        typechart[fighting] += 1
        typechart[psychic] += 1

    if type1 == "ice":
        typechart[fire] -= 1
        typechart[fighting] -= 1
        typechart[rock] -= 1
        typechart[steel] -= 1

        typechart[ice] += 1
    if type1 == "dragon":
        typechart[fairy] -= 1
        typechart[ice] -= 1
        typechart[dragon] -= 1

        typechart[electric] += 1
        typechart[fire] += 1
        typechart[grass] += 1
        typechart[water] += 1

    if type1 == "dark":
        typechart[fairy] -= 1
        typechart[fighting] -= 1
        typechart[bug] -= 1

        typechart[psychic] += 1
        typechart[dark] += 1
        typechart[ghost] += 1

    if type1 == "fairy":
        typechart[poison] -= 1
        typechart[steel] -= 1

        typechart[dragon] += 1
        typechart[bug] += 1
        typechart[fighting] += 1
        typechart[dark] += 1

    if type2 is None and type2 != "":
        if type2 == "normal":
            typechart[fighting] -= 1

            typechart[ghost] += 1
        if type2 == "fighting":
            typechart[flying] -= 1
            typechart[psychic] -= 1
            typechart[fairy] -= 1

            typechart[rock] += 1
            typechart[bug] += 1
            typechart[dark] += 1
        if type2 == "flying":
            typechart[rock] -= 1
            typechart[electric] -= 1
            typechart[ice] -= 1

            typechart[fighting] += 1
            typechart[ground] += 1
            typechart[grass] += 1

        if type2 == "poison":
            typechart[psychic] -= 1
            typechart[ground] -= 1

            typechart[fighting] += 1
            typechart[grass] += 1
            typechart[bug] += 1
            typechart[fairy] += 1
            typechart[poison] += 1

        if type2 == "ground":
            typechart[grass] -= 1
            typechart[water] -= 1
            typechart[ice] -= 1

            typechart[poison] += 1
            typechart[rock] += 1

        if type1 == "rock":
            typechart[fighting] -= 1
            typechart[grass] -= 1
            typechart[ground] -= 1
            typechart[steel] -= 1
            typechart[water] -= 1

            typechart[fire] += 1
            typechart[flying] += 1
            typechart[normal] += 1
            typechart[poison] += 1

        if type2 == "bug":
            typechart[rock] -= 1
            typechart[flying] -= 1
            typechart[fire] -= 1

            typechart[fighting] += 1
            typechart[grass] += 1
            typechart[ground] += 1

        if type2 == "ghost":
            typechart[ghost] -= 1
            typechart[dark] -= 1

            typechart[normal] += 1
            typechart[fighting] += 1
            typechart[bug] += 1
            typechart[poison] += 1

        if type2 == "steel":
            typechart[fighting] -= 1
            typechart[fire] -= 1
            typechart[ground] -= 1

            typechart[bug] += 1
            typechart[dragon] += 1
            typechart[fairy] += 1
            typechart[flying] += 1
            typechart[grass] += 1
            typechart[ice] += 1
            typechart[normal] += 1
            typechart[psychic] += 1
            typechart[rock] += 1
            typechart[steel] += 1
            typechart[poison] += 1
        if type2 == "fire":
            typechart[water] -= 1
            typechart[rock] -= 1
            typechart[ground] -= 1

            typechart[bug] += 1
            typechart[fairy] += 1
            typechart[fire] += 1
            typechart[grass] += 1
            typechart[ice] += 1
            typechart[steel] += 1

        if type2 == "water":
            typechart[grass] -= 1
            typechart[electric] -= 1

            typechart[ice] += 1
            typechart[fire] += 1
            typechart[steel] += 1
            typechart[water] += 1

        if type2 == "grass":
            typechart[fire] -= 1
            typechart[flying] -= 1
            typechart[bug] -= 1
            typechart[ice] -= 1
            typechart[poison] -= 1

            typechart[water] += 1
            typechart[grass] += 1
            typechart[electric] += 1
            typechart[ground] += 1

        if type1 == "electric":
            typechart[ground] -= 1

            typechart[electric] += 1
            typechart[flying] += 1
            typechart[steel] += 1

        if type2 == "psychic":
            typechart[bug] -= 1
            typechart[dark] -= 1
            typechart[ghost] -= 1

            typechart[fighting] += 1
            typechart[psychic] += 1

        if type2 == "ice":
            typechart[fire] -= 1
            typechart[fighting] -= 1
            typechart[rock] -= 1
            typechart[steel] -= 1

            typechart[ice] += 1
        if type2 == "dragon":
            typechart[fairy] -= 1
            typechart[ice] -= 1
            typechart[dragon] -= 1

            typechart[electric] += 1
            typechart[fire] += 1
            typechart[grass] += 1
            typechart[water] += 1

        if type2 == "dark":
            typechart[fairy] -= 1
            typechart[fighting] -= 1
            typechart[bug] -= 1

            typechart[psychic] += 1
            typechart[dark] += 1
            typechart[ghost] += 1

        if type2 == "fairy":
            typechart[poison] -= 1
            typechart[steel] -= 1

            typechart[dragon] += 1
            typechart[bug] += 1
            typechart[fighting] += 1
            typechart[dark] += 1

    return typechart
