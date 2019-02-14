class CellPhone(object):
    def __init__(self, model, color, battery=100, broken=False):
        self.model = model
        self.color = color  # 7 colors of rainbow
        self.battery = battery
        self.duration_of_battery = 2  # hours
        self.broken = broken

    def turn_on(self):
        if self.battery > 0 < 25:
            self.duration_of_battery = .5
            print("You have 30 minutes of charge. ")
        if self.battery == 0:
            self.duration_of_battery = 0
            print("Your phone is dead")
        if self.battery > 25 < 50:
            self.duration_of_battery = 1
            print("You have one more hour of charge. ")
        if self.battery >= 50:
            self.duration_of_battery = 2
            print("You have two more hours of charge. ")


my_cell_phone = CellPhone(8, 5, 0, True)

print(my_cell_phone.turn_on())
