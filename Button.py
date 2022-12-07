import pygame
import sys

pygame.init()

arialfont = pygame.font.SysFont('arial', 30)

class Button():

    def __init__(self, text):
        self.colorone = arialfont.render(text, 0, (0,0,0))
        self.colortwo = arialfont.render(text, 0, (0,0,255))

    #set coords
    def setCords(self,x,y):
        self.cord = (x,y)

    #set dimentions
    def setrangeEnd(self, rangeEndX, rangeEndY):
        self.rangeX, self.rangeY = rangeEndX, rangeEndY

    #draw de bottom in the window
    def draw(self, window, pos):
        if pos[0] in range(self.cord[0], self.cord[0] + self.rangeX) and pos[1] in range(self.cord[1], self.cord[1] + self.rangeY):
            window.blit(self.colortwo, self.cord)
        else:
            window.blit(self.colorone, self.cord)

    #get if button presed 
    def pressed(self, pos):
        if pos[0] in range(self.cord[0], self.cord[0] + self.rangeX) and pos[1] in range(self.cord[1], self.cord[1] + self.rangeY):
            return True
        else:
            return False
