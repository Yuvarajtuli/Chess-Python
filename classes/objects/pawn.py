import classes.objectProperties as obj
obj = obj.object()
class pawn:
    __digonal = 0
    __straight = 1
    __startMove = [1,2]
    __jump = 0
    __step = 1
    __error=[]
    def __getPawn(self,object,remarks=''):
        x = object[0]
        y = object[1]
        
        if remarks=='':
            objColor = object[4]
            objType = object[3]
        elif remarks=='shift':
            objColor = object[2]
            objType = object[3]
        return x,y,objColor,objType
    def __checkMovePawn(e,x,y,step):
        if step > 0:
            if step < 3:
                if step == 2:
                    if y != 2:
                        if y!=7:
                            e.__error.append(300)
                            e.__error.append("Invalid Move!")
                    elif y!=7:
                        if y!=2:
                            e.__error.append(300)
                            e.__error.append("Invalid Move!")
            elif step >= 3:
                e.__error.append(300)
                e.__error.append("Invalid Move!")
        else:
            e.__error.append(300)
            e.__error.append("Invalid Move!")
        return e.__error
    def movePawn(self,object,step=1,cut='',remarks=''):
        x,y,objcol,objtype = self.__getPawn(object,remarks)
        newy = y
        dir1 = ''
        err = self.__checkMovePawn(x,y,step)
        if err:
            return err
        if objcol == 'white':
            newy+=step
            dir1 = 'n'
        else:
            newy-=step
            dir1 = 's'
        coordinates = [x,y,x,newy,objcol,objtype]
        err = obj.checkObject(coordinates,straight=1,direction=dir1)
        if err:
            print(err)
            return err
        return coordinates
              
