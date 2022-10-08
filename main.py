import classes.objectProperties as pieces
import classes.objects.pawn as pawn
from classes.useObject import moveObject
from functions import checkTurn,convert_move,getValidMove,show_graph
chessPieces = pieces.object()
pawn = pawn.pawn()
boardList = chessPieces.createObjects()
# move a pawn
moveNo,game = 1,True
while game == True:
    turn = checkTurn(moveNo)
    peiceSelect = input("Select a peice for "+turn+" which has to be moved : ")
    oldMove = convert_move(peiceSelect,'select')
    peiceMove = input("Enter Move for "+turn+" : ")
    newMove = convert_move(peiceMove)
    moves = getValidMove(oldMove[0],oldMove[1],oldMove[2],newMove[0],newMove[1],newMove[2],turn)
    if len(moves)<=2:
        print(moves)
        del moves[0]
        del moves[0]
        continue
    newBoard = moveObject(moves)
    if len(newBoard) > 2:
        boardList = newBoard
        if moveNo%2==0:
            ans = input("Do u want to continue(Y,N)?")
            if ans.lower() != 'y':
                game=False
        moveNo+=1
    else:
        print(newBoard)
        del newBoard[0]
        del newBoard[0]
        # print(boardList)
show_graph(boardList)
    