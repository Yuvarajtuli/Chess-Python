from classes.objectProperties import object as chessPieces
from classes.objects.pawn import pawn as pawn
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