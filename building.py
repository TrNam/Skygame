import pygame
from constants import *

class Building:
    def __init__(self, screen, start, height, end):
        self.screen = screen
        self.start = start
        self.height = height
        self.end = end


        self.building = pygame.Surface((end-start, height))
        self.building.fill(BLACK)
        return

    def draw(self):
        self.screen.blit(self.building, (self.start, SCREEN_HEIGHT-self.height))
        return