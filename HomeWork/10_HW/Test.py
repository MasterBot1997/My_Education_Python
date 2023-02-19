# Сначала создадим игру

def game_pole():
    print('Привет игроки, это наше поле для игра!\n')
    print('| 1 | 2 | 3 |\n'
          '------------- \n'
          '| 4 | 5 | 6 |\n'
          '------------- \n'
          '| 7 | 8 | 9 |\n')

def game_progress(num, s):
    a = ['','','','','','','','','','']
    print(f'| {a[1]} | {a[2]} | {a[3]} |\n'
          '------------- \n'
          f'| {a[4]} | {a[5]} | {a[6]} |\n'
            '------------- \n'
         f'| {a[7]} | {a[8]} | {a[9]} |\n')

def run_people():
    a = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in range(1, 10):
        if i % 2 != 0:
            print('Ходит игрок номер 1')
            gamer_1 = int(input('Введите номер поля куда вы хотите сходить: '))
            if a[gamer_1] == ' ':
                a.pop(gamer_1)
                a.insert(gamer_1, 'X')
                print(f'| {a[1]} | {a[2]} | {a[3]} |\n'
                        '------------- \n'
                        f'| {a[4]} | {a[5]} | {a[6]} |\n'
                            '------------- \n'
                        f'| {a[7]} | {a[8]} | {a[9]} |\n')
        else:
            print('Ходит игрок номер 2')
            gamer_2 = int(input('Введите номер поля куда вы хотите сходить: '))
            if a[gamer_2] == ' ':
                a.pop(gamer_2)
                a.insert(gamer_2, 'O')
                print(f'| {a[1]} | {a[2]} | {a[3]} |\n'
                        '------------- \n'
                        f'| {a[4]} | {a[5]} | {a[6]} |\n'
                            '------------- \n'
                        f'| {a[7]} | {a[8]} | {a[9]} |\n')
        if i >= 5:
            temp = check_win(a)
            if temp == 1:
                print('Win pleyer 1')
                break
            elif temp == 2:
                print('Win pleyer 2')
                break
            else:
                print('Ничья')
           


def check_win(lst):
    if lst[1] == lst[2] == lst[3] == 'X' or lst[4] == lst[5] == lst[6] == 'X' or lst[7] == lst[8] == lst[9] == 'X':
        return 1
    elif lst[1] == lst[4] == lst[7] == 'X' or lst[2] == lst[5] == lst[8] == 'X' or lst[3] == lst[6] == lst[9] == 'X':
        return 1
    elif lst[1] == lst[5] == lst[9] == 'X' or lst[3] == lst[5] == lst[7] == 'X':
        return 1
    elif lst[1] == lst[2] == lst[3] == 'O' or lst[4] == lst[5] == lst[6] == 'O' or lst[7] == lst[8] == lst[9] == 'O':
        return 2
    elif lst[1] == lst[4] == lst[7] == 'O' or lst[2] == lst[5] == lst[8] == 'O' or lst[3] == lst[6] == lst[9] == 'O':
        return 2
    elif lst[1] == lst[5] == lst[9] == 'O' or lst[3] == lst[5] == lst[7] == 'O':
        return 2

game_pole()
run_people()

