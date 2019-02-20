class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, southeast=None, southwest=None,
                 northeast=None, northwest=None, description=""):
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

'''
R19A = Room("R19A")
parking_lot = Room('The Parking Lot', None, R19A)

R19A.north = parking_lot
'''

WINNIES_TREEHOUSE = Room("Winnie's Treehouse", None, None, None, None, None, None, None, None,
                        "This is Winnie's Treehouse. You arrived at the place after Tiger told you that he has gone"
                       " missing. You look around to see if you could find any clues on what could've"
                       "taken Winnie. You find a note that says, 'Both don't have very pleasing names, but both are "
                       "the same. Which one do you go to? Remember you will have to come back here after your trip.'")
CREEPY_CAVE = Room("The Creepy Cave", None, None, None, None, WINNIES_TREEHOUSE, None, None,
                   "The cave is extremely dark. There's bats flying everywhere, One of the bats lands on your head"
                   "so you hit it with your shoes. When it falls a note falls along with it. The note says, 'You "
                   "could go back, or you could continue. You chose?'")
POISONOUS_POND = Room("The Poisonous Pond", None, None, CREEPY_CAVE, None, None, None, None, None,
                      "It is really nasty in here. It's humid, hot, and it smells terrible. You watch a bird drink out"
                      "the water and die instantly. You look to your right and stuck on a tree you see a note that"
                      "says, 'There is two ways you could go but which one do you chose?'")
FIRE_FOREST = Room("The Fire Forest", POISONOUS_POND, None, None, None, None, None, None, None,
                   "You arrive at the forest. You soon realize why it is called the Fire Forest. There's these"
                   "bear-looking animals that shoot fire out there mouth. You look around and you find another note"
                   "written on a rock that says, 'This forest is dangerous, there is items, but there is items you"
                   "could get to make the rest of the trip easier'.")
DISTURBING_CAVE = Room("The Disturbing Cave", )