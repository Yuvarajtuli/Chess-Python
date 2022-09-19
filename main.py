import classes.objectProperties as pieces
import classes.objects.pawn as pawn
import functions as func
# move = func.get_move()
# print(func.convert_move(move))
chessPieces = pieces.object()
pawn = pawn.pawn()
# # returns a 2d list of properties of board
boardList = chessPieces.createObjects()
pawnPos = []
# print(chessPieces.checkObject([4,2,5,3,'white'],direction='ne'))
# fwp = int(input("Enter Steps(white)!"))
pawnPos = pawn.movePawn(boardList[0][1],2)
newpos = chessPieces.appendObjects(pawnPos)
boardList = newpos
# # print(pawnPos[2:5])
func.show_graph(boardList)
# # fbp = int(input("Enter Steps(black)!"))
# pawnPos = pawn.movePawn(pawnPos[2:5],1,remarks='shift')
# newpos = chessPieces.appendObjects(pawnPos)
# boardList = newpos
# print(boardList)
# # func.show_graph(boardList)