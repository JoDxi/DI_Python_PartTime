# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         print(f'{self.name} is just walking around')
#         return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         print(f"{self.name} is singing")
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         print("f{self.name} is singing")
#         return f'{sounds}'
#
#
# class Phoenix(Cat):
#     def sing(self, sounds):
#         print("f{self.name} is singing")
#         return f'{sounds}'
#
#
# Garfield = Phoenix("Garfield", 5)
# Tuluz = Bengal("Tuluz", 3)
# Grumpy = Chartreux("Grumpy Cat", 10)
# my_cats =[Garfield, Tuluz, Grumpy]
# my_pets = my_cats[1].name
# print(my_pets)
# #
# Garfield.walk()
# Tuluz.walk()
# Grumpy.walk()

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(self.name, " is barking")

    def run_speed(self):
        print(self.name, "'s running speed is", self.weight / self.age * 10, "km/h")
        return self.run_speed

    def fight(self, other_dog):
        print(self.name, " VS ", other_dog.name, "!")
        if self.run_speed > other_dog.run_speed:
            print(f"{self.name} is faster!")
        # noinspection PyUnresolvedReferences
        # dog1 = self.run_speed * self.weight
        # print(dog1)
        # dog2 = other_dog.run_speed() * other_dog.weight
        # print(dog2)        #
        # winner = self.name if dog1 > dog2 else other_dog.name
        # return f"{winner} is the winner"


Pako = Dog("Pako", 4, 27)
Merlin = Dog("Merlin", 8, 41)
Whinnie = Dog("Whinnie", 10, 14)
other_dog = Dog("Randy", 5, 30)

Pako.run_speed()
Merlin.run_speed()
Whinnie.run_speed()
other_dog.run_speed()
#
print(Pako.fight(other_dog))
