from random import randrange
def DisplayBoard(board):
    print("+------"*3,"+",sep="")
    for row in range(3):
        print("|      "*3,"|",sep="")
        for col in range(3):
            print("|   "+str(board[row][col])+" ",end=" ")
        print("|")
        print("|      "*3,"|",sep="")    
        print("+------"*3,"+",sep="")
    

def EnterMove(board):
   # the function accepts the board current status, asks the user about their move, 
   # checks the input and updates the board according to the user's decision
   Ready_for_Move=False
   while not Ready_for_Move:
        move=input("Please input your move:")
        Ready_for_Move=len(move)==1 and move>="1" and move<="9"
        if not Ready_for_Move:
           print("please put Correct move---repet your move")
           continue
        move=int(move)-1
        row=move//3
        col=move%3
        sign=board[row][col]
        Ready_for_Move=sign not in ["0","X"]
        if not Ready_for_Move:
            print("Already filled")
            continue
        board[row][col]="0"

def MakeListOfFreeFields(board):
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["0","X"]:
                free.append((row,col))
    return free 
def VictoryFor(board, sign):
    # the function analyzes the board status in order to check if 
    #the player using 'O's or 'X's has won the game
    if sign=="X":
        who="Computer"
    elif sign=="0":
        who="Human"
    else:
        who=None
    cross1=cross2=True
    for R_C in range(3):
        if board[R_C][0]==sign and board[R_C][1]==sign  and board[R_C][2]==sign :
            return who
        if board[0][R_C]==sign and board[1][R_C]==sign  and board[2][R_C]==sign :
            return who
        if board[R_C][R_C]!=sign :
            cross1=False
        if board[2-R_C][R_C]!=sign :
            cross2=False
    if cross1 or cross2:
        return who
    return None 
    

def DrawMove(board):
    # the function draws the computer's move and updates the board
    free=MakeListOfFreeFields(board)
    start_move=len(free)
    if(start_move>0):
        random_move=randrange(start_move)
        row,col=free[random_move]
        board[row][col]="X"
    
#Main Part of game
board=[[(3*j)+i+1 for i in range(3)]for j in range(3)]
board[1][1]="X"
free=MakeListOfFreeFields(board)
human_trun=True
while len(free):
    DisplayBoard(board)
    if human_trun:
        EnterMove(board)
        victory=VictoryFor(board, "0")
        #human_trun=False

    else:
        DrawMove(board)
        victory=VictoryFor(board, "X")
        #human_trun=True
    if victory !=None:
        break
    human_trun= not human_trun
    free=MakeListOfFreeFields(board)
DisplayBoard(board)
if victory=="Computer":
    print("*****Computer Won!!******")
elif victory=="Human":
    print("*****human Won!!******")
else:
    print("*****TIE!!*****")