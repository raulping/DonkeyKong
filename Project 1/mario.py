import constants
class Mario:

    def __init__(self, x, y, lives, when = 0, jumping=False, direction="right", onfloor=False, onladder=False):
        self.__posx = x
        self.__posy = y
        self.__lives = lives
        self.__when = when
        self.__jumping = jumping
        self.__direction = direction
        self.__onfloor = onfloor
        self.__onladder = onladder
        
        
    @property
    def posx(self):
        return self.__posx
    @posx.setter
    def posx(self,value):
        self.__posx = value
    
    @property
    def posy(self):
        return self.__posy
    @posy.setter
    def posy(self,value):
        self.__posy = value
        
    @property
    def when(self):
        return self.__when
    @when.setter
    def when(self,value):
        self.__when = value
        
    @property
    def jumping(self):
        return self.__jumping
    @jumping.setter
    def jumping(self,value):
        self.__jumping= value
    
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self,value):
        self.__direction= value
    
    @property
    def onfloor(self):
        return self.__onfloor
    @onfloor.setter
    def onfloor(self,value):
        self.__onfloor= value
    
    @property
    def onladder(self):
        return self.__onladder
    @onladder.setter
    def onladder(self,value):
        self.__onladder= value
    
    @property
    def lives(self):
        return self.__lives
    @lives.setter
    def lives(self,value):
        self.__lives= value
    
    
    def move(self):
        if self.__onfloor==True:
            if self.__direction == 'left':
                self.__posx -= 1.5
                self.__onfloor=False
            elif self.__direction == 'right':
                self.__posx += 1.5            
                self.__onfloor=False
                
        elif self.__onladder==True:
            if self.__direction == 'up':
                self.__posy -= 1
                self.__onladder=False
            elif self.__direction == 'down':
                self.__posy += 1
                self.__onladder=False


    def fall(self):
        if self.__posy == 6 and (self.__posx>128 or self.__posx<70):
            self.__posy= 37
        if self.__posy == 37 and self.__posx>225:
            self.__posy= 95
        if self.__posy == 95 and self.__posx<8:
            self.__posy= 150
        if self.__posy == 150 and self.__posx>225:
            self.__posy= 216

        
    def jump(self):
        if self.__direction=="right":
            self.__posy -= 12
            self.__posx += 10
            self.__jumping = True
            
        elif self.__direction=="left":     
            self.__posy -= 12
            self.__posx -= 10
            self.__jumping = True
        
        else:
            self.__posy -= 12
            self.__jumping = True
        
    def unjump(self):
        if self.__direction=="right":
            self.__posy += 12
            self.__posx += 10
            self.__jumping = False
            
        elif self.__direction=="left":     
            self.__posy += 12
            self.__posx -= 10
            self.__jumping = False
        
        else:
            self.__posy += 12
            self.__jumping = False
       
        
    def death(self):
        self.__posx= constants.MARIO_X
        self.__posy=constants.MARIO_Y
        self.__lives -= 1