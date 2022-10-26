import random

    
'''
Warm Up
'''

def print_board(board):
    for i in range(0,3):
        print(board[i], end='')
    print('\n')
    for i in range(3,6):
        print(board[i],end='')
    print('\n')
    for i in range(3,6):
        print(board[i],end='')
    print('\n ----')
    
    
    
def open_slots(board):
    open_slots=[]
    for i in range(0,9):
        q = board[i]
        if q != 'X' and q != '0':
            open_slots.append(i)
    print(open_slots)
    return open_slots


def random_move(board, symbol):
    x = open_slots(board)
    if len(x) != 0:
        move = random.choice(x)
        board[move] = symbol 
        print_board(board)
    
def check_three(board, i1, i2,i3):
    if board[i1] == 'X' and board[i2]== 'X' and board[i3] == 'X':
        return 'X'
    elif board[i1] == 'O' and board[i2]== 'O' and board[i3] == 'O':
        return 'O'
    return '-'

def win_determination(board):
    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
    for x in range(0,8): 
        i1 = combos[x][0]
        i2 = combos[x][1]
        i3 = combos[x][2]
        win = check_three(board, i1,i2,i3)
        if win == 'O' or win == 'x':
            return win

    

def game():
    board = ['','','','','','','','','']
    win = '-'
    while win != 'X' and win != 'O':
        symbol = 'X'
        random_move(board, symbol)
        win = win_determination(board)
        if win == 'X':
            return win
        symbol = 'O'
        random_move(board, symbol)
        win = win_determination(board)

    return win


        

