__author__ = 'Peck'

import pygame
import sys

SPOTS = [(0, 2), (4, 2), (2, 0), (2, 4), (1, 3), (3, 1), (1, 1), (3, 3)]

class Visualizer(object):
    def __init__(self):
        pygame.init()
        size = (600, 600) #(width, height)
        self.screen = pygame.display.set_mode(size)
        self.state = 0

    def drawDFA(self, dfa, screen):
        screen.fill((0, 0, 0))
        for x in range(len(dfa)):
            if self.state == x:
                pygame.draw.rect(screen, pygame.Color(255, 1, 85), (SPOTS[x][0]*125 - 10, SPOTS[x][1]*125- 10, 120, 120), 0)
                print (self.state)
            pygame.draw.rect(screen, pygame.Color(1, 85, 255), (SPOTS[x][0]*125, SPOTS[x][1]*125, 100, 100), 0)

        pygame.display.update()

    def setState(self, val):
        self.state = val

a = Visualizer()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a.state = 6 - a.state
    a.drawDFA([1, 1, 1, 1, 1, 1, 1, 1],a.screen)