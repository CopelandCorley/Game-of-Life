#This is an implementation of Conway's Game of Life (CGoL) by Copeland Corley.

from random import choice
import copy

class Cell:
    def __init__(self):
        self.isAlive = choice([True, False])
        self.neighbor = {}

    #spawn cell and increment its neighbors' number of living neighbors 
    def spawn(self):
        for cell in self.neighbor:
            self.neighbor[cell].livingNeighbors += 1
        self.isAlive = True

    #kill cell and decrement its neighbors' number of living neighbors 
    def die(self):
        for cell in self.neighbor:
            self.neighbor[cell].livingNeighbors -= 1
        self.isAlive = False

class GameOfLife:
    def __init__(self, size):
        self.size = size
        self.initCells()

    #initialize array of cells
    def initCells(self):
        self.cells = [Cell() for x in range(self.size ** 2)]
        cells = self.cells
        size = self.size
        for i in range(size ** 2):
            thisCell = self.cells[i]
            #establish top, left, bottom, and right neighbor relationships between cells using neighbor-finding expressions
            thisCell.neighbor['top'] = cells[(size*(size-1)+i) % (size*size)]
            thisCell.neighbor['left'] = cells[size*((i//size)+1) - (size-i%size)%size -1]
            thisCell.neighbor['bottom'] = cells[(i+size)%(size*size)]
            thisCell.neighbor['right'] = cells[size*(i//size) + (i%size+1)%size]
            #start counting living neighbors
            thisCell.livingNeighbors = thisCell.neighbor['top'].isAlive + thisCell.neighbor['left'].isAlive + \
                                       thisCell.neighbor['bottom'].isAlive + thisCell.neighbor['right'].isAlive
        for i in range(size ** 2):
            thisCell = cells[i]
            #establish topleft, bottomleft, bottomright, and topright  neighbor relationship between cells
            thisCell.neighbor['topleft'] = thisCell.neighbor['left'].neighbor['top']
            thisCell.neighbor['bottomleft'] = thisCell.neighbor['left'].neighbor['bottom']
            thisCell.neighbor['bottomright'] = thisCell.neighbor['right'].neighbor['bottom']
            thisCell.neighbor['topright'] = thisCell.neighbor['right'].neighbor['top']
            #finish counting living neighbors
            thisCell.livingNeighbors += thisCell.neighbor['topleft'].isAlive + thisCell.neighbor['bottomleft'].isAlive + \
                                        thisCell.neighbor['bottomright'].isAlive + thisCell.neighbor['topright'].isAlive

    #move one step forward in the simulation
    def step(self):
        selfCopy = copy.deepcopy(self)
        for i in range(self.size ** 2):
            thisCell = self.cells[i]
            thisCellCopy = selfCopy.cells[i]
            if not (2 <= thisCellCopy.livingNeighbors <= 3) and thisCellCopy.isAlive:
                thisCell.die()
            elif thisCellCopy.livingNeighbors == 3 and not thisCellCopy.isAlive:
                thisCell.spawn()

    #return string representing grid of cells in simulation, o = live cell, _ = dead cell
    def toString(self):
        cellsString = ""
        for i in range(self.size ** 2):
            cellsString += "o " if self.cells[i].isAlive else "_ "
            if((i + 1) % self.size == 0):
                cellsString += "\n"
        return cellsString

###uncomment to test
##x = GameOfLife(10)
##print(x.toString())
##for i in range(100):
##    x.step()
##    print(x.toString())
