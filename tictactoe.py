
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}, it's your turn!")
        
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("That space is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")
        
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a draw!")

# Start the game
tic_tac_toe()
