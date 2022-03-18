class floor:
     
    def __init__(self, x, y):
        self.__posx = x
        self.__posy = y
    
    
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


"""
    #Floors
    a = 0
    #Suelo abajo
    for i in range(0, constants.WIDTH, 7):
        pyxel.blt(floor.posx + i, floor.posy - a, 0, 0, 0, 7, 7, colkey=0)
        a += 0.25
    #Suelo medio
    for i in range(0, constants.WIDTH-20, 7):
        pyxel.blt(floor.posx + i, 150 + a , 0, 0, 0, 7, 7, colkey=0)
        a += 0.25
    #Suelo Arriba
    for i in range(20, constants.WIDTH, 7):
        pyxel.blt(floor.posx + i, 130 - a, 0, 0, 0, 7, 7, colkey=0)  
        a += 0.25
    #Suelo arrib aariiba 
    for i in range(0, constants.WIDTH-20, 7):
        pyxel.blt(floor.posx + i, 26 + a, 0, 0, 0, 7, 7, colkey=0)    
        a += 0.25
"""
