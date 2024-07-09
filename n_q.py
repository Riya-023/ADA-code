def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
def is_Queensafe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True
def solveNqueens(board, col):
    if col >= len(board):
        print_board(board)
        return True
    for i in range(len(board)):
        if is_Queensafe(board, i, col):
            board[i][col] = 'Q'  
            if solveNqueens(board, col + 1):  
                return True
            board[i][col] = '.'  
    return False
def nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solveNqueens(board, 0):
        print("Solution does not exist")
    return
n = 4
nqueens(n)