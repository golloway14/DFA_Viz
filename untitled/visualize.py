__author__ = 'Peck'

import pygame
import sys

SPOTS = [(0, 2), (4, 2), (2, 0), (2, 4), (1, 3), (3, 1), (1, 1), (3, 3)]

class Visualizer(object):
    def __init__(self):
        pygame.init()
        size = (600, 600) #(width, height)
        self.screen = pygame.display.set_mode(size)
        self.states = [0, 4, 4, 3, 1, 5, 2]
        self.state = 0
        self.phase = 0

    def drawDFA(self, dfa, screen):
        screen.fill((0, 0, 0))
        for x in range(len(dfa)):
            if self.states[self.state] == x:
                pygame.draw.rect(screen, pygame.Color(255, 1, 85), (SPOTS[x][0]*125 - 10, SPOTS[x][1]*125- 10, 120, 120), 0)
            pygame.draw.rect(screen, pygame.Color(1, 85, 255), (SPOTS[x][0]*125, SPOTS[x][1]*125, 100, 100), 0)
            font = pygame.font.SysFont("Courier", 25)
            text = font.render(str(x), 1, (0, 0, 0))
            screen.blit(text, (SPOTS[x][0]*125, SPOTS[x][1]*125))

        self.drawString("samw","i","segamgee")

    def drawString(self, begin, read, end):
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(self.screen, color, (110, 250, 380, 100), 0)

        font = pygame.font.SysFont("Courier", 17)
        text = font.render(begin, 1, (0, 0, 0))
        self.screen.blit(text, (110, 250))

        text = font.render(read, 1, (255, 0, 0))
        self.screen.blit(text, (110, 290))

        text = font.render(end, 1, (0, 0, 0))
        self.screen.blit(text, (110, 330))
        pygame.display.update()

    def visualize(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.state += 1

            self.drawDFA([1, 1, 1, 1, 1, 1, 1], self.screen)
            pygame.display.flip()

a = Visualizer()
a.visualize()
