import pygame
from constants import *
from block import Block
from building import Building

class Bomb:

    def __init__(self, screen, width, height, x_pos, y_pos):
        self.screen = screen
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.whitebomb = pygame.Surface((width, height))
        self.whitebomb.fill(WHITE)
        self.bomb = pygame.Surface((width, height))
        self.bomb.fill(BLUE)

    def draw(self):
        self.screen.blit(self.bomb, (self.x_pos, self.y_pos))
        return

    def erase(self):
        self.screen.blit(self.whitebomb, (self.x_pos, self.y_pos))
        return

    def move(self, plane):
        keys = pygame.key.get_pressed()
        self.erase()
        if keys[pygame.K_SPACE]:
            self.y_pos += 1
        else:
            self.x_pos = plane.x_pos + 15
            self.y_pos = plane.y_pos + 40
        self.draw()
        return

    def explode(self, building):
        if self.y_pos == building.height:
            self.erase()
        return

    def drop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.erase()
            self.y_pos += 1
            self.draw()
        return