class chess:
    maxColNumber_X = 8
    maxRowNumber_Y = 8
    __maxSquares = maxColNumber_X * maxRowNumber_Y
    squareColors = ['yellow','purple']
    peiceColors = ['white','black']
    maxPeices = 32
    maxPawn = 8
    maxKing = 1
    minQueen = 1
    maxQueen = 8
    minRook = 2
    maxRook = 8
    minBishop = 2
    maxBishop = 8
    minKnight = 2
    maxKnight = 8
    direction = ['n','s','e','w','ne','nw','se','sw']
    __error = []
    def checkBoard(e,board):
        tot = 0
        for i in board:
            for j in i:
                tot+=1
        if tot != e.__maxSquares:
            e.__error = [300,"Invalid Chess Board Created!"]
            return e.__error