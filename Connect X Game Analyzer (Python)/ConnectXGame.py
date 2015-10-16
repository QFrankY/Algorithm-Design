#The Challenge:
#Lets say two people are playing a game of connect X. They take they take turns
#putting pieces on a dimX by dimY board until one of them connects X pieces  
#in a line vertically, horizontally or diagonally. Given the current state of the
#board, check whether or not someone has won. If there is a winner, identify the
#winner. 

#My Approach:
#So this algorithm is meant to scale based on the dimensions of the board and
#how many pieces they have to connect to win. I decided to start from a corner
#and cycle through all the pieces checking if they are the start of a winning
#connection. Lets define the corner I start on as bottom left, I would then 
#check X pieces to the left, X pieces above and X pieces diagonally to the left
#and above to see if there is a winning connection. If there is not, I would move
#onto the next piece and do the same check. 

#To check whether or not all the pieces in a line belong to the same player, I set
#player one's pieces to a value of two and player two's pieces to a value of three
#I would multiply all the value of all the pieces in a line and check if they were
#equal to 2^X or 3^X. 

#numConnect is the number of pieces a player needs to connect to win. 
def FindWinner (board, dimX, dimY, numConnect):
    rowValue = 1
    colValue = 1
    
    diag1Value = 1
    diag2Value = 1
    print("Starting")
    
    #Cycling through the pieces
    for indexX in range (0,dimX):
        
        for indexY in range (0,dimY):

            for connectNum in range (0, numConnect):
                
                #checking the vertical connection from the piece in consideration
                #Makes sure the piece in consideration is at least numConnect pieces
                #from the end of the array or else a win is not possible
                if (indexY <= (dimY-numConnect)):
                    rowValue *= board[indexX][indexY + connectNum]
                
                #checking the horizontal connection from the piece in consideration
                if (indexX <= (dimX-numConnect)):
                    colValue *= board[indexX + connectNum][indexY]
                
                #checking diagonal 1
                if (indexX <= (dimX-numConnect) and indexY <= (dimY-numConnect)):
                    diag1Value *= board[indexX + connectNum][indexY + connectNum]
                
                #checking diagonal 2    
                if (indexX <= (dimX-numConnect) and indexY >= (numConnect)):
                    diag2Value *= board[indexX + connectNum][indexY - connectNum]
                
                #checking if player two won
                if (rowValue == 3**numConnect or colValue == 3**numConnect 
                    or diag1Value == 3**numConnect or diag2Value == 3**numConnect):
                    
                    print("Player Two Wins")
                    return True
                
                #checking if player one won
                elif  (rowValue == 2**numConnect or colValue == 2**numConnect 
                    or diag1Value == 2**numConnect or diag2Value == 2**numConnect): 
                    
                    print("Player One Wins")
                    return True    
            
            #reseting the products
            rowValue = 1
            colValue = 1
            diag1Value = 1
            diag2Value = 1
            
            #This is to prevent unnecessary checks near the end of the array
            #If a win has not happened yet, then there is no win as piece of board left is not
            #big enough to connect numConnect pieces
            #if (indexX > (dimX - numConnect + 1) and indexY > (dimY - numConnect + 1)):
            #   print ("Done")
            #   return False
    print("done")

#Test Values
a = [3,2,3,0]
b = [0,3,0,3]
c = [3,3,3,3]
d = [0,3,0,0]
e = [3,0,3,3]

board = [a,b,c,d,e]

FindWinner (board, 5, 4, 4)

#Outcome:
#Player Two Wins
