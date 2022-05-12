### Excercise 2 - Birthday Look-Up
# .1
# birthdays = {
#     'mom': '1960/01/01',
#     'dad': '1960/02/02',
#     'sister': '1990/03/03',
#     'brother': '1995/04/04',
#     'dog': '2005/05/05'
# }
# print("Hello! you can look up birthdays of the people in the list!")
# name = input('Which person would you like to look up? ')
# print('There you go! our records show they were born in ' + (birthdays[name]))


#### Excercise 2 - Birthdays Advanced
# .1
# print(birthdays.keys())
# .2
# name = input('Which person would you like to look up? ')
# if name not in birthdays:
#     print("Sorry, we dont have the birth date of " + name)
# else:
#     print('There you go! our records show they were born in ' + (birthdays[name]))


#### Exercise 3: Add Your Own Birthday
# birthdays = {
#     'mom': '1960/01/01',
#     'dad': '1960/02/02',
#     'sister': '1990/03/03',
#     'brother': '1995/04/04',
#     'dog': '2005/05/05'
# }
# new_name = input('What is the name of the person to be added to our database? ')
# new_bd = input('Please tell us the DOB in a YYY/MM/DD format ')
# birthdays[new_name] = new_bd
# print(birthdays)
# name = input('Which person would you like to look up? ')
# print('There you go! our records show they were born in ' + (birthdays[name]))

### Exercise 4: Fruit Shop
# .1
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# .2
for key, value in items.items():
    print('Our ' + key + ' are delicious and cost a mere ' + str(value) + '$')
#.3
