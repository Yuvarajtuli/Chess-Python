import classes.objectProperties as pieces
import classes.objects.pawn as pawn
import functions as func
chessPieces = pieces.object()
pawn = pawn.pawn()
boardList = chessPieces.createObjects()
pawnPos = []
# move a pawn
pawnPos = pawn.movePawn(boardList[0][1],2)
newpos = chessPieces.appendObjects(pawnPos)
boardList = newpos
func.show_graph(boardList)
pawnPos = pawn.movePawn(pawnPos[2:6],remarks='shift')
newpos = chessPieces.appendObjects(pawnPos)
boardList = newpos
func.show_graph(boardList)
pawnPos = pawn.movePawn(pawnPos[2:6],remarks='shift')
newpos = chessPieces.appendObjects(pawnPos)
boardList = newpos
func.show_graph(boardList)
pawnPos = pawn.movePawn(pawnPos[2:6],remarks='shift')
newpos = chessPieces.appendObjects(pawnPos)
boardList = newpos
func.show_graph(boardList)