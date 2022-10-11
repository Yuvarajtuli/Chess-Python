import classes.objectProperties as obj
obj = obj.object()
class knight:
    __digonal,__straight,__jump,__error = 0,0,1,[]
    def __checkMove(e,stepx,stepy):
        err = 0
        if stepx == 1:
            err = 0
            if stepy !=2:
                err = 1
            else:
                err = 0
        else:
            if stepy == 1:
                err = 0
                if stepx !=2:
                    err = 1
                else:
                    err=0
            else:
                err = 1
        if err != 0:
            return [300,"Invalid Move!"]
    def moveKnight(self,object):
        ox,oy,nx,ny,objcol,objtype = object[0],object[1],object[2],object[3],object[4],object[5]
        stepx,stepy = abs(nx-ox),abs(ny-oy)
        estep = self.__checkMove(stepx,stepy)
        if estep:
            return estep
        coordinates = [ox,oy,nx,ny,objcol,objtype]
        err = obj.checkObject(coordinates,straight=self.__straight,digonal=self.__digonal,jump=self.__jump)
        if err:
            return err
        return coordinates
              
