__author__ = 'Peck'

import pygame
import sys

SPOTS = [(0, 2), (4, 2), (2, 0), (2, 4), (1, 3), (3, 1), (1, 1), (3, 3)]

class Visualizer(object):
    def __init__(self):
        pygame.init()
        size = (600, 600) #(width, height)
        self.screen = pygame.display.set_mode(size)
        self.states = [0, 4, 3, 7, 1, 5, 2, 6]
        self.state = 0
        self.result = ""
        self.complete = False
        self.string = ""
        self.index = 0

    def drawDFA(self, dfa, screen):
        screen.fill((0, 0, 0))
        for x in range(len(dfa)):
            if self.states[self.state] == x:
                pygame.draw.rect(screen, pygame.Color(255, 1, 85), (SPOTS[x][0]*125 - 10, SPOTS[x][1]*125- 10, 120, 120), 0)
            pygame.draw.rect(screen, pygame.Color(1, 85, 255), (SPOTS[x][0]*125, SPOTS[x][1]*125, 100, 100), 0)
            font = pygame.font.SysFont("Courier", 25)
            text = font.render(str(x), 1, (0, 0, 0))
            screen.blit(text, (SPOTS[x][0]*125, SPOTS[x][1]*125))

        self.procString(self.string)
        #self.drawString("samw","i","segamgee")

    def drawString(self, begin, read, end):
        color = pygame.Color(255, 255, 255)
        pygame.draw.rect(self.screen, color, (110, 250, 380, 100), 0)

        font = pygame.font.SysFont("Courier", 17)
        if self.state < (len(self.states) - 1):
            temp = "Read: " + begin
            text = font.render(temp, 1, (0, 0, 0))
            self.screen.blit(text, (110, 250))

            temp = "Reading: " + read
            text = font.render(temp, 1, (255, 0, 0))
            self.screen.blit(text, (110, 290))

            temp = "Unread: " + end
            text = font.render(temp, 1, (0, 0, 0))
            self.screen.blit(text, (110, 330))
        else:
            self.complete = True
            if self.result == "ACCEPT":
                text = font.render(self.result, 1, (0, 255, 0))
            else:
                text = font.render(self.result, 1, (255, 0, 0))
            self.screen.blit(text, (110, 250))
        pygame.display.update()

    def procString(self, string):
        if len(string) > self.index:
            self.drawString(string[0:self.index], string[self.index:self.index+1], string[self.index+1:len(string)])
        else:
            self.drawString("","","")

    def visualize(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.display.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.index += 1
                self.state += 1
                if self.state > len(self.states) -1:
                    self.state = 0

        self.drawDFA([1, 1, 1, 1, 1, 1, 1, 1], self.screen)
        pygame.display.flip()

