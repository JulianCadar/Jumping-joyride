import pygame
from pygame.locals import *
from buttonClass import Button
import os
pygame.init()
#pygame window settings
displayWidth = 1600
displayHeight = 900
display = pygame.display.set_mode((displayWidth, displayHeight))
name = pygame.display.set_caption('Main Menu')
signedinfont = pygame.font.SysFont("arial",20)
#colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
defaultButtonSize = (100,50)
background = pygame.image.load('images/new_bg.PNG').convert_alpha()
background = pygame.transform.scale(background, (displayWidth, displayHeight))
#button images
optionsButton = pygame.image.load('images/buttons/new_options_button.png').convert_alpha()
optionsButton = pygame.transform.scale(optionsButton,defaultButtonSize)
playButton = pygame.image.load('images/buttons/new_play_button.PNG').convert_alpha()
playButton = pygame.transform.scale(playButton,defaultButtonSize)
skinsButton = pygame.image.load('images/buttons/new_skins_button.PNG').convert_alpha()
skinsButton = pygame.transform.scale(skinsButton,defaultButtonSize)
infoButton = pygame.image.load('images/buttons/info_button.png').convert_alpha()
infoButton = pygame.transform.scale(infoButton,defaultButtonSize)
editButton = pygame.image.load("images/buttons/editIcon.png").convert_alpha()
editButton = pygame.transform.scale(editButton,defaultButtonSize)
accountDeactivateButton = pygame.image.load("images/buttons/deactivateAccountButton.PNG")
accountDeactivateButton = pygame.transform.scale(accountDeactivateButton,(150,100))
#button objects
play_button = Button(800,450, playButton)
options_button = Button(500,450 ,optionsButton)
skins_button = Button(1000, 450, skinsButton)
info_button = Button(1200, 100, infoButton)
edit_button = Button(1500,800,editButton)
account_deactivate_button = Button(1350,100,accountDeactivateButton)
game_paused = False
#get username
username = ""
with open("signedInAs.txt","r") as file:
    username=file.read()
    if username == "":
        os.startfile("loginGui.py")
        quit()
#back button
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(50,50,backButtonImage)
#game loop
running = True
while running: 
    display.blit(background, (0,0))
    font = pygame.font.SysFont('arialblack',50)
    textcolour = white
    def drawtext(text, font, textcolour, x, y):
        txt = font.render(text, True, textcolour)
        display.blit(txt, (x,y))
    
    #drawing the buttons
    if game_paused == True:
        drawtext(f"Signed in as: {username}",signedinfont,(0,0,255),100,800)
        if play_button.draw(display):
            os.startfile("leveldifficultyselector.py")
            quit()
        if options_button.draw(display):
            os.startfile("iconSelector.py")
            quit()
        if skins_button.draw(display):
            os.startfile("shop.py")
            quit()
        if info_button.draw(display):
            os.startfile("infoGui.py")
            quit()
        if edit_button.draw(display):
            os.startfile("NewlevelEditor.py")
            quit()
        if backButton.draw(display):
            with open("signedInAs.txt","w") as file:
                file.write("")
            os.startfile("signin.py")
            quit()
        if account_deactivate_button.draw(display):
            os.startfile("accountDeactivator.py")
            quit()
    else:
#draws text that appears when the game is first ran
        drawtext('Press SPACE to continue', font, textcolour, 500,400)
#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
    userInput = pygame.mouse.get_pressed()
#the button towards main levels
    pygame.display.update()
pygame.quit()
