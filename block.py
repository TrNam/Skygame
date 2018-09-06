import pygame
from constants import *


class Block():

    _speed = 0.1

    def __init__(self, screen, width, height, initial_x, initial_y):
        self.screen = screen
        self.height = height
        self.width = width
        self.x_pos = initial_x
        self.y_pos = initial_y

        self.whiteblock = pygame.Surface((width, height))
        self.whiteblock.fill(WHITE)
        self.block = pygame.Surface((width, height))
        self.block.fill(RED)
        return

    def draw(self):
        self.screen.blit(self.block, (self.x_pos, self.y_pos))
        return

    def erase(self):
        self.screen.blit(self.whiteblock, (self.x_pos, self.y_pos))
        return

    def move(self):
        self.erase()
        self.x_pos += Block._speed
        if self.x_pos >= SCREEN_WIDTH:
            self.x_pos = 0
        elif self.x_pos <= -self.width:
            self.x_pos = SCREEN_WIDTH
        self.draw()
        return

    def follow(self, plane):
        self.erase()
        self.x_pos = plane.x_pos - self.x_pos
        self.y_pos = plane.y_pos - self.y_pos
        self.draw()
        return

    def speed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            Block._speed += 0.001
        if keys[pygame.K_a]:
            Block._speed -= 0.001
        return
