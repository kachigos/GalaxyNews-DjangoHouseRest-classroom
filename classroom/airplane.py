class Airplane:

    def __init__(self, mark, model, year, max_speed):
        self.mark = mark

        self.model = model

        self.year = year

        self.max_speed = max_speed

        self.odometer = 0

        self.is_flying = False

    def take_off(self):
        self.is_flying = True

        message_take = f"{self.mark} {self.model} was take off."

        return message_take

    def fly(self, km):
        self.odometer += km

        message_fly = f"{self.mark}f lew {self.odometer}km during the flying {self.max_speed} km/h."

        return message_fly

    def land(self):
        self.is_flying = False

        message_land = f"{self.mark} landed, the odometer shows {self.odometer}km."

        return message_land


start = Airplane("Sukhoi", "Su-27", "2018", 2500)

print(start.take_off())

print(start.fly(600))

print(start.fly(600))

print(start.land())