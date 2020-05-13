
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################    
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Triqui 2 jugadores")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
   
 
while(Game == Running):      
    DrawBoard()    
    if(player % 2 != 0):    
        print("Turno: jugador 1")    
        Mark = 'X'    
    else:    
        print("Turno: jugador 2")    
        Mark = 'O'    
    choice = int(input("Introduzca una posición entre [1-9] : "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()    
       
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Gana: jugador 1")    
    else:    
        print("Gana: jugador 2") 