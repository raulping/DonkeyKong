class ladder:
         
    def __init__(self, x, y):
        self.__posx = x
        self.__posy = y
    
    
    @property
    def posx(self):
        return self.__posx
    @property
    def posy(self):
        return self.__posy
    
