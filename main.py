from random import randint


def game(sign):
    signs = ('камень', 'ножницы', 'бумага')
    if sign in signs:
        sign_computer = signs[randint(0, 2)]
        print(sign_computer)
        list_win = (('камень', 'ножницы'), ('ножницы', 'бумага'), ('бумага', 'камень'))
        if sign == sign_computer:
            return 'ничья'
        elif (sign, sign_computer) in list_win:
            return 'Вы победили!'
        return 'Вы проиграли'
    return 'Неверный ввод, попробуйте еще раз'


print(game(input('Enter камень, ножницы or бумага> ').lower()))