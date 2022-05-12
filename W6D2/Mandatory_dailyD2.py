string_user = str(input('Tell us something, at least 10 characters long'))
string_length = len(string_user)

if string_length < 10:
    print(('Dont be shy, tell us some more'))

else:
    print('You talk much')

last_char = string_user[-1]
first_char = string_user[0]
print(first_char, last_char)

for i in string_user:
    print(i)

    import random
    l = list(string_user)
    random.shuffle(l)
    print(l)




