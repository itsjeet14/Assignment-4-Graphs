"""**Implement n-Queen's Problem"""

def is_valid(board, row, col, n):
    # Check if there is any queen already placed in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is any queen already placed in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is any queen already placed in the lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        # All queens have been placed, so print the solution
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
        print()
    else:
        # Try placing the queen in each column of the current row
        for col in range(n):
            if is_valid(board, row, col, n):
                board[row][col] = 1
                solve_n_queens(board, row+1, n)
                board[row][col] = 0

if __name__ == '__main__':
    n = int(input('Enter the number of queens: '))

    # Initialize the board with all zeros
    board = [[0 for j in range(n)] for i in range(n)]

    solve_n_queens(board, 0, n)

