from operator import index, le
import re
import classes.objectProperties as pieces
piece = pieces.object()
import numpy
import matplotlib.pyplot as plt
def show_graph(board):
    ax = plt.axes()
    ax.set_facecolor("gray")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j])==3:
                plt.scatter(board[i][j][0], board[i][j][1], label= "stars", color= board[i][j][2], marker= "*", s=30)
            else:
                plt.scatter(board[i][j][0], board[i][j][1], label= "Objects", color= board[i][j][4], marker= "*", s=30)

    plt.xlabel('files')
    plt.ylabel('ranks')
    plt.title('Chess Board')
    plt.show()
def get_move():
    move = input()
    return move
def convert_move(move):
    move = move.lower()
    move = move.strip()
    mlen = len(move)
    mAlpha = ['a','b','c','d','e','f','g','h']
    mSymbol = ['k','q','b','n','r','+','x','o-o','o-o-o','=','#']
    mSName = ['king','queen','bishop','knight','rook','check','cut','king side castle','queen side castle','promoted','checkmate']
    x=0
    y=0
    objName = ""
    res = []
    if mlen == 2:      
        x = mAlpha.index(move[0])+1
        y = int(move[1])
        objName = "pawn"
        res.append(x)
        res.append(y)
        res.append(objName)
    elif mlen == 3:
        si = mSymbol.index(move[0])
        objName = mSName[si]
        x = mAlpha.index(move[1])+1
        y = int(move[2])
        res.append(x)
        res.append(y)
        res.append(objName)
    elif mlen == 4:
        if move.find("=") != -1:
            si = mSymbol.index(move[len(move)-1])
            objName = mSName[si]
            x = mAlpha.index(move[0])+1
            y = int(move[1])
        elif move.find("x") != -1 and move[0] not in mAlpha:
            si = mSymbol.index(move[0])
            objName = mSName[si]
            x = mAlpha.index(move[2])+1
            y = int(move[len(move)-1])
        elif move.find("x") != -1 and move[0] in mAlpha:
            objName = "pawn"
            x = mAlpha.index(move[2])+1
            y = int(move[len(move)-1])
        res.append(x)
        res.append(y)
        res.append(objName)
    return res
def getDir(ox,oy,nx,ny):
        if ox == nx:
            if ny > oy:
                dir1 = 's'
            else:
                dir1 = 'n'
        elif ox < nx:
            if ny > oy:
                dir1 = 'sw'
            else:
                dir1 = 'nw'
        elif ox > nx:
            if ny > oy:
                dir1 = 'se'
            else:
                dir1 = 'ne'
        return dir1
def getPreviousPos(ox,oy,nx,ny,objColor,objType,moveNo,rotation=1):
    err = []
    if objType == 'pawn':
        if objColor == 'white':
            ny-=1
        else:
            ny+=1
        d = getDir(ox,oy,nx,ny)
        coordinates =[ox,oy,nx,ny,objColor,objType]
        if rotation==1 and err:
            del err
        err = piece.backtrackObject(coordinates,straight=1,direction=d)
        if moveNo !=1:
            del err[0]
            del err[0] 
        if rotation!=1:
            del err[0]
            del err[0]
        if err[0]==200:
            # print(err)
            rotation+=1
            return getPreviousPos(ox,oy,nx,ny,objColor,objType,rotation)  
        elif err[0]==201:
            # print(err)
            bc = [coordinates[2],coordinates[3],coordinates[0],coordinates[1],objColor,objType]
            return bc                   
def checkTurn(moveNumber):       
    if moveNumber == 1:
        turn = 'white'
    elif moveNumber%2==0:
        turn = 'black'
    else:
        turn='white'
    return turn