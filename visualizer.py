import pygame
import searchalgo
import utils
from problem import Problem
import numpy as np
import sys
from random import randrange



BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
colors = [BLACK, WHITE, GREEN, BLUE]

def main(solution, expanded):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    drawGrid()

    i = 1
    drawExpansion = [expanded[0]]
    clock=pygame.time.Clock()

    while True:
        drawCell(drawExpansion)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        if  i < len(expanded):
            drawExpansion.append(expanded[i])
            i += 1
        #clock.tick(60)

# Draw modified cells
def drawCell(cells):
    blockSize = 20
    for (x, y) in cells:
        rect = pygame.Rect(x*blockSize, y*blockSize,
                            blockSize, blockSize)
        pygame.draw.rect(SCREEN, BLUE, rect)

# Draw Initial Grid
def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

        


if __name__ == '__main__':
    start = (0,0)
    end = (39,39)
    prob = Problem(np.zeros((40,40)),start, end)
    solution, expanded =  searchalgo.bfs(problem=prob) 
    main(solution, expanded)
