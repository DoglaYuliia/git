from random import randint


def game(sign):
    signs = ('rock', 'scissors', 'paper')
    if sign in signs:
        sign_computer = signs[randint(0, 2)]
        print(sign_computer)
        list_win = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))
        if sign == sign_computer:
            return 'ничья'
        elif (sign, sign_computer) in list_win:
            return 'You win!'
        return 'You lose'
    return 'incorrect input, please try again'


print(game(input('Enter rock, scissors or paper> ').lower()))