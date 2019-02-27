class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, southeast=None, southwest=None,
                 northeast=None, northwest=None, description="", character=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.southwest = southwest
        self.northeast = northeast
        self.northwest = northwest
        self.description = description
        self.character = character


class Player(object):
    def __init__(self, starting_room):
        self.health = 100
        self.current_location = starting_room
        self.damage = 10
        self.inventory = []

    def move(self, newlocation):
        """

        :param newlocation: The variable containing a room object
        """
        self.current_location = newlocation


"""
R19A = Room("R19A")
parking_lot = Room('The Parking Lot', None, R19A)

R19A.north = parking_lot
"""

WINNIES_TREEHOUSE = Room("Winnie's Treehouse", None, None, None, None, None, None, None, None,
                         "This is Winnie's Treehouse. You arrived at the place after Tiger told you that he has gone"
                         "missing. You look around to see if you could find any clues on what could've"
                         "taken Winnie. Tiger tells you he has been missing for 2 days now. You find a note that says,"
                         "'Both don't have very pleasing names, but both are the same. Which one do you go to? Remember"
                         " you will have to come back here after your trip.'", "Tiger")
CREEPY_CAVE = Room("The Creepy Cave", None, None, None, None, WINNIES_TREEHOUSE, None, None,
                   "The cave is extremely dark. There's bats flying everywhere, One of the bats lands on your head,"
                   "so you hit it with your shoes. When it falls a note falls along with it. The note says, 'You "
                   "could go back, or you could continue. You chose?'")
POISONOUS_POND = Room("The Poisonous Pond", None, None, CREEPY_CAVE, None, None, None, None, None,
                      "It is really nasty in here. It's humid, hot, and it smells terrible. You watch a bird drink out "
                      "the water and die instantly. You look to your right and stuck on a tree you see a note that "
                      "says, 'There is two ways you could go but which one do you chose?'")
FIRE_FOREST = Room("The Fire Forest", POISONOUS_POND, None, None, None, None, None, None, None,
                   "You arrive at the forest. You soon realize why it is called the Fire Forest. There's these "
                   "bear-looking animals that shoot fire out there mouth. You look around and you find another note "
                   "written on a rock that says, 'This forest is dangerous, there is items, but there is items you "
                   "could get to make the rest of the trip easier'.")
DISTURBING_CAVE = Room("The Disturbing Cave", None, None, None, None, None, WINNIES_TREEHOUSE, None, None,
                       "This cave is big and really dark. There's animals crawling on the walls and there is liquids "
                       "dripping from the ceiling. On your left you see a big rat with a note on its back. You fight "
                       "the rat for the note until you finally get it. The note says, 'You chose this cave. Now where "
                       "do you go?'. ")
LOVELY_LAKE = Room("The Lovely Lake", None, None, None, DISTURBING_CAVE, None, None, None, None,
                   "The name was definitely a lie. The lake is green and it has a terrible smell coming from it. "
                   "All the animals are at least five feet from it. To the distance you see a little boat with a "
                   "box. You find a note that says, 'The name of this lake really shows how it truly is. Where do "
                   "you go from here?'.")
ROCKY_MOUNTAIN = Room("The Rocky Mountain", None, None, None, None, None, DISTURBING_CAVE, None, None,
                      "At the top of the mountain you see a flag. It takes you a long time to climb the small little "
                      "mountain and you finally reach the top. At the top there's a flag with a note. The note says '"
                      "It took you a long time to get here, but the rest of the trip is going to take even longer'.")
RAINY_RIVER = Room("The Rainy River", LOVELY_LAKE, None, None, None, None, None, None, None,
                   "Before you are even able to see the river, it starts pouring. Once you see the river, you see "
                   "an animal carrying a stick with a note on it. You snatch it and it starts attacking you, but "
                   "you hit it with the stick. The note says 'The rain got you really tired didn't it? You could "
                   "sleep here if you want, but  I don't recommend it.'")
BEAUTY_BEACH = Room("Beauty Beach", None, None, None, None, None, None, None, WINNIES_TREEHOUSE,
                    "Just like you expected, the name was a lie. The beach is full of trash and dead fish on the "
                    "sand. On one of the dead turtles, you see a note. The note says, 'This beach is beautiful. The "
                    "trash everywhere makes it look even better. Where do you want to go?'")
SLIPPERY_STREET = Room("The Slippery Street", None, None, None, None, None, None, None, BEAUTY_BEACH,
                       "The street is very slippery. On the other side of the street you see a note on a traffic cone. "
                       "It takes you forever to arrive to the other side because of how many times you fell, but you "
                       "read the note and it says, 'It was super slippery wasn't it? Where do you go here from now?'")
ABANDONED_PARK = Room("The Abandoned Park", None, None, None, None, None, None, SLIPPERY_STREET, None,
                      "There's empty rides and broken cotton candy machines. There's a lot of clown statues, you "
                      "can't tell if they're fake or real. You see one running in the distance and you panic, but "
                      "you realise he is carrying a note, so you start chasing him. Once you finally catch up, "
                      "you jump him and get the note. The note says, 'Be careful of where you go from here.'")
VIGOROUS_VOLCANO = Room("The Vigorous Volcano", None, None, None, None, None, None, ABANDONED_PARK, None,
                        "The volcano is big and steam is coming out from the top. At the top of the volcano there is a "
                        "surfboard with a paper. You walk on to the top and read the note, which says, 'How are you "
                        "going to get down.'")
VILLAINOUS_VALLEY = Room("The Villainous Valley", None, None, None, VIGOROUS_VOLCANO, None, None, None, None,
                         "It is really hot and you feel like you are about to faint. You reach into your backpack to "
                         "get water. As you reach into your backpack, you see a small lizard following you. It appears "
                         "to have a note. You read the note and it says, 'How was the last location?'")
WONDERFUL_WATERFALL = Room("The Wonderful Waterfall", None, None, VILLAINOUS_VALLEY, None, VIGOROUS_VOLCANO, None, None,
                           None,
                           "The waterfall was beautiful. It was fresh and it was right what you needed to relax. You "
                           "start picking rocks to see if you could find any note. Finally under one rock, you find "
                           "something that might help you find Winnie. It is an empty honey bowl, with a note written "
                           "at the bottom. The note says 'Where did he go? Where are you going to go?'")
PAIN_PLATEAU = Room("The Pain Plateau", None, None, None, FIRE_FOREST, VILLAINOUS_VALLEY, WONDERFUL_WATERFALL, None,
                    None,
                    "The Pain Plateau was definitely really painful to climb. When you reach the top there is 2 big "
                    "rocks. They are completely different, but they have one thing in common: they both have a note. "
                    "Both of the notes are different one talks about a wonderful place and they other one talks "
                    "about the worst place ever imaginable. You don't know which way to go.")

WINNIES_TREEHOUSE.northwest = DISTURBING_CAVE
WINNIES_TREEHOUSE.northeast = CREEPY_CAVE
CREEPY_CAVE.west = POISONOUS_POND
POISONOUS_POND.south = FIRE_FOREST
FIRE_FOREST.east = PAIN_PLATEAU
DISTURBING_CAVE.northeast = ROCKY_MOUNTAIN
DISTURBING_CAVE.east = LOVELY_LAKE
LOVELY_LAKE.north = ROCKY_MOUNTAIN
LOVELY_LAKE.south = RAINY_RIVER
ROCKY_MOUNTAIN.south = RAINY_RIVER
BEAUTY_BEACH.southeast = SLIPPERY_STREET
SLIPPERY_STREET.southwest = ABANDONED_PARK
ABANDONED_PARK.southwest = VIGOROUS_VOLCANO
VIGOROUS_VOLCANO.east = VILLAINOUS_VALLEY
VIGOROUS_VOLCANO.northwest = WONDERFUL_WATERFALL
VILLAINOUS_VALLEY.northwest = PAIN_PLATEAU
WONDERFUL_WATERFALL.northeast = PAIN_PLATEAU

player = Player(WINNIES_TREEHOUSE)

playing = True
directions = ['north', 'south', 'east', 'west', 'northeast', 'southeast', 'northwest', 'southwest']

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() in directions:
        try:
            # command =  'north'
            room_object = getattr(player.current_location, command)
            player.move(room_object)
        except KeyError:
            print("I can't go that way.")
    else:
        print("command not recognized")
