### Excercise 1 - Convert Lists Into Dictionaries ###
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# result = zip(keys, values)
# print(dict(result))
#
# print(type(result))


### Excercise 2 - Cinemax #2 ###
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# family_ages = family.values()
# total_price = []
# for i in family_ages:
#     ind_age = i
#     print(ind_age)
#     if ind_age < 3:
#         print('Infants are not required to pay')
#     elif ind_age in range(3, 13):
#         total_price.append(10)
#         print('Your ticket will be 10$')
#     else:
#         total_price.append(15)
#         print('Your ticket will be 15$')
# # combinred price and be defined as variable and called with the format function, or just use the sum function straight into the format function.
# # combined_price = sum(total_price)
# print('Your family will h`ave to pay a total of {0}$ '.format(sum(total_price)))
#


### Excercise 3 - Zara ###
# .2
# brand = {'name': 'zara',
#          'creation_date': 1975,
#          'creator_name': 'Amancio Ortega Gaona',
#          'type_of_clothes': ['men', 'women', 'children', 'home'],
#          'international_competitors': ['Gap', 'H & M', 'Benetton'],
#          'number_stores': 7000,
#          'major_color': {
#              'France': 'blue',
#              'Spain': 'red',
#              'US': ['pink', 'green'],
#          }
#          }
# # .3
# brand.update({'number_stores': 2})
# # .4- im assuming they mean explain who their competitors are, because it does not say anything about clients
#
# print(brand)
# # .5
# brand.update({'country_creation': 'Spain'})
#
# # .6
#
# if 'international_competitors' in brand:
#     brand.update({'international_competitors': ['Gap', 'H & M', 'Benetton', 'Desigual']})
#
# # .7
# brand.pop('creation_date')
#
# # .8
# print(brand['international_competitors'][-1])
#
# # .9
# print(brand.get('major_color', {}).get('US'))
# # .10
# print(len(brand))
# # .11
# print(brand.keys())
# # .12
# more_on_zara ={
#     'creation_date': 1975,
#     'number_stores': 10000,
# }
# .13
# brand.update(more_on_zara)
# print(brand)

# .14
# Provides an invalid syntax because there cannot be a space between two numbers, it treats them as two seperate integars
#

### Exercise 4 - Disney Characters ###
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# .1
# my_dict = dict()
# for key, index in enumerate(users):
#     my_dict[index] = key
# print(my_dict)
# .2
# my_dict = dict()
# for key, index in enumerate(users, 1):
#     my_dict[index] = key
# print(my_dict)
# .3
# sorted = sorted(my_dict)
# print(sorted)
# .4
# Coudlnt solve this one
# my_dict = dict()
# for i in (users):
#     if i.find('i'):
#         print("Huh")
