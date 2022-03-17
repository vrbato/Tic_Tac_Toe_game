#
SEPARATOR = "=" * 50

#welcome message and rules
def welcome_rules ():
    print(f"{SEPARATOR}",
        f"{'Welcome to Tic Tac Toe'.upper():^50}",
        f"{SEPARATOR}",
        f"GAME RULES:",
        f"Each player can place one mark (or stone) \n"
        f"per turn on the 3x3 grid. The WINNER is \n"
        f"who succeeds in placing three of their \n"
        f"marks in a:\n"
        f"* horizontal,\n"
        f"* vertical or\n"
        f"* diagonal row""",
        f"{SEPARATOR}",
        "Let\'s start the game!".center(50),
        f"{SEPARATOR}",
        sep="\n"
    )

def game():
    while True:
        tic_tac_toe_board()
        print(SEPARATOR)
        player1_input()
        print(SEPARATOR)

def tic_tac_toe_board():
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    for row in board:
        for item in row:
            print(f"{item}", end="")
        print()

def player1_input() -> str:
    player1_input = input("Player 1 | Please enter your move 1 - 9 or Q for quit:")
    return player1_input