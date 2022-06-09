import enchant
import itertools
import re


class AnagramChecker:
    def __init__(self):
        self.word = None
        with open('sowpods.txt', 'r') as sow:
            sow.read() # you are not doing anything with this

    def is_valid_word(self):
        pattern = "[0-9 ]"
        valid_word = enchant.Dict("en_US")
        self.word = input("Type a word: ").strip()
        print(self.word)
        if re.search(pattern, self.word):
            print("One word - No numbers!")
            return False
        if valid_word.check(self.word):
            print("This is a valid English word")
            return True
        else:
            print("Sorry, this is NOT a valid English word")
            return False

    def get_anagrams(self):
        print(f"You have chosen {self.word}.")
        print(f"The anagrams for {self.word} are: ", ["".join(perm) for perm in itertools.permutations(self.word)])

    @staticmethod
    def is_anagram(word1, word2):
        if sorted(word1) == sorted(word2):
            print('This is an Anagram')
            return True
        else:
            print('This is not an Anagram')
            return False
