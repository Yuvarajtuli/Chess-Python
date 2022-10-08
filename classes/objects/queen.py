import classes.objectProperties as obj
obj = obj.object()
class queen:
    __digonal,__straight,__jump,__error = 0,1,0,[]
    def __getDir(e,ox,oy,nx,ny):
        if ox == nx:
            if ny > oy:
                dir1 = 'n'
            else:
                dir1 = 's'
        elif oy == ox:
            if ox > nx:
                dir1 = 'w'
            else:
                dir1 = 'e'
        elif ox < nx:
            if ny > oy:
                dir1 = 'ne'
            else:
                dir1 = 'se'
        elif ox > nx:
            if ny > oy:
                dir1 = 'nw'
            else:
                dir1 = 'sw'
        return dir1
    def moveQueen(self,object):
        ox,oy,nx,ny,objcol,objtype = object[0],object[1],object[2],object[3],object[4],object[5]
        d = self.__getDir(ox,oy,nx,ny)
        coordinates = [ox,oy,nx,ny,objcol,objtype]
        if d == 'n' or d=='s' or d=='e' or d=='w': 
            err = obj.checkObject(coordinates,straight=self.__straight,digonal=self.__digonal,jump=self.__jump,direction=d)
        elif d =='ne' or d=='nw' or d=='se' or d=='sw':
            err = obj.checkObject(coordinates,straight=0,digonal=1,jump=self.__jump,direction=d)
        if err:
            return err
        return coordinates
              
