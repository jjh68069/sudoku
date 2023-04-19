import time


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    row_start, col_start = 3 * (row // 3), 3 * (col // 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def print_sudoku(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    sudoku_hard = [
        [0, 0, 0, 2, 0, 0, 8, 0, 0],
        [1, 0, 0, 9, 0, 0, 3, 0, 0],
        [8, 3, 0, 0, 7, 0, 6, 0, 0],
        [4, 0, 0, 0, 0, 6, 1, 0, 0],
        [3, 0, 0, 7, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 2, 0, 0, 1, 0],
        [7, 0, 0, 4, 0, 0, 0, 5, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]
    ]
    print("===================================")
    start = time.time()
    if solve_sudoku(sudoku_hard):
        print_sudoku(sudoku_hard)
    else:
        print("No solution exists.")
    end = time.time()
    print("===================================")
    print(f'It took {end - start:.3f} seconds to complete this solution using the backtracking algorithm')
    print("===================================")
