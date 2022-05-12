# Excercise 1 - Temperature Advice
import random


def get_random_temp(season):
    random_temp = random.randint(-10, 40)
    if season == 'winter':
        random_temp = random.randint(-10, 16)
        floated = float(random_temp)
        return floated
    elif season == 'fall':
        random_temp = random.randint(17, 23)
        floated = float(random_temp)
        return floated
    elif season == 'summer':
        random_temp = random.randint(24, 40)
        floated = float(random_temp)
        return floated


def main():
    season = input('Choose a season ')
    temp_out = get_random_temp(season)
    print('The current temperature is ', temp_out, ' Celsius')
    if temp_out < 0:
        print('Its freezing outside!')
    elif 0 <= temp_out <= 16:
        print('A bit chilly')
    elif 16 < temp_out <= 23:
        print('Its getting warmer!')
    elif 24 <= temp_out <= 32:
        print('Nice and sunny!')
    elif 33 <= temp_out <= 40:
        print('Its blazing hot outside!')


main()
