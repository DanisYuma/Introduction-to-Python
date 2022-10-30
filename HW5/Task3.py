# Создайте программу для игры в "Крестики-нолики".

board = list(range(1,10))

def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3],'|')
        # print('-', * 13)

def take_input(x_or_o):
    valid = False
    while not valid:
        player_input = input('Where to put'  + x_or_o+'> ')
        try:
            player_input = int(player_input)
        except:
            print('Its not a number')
            continue
        if player_input >= 1 or player_input <= 9:
            if str(board[player_input-1]) not in 'XO':
                board[player_input-1] = x_or_o
                valid = True
            else:
                print('this cell is occupied')
        else:
            print('Invalid enter. Must be number from 1 to 9')

def check_win(board):
    win_comb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_comb:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'win')
                win = True
                break
        if counter == 9:
            print('Draw')
            break
    draw_board(board)

main(board)    