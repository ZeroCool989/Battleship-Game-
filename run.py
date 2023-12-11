import random

def create_board():
    """Create an 8x8 game board."""
    return [["O"] * 8 for _ in range(8)]




def print_board(board):
    # Print the game board
    for row in board:
        print(" ".join(row))



def place_ship(board):
 #Place a ship randomly on the board.
    ship_row = random.randint(0, 7)
    ship_col = random.randint(0, 7)
    board[ship_row][ship_col] = "*"
    return (ship_row, ship_col)

def get_user_input(prompt):
    #Get user input and handle invalid/empty input.
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 7:
                return value
            else:
                print("Please enter a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Game Functionality
play_again = "Y"
while play_again == "Y":
    print(f"\nHello {player_name}! Let's play Battleship!")
    print("You have 5 turns, to sink the Battleship!")
    print("I wish you good fortune in the upcoming battle, and now it begins!")
    board = []
    for x in range(8):
        board.append(["O"] * 8)
    print_board(board)

    ship_row, ship_col = place_ship(board)

    for turn in range(5):
        print(f"\nTurn {turn + 1}")
        guess_row = int(input("Guess Row (you can choose between 0 and 7): "))
        guess_col = int(input("Guess Col (you can choose between 0 and 7): "))

        if guess_row == ship_row and guess_col == ship_col:
            print(f"\nCongratulations {player_name}! You sank my battleship! ")
            break
        else:
            if guess_row not in range(8) or guess_col not in range(8):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            print_board(board)

        if turn == 4:
            print("\nGame Over")
            print(f"Sorry {player_name}, you lost!.")
            print(f"Battleship was at row {ship_row} and column {ship_col}.")

    # Ask the player for another or ending the game
    play_again = input("Do you want to play again? (Y/N)").upper()
    print(
        f"Thank you for playing Battleship, {player_name}, till another time!")
