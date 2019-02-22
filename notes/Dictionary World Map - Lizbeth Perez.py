world_map = {
    "WINNIES_TREEHOUSE": {
        'NAME': "Winnie's Treehouse",
        'DESCRIPTION': "This is Winnie's Treehouse. You arrived at the place after Tiger told you that he has gone"
                       " missing. You look around to see if you could find any clues on what could've"
                       "taken Winnie. You find a note that says, 'Both don't have very pleasing names, but both are "
                       "the same. Which one do you go to? Remember you will have to come back here after your trip.'",
        'PATHS': {
            'NORTHEAST': "DISTURBING_CAVE",
            'NORTHWEST': "CREEPY_CAVE"

        }
    },
    'CREEPY_CAVE': {
        'NAME': "The Creepy Cave",
        'DESCRIPTION': "The cave is extremely dark. There's bats flying everywhere, One of the bats lands on your head"
                       "so you hit it with your shoes. When it falls a note falls along with it. The note says, 'You "
                       "could go back, or you could continue. You chose?'",
        'PATHS': {
            'WEST': "POISONOUS_POND",
            'SOUTHEAST': "WINNIES_TREEHOUSE"
         }
    },
    'POISONOUS_POND': {
        'NAME': "The Poisonous Pond",
        'DESCRIPTION': "It is really nasty in here. It's humid, hot, and it smells terrible. You watch a bird drink out"
                       "the water and die instantly. You look to your right and stuck on a tree you see a note that"
                       "says, 'There is two ways you could go but which one do you chose?'",
        'PATHS': {
            'SOUTH': "FIRE_FOREST",
            'EAST': "CREEPY_CAVE"
        }
    },
    'FIRE_FOREST': {
        'NAME': "The Fire Forest",
        'DESCRIPTION': "You arrive at the forest. You soon realize why it is called the Fire Forest. There's these"
                       "bear-looking animals that shoot fire out there mouth. You look around and you find another note"
                       "written on a rock that says, 'This forest is dangerous, there is items, but there is items you"
                       "could get to make the rest of the trip easier'.",
        'PATHS': {
            'NORTH': "POISONOUS_POND",
            'EAST': "PAIN_PLATEAU"
        }
    },
    'DISTURBING_CAVE': {
        'NAME': "The Disturbing Cave",
        'DESCRIPTION': "This cave is big and really dark. There's animals crawling on the walls and there is liquids"
                       "dripping from the ceiling. On your left you see a big rat with a note on its back. You fight "
                       "the rat for the note until you finally get it. The note says, 'You chose this cave. Now where"
                       "do you go?'. ",
        'PATHS': {
            'NORTHEAST': "ROCKY_MOUNTAIN",
            'SOUTHWEST': "WINNIES_TREEHOUSE",
            'EAST': "LOVELY_LAKE"
        }
    },
    'LOVELY_LAKE': {
        'NAME': "The Lovely Lake",
        'DESCRIPTION': "The name was definitely a lie. The lake is green and it has a terrible smell coming from it."
                       "All the animals are at least five feet from it. To the distance you see a little boat with a "
                       "box. You find a note that says, 'The name of this lake really shows how it truly is. Where do"
                       "you go from here?'.",
        'PATHS': {
            'NORTH': "ROCKY_MOUNTAIN",
            'SOUTH': "RAINY_RIVER",
            'WEST': 'DISTURBING_CAVE'
        }
    },
    'ROCKY_MOUNTAIN': {
        'NAME': "The Rocky Mountain",
        'DESCRIPTION': "At the top of the mountain you see a flag. It takes you a long time to climb the small little "
                       "mountain and you finally reach the top. At the top there's a flag with a note. The note says '"
                       "It took you a long time to get here, but the rest of the trip is going to take even longer'. ",
        'PATHS': {
            'SOUTH': 'RAINY_RIVER',
            'SOUTHWEST': 'DISTURBING_CAVE'
        }
    },
    'RAINY_RIVER': {
        'NAME': "The Rainy River",
        'DESCRIPTION': "Before you are even able to see the river, it starts pouring. Once you see the river, you see "
                       "an animal carrying a stick with a note on it. You snatch it and it starts attacking you, but"
                       "you hit it with the stick. The note says 'The rain got you really tired didn't it? You could"
                       "sleep here if you want, but  I don't recommend it.'",
        'PATHS': {
            'NORTH': 'LOVELY_LAKE'
        }
    },
    'BEAUTY_BEACH': {
        'NAME': "Beauty Beach",
        'DESCRIPTION': "Just like you expected, the name was a lie. The beach is full of trash and dead fish on the"
                       "sand. On one of the dead turtles, you see a note. The note says, 'This beach is beautiful. The"
                       "trash everywhere makes it look even better. Where do you want to go?'",
        'PATHS': {
            'NORTHWEST': "WINNIES_TREEHOUSE",
            'SOUTHEAST': "SLIPPERY_STREET"
        }
    },
    'SLIPPERY_STREET': {
        'NAME': "The Slippery Street",
        'DESCRIPTION': "The street is very slippery. On the other side of the street you see a note on a traffic cone."
                       "It takes you forever to arrive to the other side because of how many times you fell, but you "
                       "read the note and it says, 'It was super slippery wasn't it? Where do you go here from now?'",
        'PATHS': {
            'NORTHWEST': "BEAUTY_BEACH",
            'SOUTHWEST': 'ABANDONED_PARK'
        }
    },
    'ABANDONED_PARK': {
        'NAME': "The Abandoned Park",
        'DESCRIPTIONS': "There's empty rides and broken cotton candy machines. There's a lot of clown statues, you "
                        "can't tell if they're fake or real. You see one running in the distance and you panic, but "
                        "you realise he is carrying a note, so you start chasing him. Once you finally catch up,"
                        "you jump him and get the note. The note says, 'Be careful of where you go from here.'",
        'PATHS': {
            'SOUTHWEST': 'VIGOROUS_VOLCANO',
            'NORTHEAST': 'SLIPPERY_STREET'
        }
    },
    'VIGOROUS_VOLCANO': {
        'NAME': 'The Vigorous Volcano',
        'DESCRIPTIONS': "The volcano is big and steam is coming out from the top. At the top of the volcano there is a"
                        "surfboard with a paper. You walk on to the top and read the note, which says, 'How are you"
                        "going to get down.'",
        'PATHS': {
            'NORTHEAST': 'ABANDONED_PARK',
            'EAST': 'VILLAINOUS_VALLEY',
            'NORTHWEST': 'WONDERFUL_WATERFALL'
        }
    },
    'VILLAINOUS_VALLEY': {
        'NAME': 'The Villainous Valley',
        'DESCRIPTIONS': "It is really hot and you feel like you are about to faint. You reach into your backpack to"
                        "get water. As you reach into your backpack, you see a small lizard following you. It appears"
                        "to have a note. You read the note and it says, 'How was the last location?'",
        'PATHS': {
            'WEST': 'VIGOROUS_VOLCANO',
            'NORTHWEST': 'PAIN_PLATEAU'
        }
    },
    'WONDERFUL_WATERFALL': {
        'NAME': 'The Wonderful Waterfall',
        'DESCRIPTION': "The waterfall was beautiful. It was fresh and it was right what you needed to relax. You start"
                       "picking rocks to see if you could find any note. Finally under one rock, you find something "
                       "that might help you find Winnie. It is an empty honey bowl, with a note written at the bottom. "
                       "The note says 'Where did he go? Where are you going to go?'",
        'PATHS': {
            'EAST': 'VILLAINOUS_VALLEY',
            'SOUTHEAST': 'VIGOROUS_VOLCANO',
            'NORTHEAST': 'PAIN_PLATEAU'
        }
    },
    'PAIN_PLATEAU': {
        'NAME': 'The Pain Plateau',
        'DESCRIPTION': "The Pain Plateau was definitely really painful to climb. When you reach the top there is 2 big"
                       "rocks. They are completely different, but they have one thing in common: they both have a note."
                       "Both of the notes are different one talks about a wonderful place and they other one talks "
                       "about the worst place ever imaginable. You don't know which way to go. ",
        'PATHS': {
            'SOUTHWEST': 'WONDERFUL_WATERFALL',
            'SOUTHEAST': 'VILLAINOUS_VALLEY',
            'WEST': 'FIRE_FOREST'
        }
    }
}

# Other Variables
current_node = world_map["WINNIES_TREEHOUSE"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN", "NORTHEAST", "SOUTHEAST", "NORTHWEST", "SOUTHWEST"]
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
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
