board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]
i=1
turnip = 0

def kontrollori():
    if board[0]+board[1]+board[2]=='xxx':
        print ("fiton x")
        quit()
    if board[3] + board[4] + board[5]=='xxx':
        print ("fiton x")
        quit()
    if board[6]+board[7]+board[8]=='xxx':
        print ("fiton x")
        quit()
    if board[0]+board[3]+board[6]=='xxx':
        print ("fiton x")
        quit()
    if board[1]+board[4]+board[7]=='xxx':
        print ("fiton x")
        quit()
    if board[2]+board[5]+board[8]=='xxx':
        print ("fiton x")
        quit()
    if board[0]+board[4]+board[8]=='xxx':
        print ("fiton x")
        quit()
    if board[2]+board[4]+board[6]=='xxx':
        print ("fiton x")
        quit()
    if board[0]+board[1]+board[2]=='ooo':
        print ("fiton o")
        quit()
    if board[3] + board[4] + board[5]=='ooo':
        print ("fiton o")
        quit()
    if board[6]+board[7]+board[8]=='ooo':
        print ("fiton o")
        quit()
    if board[0]+board[3]+board[6]=='ooo':
        print ("fiton o")
        quit()
    if board[1]+board[4]+board[7]=='ooo':
        print ("fiton o")
        quit()
    if board[2]+board[5]+board[8]=='ooo':
        print ("fiton o")
        quit()
    if board[0]+board[4]+board[8]=='ooo':
        print ("fiton o")
        quit()
    if board[2]+board[4]+board[6]=='ooo':
        print ("fiton o")
        quit()

def turni():
    global  turnip
    if i % 2 == 0:
        turnip = 'o'
    else :
        turnip = 'x'
    print(turnip)
def display_board():
    print(board[0], "|" + board[1], "|" + board[2])
    print(board[3], "|" + board[4], "|" + board[5])
    print(board[6], "|" + board[7], "|" + board[8])
# vendosja e pikave
def player_x():
    poziconi = int(input(": "))
    poziconi = poziconi - 1
    board[poziconi] = "x"
def player_o():
    poziconi = int(input(": "))
    poziconi = poziconi - 1
    board[poziconi] = 'o'
# rregulli i turnit
def game():
    global turnip,i
    if i <= 9:
        turni()
        i = i + 1
    else :
        quit()
    if turnip == 'x' :
        player_x()
    else:
        player_o()
    display_board()

while 1 < 2:
    game()
    kontrollori()
