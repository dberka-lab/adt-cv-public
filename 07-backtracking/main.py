import os

import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)


    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        # TODO implement loading of the file
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                nums: list[int] = [int(n) for n in line.strip().split(";")]
                loaded_rows.append(nums)

        # convert nested list to numpy array
        self.field = np.array(loaded_rows)


    def check_sequence(self, sequence: np.ndarray) -> bool:
        # or sequence[sequence != 0] - filters out zeros
        seen = set()

        for n in sequence:
            if n in seen and n != 0:
                return False

            seen.add(n)

        return True


    def check_row(self, row_index: int) -> bool:
        return self.check_sequence(self.field[row_index])


    def check_column(self, column_index: int) -> bool:
        return self.check_sequence(self.field[:, column_index])


    def check_block(self, row_index: int, column_index: int) -> bool:
        row_start_index = (row_index // 3) * 3
        column_start_index = (column_index // 3) * 3

        return self.check_sequence(self.field[row_start_index:row_start_index + 3,
                                               column_start_index:column_start_index + 3].reshape(-1))


    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        return self.check_row(row_index) and self.check_column(column_index) and self.check_block(row_index, column_index)


    def get_empty_cell(self) -> tuple[int, int] | None:
        """ Gets the coordinates of the next empty field. """
        for row in range(9):
            for col in range(9):
                if self.field[row][col] == 0:
                    return row, col

        return None


    def solve(self) -> bool:
        """ Recursively solves the sudoku. """
        empty_cell = self.get_empty_cell()

        if not empty_cell:
            return True

        row, col = empty_cell

        for val in range(1, 10):
            self.field[row, col] = val

            if self.check_one_cell(row, col) and self.solve():
                return True

        self.field[row, col] = 0

        return False


def main() -> None:
    sudoku_solver = SudokuSolver()

    sudoku_solver.load("07-backtracking/sudoku.csv")

    print("--- Default ---")
    print(sudoku_solver.field)

    sudoku_solver.solve()

    print("--- Solved ---")
    print(sudoku_solver.field)


if __name__ == "__main__":
    main()
