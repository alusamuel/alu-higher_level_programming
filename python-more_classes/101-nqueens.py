#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the board as a list of [row, col] coordinates."""
    print([[row, col] for row, col in enumerate(board)])

def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row):
    """Try to solve the N Queens problem using backtracking."""
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)
            board[row] = -1  # Backtrack

def main():
    """Main function to handle input and solve the problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 (indicating no queen placed)
    board = [-1] * N
    solve_nqueens(N, board, 0)

if __name__ == "__main__":
    main()
