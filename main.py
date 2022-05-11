def board_printer(wid, hei, round_counter):
    if round_counter == 0:
        board_array = []
        sign = ' '
        board_array = [[sign]*hei]*wid

    for i in range(hei):
        for j in range(wid):
            print(f'|{board_array[i-1][j-1]}', end='')
        print('|')


def gra(board_width, board_height, round_counter, win_condition):
    while win_condition == False:
        board_printer(board_width, board_height, round_counter)
        round_counter += 1
        ruch = int(input('Podaj wartosc 1-7: '))

gra(7, 6, 0, 0)
