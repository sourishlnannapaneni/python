def game_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
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
    
def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_game():
    board = []
    for i in range(3):
        row = []
        for i in range(3):
            row.append(" ")
        board.append(row)
     #board = [[" " for i in range(3)] for j in range(3)]

    current_player = "x"
    while True:
        game_board(board)
        print(f"It is the {current_player}'s turn")
        row = int(input("Enter the row(0-2): "))
        col = int(input("Enter the column(0-2): "))
        
        #check if cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This cell is already taken, please try again.")
            continue
        #check for a winner\
        winner = check_winner(board) or check_diagonals(board)
        if winner:
            game_board(board)
            print(f"{winner} wins")
            break
        #check for draw
        if is_full(board):
            game_board()
            print("It's a draw")
            break
        #switching player
        current_player = "o" if current_player == "x" else "x"
play_game()
