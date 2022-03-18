import constants

class barriles:
    
    def __init__(self, x, y, move='r', falling=False):
        self.__posx = x
        self.__posy = y
        self.__move = move
        self.__falling = falling
    
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
    def falling(self):
        return self.__falling
    @falling.setter
    def falling(self,value):
        self.__falling = value
    
    def move(self):
        self.__falling = False
        if  self.__move== 'r':
            self.__posx += 1
        elif  self.__move== 'l':
            self.__posx -= 1

    def fall(self):
        self.__falling = True
        self.__posy += 1
        if constants.WIDTH - self.__posx < 50:
            self.__move= 'l'
        else:
            self.__move= 'r'