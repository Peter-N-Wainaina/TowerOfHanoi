from constants import *
from collections import deque
import time
import turtle



class Disk:
    def __init__(self,size):
        assert size >0
        self.size=size
    
    def getSize(self):
        return self.size
    
    def setCoords(self,coords):
        self.coords=coords
    
    def getCoords(self):
        return self.coords
    
    def drawDisk(self,t):
        coords=self.coords
        t.penup()
        t.goto(coords[0],coords[1])   #TODO: create a coords class
        t.pendown()
        t.forward(self.size)


class Peg:
    def __init__(self,base_coords,):
        self.base_coords=base_coords
        self.disks = deque()

    def removeDisk(self):
        return self.disks.pop()

    def addDisk(self,disk:Disk):
        factor =len(self.disks)
        disk_x = self.base_coords[0]+DISK_X_INC*factor
        disk_y = self.base_coords[1]+DISK_Y_INC*factor
        disk.setCoords((disk_x,disk_y))
        self.disks.append(disk)
    
    def getDisks(self):
        return self.disks


class HanoiTower:
    def __init__(self):
        #create pegs
        start_peg = Peg((-300,0))
        temp_peg = Peg((-100,0))
        final_peg = Peg((100,0)) 
        #create disk
        disk1 = Disk(90)
        disk2 = Disk(70)
        disk3 = Disk(50)
        #add disks to peg1
        start_peg.addDisk(disk1)
        start_peg.addDisk(disk2)
        start_peg.addDisk(disk3)
        self.hanoiTower = [start_peg,temp_peg,final_peg]
        self._createTurtle()
       
    def _createTurtle(self):
        self.t = turtle.Turtle()
        self.t.speed(PEN_SPEED)
        self.t.pencolor(DISK_COLOR)
        self.t.pensize(PEN_SIZE)
        self.t.hideturtle()

    def getTower(self):
        return self.hanoiTower
    
    def drawHanoi(self,t):
        t.clear()
        for peg in self.hanoiTower:
            if len(peg.disks)!=0:
                    for disk in peg.disks: 
                        disk.drawDisk(self.t)

    def moveDisk(self,hanoiTower,fromPeg:int,toPeg:int):
        time.sleep(DELAY_VIEW_SECONDS)
        disk = hanoiTower[fromPeg].removeDisk()
        hanoiTower[toPeg].addDisk(disk)
        self.drawHanoi(self.t)

    def solveTower(self,disks,hanoiTower,src,dest,temp):
        if disks == 1:
            self.moveDisk(hanoiTower,src,dest) 
        else:
            self.solveTower(disks - 1,hanoiTower, src, temp, dest)  
            self.moveDisk(hanoiTower,src,dest) 
            self.solveTower(disks - 1, hanoiTower,temp, dest, src) 
    