
# This class represents the problem that pathfinding algorithm needs to solve
class Problem:
    # grid 0 is valid path, 1 is invalid path
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.m = len(self.grid)
        self.n = len(self.grid[0])

    def getStartState(self):
        return self.start

    def getGoal(self):
        return self.goal

    def isGoal(self, node):
        return self.goal == node

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
        return successors

    # checks if the cell is valid
    def _validCell(self, nx, ny):
        # check if the cell is within bound and cell is not a wall
        return nx >= 0 and nx < self.m and ny >= 0 and ny < self.n  and self.grid[nx, ny] == 0