from numpy.core.shape_base import block
import pygame
import searchalgo
from problem import Problem
import sys
from mazegenerator import MazeGenerator



BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)
YELLOW = (255,255,0)
RED = (255, 0 ,0)


WINDOW_HEIGHT = 780
WINDOW_WIDTH = 780
colors = [BLACK, WHITE, GREEN, BLUE]

# Main function to draw the search algorithm result
def main(grid, solution, expanded):
    global SCREEN, CLOCK

    # Initialize the pygame object with screen and clock
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    # Draw the initial maze
    drawGrid(grid)

    # Draw the search algorithm solution
    i, j = 0, 0
    clock=pygame.time.Clock()
    while True:
        # first draw the search algorith step by step
        if i < len(expanded):
            drawCells(expanded[i])
            i += 1

        # if algorithm is finished draw the final solution path
        if i == len(expanded) and j < len(solution):
            drawPath(solution[j])
            j+=1

        # Quit the pygame event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the display
        pygame.display.update()
        clock.tick(60)

# Funciton to draw the final solution path
def drawPath(cell):
    blockSize = 20
    if cell is not (0,0)  and cell is not (39,39):
        x = cell[1]
        y = cell[0]
        rect = pygame.Rect(x*blockSize, y*blockSize,
                            blockSize, blockSize)
        pygame.draw.rect(SCREEN, GREEN, rect)



# Draw modified cells 
# Draws the single step of the search algorithm according to the historyEntry
def drawCells(historyEntry):
    currNode, seen, discovered = historyEntry
    blockSize = 20

    #  Draw seen and current node
    for (y, x) in seen:
        rect = pygame.Rect(x*blockSize, y*blockSize,
                            blockSize, blockSize)
        pygame.draw.rect(SCREEN, BLUE, rect)

    # Draw current discovery
    for (y, x) in discovered:
        rect = pygame.Rect(x*blockSize, y*blockSize,
                            blockSize, blockSize)
        if (y,  x) is not currNode and (y, x ) not in seen:
            pygame.draw.rect(SCREEN, RED, rect)

    #Draw the current cell yellow
    x = currNode[1]
    y = currNode[0]
    rect = pygame.Rect(x*blockSize, y*blockSize,
                        blockSize, blockSize)
    pygame.draw.rect(SCREEN, YELLOW, rect)

    # draw the start cell
    rect = pygame.Rect(0, 1 * blockSize,blockSize, blockSize)
    pygame.draw.rect(SCREEN, GREEN, rect)

# Draw Initial Grid
def drawGrid(grid):
    blockSize = 20 #Set the size of the grid block
    for x in range(WINDOW_WIDTH // blockSize):
        for y in range(WINDOW_HEIGHT // blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            if grid[y,x] == 0:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect)

    
if __name__ == '__main__':
    start = (1, 0)
    end = (37,38)
    grid  = MazeGenerator().prims_maze(39, 39)


    prob = Problem(grid,start, end)
    solution, expanded =  searchalgo.astar(problem=prob) 

    prob.print_stats()

    main(grid, solution, expanded[1:])
