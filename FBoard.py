# Author: Brian Hoang
# Date: 12/05/2019
# Description: fboard class that initializes 8x8 gameboard with 1 x piece and 4 o pieces. has data members and methods to
# track movement of x and o pieces and methods to analyze current state of the game

class FBoard:
    #init method initializes board, all player pieces, gamestate, and x tracker
    def __init__(self):
        self._board = [[[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
                       [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[" "]]]
        self._board[7][0] = "O"
        self._board[7][2] = "O"
        self._board[7][4] = "O"
        self._board[7][6] = "O"
        self._board[0][3] = "X"

        self._gamestate = "UNFINISHED"
        self._x_row = 0
        self._x_column = 3
    #get method to return gamestate
    def get_game_state(self):
        return self._gamestate
    #method that takes in desired row and column for x to move to.
    #checks conditions of a valid move and game state before moving x on the game board
    def move_x(self, row, column):
        if self._gamestate == "X_WON" or self._gamestate == "O_WON":
            return False
        if self._board[self._x_row + 1][self._x_column +1] == "O" and self._board[self._x_row + 1][self._x_column - 1] == "O" and self._board[self._x_row - 1][self._x_column + 1] == "O" and self._board[self._x_row - 1][self._x_column - 1] == "O":
            self._gamestate = "O_WON"
            return False
        #abs() used to check for valid 1 space diagonal movement
        if abs(self._x_row - row) != 1 or abs(self._x_column - column) != 1:
            print("invalid x movement")
            return False
        #checks to see if movement is within bounds of the board
        if row <0 or row >7 or column <0 or column >7:
            #print("Move is off board")
            return False
        #if conditional for if all conditions are met. if so, movement is made accordingly and gamestate and board are set
        if row >= 0 and row <= 7 and column >= 0 and column <= 7:
            if abs(row-self._x_row) == 1:
                if abs(column-self._x_column) == 1:
                    if self._board[row][column] == [' ']:
                        self._board[self._x_row][self._x_column] = [" "]
                        self._x_row = row
                        self._x_column = column
                        self._board[row][column] = "X"
                        #print(row)
                        if row == 7:
                            self._board[row][column] = "X"
                            self._gamestate = "X_WON"
                            self._x_row = row
                            self._x_column = column
                        #print(self._x_row,self._x_column)



    #method that takes in original board location of O and moves it to desired space if conditions are met
    def move_o(self, row1, column1, row2, column2):
        if self._gamestate == "X_WON" or self._gamestate == "O_WON":
            return False
        #checks if O piece is at original row and column
        if self._board[row1][column1] == 'O':
            #checks for if O piece is decreasing rows
            if row2 < row1:
                self._board[row1][column1] = [" "]
                self._board[row2][column2] = "O"
                #if statement for if O has won game by blocking x movement
                if (
                    self._board[self._x_row + 1][self._x_column +1] == "O" and
                    self._board[self._x_row + 1][self._x_column - 1] == "O" and
                    self._board[self._x_row - 1][self._x_column + 1] == "O" and
                    self._board[self._x_row - 1][self._x_column - 1] == "O"
                    ):
                    self._gamestate = "O_WON"
                    return False
        #if row is increasing or staying same, it is an invalid movement
        if row2 >= row1:
            #print("cant increase row for O")
            return False
        #if there is no O piece at given row and column to move from
        if self._board[row1][column1] != 'O':
            return False

    #def display_board(self):
        #print(self._board)
        #print(self._x_row)
        #print(self._x_column)

#fb = FBoard();
#fb.move_x(1,4);
#fb.move_x(2,3);
#fb.move_x(3,2);
#fb.move_x(4,3);
#fb.move_x(5,4);
#fb.move_x(6,3);
#fb.move_o(7,0,6,1);
#fb.move_o(6,1,5,2);
#fb.move_o(7,6,6,5);
#fb.move_o(6,5,5,4);
#fb.move_x(7,4)
#fb.display_board();
#print(fb.get_game_state());
