from numpy import var
import classes.objectProperties as pieces
import classes.objects.pawn as pawn
chessPieces = pieces.object()
pawn = pawn.pawn()
def moveObject(movement):
    if movement!=[]:
        if movement[5] == 'pawn':
            pawnPos = pawn.movePawn(movement)
            if len(pawnPos)<=2:
                return pawnPos
            newpos = chessPieces.appendObjects(pawnPos)
        return newpos
    else:
        return [300,"Invalid position to move"]