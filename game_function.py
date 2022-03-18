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
        player1 = user_input()
        print(SEPARATOR)
        if not check_input(player1):
            print(f"{'Try again!':^50}")
            continue


def tic_tac_toe_board():
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    for row in board: #nejdříve procházím řádek
        for item in row: #potom procházím položky na řádku
            print(f"{item}", end="") #aby mi to vytisklo položky vedle sebe
        print() #aby mi to vytisklo řádky pod sebe

def user_input() -> str:
    user_input = input("Player 1 | Please enter your move 1 - 9 or Q for quit:")
    return user_input

def check_input(player_input):
    #chek if the input is number
    if not isnum(player_input):
        return False
    player_input = int(player_input)

    #check if the value is in range 1 - 9
    if not correct_range(player_input):
        return False
    return True

def isnum(player_input):
    if not player_input.isnumeric():
        print(f"{'The input is not a number!':^50}")
        return False
    else:
        return True

def correct_range(player_input):
    if player_input > 9 or player_input < 1:
        print(f"{'Input out of the range!':^50}")
        return False
    else:
        return True




