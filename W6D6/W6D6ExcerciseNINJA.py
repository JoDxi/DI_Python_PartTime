# Excercise 2 Authentication CLI - Login
# .1
# database = {
#     'david': 'password1',
#     'john': 'password2',
#     'beth': 'password3',
# }
# log_ext = str(input('Would you like to login or Exit? '))
# logged_user_name = []
# logged_user_password =[]
# if log_ext == 'login':
#     login_user = str(input('What is your username? '))
#     for user in database:
#         if login_user in database.keys():
#             logged_user_name.append(login_user)
#             login_pass = str(input('What is your password? '))
#             if login_pass in database.values():
#                 logged_user_password.append(login_pass)
#                 print('Hellluja, you have logged in!')
#                 break
#             else:
#                 print("You could not be verified, good bye")
#                 break
#
# elif log_ext == 'exit':
#     print('Goodbye!')
#
# stored_login_data = dict(zip(logged_user_name, logged_user_password))
# print(stored_login_data)
# print(type(stored_login_data))

# Excercise 3 - Authentication CLI - Signup

database = {
    'david': 'password1',
    'john': 'password2',
    'beth': 'password3',
}
logged_user_name = []
logged_user_password = []
login_new_user = []
login_new_password = []


log_ext = str(input('Would you like to login or Exit? '))
login_user = str(input('What is your username? '))
if log_ext == 'login':
    for user in database:
        if login_user in database.keys():
            logged_user_name.append(login_user)
            login_pass = str(input('What is your password? '))
            if login_pass in database.values():
                logged_user_password.append(login_pass)
                print('Hellluja, you have logged in!')
                break
            else:
                print("You could not be verified, good bye")
                break
if login_user not in database.keys():
    register_ques = input('It appears you dont have an account with us, would you like to register? - yes/no: ')
    if register_ques == 'yes':
        reg_pic_user = str(input('Please choose your username: '))
        login_new_user.append(reg_pic_user)
        reg_pic_pass = str(input('Please choose your password: '))
        login_new_password.append(reg_pic_pass)
        # print(new_user)
    elif register_ques == 'no':
        print('Sorry, you must be registered to sign in. Goodbye!')
elif log_ext == 'exit':
    print('Goodbye!')

stored_login_data = dict(zip(logged_user_name, logged_user_password))
stored_new_user = dict(zip(login_new_user, login_new_password))
database.update(stored_new_user)
print(database)

