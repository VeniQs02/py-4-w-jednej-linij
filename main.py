def player_check(round_cr):
    if round_cr % 2 == 0:
        player_sign = 'O'
    else:
        player_sign = 'X'
    return player_sign


def board_printer(wid, hei, round_counter = 2, board_array = []):
    if round_counter == 1:
        sign = ' '
        board_array = [[sign]*hei]*wid

    for i in range(hei):
        for j in range(wid):
            print(f'|{board_array[i-1][j-1]}', end='')
        print('|')
    return board_array


def pin_positioning(move, board_ar, player_sign, height, width):
    board_ar[2][3] = 'P'
    board_printer(height, width)
    for i in range(height):
        #for j in range(move):
        if board_ar[height - i][move-1] == ' ':
            continue
        else:
            board_ar[height - i][move] = player_sign
            break





def gra(board_width, board_height):
    round_counter = 1
    win_condition = 0
    board_array = board_printer(board_width, board_height, round_counter)
    while win_condition == 0:
        while True:
            move = 5 #int(input('Podaj wartosc 1-7: '))
            if move > 1 or move < 7:
                break
        player_sign = player_check(round_counter)
        pin_positioning(move, board_array, player_sign, board_height, board_width)
        board_printer(board_width, board_height, round_counter, board_array)
        #win_check()###

        round_counter += 1

    print(f"Gracz {player_sign} wyrgywa!")

gra(7, 6)
