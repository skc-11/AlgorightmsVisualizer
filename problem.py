import time

# This class represents the problem that pathfinding algorithm needs to solve
class Problem:
    # initialize the problem with grid, start cell, and goal cell
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.m = len(self.grid)
        self.n = len(self.grid[0])

    # increment the iter var by 1 to keep track of the stat
    def incrementIter(self):
        self.iter += 1

    # method to get the start sate of given problem
    def getStartState(self):
        # initialize the stat variables when this method is called
        self.iter = 0
        self.timeStart = time.process_time()
        self.expanded = 0

        return self.start

    # method to get the goal cell of the grid 
    def getGoal(self):
        return self.goal

    # method to check if the node is goal node for given problem
    def isGoal(self, node):
        res = self.goal == node

        # if it is goal record the end time of the search algorithm
        if res:
            self.timeEnd = time.process_time()
        return res

    # method to get the valid successor nodes of given pnode.
    def getSuccessors(self, pnode):
        # four possible directions from cell
        # (left, top, right, down)
        dirs = [[0,-1], [-1, 0],  [0,1], [1, 0]]
        x = pnode[0]
        y = pnode[1]
        successors = []
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if self._validCell(nx,ny):
                successors.append((nx,ny))

        # adjust the expanded nodes counter(used for stat purpose)
        self.expanded += 1

        return successors

    # checks if the cell is valid
    def _validCell(self, nx, ny):
        # check if the cell is within bound and cell is not a wall
        return nx >= 0 and nx < self.m and ny >= 0 and ny < self.n  and self.grid[nx, ny] == 0

    # Print the stat of this problems solutoin
    def print_stats(self):
        print("Total Time: %.4f" % (self.timeEnd - self.timeStart))
        print("Total Iteration: ", self.iter)
        print("Total Expanded Nodes: ", self.expanded)