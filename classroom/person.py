class Person:
    def __init__(self, fullName, place, age=18):
        self.fullName = fullName
        self.age = age
        self.place = place  # (address)

    def __str__(self):
        return f"{self.fullName}, {self.age}, {self.place}"

    def talk(self):
        return f"Такой-то  {self.fullName} говорит"

    def move(self, adres):
        self.place = adres


a = Person('bolot', 'bishkek', 22)
print(a)
print(a.talk())
a.move('osh')
print(a)