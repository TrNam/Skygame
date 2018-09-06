import sys
import pygame
from constants import *
from block import Block
from bomb import Bomb
from building import Building


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption('Bomber')

    block = Block(screen, 40, 40, 0, SCREEN_HEIGHT // 8)
    bomb = Bomb(screen, 10, 10, block.x_pos, block.y_pos + 10)


    for i in range(len(BUILDING_TUPLE)):
        building = Building(screen, BUILDING_TUPLE[i][0], BUILDING_TUPLE[i][1], BUILDING_TUPLE[i][2])
        building.draw()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        block.move()
        block.speed()

        bomb.move(block)

        pygame.display.update()


main()
