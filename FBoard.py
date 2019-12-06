class FBoard:

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

    def get_game_state(self):
        return self._gamestate

    def move_x(self, row, column):
        if self._gamestate == "X_WON" or self._gamestate == "O_WON":
            return False
        if self._board[self._x_row + 1][self._x_column +1] == "O" and self._board[self._x_row + 1][self._x_column - 1] == "O" and self._board[self._x_row - 1][self._x_column + 1] == "O" and self._board[self._x_row - 1][self._x_column - 1] == "O":
            self._gamestate = "O_WON"
            return False
        if row >= 0 and row <= 7 and column >= 0 and column <= 7:
            if abs(row-self._x_row) == 1:
                if abs(column-self._x_column) == 1:
                    if self._board[row][column] == " ":
                        self._board[self._x_row][self._x_column] = " "
                        self._x_row = row
                        self._x_column = column
                        self._board[row][column] = "X"
                        if self._x_row == 7:
                            self._gamestate = "X_WON"
        if row <0 or row >7 or column <0 or column >7:
            print("Please make a valid move")
            return False
        if abs(self._x_row - row) != 1 or abs(self._x_column - column) != 1:
            print("Please make a valid move")



    def move_o(self, row1, column1, row2, column2):
        if self._gamestate == "X_WON" or self._gamestate == "O_WON":
            return False
        if self._board[row1][column1] == "O":
            if row2 < row1:
                self._board[row1][column1] = " "
                self._board[row2][column2] = "O"
    def display_board(self):
        print(self._board)

#fb = FBoard();
#fb.move_x(1,4);
#fb.move_x(7,7);
#fb.move_o(7,0,6,1);
#fb.display_board();
#print(fb.get_game_state());
