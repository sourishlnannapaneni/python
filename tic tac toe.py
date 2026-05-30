def game_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 10)
#print(game_board(board))

def check_winner(board, row = 0, col = 0):
    if row == 3:
        return None
    #check current row
    if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
        return board[row][0]
    
    #check current column
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
        return board[0][col]
    
    #recursively checking the next row and column
    return check_winner(board, row+1, col+1)

#check diagonals
def check_diagonals(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
