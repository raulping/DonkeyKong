import pyxel
import random
import mario
import donkey
import petra
import floor
import ladder
import barrel
import barriles
import platforms
import lives
import constants

class game:
    def __init__(self, listbarriles=[], allfloors=[], all_ladders=[], listlives=[]):
            ####Floors
        listfloor1=[]
        for i in range(0, constants.WIDTH, 7):
            floor1=floor.floor(constants.FLOOR_X + i, constants.FLOOR_Y)    
            listfloor1.append(floor1)
        
        listfloor2=[]
        for i in range(0, constants.WIDTH-20, 7):
            floor2=floor.floor(constants.FLOOR_X + i, 165)    
            listfloor2.append(floor2)
        
        listfloor3=[]
        for i in range(20, constants.WIDTH, 7):
            floor3=floor.floor(constants.FLOOR_X + i, 110)
            listfloor3.append(floor3)
        
        listfloor4=[]
        for i in range(0, constants.WIDTH-20, 7):
            floor4=floor.floor(constants.FLOOR_X + i, 52)    
            listfloor4.append(floor4)
        
        listfloor5=[]
        for i in range(0, 45, 7):
            floor5=floor.floor(80 + i, 21)    
            listfloor5.append(floor5)
        
        allfloors=[]
        allfloors.extend(listfloor1)
        allfloors.extend(listfloor2)
        allfloors.extend(listfloor3)
        allfloors.extend(listfloor4)
        allfloors.extend(listfloor5)
        
        ####Ladders
        lisladder1=[]
        for i in range(0, 56, 5):
            ladder1=ladder.ladder(constants.WIDTH - 28, constants.HEIGHT - 188 + i)    
            lisladder1.append(ladder1)
        
        lisladder2=[]
        for i in range(0, 53, 5):
            ladder2=ladder.ladder(constants.WIDTH - 219, constants.HEIGHT - 130 + i)    
            lisladder2.append(ladder2)
        
        lisladder3=[]
        for i in range(0, 68, 5):
            ladder3=ladder.ladder(constants.WIDTH - 28, constants.HEIGHT - 75 + i)    
            lisladder3.append(ladder3)
        
        lisladder4=[]
        for i in range(0, 52, 5):
            ladder4=ladder.ladder(constants.WIDTH - 95, constants.HEIGHT - 130 + i)    
            lisladder4.append(ladder4)
        
        lisladder5=[]
        for i in range(0, 34, 5):
            ladder5=ladder.ladder(constants.WIDTH - 120, constants.HEIGHT - 219 + i)    
            lisladder5.append(ladder5)
        
        listbroken1=[]
        for i in range(0, 25, 5):
            broken1=ladder.ladder(constants.WIDTH - 180, constants.HEIGHT - 75 + i)    
            listbroken1.append(broken1)
        
        listbroken2=[]
        for i in range(0, 20, 5):
            broken2=ladder.ladder(constants.WIDTH - 180, constants.HEIGHT - 27 + i)    
            listbroken2.append(broken2)
        
        listbroken3=[]
        for i in range(0, 25, 5):
            broken3=ladder.ladder(constants.WIDTH - 180, constants.HEIGHT - 188 + i)    
            listbroken3.append(broken3)
        
        listbroken4=[]
        for i in range(0, 20, 5):
            broken4=ladder.ladder(constants.WIDTH - 180, constants.HEIGHT - 150 + i)    
            listbroken4.append(broken4)
        
        all_ladders=[]
        all_ladders.extend(lisladder1)
        all_ladders.extend(lisladder2)
        all_ladders.extend(lisladder3)
        all_ladders.extend(lisladder4)
        all_ladders.extend(lisladder5)
        all_ladders.extend(listbroken1)
        all_ladders.extend(listbroken2)
        all_ladders.extend(listbroken3)
        all_ladders.extend(listbroken4)
        
        
        listlives=[]
        while len(listlives)<3:
            for i in range(0, 45, 16):
                live = lives.lives(constants.LIVES_X + i , 173)
                listlives.append(live)
        
        self.__listbarriles=listbarriles
        self.__allfloors=allfloors
        self.__all_ladders=all_ladders
        self.__listlives=listlives
        self.__listbarriles=listbarriles
        self.__mario = mario.Mario(constants.MARIO_X,constants.MARIO_Y, constants.LIVES)
        self.__kong = donkey.donkeykong(constants.KONG_X, constants.KONG_Y)
        self.__petra = petra.petra(constants.PETRA_X, constants.PETRA_Y)
        self.__barrel = barrel.barrel(constants.BARREL_X, constants.BARREL_Y) 
        self.__platform = platforms.platforms(constants.PLATFORM_X, constants.PLATFORM_Y)
        self.__pisos = [42,100,155, 221]
        self.__points = constants.POINTS
        self.__bonus = 15000
        
        # The first thing to do is to create the screen, see API for more parameters
        pyxel.init(constants.WIDTH, constants.HEIGHT, caption=constants.CAPTION)
        pyxel.load("my_resource.pyxres")
        pyxel.playm(0, loop=False)
        pyxel.run(self.update, self.draw)

        
    def moveMario(self, x, y):
        if pyxel.btn(pyxel.KEY_RIGHT):
            for f in self.__allfloors:
                if self.__mario.posy - f.posy == -15:
                    self.__mario.onfloor=True
            self.__mario.direction="right"
            self.__mario.move()
                
        elif pyxel.btn(pyxel.KEY_LEFT):
            for f in self.__allfloors:
                if self.__mario.posy - f.posy == -15:
                    self.__mario.onfloor=True
            self.__mario.direction="left"
            self.__mario.move()
    
        elif pyxel.btn(pyxel.KEY_UP):
            for l in self.__all_ladders:
                if (self.__mario.posx - l.posx in range(-10,10)) and (self.__mario.posy - l.posy in range(-14,14)):
                    self.__mario.onladder=True
            self.__mario.direction="up"
            self.__mario.move()
    
        elif pyxel.btn(pyxel.KEY_DOWN):
            for l in self.__all_ladders:
                if (self.__mario.posx - l.posx in range(-10,10)) and (self.__mario.posy - l.posy in range(-14,14)):
                    self.__mario.onladder=True
            self.__mario.direction="down"
            self.__mario.move()
    
    
        #Saltar
        if pyxel.btn(pyxel.KEY_SPACE) and (self.__mario.jumping==False):
            self.__mario.when = pyxel.frame_count
            self.__mario.jump() 
    
        if (self.__mario.jumping==True) and (pyxel.frame_count-self.__mario.when==10):
            self.__mario.unjump()
    
    ##BArrel movement
    def moveBarril(self, b):
        #piso1
        if b.posy==self.__pisos[0] and abs(b.posx - constants.WIDTH)>16:
            b.move()
            if (b.posx==224) or (b.posx==212 and random.randint(1,3)==1) or (b.posx==60 and random.randint(1,3)==1):
                b.fall()
        elif b.falling and (b.posy<self.__pisos[1]):
            b.fall()
        #piso2
        elif b.posy==self.__pisos[1] and abs(b.posx - constants.WIDTH)<232:
            b.move()
            if (b.posx==8) or (b.posx==15 and random.randint(1,3)==1) or (b.posx==142 and random.randint(1,3)==1):
                b.fall()
        elif b.falling and (b.posy<self.__pisos[2]):
            b.fall()
         #piso3
        elif b.posy==self.__pisos[2] and abs(b.posx - constants.WIDTH)>16:
            b.move()
            if (b.posx==224) or (b.posx==60 and random.randint(1,3)==1):
                b.fall()
        elif b.falling and (b.posy<self.__pisos[3]):
            b.fall()
         #piso4
        elif b.posy==self.__pisos[3] and abs(b.posx - constants.WIDTH)<200:
            b.move()
            if (b.posx==60):
                b.fall()
        elif b.falling and (b.posy<230) or (b.posx==142 and random.randint(1,3)==1):
            b.fall()
        elif b.posy==230:
            self.__listbarriles.remove(b)
        else:
            self.__listbarriles.remove(b)


    def update(self):
        print(self.__points)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        else:
            #Mario movement
            self.moveMario(self.__mario.posx,self.__mario.posy)
            self.__mario.fall()
            #Add barrels
            if len(self.__listbarriles) < 10:
                if pyxel.frame_count%40==0 and random.randint(0,300)<150:
                    self.__listbarriles.append(barriles.barriles(constants.BARRILES_X, constants.BARRILES_Y))
            
            for b in self.__listbarriles:
                self.moveBarril(b)
                #Mario getting hit
                if (self.__mario.posx - b.posx) in range(-12, 0) and (self.__mario.posy - b.posy) in range(-15,-4):
                    self.__mario.death()
                    self.__listlives.pop()
                #Points for jumping barrels
                if (self.__mario.posx- b.posx) in range(-12,5) and (self.__mario.posy - b.posy) in range(-25,-15):
                    self.__points += 100
                    
            if pyxel.frame_count%50==0:
                self.__bonus-=250    
            
        
    def draw(self):
        
        pyxel.cls(0)
        
        #Ganar
        if (71 < self.__mario.posx and self.__mario.posx < 90) and (self.__mario.posy == 6):
            #self.__points= self.__points + self.__bonus
            pyxel.cls(12)
            #Mario
            pyxel.blt(119, 85, 0, 4, 32, 14, 15, colkey=0)        
            #Petra
            pyxel.blt(90, 77, 0, 5, 178, 16, 23, colkey=0)
            #Corazon
            pyxel.blt(110, 68, 0, 191, 180, 15, 13, colkey=0)
            #Suelo
            for i in range(0, constants.WIDTH, 7):
                pyxel.blt(0 + i, 100, 0, 0, 8, 7, 7, colkey = 0)
            #Good job
            pyxel.blt(95, 120, 1, 0, 0, 38, 32, colkey = 0)
            #Score
            #pyxel.text(100, 10, "FINAL SCORE: " + str(self.__points), pyxel.frame_count % 16)
                    
        #Game over
        elif self.__mario.lives == 0:
            pyxel.blt(90, 90, 2, 0, 0, 73, 48, colkey=0)
            pyxel.text(170, 220, "Press Q to exit" , 7)
            
        else:
            #score
            pyxel.text(140, 1, "SCORE: " + str(self.__points), pyxel.frame_count % 16)
            
            #fuego
            pyxel.blt(0, 216, 0, 8, 0, 16, 16, colkey=0)  
            pyxel.blt(0, 200, 0, 54, 0, 16, 16, colkey=0)  
            
            #bonus
            pyxel.blt(196,1,0,181,100,43,19)
            pyxel.text(208, 10, str(self.__bonus), 12)
            
            #Kong
            K = pyxel.frame_count%25
            if K in range (0,10):
                pyxel.blt(self.__kong.posx, self.__kong.posy+1, 0, 4, 58, 41, 32, colkey=0)  
            elif K in range (10, 20):
                pyxel.blt(self.__kong.posx, self.__kong.posy+1, 0, 151, 58, 45, 35, colkey=0)
            else:
                pyxel.blt(self.__kong.posx, self.__kong.posy+1, 0, 151, 58, -45, 35, colkey=0)
     
            
            #Petra
            P = pyxel.frame_count%25
            if P in range (0, 10):
                pyxel.blt(self.__petra.posx, self.__petra.posy, 0, 5, 178, 16, 23, colkey=0)   
            elif P in range(10, 20):
                pyxel.blt(self.__petra.posx, self.__petra.posy, 0, 31, 179, 15, 22, colkey=0)
            else:
                pyxel.blt(self.__petra.posx, self.__petra.posy, 0, 54, 179, 16, 22, colkey=0)
                   
            
            #Lives
            for li in self.__listlives:
                pyxel.blt(li.posx, li.posy, 0, 191, 180, 15, 13, colkey=0)
            
            #Floors
            for f in self.__allfloors:
                pyxel.blt(f.posx, f.posy, 0, 0, 0, 7, 7, colkey=0)  
            
            #Plataforma de Kong 
            for i in range(0, 56, 7):
                pyxel.blt(self.__platform.posx + i, self.__platform.posy - 118, 0, 0, 8, 7, 7, colkey = 0 )
                
            #Ladders
            for l in self.__all_ladders:
                pyxel.blt(l.posx, l.posy, 0, 0, 18, 8, 5, colkey=0)
            
            #Barrel
            pyxel.blt(self.__barrel.posx, self.__barrel.posy,0, 12,103,10,16)
            
            #MARIO    
            if self.__mario.direction=="left":      
                A=pyxel.frame_count%20
                if A in range(0,10):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 29, 32, 15, 16, colkey=0)
                elif A in range(10,21):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 53, 33, 15, 15, colkey=0)
                else:
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 4, 32, 14, 15, colkey=0)
            elif pyxel.btn(pyxel.KEY_UP):      
                A=pyxel.frame_count%10
                if A in range(0,6):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 76, 31, 15, 17, colkey=0)
                elif A in range(5,11):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 76, 31, -15, 17, colkey=0)
                else:    
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 76, 31, 15, 17, colkey=0)
            elif pyxel.btn(pyxel.KEY_DOWN):      
                A=pyxel.frame_count%10
                if A in range(0,6):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 76, 31, 15, 17, colkey=0)
                elif A in range(5,11):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 76, 31, -15, 17, colkey=0)
                else:    
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 76, 31, 15, 17, colkey=0) 
            else:
                A=pyxel.frame_count%20
                if A in range(0,10):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 29, 32, -15, 16, colkey=0)
                elif A in range(10,21):
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 53, 33, -15, 15, colkey=0)
                else:
                    pyxel.blt(self.__mario.posx, self.__mario.posy, 0, 4, 32, -14, 15, colkey=0)        
            
            #Barriles moviles
            for i in self.__listbarriles:
                A=pyxel.frame_count%20
                if i.falling== False:
                    if A in range(0,10):
                       pyxel.blt(i.posx, i.posy, 0, 35, 106, 12, 10, colkey = 0 )
                    else:
                        pyxel.blt(i.posx, i.posy, 0, 35, 106, -12, 10, colkey = 0 )
                else:
                    if A in range(0,10):
                       pyxel.blt(i.posx, i.posy, 0, 129, 106, 16, 10, colkey = 0 )
                    else:
                        pyxel.blt(i.posx, i.posy, 0, 153, 106, -16, 10, colkey = 0 )

    listbarriles=[barriles.barriles(constants.BARRILES_X, constants.BARRILES_Y)]
    

    
game()