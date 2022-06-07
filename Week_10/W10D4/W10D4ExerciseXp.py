# Exercise 1 - random sentence generator
import random
import string

file_sow = 'sowpods.txt'


def get_words_from_file():
    with open(file_sow) as sow:
        lines = sow.readlines()
        print(lines)


def get_random_sentence(length):
    with open(file_sow, 'r'):
        alltext = file_sow.read()
        words = list(map(str, alltext.split()))
        print(''.join(random.choice(words) for i in range(10)))


# get_words_from_file()

get_random_sentence(5)
