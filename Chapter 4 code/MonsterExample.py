# Main program for creating monsters 

import random

class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows  # save away
        self.nCols = nCols  # save away
        self.myRow = random.randrange(self.nRows) #chooses a random row
        self.myCol = random.randrange(self.nCols) #chooses a random col
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed) # chooses a speed
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed) # chooses a speed
        # maybe set a direction or other instance variables
        # like health, power, etc.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) %  self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols
    

N_MONSTERS = 20
N_ROWS = 1000
N_COLS = 1000
MAX_SPEED = 2


monsterList = []
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)   # create a monster
    monsterList.append(oMonster)

# Later, when playing the game ...

for oMonster in monsterList:
    oMonster.move()
