ttt_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player = {'Player': 'X', 'Computer': 'O'}

def print_board(board):
    print("Current Tic Tac Toe Board:")
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def getUserInput(board):
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid input. Please enter numbers between 0 and 2.")
        return getUserInput()
    if board[row][col] != ' ':
        print("Cell already taken. Try again.")
        return getUserInput(board)
    return row, col

def getComputerInput(board):
    import random
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_move(board, row, col, player):
    board[row][col] = player
    if check_winner(board):
        print_board(board)
        print(player," win!")
        return True
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        return True
    return False

flag = False
while not flag:
    row, col = getUserInput(ttt_board)
    flag = play_move(ttt_board, row, col, player['Player'])
    
    row, col = getComputerInput(ttt_board)
    flag = play_move(ttt_board, row, col, player['Computer'])
        
    print_board(ttt_board)