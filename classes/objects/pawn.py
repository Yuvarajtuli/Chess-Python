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
        elif remarks=='shift':
            objColor = object[2]
        return x,y,objColor
    def movePawn(self,object,step=1,cut='',remarks=''):
        x,y,objcol = self.__getPawn(object,remarks)
        newy = y
        dir1 = ''
        if y==2 or y==7:
            if step>0 and step<3:
                if y == 2 or objcol == 'white':
                    newy+=step
                    dir1 = 'n'
                else:
                    newy-=step
                    dir1 = 's'
            else:
                return self.__error[300,"Invalid Move!"]
        else:
            if step >0 and step<2:
                if y == 2 or objcol == 'white':
                    newy+=step
                    dir1 = 'n'
                else:
                    newy-=step
                    dir1 = 's'
            else:
                return self.__error[300,"Invalid Move!"]
        coordinates = [x,y,x,newy,objcol]
        err = obj.checkObject(coordinates,straight=1,direction=dir1)
        if err:
            return err
        return coordinates
              
