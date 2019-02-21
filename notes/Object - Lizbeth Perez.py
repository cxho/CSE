class CellPhone(object):
    def __init__(self, model, color, battery=100, broken=False, signal=True):
        self.model = model
        self.color = color  # 7 colors of rainbow
        self.battery = battery
        self.duration_of_battery = 2  # hours
        self.broken = broken
        self.signal = signal

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

    def call(self):
        if self.battery > 0:
            if self.signal:
                print("You are now calling someone")
            if self.signal == False:
                print("You don't have signal")
        if self.battery <= 0:
            print("Your phone is dead. ]")

my_cell_phone = CellPhone('Iphone X', 'Blue', 0, True, False)

print(my_cell_phone.turn_on())
print(my_cell_phone.call())
