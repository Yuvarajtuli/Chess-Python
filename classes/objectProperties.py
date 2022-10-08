import re
import classes.chessProperties as chess
import classes.boardProperties as board
board = board.Board()
class object(chess.chess):
    __objectName = ["pawn","rook","knight","bishop","queen","king"]
    __board = board.getBoard()
    __error = []
    def __getObjectStartPos(self,x,y):
        if y == 2 or y == 7:return self.__objectName[0]
        if y==1 or y==8:
            if x==1 or x==8:return self.__objectName[1]
            elif x==2 or x==7:return self.__objectName[2]
            elif x==3 or x==6:return self.__objectName[3]
            elif x==4:return self.__objectName[4]
            elif x==5:return self.__objectName[5]
    def __newError(e,status,msg):
        e.__error.append(status)
        e.__error.append(msg)
        return e.__error
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
        # print("append coordinates are :",coordinates)
        objName = e.__board[coordinates[0]-1][coordinates[1]-1][3]
        objColor = e.__board[coordinates[0]-1][coordinates[1]-1][4]
        del e.__board[coordinates[0]-1][coordinates[1]-1][3]
        del e.__board[coordinates[0]-1][coordinates[1]-1][3]
        if len(e.__board[coordinates[2]-1][coordinates[3]-1]) <= 3:
            e.__board[coordinates[2]-1][coordinates[3]-1].append(objName)
            e.__board[coordinates[2]-1][coordinates[3]-1].append(objColor)
        elif len(e.__board[coordinates[2]-1][coordinates[3]-1]) > 3:
            e.__board[coordinates[2]-1][coordinates[3]-1].pop(3)
            e.__board[coordinates[2]-1][coordinates[3]-1].pop(3)
            e.__board[coordinates[2]-1][coordinates[3]-1].append(objName)
            e.__board[coordinates[2]-1][coordinates[3]-1].append(objColor)
        return e.__board
    def checkObject(e,coordinates,straight=0,digonal=0,direction='',jump=0,remarks=''):
        remarks = remarks.strip()
        remarks = remarks.lower()
        dir1 = direction.lower()
        oldx = coordinates[0]
        oldy = coordinates[1]
        newx = coordinates[2]
        newy = coordinates[3]
        if oldx > 8 or oldx < 1:
            return e.__newError(300,"Invalid position to move")
        if oldy > 8 or oldy < 1:
            return e.__newError(300,"Invalid position to move")
        if newx > 8 or newx < 1:
            return e.__newError(300,"Invalid position to move")
        if newy > 8 or newy < 1:
            return e.__newError(300,"Invalid position to move")
        objColor = coordinates[4]
        objType = coordinates[5]
        if len(e.__board[newx - 1][newy - 1]) > 3 and objColor == e.__board[newx - 1][newy - 1][4]:
            return e.__newError(300,"Invalid position to move")
        elif len(e.__board[newx - 1][newy - 1]) > 3 and jump == 1 and objColor == e.__board[newx - 1][newy - 1][4]:
            return e.__newError(300,"Invalid position to move")
        if straight == 1 and jump == 0 and digonal == 0:           
            if dir1 == chess.chess.direction[0] or dir1 == chess.chess.direction[1]:
                if oldx != newx:
                    return e.__newError(300,"Invalid position to move")
                start = 0
                end = 0
                move = 0
                if oldy < newy:
                    start = oldy+1
                    end = newy+1
                    move = 1
                elif newy<oldy:
                    start = oldy-1
                    end =  newy-1
                    move = -1
                for i in range(start,end,move):
                    if i != (end-1) and len(e.__board[newx - 1][i - 1]) > 3:
                        return e.__newError(300,"Invalid position to move")
                    elif i == (end-1) and len(e.__board[newx - 1][i - 1]) > 3 and objColor == e.__board[newx - 1][i - 1][4]:
                        return e.__newError(300,"Invalid position to move")
                    elif i == (end-1) and len(e.__board[newx - 1][i - 1]) > 3 and objColor != e.__board[newx - 1][i - 1][4] and objType == 'pawn':
                        return e.__newError(300,"Invalid position to move")
            elif dir1 == chess.chess.direction[2] or dir1 == chess.chess.direction[3]:
                if oldy != newy:
                    return e.__newError(300,"Invalid position to move")
                start = 0
                end = 0
                move = 0
                if oldx < newx:
                    start = oldx+1
                    end = newx+1
                    move = 1
                elif newx < oldx:
                    start = oldx-1
                    end = newx-1
                    move = -1
                for i in range(start,end,move):
                    if i != (end-1) and len(e.__board[i - 1][newy - 1]) > 3:
                        return e.__newError(300,"Invalid position to move")
                    elif i == (end-1) and len(e.__board[i - 1][newy - 1]) > 3 and objColor == e.__board[newx - 1][i - 1][4]:
                        return e.__newError(300,"Invalid position to move")
        elif straight == 0 and digonal == 1 and jump ==0:
            mx = oldx - newx
            my = oldy - newy
            m = abs(mx/my)
            if m != 1:
                return e.__newError(300,"Invalid position to move")
            start = 0
            end = 0
            move = 0
            if oldx < newx:
                start = oldx + 1
                end = newx +1
                move = 1
            elif oldx > newx:
                start = oldx-1
                end = newx-1
                move = -1
            cnt = 0
            for i in range(start,end,move):
                cnt+=1
                # print("start : ",start," end : ",end," move : ",move," count : ",cnt," length at that pos : ",len(e.__board[i - 1][(oldy + cnt) - 1])," remarks : ",remarks)
                if (dir1 == chess.chess.direction[4] or dir1 == chess.chess.direction[5]):
                    if i != (end + 1) and len(e.__board[i - 1][(oldy + cnt) - 1]) > 3:
                        # print("condition 1 : \nremarks : "+remarks+" i = ",i," ,board pos = ",e.__board[i - 1][(oldy + cnt) - 1]," ,x = ",i - 1," ,y = ",(oldy + cnt)," ,length at that pos = ",len(e.__board[i - 1][(oldy + cnt) - 1]))
                        return e.__newError(300,"Invalid position to move")
                    elif i==(end+1) and len(e.__board[i - 1][(oldy + cnt) - 1]) > 3 and objColor == e.__board[i - 1][(oldy + cnt) - 1][4]:
                        # print("condition 2 : \nremarks : "+remarks+" i = ",i," ,board pos = ",e.__board[i - 1][(oldy + cnt) - 1]," ,x = ",i - 1," ,y = ",(oldy + cnt)," ,length at that pos = ",len(e.__board[i - 1][(oldy + cnt) - 1]))
                        return e.__newError(300,"Invalid position to move")
                    elif remarks == 'cut' and i==(end+1) and len(e.__board[i - 1][(oldy + cnt) - 1]) <= 3:
                        # print("condition 3 : \nremarks : "+remarks+" i = ",i," ,board pos = ",e.__board[i - 1][(oldy + cnt) - 1]," ,x = ",i - 1," ,y = ",(oldy + cnt)," ,length at that pos = ",len(e.__board[i - 1][(oldy + cnt) - 1]))
                        return e.__newError(300,"Invalid position to move")
                elif dir1 == chess.chess.direction[6] or dir1 == chess.chess.direction[7]:
                    if i != (end - 1) and len(e.__board[i - 1][(oldy - cnt) - 1]) > 3:
                        # print("condition 1 : \nremarks : "+remarks+" i = ",i," ,board pos = ",e.__board[i - 1][(oldy - cnt) - 1]," ,x = ",i - 1," ,y = ",(oldy - cnt)," ,length at that pos = ",len(e.__board[i - 1][(oldy - cnt) - 1]))
                        return e.__newError(300,"Invalid position to move")
                    elif i==(end-1) and len(e.__board[i - 1][(oldy - cnt) - 1]) > 3 and objColor == e.__board[i - 1][(oldy - cnt) - 1][4]:
                        # print("condition 2 : \nremarks : "+remarks+" i = ",i," ,board pos = ",e.__board[i - 1][(oldy - cnt) - 1]," ,x = ",i - 1," ,y = ",(oldy - cnt)," ,length at that pos = ",len(e.__board[i - 1][(oldy - cnt) - 1]))
                        return e.__newError(300,"Invalid position to move")
                    elif remarks == 'cut' and i==(end-1) and len(e.__board[i - 1][(oldy - cnt) - 1]) <= 3:
                        # print("condition 3 : \nremarks : "+remarks+" i = ",i," ,board pos = ",e.__board[i - 1][(oldy - cnt) - 1]," ,x = ",i - 1," ,y = ",(oldy - cnt)," ,length at that pos = ",len(e.__board[i - 1][(oldy - cnt) - 1]))
                        return e.__newError(300,"Invalid position to move")