import classes.objectProperties as pieces
import classes.objects.pawn as pawn
import functions as func
# move = func.get_move()
# print(func.convert_move(move))
chessPieces = pieces.object()
pawn = pawn.pawn()
# returns a 2d list of properties of board
boardList = chessPieces.createObjects()
pawnPos = []
fwp = int(input("Enter Steps(white)!"))
pawnPos = pawn.movePawn(boardList[0][1],fwp)
newpos = chessPieces.appendObjects(pawnPos)
boardList = newpos
print(boardList)
# func.show_graph(boardList)
# fbp = int(input("Enter Steps(black)!"))
# pawnPos = pawn.movePawn(boardList[0][6],fbp)
# newpos = chessPieces.appendObjects(pawnPos)
# boardList = newpos
# func.show_graph(boardList)