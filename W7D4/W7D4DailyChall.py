def calculate():
    try:
        number = 5 / 0
        print('Divided')
    except ZeroDivisionError:
        print('Cant do that')


calculate()
