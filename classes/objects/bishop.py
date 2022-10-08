import classes.objectProperties as obj
obj = obj.object()
class bishop:
    __digonal,__straight,__jump,__error = 1,0,0,[]
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
    def __checkdir(e,d):
        if d=='n' or d=='s' or d=='e' or d=='w':
            return [300,"Invalid Move!"]
    def moveBishop(self,object):
        ox,oy,nx,ny,objcol,objtype = object[0],object[1],object[2],object[3],object[4],object[5]
        d = self.__getDir(ox,oy,nx,ny)
        derr = self.__checkdir(d)
        if derr:
            return derr
        coordinates = [ox,oy,nx,ny,objcol,objtype]
        err = obj.checkObject(coordinates,straight=self.__straight,digonal=self.__digonal,jump=self.__jump,direction=d)
        if err:
            return err
        return coordinates
              
