import datetime
import random
import string
from datetime import date

# Exercise 1
# def addOperator(num1, num2):
#     print(num1 + num2)
#     return num1 + num2

# Exercise 2
# def randomNumber():
#     user_num = int(input("Choose number between 1 - 100: "))
#     pc_num = random.randint(1, 100)
#     print(f"generated number is - ", pc_num)
#     if user_num == pc_num:
#         print("Its a match")

# Exercise 3
# def randomString():
#     letters = string.ascii_letters
#     result_str = ''.join(random.choice(letters) for i in range(6))
#     print("Random string of length 5 is - ", result_str)

# Exercise 4
# def displayCurrentDate():
#     today_date = date.today()
#     print("Today's date is: ", today_date)

# #Exercise 5
# def daysLeftJanuary():
#     today_date = date.today()
#     jan_date = datetime.date(2023, 1, 1)
#     delta = jan_date - today_date
#     print(f"There are {delta} days left until Janurary 1st, 2023")

# Exercise 6

# def minutesLived(birthdate):
#     today = date.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age


# Exercise 7
# from datetime import date
#
#
# def displayCurrentDate():
#     upcoming_holiday = "Shavuot"
#     upcoming_holiday_date = date(2022, 6, 5)
#     time_to_holiday = upcoming_holiday_date - date.today()
#     today = date.today()
#     print(f"The next holiday ({upcoming_holiday}) will be in - {time_to_holiday} days")




# Exercise 9
from faker import Faker

fake_data = Faker()
users = []


def addUsers():
    users_dict = {"name": fake_data.name(),
                  "address": fake_data.address(),
                  }

    users.append(users_dict)



