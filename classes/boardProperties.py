import classes.chessProperties as c
class Board(c.chess):
    __maxX = c.chess.maxColNumber_X
    __maxY = c.chess.maxRowNumber_Y
    __sqColNumber_X = 1
    __sqRowNumber_Y = 0
    __sqColor = ""
    def __getColor(self):
        coordinateSum = self.__sqColNumber_X + self.__sqRowNumber_Y
        if coordinateSum%2 == 0:
            self.__sqColor = c.chess.squareColors[1]
        else:
            self.__sqColor = c.chess.squareColors[0]
        return self.__sqColor
    # def getBoard(e,x=0,y=0):
    def getBoard(e):
        board = []
        for i in range(e.__maxX):
            board.append([])
            for j in range(e.__maxY):
                board[i].append([])
                e.__sqRowNumber_Y +=1
                board[i][j].append(e.__sqColNumber_X)
                board[i][j].append(e.__sqRowNumber_Y)
                board[i][j].append(e.__getColor())
            e.__sqColNumber_X +=1
            e.__sqRowNumber_Y = 0
        error = c.chess.checkBoard(e,board)
        if error == None:
            return board
        else:
            return error
