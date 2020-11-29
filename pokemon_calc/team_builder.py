import defense_type_chart
import random

def buildTeam():
    # We are assuming that they only have one pokemon they
    # are building off of
    # first we get the pokemon that is in the first slot
    # and check it's type weaknesses/resistances
    # then we put another pokemon in then check the
    # teams weakness/resistances until we get to 6
    # pokemon
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

    # The following are the possible pokemon sets formatted to find the best
    # defensive pairs
    # format is Pokemon, type1, type2, pokemon moveset data

    samplePokemon = [
        ["Blaziken", "fire", "fighting", "Blaziken @ Life Orb\nAbility: Speed Boost\n"
         "Jolly Nature\n- Swords Dance\n- Flare Blitz\n- Close Combat\n- Thunder Punch" ],

        ["Blissey", "normal", "", "Blissey @ Heavy-Duty Boots\nAbility: Natural Cure\n"
         "Bold Nature\n- Teleport\n- Seismic Toss\n- Soft-Boiled\n- Thunder Wave"],

        ["Buzzwole", "fighting", "bug", "Buzzwole @ Heavy-Duty Boots\nAbility: Beast Boost\n"
         "Impish Nature\n- Drain Punch\n- Ice Punch\n- Roost\n- Bulk Up"],

        ["Cinderace", "fire", "", "Cinderace @ Heavy-Duty Boots\nAbility: Libero\n"
         "Jolly Nature\n- Pyro Ball\n- U-turn\n- High Jump Kick\n- Zen Headbutt"],

        ["Clefable", "fairy", "", "Clefable @ Leftovers\nAbility: Magic Guard\n"
         "Bold Nature\n- Moonblast\n- Soft-Boiled\n- Stealth Rock\n- Knock Off"],

        ["Corviknight", "steel", "flying", "Corviknight @ Leftovers\n# Ability: Pressure\n"
         "Careful Nature\n- Defog\n- Roost\n- U-turn\n- Brave Bird"],

        ["Dragapult", "dragon", "ghost", "Dragapult @ Choice Specs\nAbility: Infiltrator\n"
         "Modest Nature\n- Shadow Ball\n- Draco Meteor\n- Flamethrower\n- Hex"],

        ["Dragonite", "dragon", "flying", "Dragonite @ Heavy-Duty Boots\nAbility: Multiscale\n"
         "Jolly Nature\n- Dragon Dance\n- Dual Wingbeat\n- Earthquake\n- Extreme Speed"],

        ["Excadrill", "ground", "steel", "Excadrill @ Leftovers\nAbility: Mold Breaker\n"
         "Jolly Nature\n- Earthquake\n- Iron Head\n- Toxic\n- Stealth Rock"],

        ["Ferrothorn", "grass", "steel", "Ferrothorn @ Leftovers\nAbility: Iron Barbs\n"
         "Impish Nature\n- Spikes\n- Knock Off\n- Body Press\n- Leech Seed" ],

        ["Garchomp", "ground", "dragon", "Garchomp @ Life Orb\nAbility: Rough Skin\n"
         "Jolly Nature\n- Stealth Rock\n- Earthquake\n- Swords Dance\n- Stone Edge"],

        ["Heatran", "fire", "steel", "Heatran @ Leftovers\nAbility: Flash Fire\n"
         "Calm Nature\n- Magma Storm\n- Earth Power\n- Taunt\n- Stealth Rock"],

        ["Kartana", "grass", "steel", "Kartana @ Choice Scarf\nAbility: Beast Boost\n"
         "Jolly Nature\n- Leaf Blade\n- Smart Strike\n- Sacred Sword\n- Knock Off"],

        ["Landorus-Therian", "ground", "flying", "Landorus-Therian @ Choice Scarf\nAbility: Intimidate\n"
         "Jolly Nature\n- Earthquake\n- U-turn\n- Stone Edge\n- Defog"],

        ["Latios", "psychic", "dragon", "Latios @ Choice Specs\nAbility: Levitate\n"
         "Timid Nature\n- Draco Meteor\n- Psychic\n- Mystical Fire\n- Trick"],

        ["Magearna", "steel", "fairy", "Magearna @ Weakness Policy\nAbility: Soul-Heart\n"
         "Timid Nature\n- Shift Gear\n- Calm Mind\n- Draining Kiss\n- Stored Power"],

        ["Mandibuzz", "flying", "dark", "Mandibuzz @ Heavy-Duty Boots\nAbility: Overcoat\n"
         "Impish Nature\n- Foul Play\n- Roost\n- Defog\n- U-turn"],

        ["Melmetal", "steel", "", "Melmetal @ Choice Band\nAbility: Iron Fist\n"
         "Adamant Nature\n- Double Iron Bash\n- Earthquake\n- Superpower\n- Thunder Punch"],

        ["Moltres", "fire", "flying", "Moltres @ Heavy-Duty Boots\nAbility: Flame Body\n"
         "Bold Nature\n- Defog\n- Flamethrower\n- Roost\n- Scorching Sands"],

        ["Nidoking", "poison", "ground", "Nidoking @ Life Orb\nAbility: Sheer Force\n"
         "Timid Nature\n- Sludge Wave\n- Earth Power\n- Ice Beam\n- Substitute"]
    ]

    type1 = "water"
    type2 = "ground"
    weaknesses = defense_type_chart.def_type_calc(type1, type2)

    currentTeam = []

    for i in range(1,6):
        # i will go find the 5 best pokemon to add to the team
        currentBest = -9999
        currentBestPokemon = ""
        currentBestLocation = 0
        currentBestWeaknesses = []


        for j in range(0,len(samplePokemon)):
            # j will look through all of the sample pokemon the find the one with the best synergy
            if samplePokemon[j][0] in currentTeam:
                continue
            typea = samplePokemon[j][1]
            typeb = samplePokemon[j][2]
            value = 0
            sampleWeakness = defense_type_chart.def_type_calc(typea, typeb)

            for k in range(0, 17):
                # k finds the synergy value
                tempVal = 0
                tempVal += weaknesses[k] + sampleWeakness[k]
                if tempVal == 0:
                    value -= 1
                if tempVal < 0:
                    value -= 2
                if tempVal < -2:
                    value -= 4
                if 0 < tempVal <= 1:
                    value += 1
                if tempVal > 1:
                    value += 0
            if value > currentBest:
                currentBest = value
                currentBestPokemon = samplePokemon[j][0]
                currentBestLocation = j
                currentBestWeaknesses = sampleWeakness

            if value == currentBest:
                rand = random.randint(0, 9)
                if rand > 5:
                    currentBest = value
                    currentBestPokemon = samplePokemon[j][0]
                    currentBestLocation = j
                    currentBestWeaknesses = sampleWeakness

        print(currentBestPokemon)
        for i in range(0,17):
            weaknesses[i] += currentBestWeaknesses[i]
        pokemon = samplePokemon[currentBestLocation][0]
        currentTeam.append(pokemon)
        print(weaknesses)

    print(currentTeam)
buildTeam()


# The following are possible team members


# Blaziken @ Life Orb
# Ability: Speed Boost
# Jolly Nature
# - Swords Dance
# - Flare Blitz
# - Close Combat
# - Thunder Punch
#
# Blissey @ Heavy-Duty Boots
# Ability: Natural Cure
# Bold Nature
# - Teleport
# - Seismic Toss
# - Soft-Boiled
# - Thunder Wave
#
# Buzzwole @ Heavy-Duty Boots
# Ability: Beast Boost
# Impish Nature
# - Drain Punch
# - Ice Punch
# - Roost
# - Bulk Up
#
# Cinderace @ Heavy-Duty Boots
# Ability: Libero
# Jolly Nature
# - Pyro Ball
# - U-turn
# - High Jump Kick
# - Zen Headbutt
#
# Clefable @ Leftovers
# Ability: Magic Guard
# Bold Nature
# - Moonblast
# - Soft-Boiled
# - Stealth Rock
# - Knock Off
#
# Corviknight @ Leftovers
# Ability: Pressure
# Careful Nature
# - Defog
# - Roost
# - U-turn
# - Brave Bird
#
# Dragapult @ Choice Specs
# Ability: Infiltrator
# Modest Nature
# - Shadow Ball
# - Draco Meteor
# - Flamethrower
# - Hex
#
# Dragonite @ Heavy-Duty Boots
# Ability: Multiscale
# Jolly Nature
# - Dragon Dance
# - Dual Wingbeat
# - Earthquake
# - Extreme Speed
#
# Excadrill @ Leftovers
# Ability: Mold Breaker
# Jolly Nature
# - Earthquake
# - Iron Head
# - Toxic
# - Stealth Rock
#
# Ferrothorn @ Leftovers
# Ability: Iron Barbs
# Impish Nature
# - Spikes
# - Knock Off
# - Body Press
# - Leech Seed
#
# Garchomp @ Life Orb
# Ability: Rough Skin
# Jolly Nature
# - Stealth Rock
# - Earthquake
# - Swords Dance
# - Stone Edge
#
# Heatran @ Leftovers
# Ability: Flash Fire
# Calm Nature
# - Magma Storm
# - Earth Power
# - Taunt
# - Stealth Rock
#
# Kartana @ Choice Scarf
# Ability: Beast Boost
# Jolly Nature
# - Leaf Blade
# - Smart Strike
# - Sacred Sword
# - Knock Off
#
# Landorus-Therian @ Choice Scarf
# Ability: Intimidate
# Jolly Nature
# - Earthquake
# - U-turn
# - Stone Edge
# - Defog
#
# Latios @ Choice Specs
# Ability: Levitate
# Timid Nature
# - Draco Meteor
# - Psychic
# - Mystical Fire
# - Trick
#
# Magearna @ Weakness Policy
# Ability: Soul-Heart
# Timid Nature
# - Shift Gear
# - Calm Mind
# - Draining Kiss
# - Stored Power
#
# Mandibuzz @ Heavy-Duty Boots
# Ability: Overcoat
# Impish Nature
# - Foul Play
# - Roost
# - Defog
# - U-turn
#
# Melmetal @ Choice Band
# Ability: Iron Fist
# Adamant Nature
# - Double Iron Bash
# - Earthquake
# - Superpower
# - Thunder Punch
#
# Moltres @ Heavy-Duty Boots
# Ability: Flame Body
# Bold Nature
# - Defog
# - Flamethrower
# - Roost
# - Scorching Sands
#
# Nidoking @ Life Orb
# Ability: Sheer Force
# Timid Nature
# - Sludge Wave
# - Earth Power
# - Ice Beam
# - Substitute
#
# Pheromosa @ Heavy-Duty Boots
# Ability: Beast Boost
# Naive Nature
# - Close Combat
# - U-turn
# - Ice Beam
# - Rapid Spin
#
# Regieleki @ Choice Specs
# Ability: Transistor
# Modest Nature
# - Thunderbolt
# - Volt Switch
# - Swift
# - Rapid Spin
#
# Rillaboom @ Life Orb
# Ability: Grassy Surge
# Adamant Nature
# - Swords Dance
# - Grassy Glide
# - Knock Off
# - Drain Punch
#
# Slowbro @ Heavy-Duty Boots
# Ability: Regenerator
# IVs: 0 Spe
# Relaxed Nature
# - Scald
# - Slack Off
# - Teleport
# - Future Sight
#
# Spectrier @ Choice Specs
# Ability: Grim Neigh
# Timid Nature
# - Shadow Ball
# - Hex
# - Will-O-Wisp
# - Mud Shot
#
# Swampert @ Leftovers
# Ability: Damp
# Relaxed Nature
# - Stealth Rock
# - Flip Turn
# - Earthquake
# - Toxic
#
# Tapu Fini @ Leftovers
# Ability: Misty Surge
# Bold Nature
# - Calm Mind
# - Taunt
# - Draining Kiss
# - Surf
#
# Tapu Koko @ Heavy-Duty Boots
# Ability: Electric Surge
# Timid Nature
# - Thunderbolt
# - Dazzling Gleam
# - U-turn
# - Roost
#
# Tornadus-Therian @ Heavy-Duty Boots
# Ability: Regenerator
# Timid Nature
# - Hurricane
# - Knock Off
# - U-turn
# - Defog
#
# Toxapex @ Rocky Helmet
# Ability: Regenerator
# Bold Nature
# - Scald
# - Recover
# - Haze
# - Knock Off
#
# Tyranitar @ Leftovers
# Ability: Sand Stream
# Careful Nature
# - Rock Blast
# - Stealth Rock
# - Thunder Wave
# - Ice Beam
#
# Urshifu @ Choice Band
# Ability: Unseen Fist
# Jolly Nature
# - Wicked Blow
# - Close Combat
# - Iron Head
# - U-turn
#
# Urshifu-Rapid-Strike @ Choice Band
# Ability: Unseen Fist
# Adamant Nature
# - Surging Strikes
# - Close Combat
# - Aqua Jet
# - U-turn
#
# Zapdos @ Heavy-Duty Boots
# Ability: Static
# Timid Nature
# - Discharge
# - Roost
# - Heat Wave
# - Defog
#
# Zapdos-Galar @ Choice Band
# Ability: Defiant
# Jolly Nature
# - Close Combat
# - Brave Bird
# - U-turn
# - Stomping Tantrum