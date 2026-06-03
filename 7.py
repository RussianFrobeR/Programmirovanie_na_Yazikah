class SudokuSolver:
    SIZE = 9

    @staticmethod
    def is_valid(board, row, col, num):
        for x in range(SudokuSolver.SIZE):
            if board[row][x] == num:
                return False

        for x in range(SudokuSolver.SIZE):
            if board[x][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    @staticmethod
    def find_empty_cell(board):
        """Возвращает (row, col) первой пустой ячейки или None"""
        for row in range(SudokuSolver.SIZE):
            for col in range(SudokuSolver.SIZE):
                if board[row][col] == 0:
                    return (row, col)
        return None

    @staticmethod
    def solve(board):
        empty = SudokuSolver.find_empty_cell(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, SudokuSolver.SIZE + 1):
            if SudokuSolver.is_valid(board, row, col, num):
                board[row][col] = num
                if SudokuSolver.solve(board):
                    return True
                board[row][col] = 0  
        return False

    @staticmethod
    def print_board(board):
        for i in range(SudokuSolver.SIZE):
            sys.stdout.write("│ ")
            for j in range(SudokuSolver.SIZE):
                if board[i][j] == 0:
                    sys.stdout.write(". ")
                else:
                    sys.stdout.write(str(board[i][j]) + " ")
                if (j + 1) % 3 == 0:
                    sys.stdout.write("│ ")
            sys.stdout.write("\n")
            if (i + 1) % 3 == 0 and i < SudokuSolver.SIZE - 1:
                sys.stdout.write("─────────────────────────\n")


def main():
    board = [
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

    print("Исходное судоку:")
    SudokuSolver.print_board(board)

    print("Решаем...")
    if SudokuSolver.solve(board):
        print("Решенное судоку:")
        SudokuSolver.print_board(board)
    else:
        print("Это судоку не имеет решения!")


if __name__ == "__main__":
    import sys
    main()
