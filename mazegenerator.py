import numpy as np
from utils import manhattanDistance
from random import randrange

# all four possible dir of given cell
dirs = [[1, 0],[0, -1],[-1, 0],[0, 1]]

class MazeGenerator():
    # Provided cell, list of current walls, get the walls around the cells
    def getWalls(self, cell,walls):
        wallSet = set(walls)
        dirs = [[1, 0],[0, -1],[-1, 0],[0, 1]]
        wall = []
        # generate all four walls possible, only add ones which are  in the
        # walls list
        for dir in dirs:
            x = cell[0] + dir[0]
            y = cell[1] + dir[1]

            if (x, y) in wallSet:
                wall.append((x,y))
        return wall

    # Get neighbor cells from given a cell co-ordinate
    def getNeighborCells(self,cell, cells, maze):
        cellSet = set(cells)
        neighbors = []
        for dir in dirs:
            x = cell[0] + dir[0] * 2
            y = cell[1] + dir[1] * 2

            if (x, y) in cellSet and (x, y) not  in maze:
                neighbors.append((x,y))

        return neighbors


    # Provided a cell, get random closest cell to 'cell' in maze set
    def getClosestRandomCell(self, cell, maze):
        nei = []

        for mazeCell in maze:
            if mazeCell != cell and manhattanDistance(cell, mazeCell) == 2:
                nei.append(mazeCell)

        return nei[randrange(len(nei))]


    # method to remove wall between cell1  and cell2
    def removeWall(self,cell1, cell2, maze):
        # Wall is either on left or right side of cell1
        if cell1[0] == cell2[0]:
            x = cell1[0]
            # wall is on right side of cell1
            if cell1[1] < cell2[1]:
                y = cell1[1] + 1
            # wall on left side of cell1
            else:
                y = cell1[1] - 1

        # wall is either up or down of cell1
        else:
            y = cell1[1]
            # wall is on south of cell1
            if cell1[0] < cell2[0]:
                x = cell1[0] + 1
            # wall is on north of cell1
            else:
                x = cell1[0] - 1

        # convert the wall to cell by adding it to the maze
        maze.add((x,y))
        return (x,y)


    # Prim's Maze generator algorithm
    def prims_maze(self, w, h):
        def _prims_maze(w,h):
            grid = np.ones((w, h))
            cells = []
            walls = []
            for i in range(h):
                for j in range(w):
                    if i %  2 == 1  and j % 2 == 1:
                        grid[i, j] = 0
                        cells.append((i,j))
                    elif i != 0 and j != 0 and i != h - 1 and j != w - 1:
                        walls.append((i,j))

            return grid, cells, walls

        grid,cells, walls   = _prims_maze(w,h)

        maze = set()    # keeps track of valid cells in maze
        frontier = []   # unvisited cells


        initialCell = cells[randrange(len(cells))]
        frontier.extend(self.getNeighborCells(initialCell, cells, maze))
        maze.add(initialCell)

        while frontier:
            # get the random index from the frontier
            index = randrange(len(frontier))

            # get the random cell from frontier via random index
            randomFrontierCell = frontier[index]

            # Add the cell to maze
            maze.add(randomFrontierCell)

            # remove the cell from the frontier
            frontier.remove(randomFrontierCell)

            # Get Closest maze Cell to this cell to open path with
            # Breaks ties randomly
            openPathWith = self.getClosestRandomCell(randomFrontierCell, maze)

            # remove the wall between random cell from frontier and closest cell in maze
            self.removeWall(randomFrontierCell, openPathWith, maze)

            # add  all neighbors of random  cell to the frontier
            frontier.extend(self.getNeighborCells(randomFrontierCell, cells, maze))

        # construct the maze in 2d Array
        for cell in maze:
            grid[cell[0], cell[1]] = 0

        # Open Start and End of the grid
        grid[1,0] = 0
        grid[w-2, h-1] = 0

        # return the maze
        return grid
