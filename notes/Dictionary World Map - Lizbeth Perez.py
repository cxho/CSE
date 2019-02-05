world_map = {
    "WINNIE'S_TREEHOUSE": {
        'NAME': "Winnie's Treehouse",
        'DESCRIPTION': "This is Winnie's Treehouse. You look around to see if you could find any clues on what could've"
                       "taken Winnie. You find a note that says, '",
        'PATHS': {
            'NORTHEAST': "",
            'NORTHWEST': "CREEPY_CAVE"

        }
    },
    'CREEPY_CAVE': {
        'NAME': "The Creepy Cave",
        'DESCRIPTION': "The cave is extremely dark. There's  ' ",
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
