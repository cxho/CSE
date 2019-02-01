world_map = {
    "WINNIE'S_TREEHOUSE": {
        'NAME': "Winnie's Treehouse",
        'DESCRIPTION': "This is the classroom that you are in right now. It has two exits to the north side.",
        'PATHS': {
            'NORTHEAST': "CREEPY_CAVE"

        }
    },
    'CREEPY_CAVE': {
        'NAME': "The Creepy Cave",
        'DESCRIPTION': "There are cars parked here. To the south is Mr. Wiebe's room.",
        'PATHS': {
            'EAST': "POISONOUS_POND",
            'SOUTHWEST': "WINNIE'S_TREEHOUSE"
         }
    },
    'POISONOUS_POND': {
        'NAME': "The Poisonous Pond",
        'DESCRIPTION': "t",
        'PAST': {
            'SOUTH': "",
            'WEST': "CREEPY_CAVE"
        }
    }
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
