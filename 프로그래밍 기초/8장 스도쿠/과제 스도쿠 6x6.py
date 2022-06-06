import random


def initialize_board_6x6():
    row0 = [1, 2, 3, 4, 5, 6]
    random.shuffle(row0)
    row1 = row0[4:6] + row0[0:2] + row0[2:4]
    row2 = row0[2:4] + row0[4:6] + row0[0:2]
    row3 = [row0[1], row0[0], row0[3], row0[2], row0[5], row0[4]]
    row4 = row3[4:6] + row3[0:2] + row3[2:4]
    row5 = row3[2:4] + row3[4:6] + row3[0:2]

    return [row0, row1, row2, row3, row4, row5]


# print(initialize_board_6x6())


def shuffle_ribbons(board):
    top = board[:3]
    bottom = board[3:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom


def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            transposed[j].append(board[i][j])
    return transposed


def transpose(board):
    size = len(board)
    transposed = [[] for _ in range(size)]
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed


def crate_solution_board_6x6():
    board = initialize_board_6x6()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board


def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone


def get_level():
    print('Enter your level.')
    level = input('Beginner = 1, Intermediate = 2, Advanced = 3: ')
    while level not in ('1', '2', '3'):
        level = input('Beginner = 1, Intermediate = 2, Advanced = 3: ')
    if level == '1':
        return 6
    elif level == '2':
        return 8
    else:
        return 10


def make_holes(board, number_of_holes):
    size = len(board)
    while number_of_holes > 0:
        i = random.randint(0, size-1)
        j = random.randint(0, size-1)
        if board[i][j] != 0:
            board[i][j] = 0
            number_of_holes -= 1
    return board


def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()


def get_integer(message, i, j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)


def sudoku_mini():
    solution_board = crate_solution_board_6x6()
    puzzle_board = copy_board(solution_board)
    number_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, number_of_holes)
    show_board(puzzle_board)
    while number_of_holes > 0:
        i = get_integer('Row#(1, 2, 3, 4, 5, 6): ', 1, 6)-1
        j = get_integer('Column#(1, 2, 3, 4, 5, 6): ', 1, 6)-1
        if puzzle_board[i][j] != 0:
            print('Not empty!')
            continue
        n = get_integer('Number(1,2,3,4,5,6):', 1, 6)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            number_of_holes -= 1
        else:
            print(n, ': Wrong number! Try again.')
    print('Well done! Come again.')


sudoku_mini()
