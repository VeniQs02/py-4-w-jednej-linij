def board_printer(wid, hei, round_counter, board_array = []):
    if round_counter == 0:
        sign = ' '
        board_array = [[sign]*hei]*wid

    for i in range(hei):
        for j in range(wid):
            print(f'|{board_array[i-1][j-1]}', end='')
        print('|')
    return board_array

def pin_positioning(move, board_ar, round_cr):
    hig = len(board_ar)
    for i in range(hig-1):
        if board_ar[move][hig-1] == ' ':
            continue
        else:

            board_ar[move][hig] = player_sign



def gra(board_width, board_height):
    round_counter, win_condition = 0
    board_array = board_printer(board_width, board_height, round_counter)
    while win_condition == False:
        while True:
            move = int(input('Podaj wartosc 1-7: '))
            if move < 1 or move > 7:
                continue
        pin_positioning(move, board_array, round counter)
        board_printer(board_width, board_height, round_counter, board_array)

        round_counter += 1


gra(7, 6)
