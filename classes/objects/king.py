import classes.objectProperties as obj
obj = obj.object()
class king:
    __digonal,__straight,__jump,__step,__error = 0,1,0,1,[]
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
    def __checkSteps(e,stepy='',stepx=''):
        if stepy!='':
            if stepy >e.__step:
                return [300,"Invalid Move!"]
        if stepx!='':
            if stepx > e.__step:
                return [300,"Invalid Move!"]
            
    def moveKing(self,object):
        ox,oy,nx,ny,objcol,objtype = object[0],object[1],object[2],object[3],object[4],object[5]
        d = self.__getDir(ox,oy,nx,ny)
        coordinates = [ox,oy,nx,ny,objcol,objtype]
        if d == 'n' or d=='s': 
            stepy = abs(ny-oy)
            checkStep = self.__checkSteps(stepy=stepy)
            if checkStep is not None:
                return checkStep
            err = obj.checkObject(coordinates,straight=1,direction=d)
        elif d=='e' or d=='w':
            stepx = abs(nx-ox)
            checkStep = self.__checkSteps(stepx=stepx)
            if checkStep is not None:
                return checkStep
            err = obj.checkObject(coordinates,straight=1,direction=d)
        elif d =='ne' or d=='nw' or d=='se' or d=='sw':
            stepx = abs(nx-ox)
            stepy = abs(ny-oy)
            checkStep = self.__checkSteps(stepy = stepy,stepx=stepx)
            if checkStep is not None:
                return checkStep
            err = obj.checkObject(coordinates,digonal=1,direction=d)
        if err:
            return err
        return coordinates