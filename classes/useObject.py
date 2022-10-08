import classes.objectProperties as obj
chessPieces = obj.object()
import classes.objects.pawn as pawn
pawn = pawn.pawn()
import classes.objects.rook as rook
rook = rook.rook()
import classes.objects.bishop as bishop
bishop=bishop.bishop()
import classes.objects.knight as knight
knight =knight.knight()
import classes.objects.queen as queen
queen=queen.queen()
import classes.objects.king as king
king=king.king()
def moveObject(movement):
    if movement!=[]:
        if movement[5] == chessPieces.objectName[0]:
            objectPos = pawn.movePawn(movement)
        elif movement[5] == chessPieces.objectName[1]:
            objectPos = rook.moveRook(movement)
        elif movement[5] == chessPieces.objectName[2]:
            objectPos = knight.moveKnight(movement)
        elif movement[5] == chessPieces.objectName[3]:
            objectPos = bishop.moveBishop(movement)
        elif movement[5] == chessPieces.objectName[4]:
            objectPos = queen.moveQueen(movement)
        elif movement[5] == chessPieces.objectName[5]:
            objectPos = king.moveKing(movement)
        if len(objectPos)<=2:
                return objectPos
        newpos = chessPieces.appendObjects(objectPos)
        return newpos
    else:
        return [300,"Invalid position to move"]