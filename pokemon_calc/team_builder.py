import defense_type_chart
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

    type1 = "grass"
    type2 = "poison"
    weaknesses = defense_type_chart.def_type_calc(type1, type2)



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