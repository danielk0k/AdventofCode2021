def reduce(function, init, iterable):
    it = iter(iterable)
    if init is None:
        value = next(it)
    else:
        value = init
    for element in it:
        value = function(element, value)
    return value


def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)


def get_bingo_boards(lst):
    all_bingo_board = []
    temp = []

    for elt in lst:
        if len(temp) == 5:
            all_bingo_board.append(temp)
            temp = []
        elif not(elt == "\n"):
            temp.append(elt.split())

    all_bingo_board.append(temp)
    return all_bingo_board


def get_bingo_num(lst):
    return lst[0][:-1].split(",")


def check_bingo_board(board):
    # check rows
    row_result = reduce(lambda x, y: reduce(lambda xx, yy: xx == "X" and yy, True, x) or y, False, board)

    # check columns
    col_result = False
    for col in range(5):
        col_result = col_result or reduce(lambda x, y: x[col] == "X" and y, True, board)

    return row_result or col_result


def update_bingo_board(num, board):
    for elt in board:
        if num in elt:
            elt[elt.index(num)] = "X"
            break


def winning_sum(winning_bingo_num, board):
    sum_unmarked = reduce(lambda xx, yy: reduce(lambda x, y: int(x) + int(y) if not(x == "X") else y, 0, xx) + yy, 0, board)
    return sum_unmarked * int(winning_bingo_num)


def main():
    input_result = txt_to_list()
    bingo_num = get_bingo_num(input_result)
    bingo_board = get_bingo_boards(input_result[1:])

    for num in bingo_num:
        for board in bingo_board:
            update_bingo_board(num, board)
            if check_bingo_board(board):
                return winning_sum(num, board)


print("Final score of first winning board:", main())


def main2():
    input_result = txt_to_list()
    bingo_num = get_bingo_num(input_result)
    bingo_board = get_bingo_boards(input_result[1:])
    track_completion = []

    for num in bingo_num:
        for board in bingo_board:
            if not(bingo_board.index(board) in track_completion):
                update_bingo_board(num, board)

                if check_bingo_board(board):
                    track_completion.append(bingo_board.index(board))
                    if len(track_completion) == len(bingo_board):
                        last_winning_board_index = track_completion[-1]
                        return winning_sum(num, bingo_board[last_winning_board_index])


print("Final score of last winning board:", main2())

