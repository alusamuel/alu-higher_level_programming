#!/usr/bin/python3
import sys


def print_solution(board):
    """Helper function to print the current solution."""
    print([[row, col] for row, col in enumerate(board)])

def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve_nqueens(board, row, n):
    """Backtracking function to solve the N Queens problem."""
    if row == n:
        print_solution(board)
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # Backtrack

def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize board with -1 indicating no queen placed in that row
    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
