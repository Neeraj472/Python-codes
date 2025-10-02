
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
def player_moves(board,player):
    while True:
        move =int(input(f"player {player} enter your move b/t(1-9) :")) -1
        if move>=0 and move<9 and board[move]==" ":
            board[move] =player
            break
        else:
            print("invalid move!, try again")
    
def check_win(board,player):
    win_condition =[[0,1,2],[3,4,5],[6,7,8], #row
                    [0,3,6],[1,4,7],[2,5,8], #col
                    [0,4,8],[2,4,6]  #diagonal
                    ]
    for i in win_condition:
        if board[i[0]] ==board[i[1]]==board[i[2]]==player:
            return True
    return False

def play_game():
    board =[" " for _ in range(9)]
    current_player ="X"
    for turn in range(9):
        print_board(board)
        player_moves(board,current_player)
        if check_win(board,current_player):
            print_board(board)
            print(f"player {current_player} wins")
            return
        current_player ="O" if current_player=="X" else "X"
    print_board(board)
    print("draw")
    
play_game()
