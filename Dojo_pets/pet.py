
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound


class Pet:
    def __init__(self, name, type, tricks, pet_sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.pet_sound = pet_sound

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.pet_sound)
        return self

    def list_attributes(self):
        print(f"{self.type}\n"
              f"{self.tricks}\n"
              f"{self.health}\n"
              f"{self.energy}\n"
              f"{self.pet_sound}")
        return self
