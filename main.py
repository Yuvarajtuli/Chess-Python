import classes.objectProperties as pieces
import classes.objects.pawn as pawn
from classes.useObject import moveObject
import functions as func
chessPieces = pieces.object()
pawn = pawn.pawn()
boardList = chessPieces.createObjects()
# move a pawn
moveNo,game = 1,True
while game == True:
    turn = func.checkTurn(moveNo)
    move = input("Enter Move for "+turn)
    newmove = func.convert_move(move)
    moves = func.getPreviousPos(newmove[0],newmove[1],newmove[0],newmove[1],turn,newmove[2],moveNo=moveNo)
    newBoard = moveObject(moves)
    if len(newBoard) > 2:
        boardList = newBoard
        func.show_graph(boardList)
        if moveNo%2==0:
            ans = input("Do u want to continue(Y,N)?")
            if ans.lower() != 'y':
                game=False
        moveNo+=1
    else:
        print(newBoard)