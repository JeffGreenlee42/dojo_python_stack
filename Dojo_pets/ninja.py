from pet import Pet

#class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_namme = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()


marley = Pet("Marley", "Cat", "Plays Piano", "Meow")
bob = Ninja("Robert", "Godhead", ["jerky", "cheeseBalls", "TunaMorsel"], "squirrel", marley)

bob.pet.list_attributes()
bob.walk()
bob.pet.list_attributes()
bob.feed()
bob.pet.list_attributes()
bob.bathe()
bob.pet.list_attributes()

