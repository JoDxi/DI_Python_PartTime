# Exercise 1#
# Write a script that inserts an item at a defined index in a list.
# list1 = ['a', 'b', 'c', 'd']
# list1.insert(0, 'e')
# print(list1)

# Exercise 2 #
# Write a script that counts the number of spaces in a string.
# example = 'This is a string'
# print(example.count(' '))
#

# Exercise 3 #
# Write a script that calculates the number of upper case letters and lower case letters in a string.
# string=input("Enter string: ")
# count1=0
# count2=0
# for i in string:
#       if i.islower():
#             count1=count1+1
#       elif i.isupper():
#             count2=count2+1
# print("The number of lowercase characters is: ", count1)
#
# print("The number of uppercase characters is: ", count2)

# Exercise 4
# Write a function to find the sum of an array without using the built in function:
# def calcSum():
#     numbers = ([1, 5, 4, 2])
#     total = 0
#     for i in numbers:
#         total= total+[i] numbers[i]
#         print(total)
#
#
# calcSum()

# Exercise 5 #
# def my_max(data):
#     maximum = 0
#     for num in data:
#         if num > maximum:
#             maximum = num
#     return maximum
#
#
# print(my_max([0, 1, 3, 50]))


# Exercise 6
# Python program to find the factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)
#

# Exercise 7

list_count = (['a', 'a', 't', 'o'], 'a')

def count_element(list_count):
    count = 0
    for elem in list_count:
        if elem == 'a':
            count += 1
            return count


print(countElement(list_count))


