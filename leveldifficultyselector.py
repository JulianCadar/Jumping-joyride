import pygame
from pygame.locals import *
from buttonClass import Button
import os
#display variables
displayWidth = 1600
displayHeight = 900
display = pygame.display.set_mode((displayWidth,displayHeight))
caption = pygame.display.set_caption("Level Difficulty Selector")
#game loop running variable
running = True
#load button images
easyLevelButton = pygame.image.load("images/buttons/easyLevelButton.PNG").convert_alpha()
mediumLevelButton = pygame.image.load("images/buttons/mediumLevelButton.PNG").convert_alpha()
hardLevelButton = pygame.image.load("images/buttons/hardLevelButton.PNG").convert_alpha()
expertLevelButton = pygame.image.load("images/buttons/expertLevelButtons.PNG").convert_alpha()
#scale button images correctly
easyLevelButton = pygame.transform.scale(easyLevelButton, (200, 150))
mediumLevelButton = pygame.transform.scale(mediumLevelButton, (200, 150))
hardLevelButton = pygame.transform.scale(hardLevelButton, (200, 150))
expertLevelButton = pygame.transform.scale(expertLevelButton, (200, 150))
#load and scale background image
background = pygame.image.load("images/new_bg.png")
background = pygame.transform.scale(background, (displayWidth, displayHeight))
#create button objects
easyLevels = Button(400, 400, easyLevelButton)
mediumLevels = Button(700, 400, mediumLevelButton)
hardLevels = Button(1000, 400, hardLevelButton)
expertLevels = Button(1300, 400, expertLevelButton)
#back button
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(50,50,backButtonImage)
while running:
    display.blit(background,(0,0))
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw buttons and check for clicks
    if easyLevels.draw(display):
        os.startfile("easyLevelSelector.py")
        quit()
    if mediumLevels.draw(display):
        os.startfile('mediumlevelselector.py')
        quit()
    if hardLevels.draw(display):
        pass
    if expertLevels.draw(display):
        pass
    if backButton.draw(display):
        os.startfile("mainMenu.py")
        quit()
    pygame.display.update()
