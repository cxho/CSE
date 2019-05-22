def fight(enemy):
    print("A %s appears and wants to fight!" % enemy.name)
    while Dora_the_detective.health > 0 and enemy.health > 0:
        enemy.attack(Dora_the_detective)
        if Dora_the_detective.health <= 0:
            print("GAME OVER")
            quit(0)
        if enemy.health <= 0:
            print("%s has died. oops!" % enemy.name)
        input("Press any key to attack")
        Dora_the_detective.attack(enemy)


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, southeast=None, southwest=None,
                 northeast=None, northwest=None, description="", items=None, character=None):
        if items is None:
            items = []
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
        self.items = items
        self.character = character


class Item(object):
    def __init__(self, name, packaging, labels, protection, description):
        self.name = name
        self.packaging = packaging
        self.labels = labels
        self.protection = protection
        self.description = description

    def pick_up(self):
        self.packaging = "In a backpack"
        print("You picked up an item.")


class Character(object):
    def __init__(self, name, health, weapons, armor):
        self.name = name
        self.health = health
        self.weapons = weapons
        self.armor = armor

    def take_damage(self, damage):
        print("%s has %d health left" % (self.name, self.health))
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapons.damage))
        target.take_damage(self.weapons.damage)


class Enemy(Character):
    def __init__(self, name, health, weapons, armor):
        super(Enemy, self).__init__(name, health, weapons, armor)


class BackpackStuff(Item):
    def __init__(self, name, packaging, labels, protection, description):
        super(BackpackStuff, self).__init__(name, packaging, labels, protection, description)

    def take_out(self):
        self.packaging = "Outside a backpack"
        print("You take an item out of your backpack.")

    def put_in(self):
        self.packaging = "In a backpack"
        print("You put an item in your backpack")


class Drinks(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, temperature, description):
        super(Drinks, self).__init__(name, packaging, labels, protection, description)
        self.temperature = temperature
        self.quantity = 25

    def drink_liquid(self):
        self.quantity -= 1
        print("You drank the liquid")

    def throw_liquid(self):
        self.quantity = 0
        print("You threw the drink")


class HotDrinks(Drinks):
    def __init__(self, name, packaging, labels, protection, temperature, description):
        super(HotDrinks, self).__init__(name, packaging, labels, protection, temperature, description)
        self.temperature = 75


class Coffee(HotDrinks):
    def __init__(self):
        super(Coffee, self).__init__("Coffee", "Coffee Cup", "How to prepare it", 20, 75, "Energizing and Calming "
                                     "Coffee")


class Armor(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, description):
        super(Armor, self).__init__(name, packaging, labels, protection, description)

    def wear_it(self):
        self.protection -= 5
        print("You are now wearing the item.")


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", "none", "Dora the Destroyer", 78, "Helps protect the head")


class ChestPlate(Armor):
    def __init__(self):
        super(ChestPlate, self).__init__("A Protective Chest Plate", "none", "Dora the Destroyer", 98, "Protects the "
                                         "chest completely")


class Weapons(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, damage, description):
        super(Weapons, self).__init__(name, packaging, labels, protection, description)
        self.damage = damage
        self.description = description


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__("Magical Honey Sword", "none", "none", 80, 40, "Could cut things in half "
                                    "(Even humans)")


class ToyBaseballBat(Weapons):
    def __init__(self):
        super(ToyBaseballBat, self).__init__("Super Dangerous Bat", "none", "none", 67, 50, "Could knock you out with "
                                             "one hit")


class BBGun(Weapons):
    def __init__(self):
        super(BBGun, self).__init__("Scary BB Gun", "none", "none", 56, 28, "Could make you go bye bye")


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Traumatizing Knife", "none", "none", 46, 78, "stabs you until you're dead")


class BackupAx(Weapons):
    def __init__(self):
        super(BackupAx, self).__init__("Backup Ax", "none", "none", 70, 67, "Could cut you in half")


class Screwdriver(Weapons):
    def __init__(self):
        super(Screwdriver, self).__init__("Screwdriver", "none", "none", 30, 25, "Could poke you in the eye")


class HealingStuff(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, healing, description):
        super(HealingStuff, self).__init__(name, packaging, labels, protection, description)
        self.healing_amt = healing

    def use_stuff(self):
        self.healing_amt += 10
        print("You have been healed")


class MedKit(HealingStuff):
    def __init__(self):
        super(MedKit, self).__init__("Med Kit", "none", "none", 0, 89, "Safety first")


class RandomItems(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, description):
        super(RandomItems, self).__init__(name, packaging, labels, protection, description)


class Bible(RandomItems):
    def __init__(self):
        super(Bible, self).__init__("Bible", "none", "none", 56, "You need Jesus")


class Shield(RandomItems):
    def __init__(self):
        super(Shield, self).__init__("Protective Shield", "none", "none", 95, "Blocks away the haters and the hits :)")


class Map(RandomItems):
    def __init__(self):
        super(Map, self).__init__("The Map", "none", "Ashdown Map", 0, "Could help you find locations, but not your "
                                  "will to live :(")


class PlasticBag(RandomItems):
    def __init__(self):
        super(PlasticBag, self).__init__("A Plastic Bag", "none", "Evidence", 0, "You should know what a platic bag is "
                                         "used for. If you don't, you're too rich for this game :(")


class ItemsFound(Item):
    def __init__(self, name, packaging, labels, protection, description):
        super(ItemsFound, self).__init__(name, packaging, labels, protection, description)


class Key(ItemsFound):
    def __init__(self):
        super(Key, self).__init__("The Magical Key", "none", "Opens secret room", 0, "Opens secret room or you can "
                                  "stab people")


class PuddleOfHoney(ItemsFound):
    def __init__(self):
        super(PuddleOfHoney, self).__init__("Puddle of honey", "none", "none", 0, "You could eat it and die from food"
                                            " poisoning, or use it as evidence.")


class HoneyBowls(ItemsFound):
    def __init__(self):
        super(HoneyBowls, self).__init__("Honey Bowls", "none", "honey", 0, "No wonder Winnie is so fat. ")


class EvilElmo(Enemy):
    def __init__(self):
        super(EvilElmo, self).__init__("Possesed Elmo", 100, BBGun(), "none")


class Player(object):
    def __init__(self, starting_room):
        self.name = "Dora the Detective"
        self.health = 100
        self.current_location = starting_room
        self.damage = 10
        self.inventory = []
        self.weapons = a_sword

    def move(self, newlocation):
        """

        :param newlocation: The variable containing a room object
        """
        self.current_location = newlocation

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapons.damage))
        target.take_damage(self.weapons.damage)

    def take_damage(self, damage):
        print("%s has %d health left" % (self.name, self.health))
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def equip(self):
        print("Which item do you want to equip? (Type in a number)")
        for num, item in enumerate(self.inventory):
            print(str(num + 1) + ": " + item.name)
        print()
        index = -1
        while 0 > index or index > len(self.inventory):
            try:
                index = int(input(">_"))
            except ValueError:
                print("That is not a number")
        item_to_equip = self.inventory[index - 1]

        if isinstance(item_to_equip, ChestPlate):
            self.protection = 100
            print("You have %s protection" % self.protection)
        if isinstance(item_to_equip, Helmet):
            self.protection = 100
            print("You have %s protection" % self.protection)
        if isinstance(item_to_equip, Sword):
            Dora_the_detective.damage = 78
            print("You could do %s damage with one hit." % self.damage)
        if isinstance(item_to_equip, ToyBaseballBat):
            Dora_the_detective.damage = 50
            print("You could do %s damage with one hit." % self.damage)
        if isinstance(item_to_equip, BBGun):
            Dora_the_detective.damage = 15
            print("You could do %s damage with one hit." % self.damage)
        if isinstance(item_to_equip, Knife):
            Dora_the_detective.damage = 46
            print("You could do %s damage with one hit." % self.damage)
        if isinstance(item_to_equip, BackupAx):
            Dora_the_detective.damage = 58
            print("You could do %s damage with one hit." % self.damage)
        if isinstance(item_to_equip, Screwdriver):
            Dora_the_detective.damage = 23
            print("You could do %s damage with one hit." % self.damage)
        if isinstance(item_to_equip, MedKit):
            Dora_the_detective.health = 100
            print("Your health is now at %s" % self.health)
        if isinstance(item_to_equip, Bible):
            Dora_the_detective.damage = 100
            print("You could do %s damage with one use." % self.damage)
        if isinstance(item_to_equip, Shield):
            self.protection = 89
            print("You have %s protection" % self.protection)
        if isinstance(item_to_equip, Map):
            print("You have to figure this out on your own sucker.")


class Dora(Player):
    def __init__(self):
        super(Dora, self).__init__(WINNIES_TREEHOUSE)


"""
R19A = Room("R19A")
parking_lot = Room('The Parking Lot', None, R19A)

R19A.north = parking_lot
"""

first_key = Key()
yummy_coffee = Coffee()
protective_helmet = Helmet()
protective_chest_plate = ChestPlate()
a_sword = Sword()
toy_baseball_bat = ToyBaseballBat()
only_bbgun = BBGun()
pointy_knife = Knife()
backup_ax = BackupAx()
a_screwdriver = Screwdriver()
healing_medkit = MedKit()
holy_bible = Bible()
only_shield = Shield()
ashdown_forest_map = Map()
a_plastic_bag = PlasticBag()
winnies_puddle_of_honey = PuddleOfHoney()

Evil_Elmo = Character("Possesed Elmo", 100, a_screwdriver, None)
WinnieThePooh = Character("Winnie the Pooh", 666, toy_baseball_bat, protective_chest_plate)

WINNIES_TREEHOUSE = Room("Winnie's Treehouse", None, None, None, None, None, None, None, None,
                         "This is Winnie's Treehouse. You arrived at the place after Tiger told you that he has gone "
                         "missing. You look around to see if you could find any clues on what could've "
                         "taken Winnie. Tiger tells you he has been missing for 2 days now. You find a note that says,"
                         "'Both don't have very pleasing names, but both are the same. Which one do you go to?",
                         [first_key])
SECRET_ROOM = Room("Winnie's Secret Room", WINNIES_TREEHOUSE, None, None, None, None, None, None, None, "This is "
                   "This is Winnie's Secret Room. You look around to see if he is in here somewhere. He isn't.",
                   [HoneyBowls])
CREEPY_CAVE = Room("The Creepy Cave", None, None, None, None, WINNIES_TREEHOUSE, None, None, None,
                   "The cave is extremely dark. There's bats flying everywhere, One of the bats lands on your head, "
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
                   "could get to make the rest of the trip easier'.", [backup_ax, pointy_knife, only_shield])
DISTURBING_CAVE = Room("The Disturbing Cave", None, None, None, None, None, WINNIES_TREEHOUSE, None, None,
                       "This cave is big and really dark. There's animals crawling on the walls and there is liquids "
                       "dripping from the ceiling. On your left you see a big rat with a note on its back. You fight "
                       "the rat for the note until you finally get it. You find a puddle of honey on the floor. "
                       "Winnie must've been here. Maybe you should pick up the honey. The note says, 'You chose this "
                       "cave. Now where ""do you go?'. ", [winnies_puddle_of_honey])
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
                      "you jump him and get the note. The note says, 'Be careful of where you go from here.' "
                      "In the distance, it appears someone is playing party music. Someone is playing the cha cha slide"
                      ". This place is abandoned, which makes it creepy, but you join in because its your favorite "
                      " party song. Cha cha real smooth. ")
VIGOROUS_VOLCANO = Room("The Vigorous Volcano", None, None, None, None, None, None, ABANDONED_PARK, None,
                        "The volcano is big and steam is coming out from the top. At the top of the volcano there is a "
                        "surfboard with a paper. You walk on to the top and read the note, which says, 'How are you "
                        "going to get down.' You use the surfboard to get down. When you get there you see Winnie the "
                        "Pooh. How are you going to attack him? ", None, WinnieThePooh)
VILLAINOUS_VALLEY = Room("The Villainous Valley", None, None, None, VIGOROUS_VOLCANO, None, None, None, None,
                         "It is really hot and you feel like you are about to faint. You reach into your backpack to "
                         "get water. As you reach into your backpack, you see a small lizard following you. It appears "
                         "to have a note. You read the note and it says, 'How was the last location?'")
WONDERFUL_WATERFALL = Room("The Wonderful Waterfall", None, None, None, None, VIGOROUS_VOLCANO, None, None,
                           None,
                           "The waterfall was beautiful. It was fresh and it was right what you needed to relax. You "
                           "start picking rocks to see if you could find any note. Finally under one rock, you find "
                           "something that might help you find Winnie. It is an empty honey bowl, with a note written "
                           "at the bottom. The note says 'Where did he go? Where are you going to go?'")
PAIN_PLATEAU = Room("The Pain Plateau", None, None, None, FIRE_FOREST, VILLAINOUS_VALLEY, WONDERFUL_WATERFALL, None,
                    None,
                    "The Pain Plateau was definitely really painful to climb. When you reach the top there is 2 big "
                    "rocks. The are completely different, but they have one thing in common: they both have a note. "
                    "Both of the notes are different one talks about a wonderful place and they other one talks "
                    "about the worst place ever imaginable. You don't know which way to go, but out of nowhere an evil "
                    "looking creature comes out from one of the rocks. You look at it closely and realize its Elmo. He "
                    "throws fire at you and you dodge it. He appears to be possessed.",
                    None, Evil_Elmo)
HEEAVEN = Room("Hee Hee Heaven", None, None, None, None, None, None, None, None, "This is Hee Hee Heaven. Michael "
               "Jackson is our god and we worship him everyday. All hail Hee Hee Man.")
HEE_HELL = Room("Hee Hee Hell", None, None, None, None, None, None, None, None, "You are in Hee Hee Hell. We worship "
                "Miranda Cosgrove here because she is a god. Be like everyone of us in here and sell your soul to "
                "Miranda, hee hee. ")

WINNIES_TREEHOUSE.northwest = CREEPY_CAVE
WINNIES_TREEHOUSE.northeast = DISTURBING_CAVE
WINNIES_TREEHOUSE.south = SECRET_ROOM
CREEPY_CAVE.west = POISONOUS_POND
POISONOUS_POND.south = FIRE_FOREST
FIRE_FOREST.east = PAIN_PLATEAU
DISTURBING_CAVE.northeast = ROCKY_MOUNTAIN
DISTURBING_CAVE.east = LOVELY_LAKE
LOVELY_LAKE.north = ROCKY_MOUNTAIN
LOVELY_LAKE.south = RAINY_RIVER
ROCKY_MOUNTAIN.south = LOVELY_LAKE
BEAUTY_BEACH.southeast = SLIPPERY_STREET
SLIPPERY_STREET.southwest = ABANDONED_PARK
ABANDONED_PARK.southwest = VIGOROUS_VOLCANO
VIGOROUS_VOLCANO.east = VILLAINOUS_VALLEY
VIGOROUS_VOLCANO.northwest = WONDERFUL_WATERFALL
VILLAINOUS_VALLEY.northwest = PAIN_PLATEAU
WONDERFUL_WATERFALL.northeast = PAIN_PLATEAU
HEEAVEN.out = WINNIES_TREEHOUSE
HEE_HELL.out = WINNIES_TREEHOUSE


Dora_the_detective = Player(WINNIES_TREEHOUSE)

sword = Weapons("Sword", "none", "none", 5, 15, "A sword")
sword2 = Weapons("Orc Sword", "none", "none", 5, 80, "Another Sword")

Dora_the_detective.inventory = [yummy_coffee, protective_helmet, protective_chest_plate, a_sword, toy_baseball_bat,
                                only_bbgun, a_screwdriver, holy_bible, healing_medkit, ashdown_forest_map,
                                a_plastic_bag]

directions = ['north', 'south', 'east', 'west', 'northeast', 'southeast', 'northwest', 'southwest', 'out']
short_directions = ['n', 's', 'e', 'w', 'ne', 'se', 'nw', 'sw', 'o']
playing = True

# Controller
while playing:
    if Dora_the_detective.current_location.character is not None:
        fight(Dora_the_detective.current_location.character)
        Dora_the_detective.current_location.character = None
    print(Dora_the_detective.current_location.name)
    print(Dora_the_detective.current_location.description)
    command = input(">_")
    print("")
    if command.lower() in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit', 'adios sucker', 'adios']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(Dora_the_detective.current_location, command)
            if room_name is None:
                raise AttributeError
            Dora_the_detective.move(room_name)
        except KeyError:
            print("This key does not exist")
        except AttributeError:
            print("I can't go that way.")
            print()
    elif command.lower() in ["dora's backpack", "backpack", "b"]:
        ting = 0
        for i in Dora_the_detective.inventory:
            print(Dora_the_detective.inventory[ting].name)
            ting += 1
    elif command.lower() in ['check']:
        if len(Dora_the_detective.current_location.items) > 0:
            print()
            print("The following items are in the room:")
            for num, item in enumerate(Dora_the_detective.current_location.items):
                print(str(num + 1) + ": " + item.name)
                print()
        else:
            print("There are no items in this room.")
            print()

    elif command.lower() in ['pick up', 'pickup']:
        choice = input("what will you pick up: ")

        number = int(choice)
        if len(Dora_the_detective.current_location.items) >= number > 0:
            Dora_the_detective.inventory.append(Dora_the_detective.current_location.items[number - 1])
            Dora_the_detective.current_location.items.pop(number - 1)

            print("The item is now in your backpack.")
            print()
        else:
            print("invalid number")
    elif "drop" in command:
        choice = input("What will you drop: ")

        number = int(choice)
        if len(Dora_the_detective.current_location.items) > 0:
            Dora_the_detective.current_location.items.append(Dora_the_detective.inventory[number - 1])
            Dora_the_detective.inventory.pop(number - 1)
    elif command.lower() in ['hee hee man is a god']:
        Dora_the_detective.current_location = HEEAVEN
    elif command.lower() in ['hee hee woman is a god']:
        Dora_the_detective.current_location = HEE_HELL
    elif command.lower() in ['help', 'ayuda']:
        print("~The commands for this game are~: \n",
              "pickup, pick up = pick up items \n",
              "drop = drop items \n",
              "backpack, b = print inventory \n",
              "hee hee man is a god = go to Hee Hee Heaven \n",
              "hee hee woman is a god = go to Hee Hee Hell \n",
              "check = look for items in the room \n",
              "~The directions for this game are~: \n",
              "north, n \n",
              "northeast, ne \n",
              "southeast, se \n",
              "south, s \n",
              "east, e \n",
              "west, w \n",
              "northwest, nw \n",
              "southwest, sw \n")
        print()
    elif command.lower() in ["equip", "e"]:
        what = input("weapon or clothing: ")
        if what.lower() == "clothing":
            Dora_the_detective.equip()
        elif what.lower() == "weapon":
            Dora_the_detective.equip()
    elif command.lower() in ["unequip"]:
        pass
    elif command.lower() in ['we did it!']:
        print("we did it \n"
              "we did it \n"
              "we did it yeah \n"
              "lo hicimos \n"
              "we did it")
    elif command.lower() in ['vamonos']:
        print("c'mon vamonos\n"
              "everybody lets go \n"
              "c'mon lets get to it \n"
              "i know that we can do it")
    elif command.lower() in ["cha cha real smooth"]:
        print("To the left, take it back now yall \n",
              "One hop this time, right foot lets stomp \n",
              "Left foot let's stomp, cha cha real smooth \n",
              "Turn it out, to the left \n",
              "Take it back now y'all \n",
              "One hop this time, right foot let's stomp \n",
              "Left foot let's stomp, cha cha now y'all \n",
              "Now it's time to get funky \n",
              "To the right now, to the left \n",
              "Take it back now y'all \n",
              "One hop this time, one hop this time \n",
              "Right foot two stomps, left foot two stomps\n",
              "Slide to the left, slide to the right \n",
              "Crisscross, crisscross \n",
              "Cha cha real smooth \n",
              "Let's go to work \n",
              "To the left, take it back now y'all \n",
              "Two hops this time, two hops this time \n",
              "Right foot two stomps, left foot two stomps \n",
              "Hands on your knees, hands on your knees \n",
              "Get funky with it, aahhhhhhhhhh yaaaa \n",
              "Come on, cha cha now y'all \n",
              "Turn it out, to the left \n",
              "Take it back now y'all \n",
              "Five hops this time \n",
              "Right foot let's stomp, left foot let's stomp \n",
              "Right foot again, left foot again \n",
              "Right foot let's stomp, left foot let's stomp \n",
              "Freeze, everybody clap yo hands \n",
              "Come on y'all, check it out \n",
              "How low can you go? \n",
              "Can you go down low? \n",
              "All the way to da floor? \n",
              "How low can you go? \n",
              "Can you bring it to the top? \n",
              "Like it never never stop? \n",
              "Can you bring it to the top? \n",
              "One hop, right foot now \n",
              "Left foot now y'all \n",
              "Cha cha real smooth \n",
              "Turn it down, to the left \n",
              "Take it back now y'all \n",
              "One hop this time, one hop this time \n",
              "Reverse, reverse \n",
              "Slide to the left, slide to the right \n",
              "Reverse reverse, reverse reverse \n",
              "Cha cha now y'all \n",
              "Cha cha again \n",
              "Cha cha now y'all \n",
              "Cha cha again \n",
              "Turn it down \n",
              "To the left, that it back now y'all \n",
              "Two hops two hops, two hops two hops \n")
    else:
        print("Command Not ~Recognized~")
        print("Cha cHA REAL SMOOTH 😊🎉🐱‍👓")
        print()
