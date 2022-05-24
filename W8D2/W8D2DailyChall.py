class Farm:
    def __init__(self, name):
        self.name_of_farm = name
        self.stock = {}

    def add_animal(self, animal, amount=1):
        self.stock[animal] = amount

    def get_info(self):
        print(self.name_of_farm)
        for animal, amount in self.stock.items():
            if amount > 1:
                print("The farm has", amount, animal, "s")
            else:
                print("The farm has", amount, animal)
        print('E-I-E-I-0!')

    def get_animal_types(self):
        sorted_animals = []
        for animal in self.stock:
            sorted_animals.append(animal)
        ab_list = sorted(sorted_animals)
        print(ab_list)

    # def get_short_info(self):
    #     the_animals = self.get_animal_types()
    #     print(self.name_of_farm, " has", the_animals, " on the farm!")


macdonald = Farm("McDonald's Farm")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
# macdonald.get_short_info()