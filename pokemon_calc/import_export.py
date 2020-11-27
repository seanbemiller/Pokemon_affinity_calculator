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

def importer(Pokemon):
    # fills out all of the info that is left blank after being given a string formatted as:
    # Rockruff @ Choice Band
    # Ability: Own Tempo
    # Sassy Nature
    # - Earth Power
    # - Facade
    # - Endeavor
    # - Crunch

    info = Pokemon.split('\n')
    name = ""
    item = ""
    ability = ""
    nature = ""
    move1 = ""
    move2 = ""
    move3 = ""
    move4 = ""

    for i in info[0]:
        if i == " ":
            break
        else:
            name += i
    state = 0
    for i in info[0]:
        if state == 1:
            item+=i
        if i =='@':
            state = 1
    item = item[1:len(item)]
    state = 0
    for i in info[1]:
        if state == 1:
            ability += i
        if i == ':':
            state = 1
    ability = ability[1:len(ability)]

    for i in info[2]:
        if i == ' ':
            break
        else:
            nature += i

    for i in info[3][2:len(info[3])]:
        move1 += i
    for i in info[4][2:len(info[4])]:
        move2 += i
    for i in info[5][2:len(info[5])]:
        move3 += i
    for i in info[6][2:len(info[6])]:
        move4 += i

    # print(name + " " + item + " " + nature + " " + ability + " "
    #       + move1 + " " + move2 + " " + move3 + " " + move4)














importer("Bulbasaur @ life orb\n"
"Ability: overgrowth\n"  
"jolly Nature\n"  
"- Fire Punch\n"  
"- Thunder Punch\n"  
"- Ice Punch\n" 
"- Earthquake")