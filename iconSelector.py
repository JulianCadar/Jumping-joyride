import pygame
from pygame.locals import *
import os
import sqlite3
from buttonClass import Button
from playerClass import Player
connection = sqlite3.connect("userdata.db")
font = pygame.font.SysFont("arial",75)
regularfont = pygame.font.SysFont("arial",25)
cursor = connection.cursor()
iconsOwned = []
username = ""
display = pygame.display.set_mode((900,900))
pygame.display.set_caption("Icon selector")
background = pygame.image.load("images/new_bg.PNG")
background = pygame.transform.scale(background,(900,900))
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(50,50,backButtonImage)
with open("signedInAs.txt","r") as file:
    username = file.read()
#get owned icons
iconsOwned = []
for row in cursor.execute("SELECT ItemOwned FROM Ownership WHERE Username = ?",(username,)):
    iconsOwned.append(row)
lastOwnedIcons = []
for row in iconsOwned[-1]:
    lastOwnedIcons.append(row)
lastOwnedIconsString = lastOwnedIcons[-1]
#if user doesnt have anything, we give them the standard icon
if lastOwnedIconsString == "":
    lastOwnedIconsString+= "1"
running = True
print(lastOwnedIconsString)
#icon images
#buy buttons and icon images
numberOfIcons = len(lastOwnedIcons[0])
width = 400 / numberOfIcons
iconSize = (100,100)
iconImages = []
for i in lastOwnedIconsString:
    icon = pygame.image.load(f"images/playerSprites/{i}.PNG")
    icon = pygame.transform.scale(icon,(50,50))
    iconImages.append(icon)
buyButtonImage = pygame.image.load("images/buttons/Select.PNG")
buyButtonImage = pygame.transform.scale(buyButtonImage,(100,50))

helperArray = []


for i,icon in enumerate(lastOwnedIconsString):
    selectButton = Button(110*i+20,575,buyButtonImage)
    helperArray.append((selectButton,icon))
while running:
    display.blit(background,(0,0))
    if backButton.draw(display):
        os.startfile("mainMenu.py")
        quit()
    
    for i,iconImage in enumerate(iconImages):
        display.blit(iconImage,(i*110 + 40,500))
    for buttonAndIcon in helperArray:
        #button is held in index 0, icon is held in index 1
        
        #draw buttons
        if buttonAndIcon[0].draw(display):
            with open("selectedsprite.txt","w") as file:
                file.write(buttonAndIcon[1])
            helperArray.remove(buttonAndIcon)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    