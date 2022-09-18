import classes.chessProperties as chess
import classes.boardProperties as board
board = board.Board()
class object(chess.chess):
    __objectName = ["pawn","rook","knight","bishop","queen","king"]
    __board = board.getBoard()
    def __getObjectStartPos(self,x,y):
        if y == 2 or y == 7:return self.__objectName[0]
        if y==1 or y==8:
            if x==1 or x==8:return self.__objectName[1]
            elif x==2 or x==7:return self.__objectName[2]
            elif x==3 or x==6:return self.__objectName[3]
            elif x==4:return self.__objectName[4]
            elif x==5:return self.__objectName[5]
    def __getObjectColor(self,y):
        if y<=2:
            return chess.chess.peiceColors[0]
        elif y>=7:
            return chess.chess.peiceColors[1]
    def createObjects(self):
        cnt = 0
        for i in range(self.maxColNumber_X):
            for j in range(self.maxRowNumber_Y):
                x = self.__board[i][j][0]
                y = self.__board[i][j][1]
                newVal = self.__getObjectStartPos(x,y)
                if newVal!=None:
                    self.__board[i][j].append(newVal)
                    self.__board[i][j].append(self.__getObjectColor(y))
        mainBoard = self.__board
        return self.__board
    def appendObjects(e,coordinates):
        objName = e.__board[coordinates[0]-1][coordinates[1]-1][3]
        objColor = e.__board[coordinates[0]-1][coordinates[1]-1][4]
        del e.__board[coordinates[0]-1][coordinates[1]-1][3]
        del e.__board[coordinates[0]-1][coordinates[1]-1][3]
        e.__board[coordinates[2]-1][coordinates[3]-1].append(objName)
        e.__board[coordinates[2]-1][coordinates[3]-1].append(objColor)
        return e.__board

