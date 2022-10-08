import classes.objectProperties as obj
obj = obj.object()
class pawn:
    __digonal,__straight,__startMove,__jump,__step,__error = 0,1,[1,2],0,1,[]
    def __getDir(e,ox,oy,nx,ny):
        if ox == nx:
            if ny > oy:
                dir1 = 'n'
            else:
                dir1 = 's'
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
    def __checkMovePawn(e,ox,oy,nx,ny,ocol,otype,step,d):
        if d=='n' or d=='s':
            if step > 0:
                if step < 3:
                    if step == 2:
                        if oy != 2:
                            if oy!=7:
                                e.__error.append(300)
                                e.__error.append("Invalid Move!")
                        elif oy!=7:
                            if oy!=2:
                                e.__error.append(300)
                                e.__error.append("Invalid Move!")
                elif step >= 3:
                    e.__error.append(300)
                    e.__error.append("Invalid Move!")
            else:
                e.__error.append(300)
                e.__error.append("Invalid Move!")
            return e.__error
    def movePawn(self,object):
        ox,oy,nx,ny,objcol,objtype = object[0],object[1],object[2],object[3],object[4],object[5]
        step,dir1 = abs(ny-oy),self.__getDir(ox,oy,nx,ny)
        err = self.__checkMovePawn(ox,oy,nx,ny,objcol,objtype,step,dir1)
        if err:
            return err 
        if dir1!='n' and dir1!='s':
            stepx = abs(nx-ox)
            stepy = abs(ny-oy)
            if stepx>1 or stepy>1:
                self.__error.append(300)
                self.__error.append("Invalid Move!")
                return self.__error   
            coordinates = [ox,oy,nx,ny,objcol,objtype]
            err = obj.checkObject(coordinates,straight=0,digonal=1,direction=dir1,remarks='cut')
            if err:
                return err
            return coordinates
        else:  
            coordinates = [ox,oy,nx,ny,objcol,objtype]
            err = obj.checkObject(coordinates,straight=1,direction=dir1)
            if err:
                return err
            return coordinates
              
