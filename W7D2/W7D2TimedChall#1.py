from collections import Counter

string = input('Write a sentence ')
character = input('Choose a single alphabetical character ')

count = Counter(string)
print(count[character])