import random
import json


def create_board():
    """Create an 8x8 game board."""
    return [["O"] * 8 for _ in range(8)]


def print_board(board):
    """Print the game board."""
    for row in board:
        print(" ".join(row))


def place_ship(board):
    """Place a ship randomly on the board."""
    ship_row = random.randint(0, 7)
    ship_col = random.randint(0, 7)
    # Use '*' for ship, hidden from player
    board[ship_row][ship_col] = "*"
    return ship_row, ship_col


def get_user_input(prompt):
    """Get user input and handle invalid/empty input."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 7:
                return value
            else:
                print("Please enter a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def save_score(name, score):
    """Save the player's score to a JSON file."""
    try:
        with open('leaderboard.json', 'r+') as file:
            leaderboard = json.load(file)
            leaderboard.append({'name': name, 'score': score})
            leaderboard.sort(key=lambda x: x['score'], reverse=True)
            file.seek(0)
            json.dump(leaderboard, file, indent=4)
    except FileNotFoundError:
        with open('leaderboard.json', 'w') as file:
            json.dump([{'name': name, 'score': score}], file, indent=4)


def display_leaderboard():
    """Display the top 5 scores from the leaderboard."""
    try:
        with open('leaderboard.json', 'r') as file:
            leaderboard = json.load(file)
            print("\nTop Scores:")
            for entry in leaderboard[:5]:
                print(f"{entry['name']} - {entry['score']}")
    except FileNotFoundError:
        print("No scores recorded yet.")


def main():
    """Main function for the game."""
    player_name = input("What is your name, player? ")
    print(f"\nHello {player_name}! Let's play Battleship!")
    print("You have 5 turns to sink the Battleship!")

    board = create_board()
    ship_row, ship_col = place_ship(board)
    print_board([["O"] * 8 for _ in range(8)])
    # Hide ship location from player

    score = 0
    for turn in range(5):
        print(f"\nTurn {turn + 1} of 5")
        guess_row = get_user_input("Guess Row (0 to 7): ")
        guess_col = get_user_input("Guess Col (0 to 7): ")

        if guess_row == ship_row and guess_col == ship_col:
            print(f"\nCongratulations {player_name}! You sank my battleship!")
            score = 5 - turn  # Higher score for fewer turns
            break
        else:
            if board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            print_board(board)

        if turn == 4:
            print("\nGame Over")
            print(f"Sorry {player_name}, you didn't find the battleship.")
            print(f"The Battleship was at row {ship_row}, column {ship_col}.")

    save_score(player_name, score)
    display_leaderboard()

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == "Y":
        main()
    else:
        print(f"Thank you for playing Battleship, {player_name}. Goodbye!")


if __name__ == "__main__":
    main()