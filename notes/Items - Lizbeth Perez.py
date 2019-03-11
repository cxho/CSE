class Item(object):
    def __init__(self, name, packaging, labels, protection):
        self.name = name
        self.packaging = packaging
        self.labels = labels
        self.protection = protection

    def pick_up(self):
        self.packaging = "In a backpack"
        print("You picked up an item.")


class BackpackStuff(Item):
    def __init__(self, name, packaging, labels, protection):
        super(BackpackStuff, self).__init__(name, packaging, labels, protection)

    def take_out(self):
        self.packaging = "Outside a backpack"
        print("You take an item out of your backpack.")

    def put_in(self):
        self.packaging = "In a backpack"
        print("You put an item in your backpack")


class Drinks(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, temperature):
        super(Drinks, self).__init__(name, packaging, labels, protection)
        self.temperature = temperature
        self.quantity = 25

    def drink_liquid(self):
        self.quantity -= 1
        print("You drank the liquid")

    def throw_liquid(self):
        self.quantity = 0
        print("You threw the drink")


class HotDrinks(Drinks):
    def __init__(self, name, packaging, labels, protection, temperature):
        super(HotDrinks, self).__init__(name, packaging, labels, protection, temperature)
        self.temperature = 75


class Tea(HotDrinks):
    def __init__(self):
        super(Tea, self).__init__("Tea", "Tea bag", "How to prepare it", 20, 75)


class Armor(BackpackStuff):
    def __init__(self, name, packaging, labels, protection):
        super(Armor, self).__init__(name, packaging, labels, protection)

    def wear_it(self):
        self.protection -= 5
        print("You are now wearing the item.")


class Helmet(BackpackStuff):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", "none", "Dora the Destroyer", 78)


class ChestPlate(Armor):
    def __init__(self):
        super(ChestPlate, self).__init__("A Protective Chest Plate", "none", "Dora the Destroyer", 98)


class Weapons(BackpackStuff):
    def __init__(self, name, packaging, labels, protection):
        super(Weapons, self).__init__(name, packaging, labels, protection)


class Sword(Weapons):
    def __init__(self):
        super(Weapons, self).__init__("Magical Honey Sword", "none", "none", 80)


class ToyBaseballBat(Weapons):
    def __init__(self):
        super(Weapons, self).__init__("Super Dangerous Bat", "none", "none", 67)


class BBGun(Weapons):
    def __init__(self):
        super(Weapons, self).__init__("Scary BB Gun", "none", "none", 56)


class Knife(Weapons):
    def __init__(self):
        super(Weapons, self).__init__("Traumatizing Knife", "none", "none", 46)


class BackupAx(Weapons):
    def __init__(self):
        super(Weapons, self).__init__("Backup Ax", "none", "none", 70)


class Screwdriver(Weapons):
    def __init__(self):
        super(Screwdriver, self).__init__("Screwdriver", "none", "none", 30)


class HealingStuff(BackpackStuff):
    def __init__(self, name, packaging, labels, protection, healing):
        super(HealingStuff, self).__init__(name, packaging, labels, protection)
        self.healing_amt = healing

    def use_stuff(self):
        self.protection -= 1
        print("You have been healed")


class MedKit(HealingStuff):
    def __init__(self):
        super(MedKit, self).__init__("Med Kit", "none", "none", 0, 89)


class RandomItems(BackpackStuff):
    def __init__(self, name, packaging, labels, protection):
        super(RandomItems, self).__init__(name, packaging, labels, protection)


class Bible(RandomItems):
    def __init__(self):
        super(Bible, self).__init__("Bible", "none", "none", 56)


class Shield(RandomItems):
    def __init__(self):
        super(Shield, self).__init__("Protective Shield", "none", "none", 95)


class Map(RandomItems):
    def __init__(self):
        super(Map, self).__init__("The Map", "none", "Ashdown Map", 0)


class PlasticBag(RandomItems):
    def __init__(self):
        super(PlasticBag, self).__init__("A Plastic Bag", "none", "Evidence", 0)


class ItemsFound(Item):
    def __init__(self, name, packaging, labels, protection):
        super(ItemsFound, self).__init__(name, packaging, labels, protection)


class Key(ItemsFound):
    def __init__(self):
        super(Key, self).__init__("The Magical Key", "none", "Opens secret room", 0)


class PuddleOfHoney(ItemsFound):
    def __init__(self):
        super(PuddleOfHoney, self).__init__("Puddle of honey", "none", "none", 0)


first_key = Key()
yummy_tea = Tea()
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
