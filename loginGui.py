import pygame
from pygame.locals import *
from buttonClass import Button
import os
#display
display = pygame.display.set_mode((900,900))
pygame.display.set_caption("Login system")
background = pygame.image.load("images/new_bg.png").convert_alpha()
background = pygame.transform.scale(background,(900,900))
running = True
#button images
signUpButton = pygame.image.load("images/buttons/signUpButton.PNG").convert_alpha()
signUpButton = pygame.transform.scale(signUpButton,(200,100))
loginButton = pygame.image.load("images/buttons/loginButton.PNG").convert_alpha()
loginButton = pygame.transform.scale(loginButton,(200,100))
#button objects
sign_up_button = Button(250,400,signUpButton)
login_button = Button(550,400,loginButton)
#main loop
while running:
    display.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    with open("signedInAs.txt","r") as file:
        if file.read() == "":
            if sign_up_button.draw(display):
                running = False
                os.startfile("signup.py")
                quit()
            if login_button.draw(display):
                running = False
                os.startfile("signin.py")
                quit()
        else:
            os.startfile("mainMenu.py")
            quit()
    pygame.display.update()
pygame.quit()