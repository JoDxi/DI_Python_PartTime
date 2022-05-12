# def calculation (num1, num2):
#     return num1 - num2, num1 + num2
#
# result = calculation(50, 100)
# print(result)

def greetings_users (users):
    for user in users:
        print('Hello ' + user.title() + ' !')

usernames = ['steve', 'stan', 'debbie']
greetings_users(usernames)