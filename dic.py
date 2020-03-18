#Create the board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]

#Create some variables that wil help us for tun exchange
i=1
turnip = 0
#Create a function that will check for winner or draw
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
     else :
         print ("Draw")
#Create a turn for each player
def turni():
    global  turnip
    if i % 2 == 0:
        turnip = 'o'
    else :
        turnip = 'x'
    print(turnip)
#Create a diplayed board
def display_board():
    print(board[0], "|" + board[1], "|" + board[2])
    print(board[3], "|" + board[4], "|" + board[5])
    print(board[6], "|" + board[7], "|" + board[8])
# Where players wants to move/play
#We have two player (Player X) and (Player O)
def player_x():
    poziconi = int(input(": "))
    poziconi = poziconi - 1
    board[poziconi] = "x"
def player_o():
    poziconi = int(input(": "))
    poziconi = poziconi - 1
    board[poziconi] = 'o'
#Tur exchange
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
#Create an infinite loop that keeps our game going on
while 1 < 2:
    game()
    kontrollori()
