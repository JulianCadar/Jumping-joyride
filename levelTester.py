import pygame
import os
from pygame.locals import *
from buttonClass import Button
from playerClass import Player
from levelClass import Level
from leveldatatext import levelData
level6 = Level(levelData)
speedx = 5
speedy = 13
playerX = 100
playerY = 850
player = Player(playerX,playerY)
running = True
clock = pygame.time.Clock()
FPS = 60
display = pygame.display.set_mode((900,900))
background = pygame.image.load("images/background.png").convert_alpha()
background = pygame.transform.scale(background,(900,900))
font = pygame.font.SysFont("arialblack",25)
pygame.display.set_caption("Test level")
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(50,50,backButtonImage)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.blit(background,(0,0))
    level6.draw()
    player.update(level6)
    if player.levelCompleted:
        Player.drawtext(f"Level Complete!",font,(0,0,0),100,450)
    if backButton.draw(display):
        os.startfile("NewLevelEditor.py")
        quit()
    clock.tick(60)
    pygame.display.update()