import turtle
from collections import deque
from Model import *


def startGame():
    hanoiTower = HanoiTower()
    hanoiTower.drawHanoi(hanoiTower.t)
    hanoiTower.solveTower(3,hanoiTower.getTower(),0,2,1)
    turtle.done()

startGame()






