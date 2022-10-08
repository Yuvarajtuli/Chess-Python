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
def convert_move(move,remarks=''):
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
    elif mlen == 4 and remarks=='':
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
def checkTurn(moveNumber):       
    if moveNumber == 1:
        turn = 'white'
    elif moveNumber%2==0:
        turn = 'black'
    else:
        turn='white'
    return turn
def getDir(ox,oy,nx,ny):
        if ox == nx:
            if ny > oy:
                dir1 = 'n'
            else:
                dir1 = 's'
        elif ox < nx:
            if ny > oy:
                dir1 = 'ne'
            else:
                dir1 = 'se'
        elif ox > nx:
            if ny > oy:
                dir1 = 'nw'
            else:
                dir1 = 'sw'
        return dir1
def getValidMove(ox,oy,otype,nx,ny,ntype,objColor):
    coordinate = []
    d = getDir(ox,oy,nx,ny)
    if objColor == 'white':
        if d!='n':
            if d!='ne':
                if d!='nw':
                    return [300,"White's Turn"]
    else:
        if d!='s':
            if d!='se':
                if d!='sw':
                    return [300,"Black's Turn"]
    if otype == ntype:
        coordinate.append(ox)
        coordinate.append(oy)
        coordinate.append(nx)
        coordinate.append(ny)
        coordinate.append(objColor)
        coordinate.append(ntype)
    else:
        return [300,"Peice Seleted and Peice Moved are different!"]
    if len(coordinate)>6:
        del coordinate[0]
        del coordinate[0]
        del coordinate[0]
        del coordinate[0]
        del coordinate[0]
        del coordinate[0]
    return coordinate
