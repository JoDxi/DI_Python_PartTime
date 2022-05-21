# Exercise 1 - Cats
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# whiskers = Cat('Whiskers', 2)
# maple = Cat('maple', 5)
# beeny = Cat('beeny', 3)
#
#
# def find_oldest(Whiskers, Maple, Beeny):
#     return max(Whiskers, Maple, Beeny)
#
#
# print(
#     f"the oldest cat is {find_oldest(whiskers.name, maple.name, beeny.name)}, she is {find_oldest(whiskers.age, maple.age, beeny.age)} years old")
#

# Exercise 2 - Dogs
# INCOMPLETE
# class Dog:
#
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print(random_dog.name + " barks! WOOF!")
#
#     def jump(self):
#         print("{} has jumped {} CM high!".format(random_dog.name, random_dog.height * 2))
#
#
# random_dog = Dog('Pako', 70)
# random_dog.bark()
# random_dog.jump()
#
# davids_dog = Dog("Rex", 50)
# print("David's dog is named {}, he can jump {} CM high!".format(davids_dog.name, davids_dog.height))
# davids_dog.bark()
# davids_dog.jump()
#
# sarahs_dog = Dog('Teacup', 20)
# sarahs_dog.bark()


# Exercise 3 - Who's the song producer?

# class Song:
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for elem in self:
#             print(elem)
#
#     # print(lyrics)
#
#
# warPigs = Song(['Generals gathered in their masses',
#                 'Just like witches at black masses',
#                 'Evil mind that plot destruction',
#                 'Sorcerer of death construction',
#                 'In the field the bodies burning',
#                 'As the war machine keeps turning',
#                 'Death and hatred to mankind',
#                 'Poisoning their brainwashed minds'])
#
# flyingWhales = Song(['Waters of chaos have invaded all space',
#                      'The flood on earth again, I have to find the whales',
#                      'That once did guide us to the dry lands of life',
#                      'I wont despair, ill break this dark around',
#                      'Under heavy sea',
#                      'Ill search, the flight, of whales'])
#
# print_song = Song.sing_me_a_song(warPigs.lyrics)
#
# print_song = Song.sing_me_a_song(flyingWhales.lyrics)


# Exercise 4 : Afternoon At The Zoo
#INCOMPLETE
# class Zoo:
#
#     def __init__(self, zoo_name):
#         self.name = zoo_name
#
#     def add_animal(new_animal):
#         if new_animal not in animals:
#             animals.append(new_animal)
#
#     def get_animals(self):
#         print('The following animals are in the farm: ')
#         for animal in self:
#             print(animal)
#
#
#     def sell_animal(animal_sold):
#         animals.remove(animal_sold)
#         pass
#
#     def sort_animals(self):
#         print(sorted(animals))
#
# animals = []
#
# Zoo.add_animal('Pig')
# Zoo.add_animal('Chicken')
# Zoo.add_animal('Goat')
# Zoo.add_animal('Cow')
# Zoo.add_animal('Horse')
# Zoo.get_animals(animals)
# Zoo.sell_animal('Chicken')
#
#
