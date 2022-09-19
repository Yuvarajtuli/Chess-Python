import classes.objectProperties as pieces
import classes.objects.pawn as pawn
import functions as func
chessPieces = pieces.object()
pawn = pawn.pawn()
boardList = chessPieces.createObjects()
pawnPos = []
# move a pawn
x = int(input())
x-=1
y = int(input())
y-=1
pawnPos = pawn.movePawn(boardList[x][y],2)
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