def check_win(lst, i):
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
    elif i == 10:
        return 3

def check(b):
    a = ['0','1','2','3','X','5','6','7','8','9','Начать сначала']
    for i in range(1, len(a)):
        if a[i] == b:
            return True

