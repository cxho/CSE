world_map = {
    "WINNIE'S_TREEHOUSE": {
        'NAME': "Winnie's Treehouse",
        'DESCRIPTION': "This is Winnie's Treehouse. You look around to see if you could find any clues on what could've"
                       "taken Winnie. You find a note that says, '",
        'PATHS': {
            'NORTHEAST': "DISTURBING_CAVE",
            'NORTHWEST': "CREEPY_CAVE"

        }
    },
    'CREEPY_CAVE': {
        'NAME': "The Creepy Cave",
        'DESCRIPTION': "The cave is extremely dark. There's bats flying everywhere ' ",
        'PATHS': {
            'WEST': "POISONOUS_POND",
            'SOUTHEAST': "WINNIE'S_TREEHOUSE"
         }
    },
    'POISONOUS_POND': {
        'NAME': "The Poisonous Pond",
        'DESCRIPTION': "It is really nasty in here. It's humid, hot, and it smells terrible. You watch a bird drink out"
                       "the water and die instantly. You look to your right and stuck on a tree you see a note that"
                       "says, '",
        'PATHS': {
            'SOUTH': "FIRE_FOREST",
            'EAST': "CREEPY_CAVE"
        }
    },
    'FIRE_FOREST': {
        'NAME': "The Fire Forest",
        'DESCRIPTION': "You arrive at the forest. You soon realize why it is called the Fire Forest. There's these"
                       "bear-looking animals that shoot fire out there mouth. You look around and you find another note"
                       "written on a rock that says, '",
        'PATHS': {
            'NORTH': "POISONOUS_POND",
            'EAST': ""
        }
    },
    'DISTURBING_CAVE': {
        'NAME': "The Disturbing Cave",
        'DESCRIPTION': "This cave is big and really dark. There's animals crawling on the walls and there is liquids"
                       "dripping from the ceiling. On your left you see a big rat with a note on its back. You fight "
                       "the rat for the note until you finally get it. The note says, ''",
        'PATHS': {
            'NORTH': "DISTURBING_CAVE",
            'SOUTHWEST': "WINNIE'S_TREEHOUSE",
            'EAST': "LOVELY_LAKE"
        }
    },
    'LOVELY_LAKE': {
        'NAME': "The Lovely Lake",
        'DESCRIPTION': "The name was definitely a lie. The lake is green and it has a terrible smell coming from it."
                       "All the animals are at least five feet from it. To the distance you see a little boat with a "
                       "box. You find a note that says, '",
        'PATHS': {
            'NORTH': "ROCKY_MOUNTAIN",
            'SOUTH': "RAINY_RIVER"
        }
    },
    'ROCKY_MOUNTAIN': {
        'NAME': "The Rocky Mountain",
        'DESCRIPTION': "At the top of the mountain you see a flag. It takes you a long time to climb the small little "
                       "mountain and you finally reach the top. At the top there's a flag with a note. The note says '",
        'PATHS': {
            'SOUTH': 'RAINY_RIVER',
            'SOUTHWEST': 'DISTURBING_CAVE'
        }
    },
    'RAINY_RIVER': {
        'NAME': "The Rainy River",
        'DESCRIPTION': "Before you are even able to see the river, it starts pouring. Once you see the river, you see"
                       "an animal carrying a stick with a note on it. You read it and it says, '",
        'PATHS': {
            'NORTH': 'LOVELY_LAKE'
        }
    },
    'BEAUTY_BEACH': {
        'NAME': "Beauty Beach",
        'DESCRIPTION': "Just like you expected, the name was a lie. The beach is full of trash and dead fish on the"
                       "sand. On one of the dead turtles, you see a note. The note says, ",
        'PATHS': {
            'NORTHWEST': "WINNIE'S_TREEHOUSE",
            'SOUTHEAST': "SLIPPERY_STREET"
        }
    },
    'SLIPPERY_STREET': {
        'NAME': "The Slippery Street",
        'DESCRIPTION': "The street is very slippery. On the other side of the street you see a note on a traffic cone."
                       "It takes you forever to arrive to the other side because of how many times you fell, but you "
                       "read the note and it says, '",
        'PATHS': {
            'NORTHWEST': "BEAUTY_BEACH",
            'SOUTHWEST': 'ABANDONED_PARK'
        }
    },
    'ABANDONED_PARK': {
        'NAME': "The Abandoned Park",
        'DESCRIPTIONS': "There's empty rides and broken cotton candy machines. There's a lot of clown statues, you "
                        "can't tell if they're fake or real. You see one running in the distance and you panick, but "
                        "you realise he is carrying a note. ",
        'PATHS': {
            'SOUTHWEST': '',
            'NORTHEAST': 'SLIPPERY_STREET'
        }
    },
}

# Other Variables
current_node = world_map["WINNIE'S_TREEHOUSE"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", "NORTHEAST", "SOUTHEAST", "NORTHWEST", "SOUTHWEST"]
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("command not recognized")
