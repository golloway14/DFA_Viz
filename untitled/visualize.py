__author__ = 'Peck'

import pygame

SPOTS = [(0, 2), (4, 2), (2, 0), (2, 4), (1, 3), (3, 1), (1, 1), (3, 3)]

class Visualizer(object):
    def __init__(self):
        pygame.init()
        size = (600, 600) #(width, height)
        self.screen = pygame.display.set_mode(size)

    def drawDFA(self, dfa, screen):
        for x in range(len(dfa)):
            pygame.draw.rect(screen, pygame.Color(1, 85, 255), (SPOTS[x][0]*125, SPOTS[x][1]*125, 100, 100), 0)

        pygame.display.update()

a = Visualizer()

while True:
    a.drawDFA([1, 1, 1, 1, 1, 1, 1, 1],a.screen)