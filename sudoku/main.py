global gameBoard


class Sudoku:

    def __init__(self):
     self.__gameBoard = [[None for _ in range(4)] for _ in range(4)] #Comprehensive List
     
    def checkDuplicacy(self,row,col,value):
        for i in range(4):
            #Checks the duplicacy in its own lines of rows and columns
            if(self.__gameBoard[row][i] == value):
                return True

            if(self.__gameBoard[i][col] == value):
                return True

            #To check duplicacy in the respective diagonal items
        startrow = (row//2) * 2
        startcol = (col//2) * 2

        for i in range(startrow, startrow +2):
            for j in range(startrow,startcol+2):
                
                if (self.__gameBoard[i][j] == value):
                    return True

                    
        return False

    def showGameBoard(self):
        horizontalDash ='_'
        for i in range(4):
            print()
            for j in range(4):
                print("|\t{} ->({},{})\t".format(self.__gameBoard[i][j],i,j),end="")
            print("\n|",horizontalDash*90)


    def insertTheValue(self,row,col,value):
        if(self.checkDuplicacy(row,col,value)):
            return False
        else:
            self.__gameBoard[row][col] = value
            return True


#The real instantiation


option=''

gameone = Sudoku()

# showing the gameboard initially
gameone.showGameBoard()

while(True and not(option == 'x')):

    option = input("Press:\n i -> TO INSERT VALUE AND THE POSITION \n s -> TO SHOW GAMEBOARD\n x -> TO EXIT\n")

    if(option == 'i'):


        position = input("Please choose the position from the board, from\"(0,0)\" to \"(3,3)\" \n \"PLEASE ENTER THE ROW AND COLUMN SEPARATED BY SPACE RESPECTIVELY!!!\"\n ")
        
        rowPosition,colPosition =position.split(" ")
        
        while(not(0<=int(rowPosition)<4 and 0<=int(colPosition)<4)):
            position = input("The position entered should be in-between 0 and 3 for both ROW and COLUMN. So please enter the correct ROW and COLUMN again\t")
            rowPosition,colPosition =position.split(" ")


        value = input("Enter the value in the board\t")

        while(not(1<=int(value)<5)):
            value = input("The values entered should be in-between 1 and 4. So please enter the correct value again\t")



        if(not gameone.insertTheValue(int(rowPosition),int(colPosition), int(value))):
            print("Cannot be inserted due to duplicacy")
        



    
    elif(option == 's'):
        gameone.showGameBoard()







if __name__=="__main__":
    print("Thank you for playing our game")


