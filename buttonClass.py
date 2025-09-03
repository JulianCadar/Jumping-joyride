import pygame
from pygame.locals import *
display = pygame.display.set_mode((1200,1000))
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
#is used to draw buttons on screen
    def draw(self,display):
        action = False
#get the mouse's position
        mousePositon = pygame.mouse.get_pos()
#check if the mouse is touching a button on screen and  clicking it
        if self.rect.collidepoint(mousePositon):
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False:
#check if the mouse is clicked or not
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False
#draw buttons on screen
        display.blit(self.image, (self.rect.x, self.rect.y))
        return action