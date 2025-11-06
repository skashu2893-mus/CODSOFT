import random

board = [' ' for _ in range(16)]

def print_board():
    print()
    for i in range(0, 16, 4):
        print(" | ".join(board[i:i+4]))
        if i < 12:
            print("--+---+---+--")
    print()

def check_winner(player):
    # Horizontal and vertical checks
    for i in range(4):
        if all(board[i*4 + j] == player for j in range(4)):  # row
            return True
        if all(board[j*4 + i] == player for j in range(4)):  # column
            return True
    # Diagonals
    if all(board[i*5] == player for i in range(4)):  # main diagonal
        return True
    if all(board[i*3 + 3] == player for i in range(1,5)):  # opposite diagonal
        return True
    return False

def player_move():
    while True:
        move = input("Enter your move (1-16): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 16:
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("That spot is already taken.")
            else:
                print("Choose a number between 1 and 16.")
        else:
            print("Please enter a valid number.")

def computer_move():
    for i in range(16):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '
    for i in range(16):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '
    move = random.choice([i for i in range(16) if board[i] == ' '])
    board[move] = 'O'

def is_full():
    return ' ' not in board

def play_game():
    print("TIC TAC TOE 4x4")
    print("You are X and computer is O")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner('X'):
            print("You win! 🎉")
            break
        if is_full():
            print("It's a draw! 🤝")
            break

        computer_move()
        print_board()
        if check_winner('O'):
            print("Computer wins! 😔")
            break
        if is_full():
            print("It's a draw! 🤝")
            break

def main():
    while True:
        global board
        board = [' ' for _ in range(16)]  # reset board
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! 👋")
            break

main()
