class Item(object):
    def __init__(self, name, packaging, labels, protection):
        self.name = name
        self.packaging = packaging
        self.labels = labels
        self.edible = True
        self.protection = protection

    def pick_up(self):
        print("You picked up a type of food.")


class Drinks(Item):
    def __init__(self, name, packaging, labels, protection, temperature):
        super(Drinks, self).__init__(name, packaging, labels, protection)
        self.temperature = temperature
        self.quantity = 100

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


class Coffee(HotDrinks):
    def __init__(self):
        super(Coffee, self).__init__("Coffee", "Wrapper", "Ingredients", 20, 75)


class Tea(HotDrinks):
    def __init__(self):
        super(Tea, self).__init__("Tea", "Tea bag", "How to prepare it", 20, 75)


class HotChocolate(HotDrinks):
    def __init__(self):
        super(HotChocolate, self).__init__("Hot Chocolate", "none", "none", 20, 75)


class Weapons(Item):
    def __init__(self, name, ):

