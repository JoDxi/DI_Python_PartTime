# Excercise 1
# my_fav_numbers = {5, 10, 15, 20, 25, 30}
# my_fav_numbers.update([60, 50, 40])
# my_fav_numbers.discard(60)
# print(my_fav_numbers)
#
# friend_fav_numbers={80, 90, 100}
# our_favorite_numbers = my_fav_numbers | friend_fav_numbers
# print(our_favorite_numbers)
#
#
# Excercise 2
# You cannot change a tuple once set.
#
#
# Excercise 3
# num = range(1,21)
# for i in num:
#     print(i)
#
#
#
# Excercise 4
# 1) Two different data types, an integar is a complete number with no decimal points, a float has a decimal place
# 2) No.
# 3) Im not sure what does that even mean
#
#
# Excercise 5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.pop()
# basket.append('Kiwi')
# basket.insert(1, 'Apples')
# basket.index('Apples')
# basket.count('Apples')
# print(basket)
# print(basket.count('Apples'))
#
# Excercise 6
# my_name = 'Shachaf'
# user_name = str(input("What is your name?")).lower()
# print(user_name)
# while user_name != my_name:
#     user_name = input('What is your name?')
#
#
#
# Excercise 7
#
#
# Excercise 8
#
# multiples=[]
# for x in range(1500, 2501):
#     if (x%7==0) and (x%5==0):
#         multiples.append(str(x))
# print (','.join(multiples))
#
#
# Excercise 9
#
# favorite_fruits = str(input('What are your favorite fruit(s)? separate your answer using "space" '))
# list_favorite_fruits = favorite_fruits.split()
# print(list_favorite_fruits)
# random_fruit = input('Name a fruit ')
# if random_fruit in favorite_fruits:
#     print('You chose one of your favorite fruits! Enjoy!”.')
# else:
#     print('You chose a new Fruit. I hope you enjoy!')
#
#
# Excercise 10
# #
# user_toppings = ''
# list_toppings = user_toppings.split()
# base_price = 10
#
# while user_toppings != 'quit':
#     user_toppings = input('What kind of topping would you like to add? ')
#     print('Ill add that on the pizza!')
#     list_toppings.append(user_toppings)
#
# if user_toppings == 'quit':
#     list_toppings.remove('quit')
#     topping_price = 2.5 * len(list_toppings)
#     print("Youve ordered a pizza with", list_toppings, ' for a total of ', base_price + topping_price)
#
#
#
# Excercise 11'
# Most of this excercise i could not solve properly, could not find the solution, would appreciate any input.
# 1
# ticket_price = []
# person_age = int(input('How old are your family members? separate your answers with a comma '))
# # family_age = person_age.split()
# # print(family_age)
# 2
# if person_age <= 3:
#     ticket_price = 0
# elif person_age == 3 <= 12:
#     ticket_price = 10
# elif person_age >= 13:
#     ticket_price = 15
#
# print(ticket_price)
# #
# # 4
# names_list = ["Daniel", "Mikr", "Dada", "Kiraly"]
# for i in names_list :
#     age = int(input('What is your age? '))
#     if age in range(16, 22):
#         print('You can go in, just dont make a mess')
#     elif age < 16:
#         names_list.remove(i)
#         print('No bueno mi amigos')
#
# Exercise 12
# list_names = ['Daniel', 'Samuel', 'Ruth', 'David']
# for name in list_names:
#     age = int(input('What is your age? '))
#     if age < 16:
#         list_names.remove(name)
#     print(list_names)
#
#
# Excercise 13
#
# sandwich_orders = ['Mayo', 'Egg', 'Ham', 'Bologne']
# finished_sandwiches = []
#
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
#     print('i have made you a ' + sandwich + ' sandwich')
#
# Excercise 14
# sandwich_orders = ['Mayo', 'Pastrami', 'Egg', 'Pastrami', 'Ham', 'Bologne', 'Pastrami']
# finished_sandwiches = []
#
# print("Incoming order: {}".format(sandwich_orders) + ' sandwiches!')
# print('Oh no!! The Deli seems to have run out of Pastrami! ')
#
# while 'Pastrami' in sandwich_orders:
#     sandwich_orders.remove('Pastrami')
#     if sandwich_orders != 'Pastrami':
#     finished_sandwiches.append(sandwich_orders)
# print(finished_sandwiches)
