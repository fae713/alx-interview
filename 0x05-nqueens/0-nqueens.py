#!/usr/bin/python3
"""
N Queens Algorithm
"""

import sys


class NQueen:
    """
    Class for solving the N Queen Problem.
    """

    def __init__(self, n):
        """
        Initialize the problem size and solutions.
        """
        self.n = n
        self.positions = [-1] * n  # Initialize positions array
        self.solutions = []

    def is_safe(self, row, col):
        """
        Check if a queen can be placed at board[row][col].
        This function checks if there is any queen
        in the current column (col) or diagonals.
        """
        for i in range(row):
            if self.positions[i] == col or \
               abs(self.positions[i] - col) == abs(i - row):
                return False
        return True

    def solve_n_queens(self, row=0):
        """
        Use backtracking to find all solutions.
        """
        if row == self.n:
            # All queens are placed successfully
            self.solutions.append(self.positions[:])  # Copy current solution
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.positions[row] = col  # Place queen at board[row][col]
                self.solve_n_queens(row + 1)  # Recur for next row

    def print_solutions(self):
        """Print all found solutions."""
        for solution in self.solutions:
            print(solution)


def main():
    try:
        N = int(sys.argv[1])
    except IndexError:
        print("Usage: nqueens.py N")
        sys.exit(1)
    except ValueError:
        print("N must be a number.")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4.")
        sys.exit(1)

    solver = NQueen(N)
    solver.solve_n_queens()
    solver.print_solutions()


if __name__ == "__main__":
    main()
