TYPES = [
    'Normal',
    'Fight',
    'Flying',
    'Poison',
    'Ground',
    'Rock',
    'Bug',
    'Ghost',
    'Steel',
    'Fire',
    'Water',
    'Grass',
    'Electric',
    'Psychic',
    'Ice',
    'Dragon',
    'Dark',
    'Fairy'
]


CHARACTER_TYPES = {
    'Pikachu': ['Electric'],
    'Charizard': ['Fire', 'Flying'],
    'Squirtle': ['Water'],
    'Jigglypuff': ['Normal', 'Fairy'],
    'Gengar': ['Ghost', 'Poison'],
    'Magnemite': ['Electric', 'Steel'],
    'Bulbasaur': ['Grass', 'Poison'],
    'Charmander': ['Fire'],
    'Beedrill': ['Bug', 'Poison'],
    'Golem': ['Rock', 'Ground'],
    'Dewgong': ['Water', 'Ice'],
    'Hypno': ['Psychic'],
    'Cleffa': ['Fairy'],
    'Cutiefly': ['Fairy', 'Bug']
}


HIT_POINTS = {
    'Pikachu': 35,
    'Charizard': 78,
    'Squirtle': 44,
    'Jigglypuff': 115,
    'Gengar': 60 ,
    'Magnemite': 25,
    'Bulbasaur': 45,
    'Charmander': 39,
    'Beedrill': 65,
    'Golem': 80,
    'Dewgong': 90,
    'Hypno': 85,
    'Cleffa': 50,
    'Cutiefly': 40
}

ATTACKS = {
    'Pikachu': ['Thunder Shock',  'Double Kick', 'Thunderbolt'],
    'Charizard': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'],
    'Squirtle': ['Tackle',  'Bubble', 'Bite'],
    'Jigglypuff': ['Pound', 'Body Slam', 'Double Slap'],
    'Gengar': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'],
    'Magnemite': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],
    'Bulbasaur': ['Tackle', 'Vine Whip', 'Razor Leaf'],
    'Charmander': ['Scratch', 'Ember', 'Fire Spin'],
    'Beedrill': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'],
    'Golem': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'],
    'Dewgong': ['Aqua Jet',  'Ice Shard', 'Headbutt'],
    'Hypno': ['Pound', 'Confusion', 'Dream Eater'],
    'Cleffa': [ 'Pound', 'Magical Leaf'],
    'Cutiefly': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss']
    
}


# MOVES = {
#     "Normal" : [ 'Scratch', 'Tackle',  'Pound', 'Rage', 'Fury Attack', 'Body Slam', 'Double Slap', 'Headbutt'] ,
#     "Fire" : ['Ember', 'Fire Spin'],
#     "Water" : ['Bubble', 'Aqua Jet'],
#     "Electric" : ['Thunder Shock', 'Thunderbolt'],
#     "Grass" : ['Vine Whip', 'Magical Leaf', 'Razor Leaf', 'Absorb'],
#     "Ice" : ['Ice Shard'],
#     "Fighting" : ['Double Kick'],
#     "Poison" : ['Smog'],
#     "Ground" : ['Earthquake'],
#     "Flying" : ['Wing Attack', 'Peck'],
#     "Psychic" : ['Confusion', 'Dream Eater'] ,
#     "Bug" : ['Twineedle', 'Struggle Bug'],
#     "Rock" : ['Rock Throw', 'Rock Slide'],
#     "Ghost" : ['Lick', 'Shadow Ball'] ,
#     "Dragon" : ['Outrage'],
#     "Dark" : ['Crunch', 'Bite'],
#     "Steel" : ['Flash Cannon'],
#     "Fairy" : ['Fairy Wind', 'Draining Kiss']
# }


SUPER_EFFECTIVE = {
    "Normal" : ["N/A"],
    "Fire" : ["Grass", "Ice", "Bug", "Steel"],
    "Water" : ["Fire", "Ground", "Rock"],
    "Electric" : ["Water", "Flying"],
    "Grass" : ["Water", "Ground", "Rock"],
    "Ice" : ["Grass", "Ground", "Flying", "Dragon"],
    "Fighting" : ["Normal", "Ice", "Rock", "Dark", "Steel"],
    "Poison" : ["Grass", "Fairy"],
    "Ground" : ["Fire", "Electric", "Poison", "Rock", "Steel"],
    "Flying" : ["Grass", "Fighting", "Bug"],
    "Psychic" : ["Fighting", "Poison"],
    "Bug" : ["Grass", "Psychic", "Dark"],
    "Rock" : ["Fire", "Ice", "Flying", "Bug"],
    "Ghost" : ["Psychic", "Ghost"],
    "Dragon" : ["Dragon"],
    "Dark" : ["Psychic", "Ghost"],
    "Steel" : ["Ice", "Rock", "Fairy"],
    "Fairy" : ["Fighting", "Dragon", "Dark"]
}

NOT_VERY_EFFECTIVE = {
    "Normal" : ["Rock", "Steel"],
    "Fire" : ["Fire", "Water", "Rock", "Dragon"],
    "Water" : ["Water", "Grass", "Dragon"],
    "Electric" : ["Electric", "Grass", "Dragon"],
    "Grass" : ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"],
    "Ice" : ["Fire", "Water", "Ice", "Steel"],
    "Fighting" : ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
    "Poison" : ["Poison", "Ground", "Rock", "Ghost"],
    "Ground" : ["Grass", "Bug"],
    "Flying" : ["Electric", "Rock", "Steel"],
    "Psychic" : ["Psychic", "Steel"],
    "Bug" : ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"],
    "Rock" : ["Fighting", "Ground", "Steel"],
    "Ghost" : ["Dark"],
    "Dragon" : ["Steel"],
    "Dark" : ["Fighting", "Dark", "Fairy"],
    "Steel" : ["Fire", "Water", "Electric", "Steel"],
    "Fairy" : ["Fire", "Poison", "Steel"]
}


# handwritten
NOT_EFFECTIVE = {
    "Normal" : ["Ghost"],
    "Fire" : [""],
    "Water" : [""],
    "Electric" : ["Ground"],
    "Grass" : [""],
    "Ice" : [""],
    "Fighting" : ["Ghost"],
    "Poison" : ["Steel"],
    "Ground" : ["Flying"],
    "Flying" : [""],
    "Psychic" : ["Dark"],
    "Bug" : [""],
    "Rock" : [""],
    "Ghost" : ["Normal"],
    "Dragon" : ["Fairy"],
    "Dark" : [""],
    "Steel" : [""],
    "Fairy" : [""]
}


# POWERS = {
#     'Scratch': 40,
#     'Tackle': 40,
#     'Pound': 40,
#     'Rage': 20,
#     'Fury Attack': 15,
#     'Ember': 40,
#     'Fire Spin': 35,
#     'Bubble': 40, 
#     'Aqua Jet': 40,
#     'Thunder Shock': 40,
#     'Thunderbolt': 90,
#     'Vine Whip': 45,
#     'Magical Leaf': 60,
#     'Ice Shard': 40,
#     'Double Kick': 30,
#     'Earthquake': 100,
#     'Wing Attack': 60,
#     'Peck': 35,
#     'Confusion': 50,
#     'Twineedle': 25,
#     'Rock Throw': 50,
#     'Rock Slide': 75,
#     'Lick': 30,
#     'Outrage': 120,
#     'Crunch': 80,
#     'Bite': 60,
#     'Flash Cannon': 80,
#     'Smog': 30,
#     'Dream Eater': 100,
#     'Body Slam': 85,
#     'Double Slap': 15,
#     'Razor Leaf': 55,
#     'Headbutt': 70,
#     'Absorb': 20, 
#     'Fairy Wind': 40, 
#     'Struggle Bug': 50, 
#     'Draining Kiss': 50,
#     'Shadow Ball': 80
# }


MOVES_DICTIONARY = {
    'Scratch': 
    {
        'name': 'Scratch',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    }, 
    'Tackle': 
    {
        'name': 'Tackle',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    }, 
    'Pound': {'name': 'Pound', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Rage': {'name': 'Rage', 'power': 20, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']}, 
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting', 'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']}, 
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']}, 
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}, 
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'], 'not very effective against': ['Steel']}, 
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel', 'super effective against': ['Ice', 'Rock', 'Fairy'], 'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']}, 
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']}, 
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}
}






STATS = {
    'Pikachu': {'Attack': 55, 'Defense': 40},
    'Charizard': {'Attack': 84, 'Defense': 78},
    'Squirtle': {'Attack': 48, 'Defense': 65},
    'Jigglypuff': {'Attack': 45, 'Defense': 20},
    'Gengar': {'Attack': 65, 'Defense': 60},
    'Magnemite': {'Attack': 35, 'Defense': 70},
    'Bulbasaur': {'Attack': 49, 'Defense': 49},
    'Charmander': {'Attack': 52, 'Defense': 43},
    'Beedrill': {'Attack': 90, 'Defense': 40},
    'Golem': {'Attack': 120, 'Defense': 130},
    'Dewgong': {'Attack': 70, 'Defense': 80},
    'Hypno': {'Attack': 73, 'Defense': 70},
    'Cleffa': {'Attack': 25, 'Defense': 28},
    'Cutiefly': {'Attack': 45, 'Defense': 40},
}

POKEMONS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40}
}


POKEMONS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70, 'Speed': 45},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84}
}

CHARACTERS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90, 'Experience': 112},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100, 'Experience': 240},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43, 'Experience': 63},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20, 'Experience': 95},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110, 'Experience':225},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70, 'Speed': 45, 'Experience': 65},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45, 'Experience': 64},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65, 'Experience': 62},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75, 'Experience': 178},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45, 'Experience': 223},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70, 'Experience': 166},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67, 'Experience': 169},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15, 'Experience': 44},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84, 'Experience': 61}
}

pikachu = ['       \:.             .:/',
"        \``._________.''/ ",
'         \             / ',
" .--.--, / .':.   .':. \"",
"/__:  /  | '::' . '::' |",
"   / /   |`.   ._.   .'|",
"  / /    |.'         '.|",
' /___-_-,|.\  \   /  /.|',
"      // |''\.;   ;,/ '|",
'      `==|:=         =:|',
"         `.          .'",
'           :-._____.-:',
"          `''       `''"]

#for row in pikachu:
#  print(row)
  
'''IMAGES = {
    'Pikachu': ,
    'Charizard': ,
    'Squirtle': ,
    'Jigglypuff': ,
    'Gengar': ,
    'Magnemite': ,
    'Bulbasaur': ,
    'Charmander': ,
    'Beedrill': ,
    'Golem': ,
    'Dewgong': ,
    'Hypno': ,
    'Cleffa': ,
    'Cutiefly': ,
}
'''