import pygame
import random
import time
import math

HEIGHT = 400
WIDTH = 400


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

grids = []
openSet = []
closedSet = []
cameFrom = []
path = []

rows = 20
columns = 20

def heuristic(neighbor, end):
    #return (math.sqrt(pow(abs(neighbor.row - end.row), 2) + pow(abs(neighbor.column - end.column), 2)))
    return abs(neighbor.row - end.row) + abs(neighbor.column - end.column)
class cell():
    def __init__(self):
        self.f = 0
        self.g = 0
        self.h = 0
        self.rect = 0
        self.row = 0
        self.column = 0
        self.neighbors = []
        self.previous = None
        self.block = False

    def show(self, row, column, rowBlockSize, ColumnBlockSize):
        self.row = row
        self.column = column
        self.rect = pygame.Rect(row*rowBlockSize, column*ColumnBlockSize, rowBlockSize, ColumnBlockSize)
        pygame.draw.rect(display, black, self.rect, 1)
        if(random.random() < 0.2):
            self.block = True
            pygame.draw.rect(display, black, self.rect, 0)

    def update(self, color):
        pygame.draw.rect(display, color, self.rect, 0)

    def findNeighbors(self):
        if(self.row < rows - 1):
            self.neighbors.append(grids[self.row + 1][self.column])
            # if (self.column < columns - 1):
            #     self.neighbors.append(grids[self.row + 1][self.column + 1])
            # if (self.column > 0):
            #     self.neighbors.append(grids[self.row + 1][self.column - 1])
        if(self.column < columns - 1):
            self.neighbors.append(grids[self.row][self.column + 1])
        if(self.column > 0):
            self.neighbors.append(grids[self.row][self.column - 1])
            # if (self.column < columns - 1):
            #     self.neighbors.append(grids[self.row - 1][self.column + 1])
            # if (self.column > 0):
            #     self.neighbors.append(grids[self.row - 1][self.column - 1])
        if(self.row > 0):
            self.neighbors.append(grids[self.row - 1][self.column])

pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(white)

def createGrid(rows_num, columns_num):
    for i in range(rows_num):
        columns = []
        for j in range(columns_num):
            columns.append(cell())
        grids.append(columns)

def main():

    createGrid(rows,columns)

    start = grids[0][0]
    end = grids[rows - 1][columns - 1]

    openSet.append(start)

    for i in range(rows):
        for j in range(columns):
            grids[i][j].show(i, j, int(WIDTH / rows), int(HEIGHT / columns))

    for i in range(rows):
        for j in range(columns):
            grids[i][j].findNeighbors()

    if start.block:
        start.block = False
        start.update(white)
    if end.block:
        end.block = False
        end.update(white)

    while True:

        if len(openSet) > 0:
            lowestF = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[lowestF].f:
                    lowestF = i

            current = openSet[lowestF]
            if current == end:
                print("Done")
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()


            openSet.remove(current)
            closedSet.append(current)

            neighbors = current.neighbors
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                if(not(neighbor in closedSet) and neighbor.block == False):
                    tempG = current.g + 1

                    if(neighbor in openSet):
                        if(tempG < neighbor.g):
                            neighbor.g = tempG

                    else:
                        neighbor.g = tempG
                        openSet.append(neighbor)

                    neighbor.h = heuristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current

                    temp = current
                    path = []
                    path.append(temp)
                    while temp.previous is not None:
                        path.append(temp.previous)
                        temp = temp.previous

        else:
            print("Path not found")
            return

        for i in range(len(openSet)):
            openSet[i].update(green)
        for i in range(len(closedSet)):
            closedSet[i].update(red)
        for i in range(len(path)):
            path[i].update(blue)


        #code


        pygame.display.update()
        #time.sleep(0.1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



if __name__ == "__main__":
    main()



