from graphics import *
from random import *
from math import sqrt
import time

'''def Openscene(win,x,y,open1,open2,open3):
        open1_filename = open1 
        open1_image = Image(Point(x, y),open1_filename )
        open1_image.draw(win)
        time.sleep(3)
        open1_image.undraw()
        open2_filename = open2 
        open2_image = Image(Point(x, y),open2_filename )
        open2_image.draw(win)
        time.sleep(8)
        open2_image.undraw()
        open3_filename = open2 
        open3_image = Image(Point(x, y),open3_filename )
        open3_image.draw(win)
        time.sleep(2)
        open3_image.undraw()'''
        

        
        
        
        

class Lola:
    def __init__(self, win, center1, distance1,speed1,jumpHeight1,LolaRadius):
        self.center=center1
        self.x, self.y= center1.getX(), center1.getY()
        self.speed= speed1
        self.distance= distance1
        self.jumpHeight=jumpHeight1
        self.LolaRadius=LolaRadius
        self.Lola=Circle(self.center,LolaRadius)
        self.Lola.draw(win)
                       
    #following functions changes some values for this object
    def accelerate(self,speedValue):
        self.speed= self.speed+speedValue
    def decelerate(self,speedValue):
        self.speed= self.speed-speedValue
    def changeDistance(self,distance):
        self.distance= self.distance + distance

        
    #not sure if the undraw here is going to work or not
    def jump(self):
        self.Lola.undraw(win)
        self.y=self.y+self.jumpHeight
        self.center=Point(self.x, self.y)
        self.Lola=Circle(self.center,LolaRadius)
        self.Lola.draw(win)
               
    def land(self):
        self.Lola.undraw(win)
        self.y=self.y-self.jumpHeight
        self.center=Point(self.x, self.y)
        self.Lola=Circle(self.center,LolaRadius)
        self.Lola.draw(win)

        
    def collisionChecker(self,centerOfObject,radiusOfObject):
        #centerOfObject should be the coordinate of the object on the graph
        #return True if collision happened
        x, y= centerOfObject.getX(), centerOfObject.getY()
        d=self.LolaRadius()+radiusOfObject
        seperation=sqrt((self.x-x)**2+(self.y-y)**2)
        if (seperation<d):
            return True
        else:
            return False
        
    #following functions returns values for this object
    def getSpeed(self):
        return self.speed
    def getCenter(self):
        return self.center
    def getDistance(self):
        return self.distance
    
class BgAndObj:
    def __init__(self, win, speed, BgCenter, objRadius, numberOfObjects,w,
                 BgPicName):
        #w stands for the setting for the coordinate
        #BgPicName is supposed to be the name of the Image
        self.speed=speed
        self.BgX, self.BgY=BgCenter.getX(),BgCenter.getY()
        self.BgCenter=BgCenter
        self.objRadius=objRadius
        self.ObjCenters=[]
        self.BgImage=Image(BgCenter,BgPicName)
        self.parts=[]
        self.parts.append(self.BgImage)
        #using random function to distributes those objects
        for i in range(numberOfObjects):
            #generate object centers
            ObjCenter=Point(randint(-w,w),randint(-w,w))
            self.ObjCenters.append(ObjCenter)
            ObjCircle=Circle(ObjCenter,objRadius)
            #put object generated in self.parts
            self.parts.append(ObjCircle)
        #draw object
        for part in self.parts:
            part.draw(win)
        
    def getBgCenter(self):
        return self.BgCenter
    def getObjRadius(self):
        return self.objRadius
    def getSpeed(self):
        return self.speed
    
    #return the center of each object as a list
    def getCentersForObjects(self):
        return self.ObjCenters

    #move background and all of the objects 
    def MoveDisp( self, dx, dy ):
        '''Move BgAndObj by dx,dy, just like move()'''
        for part in self.parts:
            part.move( dx, dy )

        # Must update instance var:
        self.BgX,self.BgY = self.BgX+dx, self.BgY+dy
        self.BgCenter = Point(self.BgX,self.BgY)
        for ObjCenter in self.ObjCenters:
            x,y=ObjCenter.getX(),ObjCenter.getY()
            newX, newY=x+dx, y+dy
            ObjCenter=Point(newX,newY)

 
        
def main():
    win = GraphWin( 'Run, Lola, run', 800, 500, autoflush=False )
    win.setBackground( 'cornflower blue' )
    w = 100
    win.setCoords( -w, -w, w, w )
    #Openscene(win,400,250,"open1.gif","open2.gif","open1.gif")
    

    initialSpeed=10
    BgCenter=Point(0,0)
    objRadius=4
    numberOfObjects=3
    BgPicName=""
    gif=[]
    gif1=Image(Point(0,0), "lola1.gif")
    gif2=Image(Point(0,0), "lola2.gif")
    gif3=Image(Point(0,0), "lola3.gif")
    gif4=Image(Point(0,0), "lola4.gif")
    gif.append(gif1)
    gif.append(gif2)
    gif.append(gif3)
    gif.append(gif4)
    number=0
    BgCenter=Point(0,0)
    BgPicName="setting1.gif"
    speed=2
    n=0
    
    while (n<15):
        
        bgAndObj=BgAndObj(win, speed, BgCenter, objRadius, numberOfObjects,w,
                 BgPicName)
        bgAndObj.MoveDisp( -5, 0 )

        #Lola's gif      
        '''gif[number].draw(win)
        time.sleep(1)
        gif[number].undraw()
        gif[number+1].draw(win)
        time.sleep(1)
        gif[number+1].undraw()'''
        gif1=Image(Point(0,0), "lola1.gif")
        gif2=Image(Point(0,0), "lola2.gif")
        gif3=Image(Point(0,0), "lola3.gif")
        gif4=Image(Point(0,0), "lola4.gif")

        gif1.draw(win)
        update()
        time.sleep(0.05)
        gif1.undraw()
        gif2.draw(win)
        update()
        time.sleep(0.05)
        gif2.undraw()
        gif3.draw(win)
        update()
        time.sleep(0.05 )
        gif3.undraw()

        #lola collides with objects
        #open the game
        #pause while playing the typing game
        #get key
        #jump if space is pressed
        #time bar
        #progress bar
        n=n+1
main()
