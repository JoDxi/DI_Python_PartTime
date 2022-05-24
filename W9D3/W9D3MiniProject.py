class Character:

    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, life):
        if life <= 0:
            self.__life = 0
            print(f"{self.name} DIED")
        else:
            self.__life = life

    def basic_attack(self):
        self.attack -= other_char.life
        print(f"{self.name} attacked {other_char.name}")
        print(f"{other_char.name} life has decreased by {self.attack}")


class Druid(Character):
    print("I am a Druid, master of the forest")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name}'s HP has increased by 10 but AP decreased by -2!")

    def animal_help(self):
        print(f"{self.name}'s attack power has been increased by 5!")
        self.attack += 5

    def fight(self, other_char):
        print(f"{self.name} attacks {other_char.name}!")
        print(f"{other_char.name}'s HP has been decreased by", (0.75 * self.life + 0.75 * self.attack), "!")
        other_char.life -= (0.75 * self.life + 0.75 * self.attack)


class Warrior(Character):
    print("I am a Warrior, master of the arena!")

    def brawl(self, other_char):
        print(f"{self.name} brawls with {other_char.name}!")
        print(f"{other_char.name}'s HP has been decreased by", (2 * self.attack))
        other_char.life -= (2 * self.attack)

    def train(self):
        print(f"{self.name} roars!")
        print(f"{self.name}'s AP & HP has been increased by two!")
        self.attack += 2
        self.life += 2

    def roar(self, other_char):
        other_char.attack -= 3
        print(f"{other_char.name}'s attack power has been decreased by 3!")


class Mage(Character):
    print("I am a Mage, master of the dark arts")

    def curse(self, other_char):
        print(f"{self.name} curses {other_char.name}!")
        other_char.attack -= 2
        print(f"{other_char.name}'s attack power has been decreased by 2!")

    def summon(self):
        print(f"{self.name} summons the power of the dark arts!")
        print(f"{self.name}'s AP has increaed by 3!")
        self.attack += 3

    def cast_spell(self, other_char):
        print(f"{self.name} has cast a spell!")
        print(f"{other_char.name}'s life was decreased by", (self.attack / self.life))
        other_char.life -= (self.attack / self.life)


Blancko = Druid('Blancko')
Khamzer = Warrior('Khamzer')
Gandalf = Mage('Gandalf')
other_char = Warrior('Training Dummy')

Blancko.fight(other_char)
Khamzer.roar(Blancko)
Khamzer.basic_attack()
Blancko.animal_help()

