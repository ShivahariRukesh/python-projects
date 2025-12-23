import math

class Sudoku:
    def __init__(self, size):
        if int(math.sqrt(size)) ** 2 != size:
            raise ValueError("Board size must be a perfect square (4, 9, 16, ...)")

        self.size = size
        self.subgrid_size = int(math.sqrt(size))
        self.__game_board = [[None for _ in range(size)] for _ in range(size)]

    def get_game_board(self):
        return self.__game_board

    def check_duplicacy(self, row, col, value):

        for i in range(self.size):
            #Checks the duplicacy in its own lines of rows and columns
            if self.__game_board[row][i] == value:
                return True
            if self.__game_board[i][col] == value:
                return True

        #To check duplicacy in the respective diagonal items
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size

        for i in range(start_row, start_row + self.subgrid_size):
            for j in range(start_col, start_col + self.subgrid_size):
                if self.__game_board[i][j] == value:
                    return True

        return False

    def insert_value(self, row, col, value):
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False

        if not (1 <= value <= self.size):
            return False

        if self.check_duplicacy(row, col, value):
            return False

        self.__game_board[row][col] = value
        return True

    def show_game_board(self):
        for row in range(self.size):
            print()
            for col in range(self.size):
                print(f"| {self.__game_board[row][col]} ", end="")
            print("|")

#The real instantiation

def start_the_game():
    option=''

    gameone = Sudoku(9)

    # showing the gameboard initially
    gameone.show_game_board()

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



            if(not gameone.insert_value(int(rowPosition),int(colPosition), int(value))):
                print("Cannot be inserted due to duplicacy")
            



        
        elif(option == 's'):
            gameone.show_game_board()







if __name__=="__main__":
    start_the_game()


