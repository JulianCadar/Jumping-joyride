import pygame
from pygame.locals import *
from buttonClass import Button
import os
pygame.init()
#background and display
displayWidth = 1600
displayHeight = 900
background = pygame.image.load("images/new_bg.PNG").convert_alpha()
pygame.display.set_caption("Easy Levels")
background = pygame.transform.scale(background,(displayWidth,displayHeight))
display = pygame.display.set_mode((displayWidth,displayHeight))
running = True
#button images loading
defaultButtonSize = (75,75)
L1Button = pygame.image.load("images/buttons/Level1.PNG").convert_alpha()
L2Button = pygame.image.load("images/buttons/Level2.PNG").convert_alpha()
L3Button = pygame.image.load("images/buttons/Level3.PNG").convert_alpha()
L4Button = pygame.image.load("images/buttons/Level4.PNG").convert_alpha()
L5Button = pygame.image.load("images/buttons/Level5.PNG").convert_alpha()
L6Button = pygame.image.load("images/buttons/Level6.PNG").convert_alpha()
L7Button = pygame.image.load("images/buttons/Level7.PNG").convert_alpha()
L8Button = pygame.image.load("images/buttons/Level8.PNG").convert_alpha()
L9Button = pygame.image.load("images/buttons/Level9.PNG").convert_alpha()
L10Button = pygame.image.load("images/buttons/Level10.PNG").convert_alpha()
#scaling
L1Button = pygame.transform.scale(L1Button,defaultButtonSize)
L2Button = pygame.transform.scale(L2Button,defaultButtonSize)
L3Button = pygame.transform.scale(L3Button,defaultButtonSize)
L4Button = pygame.transform.scale(L4Button,defaultButtonSize)
L5Button = pygame.transform.scale(L5Button,defaultButtonSize)
L6Button = pygame.transform.scale(L6Button,defaultButtonSize)
L7Button = pygame.transform.scale(L7Button,defaultButtonSize)
L8Button = pygame.transform.scale(L8Button,defaultButtonSize)
L9Button = pygame.transform.scale(L9Button,defaultButtonSize)
L10Button = pygame.transform.scale(L10Button,defaultButtonSize)
#button object creation
Level1Button = Button(300,450,L1Button)
Level2Button = Button(400,450,L2Button)
Level3Button = Button(500,450,L3Button)
Level4Button = Button(600,450,L4Button)
Level5Button = Button(700,450,L5Button)
Level6Button = Button(800,450,L6Button)
Level7Button = Button(900,450,L7Button)
Level8Button = Button(1000,450,L8Button)
Level9Button = Button(1100,450,L9Button)
Level10Button = Button(1200,450,L10Button)
#back button
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(50,50,backButtonImage)
while running:
    display.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #button drawing
    if Level1Button.draw(display):
        os.startfile("mediumlevel1.py")
        quit()
    if Level2Button.draw(display):
        os.startfile('mediumlevel2.py')
        quit()
    if Level3Button.draw(display):
        os.startfile('mediumlevel3.py')
        quit()
    if Level4Button.draw(display):
        os.startfile('mediumlevel4.py')
        quit()
    if Level5Button.draw(display):
        os.startfile('mediumlevel5.py')
        quit()
    if Level6Button.draw(display):
        os.startfile('mediumlevel6.py')
        quit()
    if Level7Button.draw(display):
        os.startfile('mediumlevel7.py')
        quit()
    if Level8Button.draw(display):
        os.startfile('mediumlevel8.py')
        quit()
    if Level9Button.draw(display):
        os.startfile('mediumlevel9.py')
        quit()
    if Level10Button.draw(display):
        os.startfile('mediumlevel10.py')
        quit()
    if backButton.draw(display):
        os.startfile("leveldifficultyselector.py")
        quit()
    pygame.display.update()
pygame.quit()