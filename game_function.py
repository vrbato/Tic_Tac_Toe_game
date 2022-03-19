#
SEPARATOR = "=" * 50

BOARD = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]



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
    TURN = 0
    PLAYER = True  # pokud je True = x, jinak o
    while TURN < 9:
        player_sign = current_player(PLAYER)
        tic_tac_toe_board(BOARD)
        print(SEPARATOR)
        player = user_input()
        print(SEPARATOR)
        quit_game(player)
        if not check_input(player):
            print(f"{'Try again!':^50}")
            continue
        player = int(player) - 1
        position = board_position(player)
        #BOARD[0][0] = "x" test zda to funguje a hlásí to obsazené místo v hracím poli
        if is_taken(position,BOARD):
            print(f"{'Try again!':^50}")
            continue
        add_input_to_board(position,BOARD,player_sign)
        if is_win(player_sign,BOARD):
            print(f"Congratulation player: {player_sign.upper()} won!")
            break
        run_out_of_turns(TURN)

        PLAYER = not PLAYER

def tic_tac_toe_board(board):
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

def quit_game(player_input):
    if player_input.lower() == "q":
        print(f"{'Thank you for the game':^50}")
        return exit()

#určení pozice zadané hráčem
def board_position(player_input):
    row = int(player_input / 3) # všechno co bude mezi 0 - 2 mi dá pozici 0 protože int neni des. a vrátí vždy nulu, 2. řádek pozice mezi 3 - 5 vrátí 1, 3. řádek pozice mezi 6 - 8 vrátí 2
    column = player_input # od 0 - 2 to bere první vrchní hodnoty v tabulce
    if column > 2:  #pokud je to větší musí pomocí modula zjistit zbytek a ten uložit - a stanoví to ty vertikální pozice
        column = int(column % 3)
    return (row, column) #vrátí tuple

#ověření zda je pozice obsazená na hrací ploše
def is_taken(position, board):
    row = position[0] #beru z tuplu index 0 a index 1, který určuje pozici zadanou hráče řádek,sloupec
    column = position[1]
    if board[row][column] != "-": #ověřuji pokud je stále prázdno
        print(f"{'This position is taken.':^50}")
        return True
    else:
        return False

#přidání do hracího pole
def add_input_to_board(position, board, current_user):
    row = position[0]
    column = position[1]
    board[row][column] = current_user #sem přidám rovnou znak podle toho kdo zrovna hraje

def current_player(player):
    if player == True:
        return "x"
    else:
        return "o"

#určení výhry / remízy pomocí kontroly řádků
def is_win(user, board):
    if check_row(user,board):
        return True
    if check_column(user,board):
        return True
    if check_diagonal(user, board):
        return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row: #kontroluje to každé pole v řádku - nestovaná funkce
            if slot != user:
                complete_row = False #pokud tam nemá zadáno uživatel není furt hotovo a je tam False
                break
        if complete_row:
            return True
    return False

def check_column(user, board): #dá se přepsat FOR přes iterování range(3) podobně jako nahoře row
    if board[0][0] == user and  board[1][0] == user and  board[2][0] == user:
        return True
    elif board[0][1] == user and  board[1][1] == user and  board[2][1] == user:
        return True
    elif board[0][2] == user and  board[1][2] == user and  board[2][2] == user:
        return True
    else:
        return False

def check_diagonal(user,board):
    if board[0][0] == user and  board[1][1] == user and board[2][2] == user:
        return True
    elif board[2][0] == user and board[1][1] == user and board[0][2] == user:
        return True
    else:
        return False

def run_out_of_turns(turn):
    turn += 1
    if turn == 9:
        print(f"{'Tie! Thanks for the game. Bye!':^50}")
        exit()









