import random

def display_instruct():
    print("Welcome to Tic-Tac-Toe!")
    print("Here's the board with positions:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \n")
    print("You need to choose a position by entering the corresponding number.")

def pieces():
    human = ""
    computer = ""
    while human not in ['X', 'O']:
        human = input("Do you want to be X or O? ").upper()
    if human == 'X':
        computer = 'O'
    else:
        computer = 'X'
    return human, computer

def new_board():
    board = [' '] * 9
    return board

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def winner(board):
    for i in range(0, 3):
        if (board[i] == board[i+3] == board[i+6] != ' '):  # Check columns
            return board[i]
        if (board[i*3] == board[i*3+1] == board[i*3+2] != ' '):  # Check rows
            return board[i*3]
    if (board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' '):  # Check diagonals
        return board[4]
    if ' ' not in board:
        return 'TIE'
    return None

def human_move(board, human):
    while True:
        move = input(f"Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            return int(move) - 1
        else:
            print("Invalid move. Please try again.")

def computer_move(board, human, computer):
    legal_moves = [i for i, val in enumerate(board) if val == ' ']

    for move in legal_moves:
        board[move] = computer
        if winner(board) == computer:
            return move
        board[move] = ' ' 

    for move in legal_moves:
        board[move] = human
        if winner(board) == human:
            return move
        board[move] = ' '

    if 4 in legal_moves:
        return 4

    return random.choice(legal_moves)

def next_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'

def congratulate_winner(winner, human, computer):
    if winner == 'TIE':
        print("It's a tie!")
    elif winner == human:
        print("Congratulations! You win!")
    else:
        print("Computer wins. Better luck next time.")

def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def main():
    display_instruct()
    human, computer = pieces()
    turn = 'X'
    board = new_board()
    winner_result = None 
    
    start_first = ask_yes_no("Do you want to start first? (y/n): ")
    if start_first == 'y':
        turn = human
    else:
        turn = computer

    while True:
        if turn == human:
            move = human_move(board, human)
        else:
            move = computer_move(board, human, computer)
        
        board[move] = turn
        winner_result = winner(board) 
        display_board(board)
        
        if winner_result:
            congratulate_winner(winner_result, human, computer)
            break

        turn = next_turn(turn)
main()
