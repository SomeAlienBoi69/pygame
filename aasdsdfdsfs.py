import pygame
import datetime
pygame.init()
#----------------classes-------------------#
class GameObject:
    def __init__(self,x,y,color):
        self.__x = x
        self.__y = y
        self._color = color
    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x = x
    def gety(self):
        return self.__y
    def sety(self,y):
        self.__y = y
class Frame(GameObject):
    def __init__(self,x,y,color,endx,endy):
        super().__init__(x,y,color)
        self.__x = x
        self.__y = y
        self._endx = endx
        self._endy = endy
    def draw(self):
        self.diffrencex = self._endx - self.__x
        self.diffrencey = self._endy - self.__y
        self.diffrence_x = self.diffrencex * -1
        self.diffrence_y = self.diffrencey * -1
        pygame.draw.rect(screen,self._color,(self.getx(),self.gety(),self.diffrencex,2))
        pygame.draw.rect(screen,self._color,(self.getx(),self.gety(),2,self.diffrencey))

        pygame.draw.rect(screen,self._color,(self._endx,self._endy + self.diffrence_y,2,self.diffrencey))
        pygame.draw.rect(screen,self._color,(self._endx + self.diffrence_x,self._endy,self.diffrencex,2))
class Unit(GameObject):
    def __init__(self,x,y,color):
        super().__init__(x,y,color) 
        self._x = x
        self._y = y
    def move(self,x,y):
        self._difx = self.getx() - x
        self._dify = self.gety() - y
        self.setx(self.getx() - self._difx)
        self.sety(self.gety() - self._dify)
        print(self._x,self._y)
    def draw(self):
        pygame.draw.circle(screen,self._color,(self.getx(),self.gety()),10,10)


class ArmourPiercingDiscardingSabotFinStabilizedHighExplosiveGeneralPurposeSquashHeadAntiTankUngeneralPurposeAntiPersonelBalisticAntiAircraftIntercontidentalAlienDestroyingWiktorRound:
    pass
#--------------------------------------------#


#------------------colors-----------------------#
orange = (204,102,0)
reb = (200,0,0)
black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
bright_red = (255,0,0)
limon = (0,255,0)
#-----------------------------------------------#
clock = pygame.time.Clock()
res = (1000, 1000)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("coh12")



unit = Unit(250,250,reb)

def maingame():
    running = True
    drag = False
    holdx = 0
    holdy = 0
        
    file = open("abcd.txt", "a")
    data = datetime.datetime.now()
    date = data.strftime("%Y-%m-%d %H:%M:%S")

    file.write("Game opened on: " + date + "\n")
    file.close()

    while running:
        h = list(pygame.mouse.get_pos())
        x = h[0]
        y = h[1]

        screen.fill(limon)
 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                file = open("abcd.txt", "a")
                file.write("Game closed on: " + date + "\n" + "\n")
                file.close()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = True
                holdx = h[0]
                holdy = h[1]
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    unit.move(x,y)


        if drag == True:
            frame = Frame(holdx,holdy,reb,x,y)
            frame.draw()
        

        

        unit.draw()
        
        pygame.display.flip()
        clock.tick(300)
        


        #print(x , y)
        #print(drag)
        #print(holdx, holdy)










maingame()