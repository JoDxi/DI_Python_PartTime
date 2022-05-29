import random
tools = ['rock', 'paper', 'scissors']


class Game():
    def get_user_item(self):
        user_item = str(input('Please choose - Rock, Paper or Scissors : '))
        while user_item not in tools:
            user_item = str(input('Please choose - Rock, Paper or Scissors : '))
        else:
            print('User selected: ', user_item)
            return user_item

    def get_computer_item(self):
        computer_item = random.choice(tools)
        print('Computer selected: ', computer_item)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            print('Its a draw!')
        elif user_item == 'rock':
            if computer_item == 'scissors':
                print('Rock smashes scissors! USER WINS!')
            else:
                print('Paper covers rock! COMPUTER WINS!')
        elif user_item == 'paper':
            if computer_item == 'rock':
                print('Paper covers rock! USER WINS!')
            else:
                print('Scissors cuts paper! COMPUTER WINS!')

        elif user_item == 'scissors':
            if computer_item == 'paper':
                print('Scissors cuts paper! USER WINS!')
            else:
                print('Rock smashes scissors, COMPUTER WINS!')

    def play(self):
        user_input = game.get_user_item()
        computer_input = game.get_computer_item()
        game.get_game_result(user_input, computer_input)
        pass

game = Game()
game.play()

