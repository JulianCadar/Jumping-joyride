import pygame
import os
from pygame.locals import *
from buttonClass import Button
from playerClass import Player
import sqlite3 
import datetime
pygame.init()
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()
font = pygame.font.SysFont("arial",25)
display = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Shop")
running = True
money = 0
#background image
background = pygame.image.load("images/shop_bg.png")
background = pygame.transform.scale(background,(1200,900))
#get user balance and username
username = ""
with open("signedInAs.txt","r") as file:
    username = file.read()
    if username == "":
        os.startfile("loginGui.py")
        quit()
moneyArr = []
for row in cursor.execute("SELECT CurrentBalance FROM Ownership WHERE Username = ?", (username,)):
    moneyArr.append(row)
money = int(moneyArr[-1][0])
# back button
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(50,50,backButtonImage)
#get icons owned
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
#icon images
#buy buttons and icon images
numberOfIcons = 8
iconSize = (100,100)
iconImages = []
for i in range(1,numberOfIcons+1):
    icon = pygame.image.load(f"images/playerSprites/{i}.PNG")
    icon = pygame.transform.scale(icon,iconSize)
    iconImages.append(icon)
buyButtonImage = pygame.image.load("images/buttons/buyButton.PNG")
buyButtonImage = pygame.transform.scale(buyButtonImage,(100,50))

helperArray = []

unOwnedIcons = []
for character in "12345678":
    if not character in lastOwnedIconsString:
        unOwnedIcons.append(character)

unOwnedIconsString = "".join(unOwnedIcons)

for i,icon in enumerate(unOwnedIconsString):
    buyButton = Button(125*i + 150,575,buyButtonImage)
    helperArray.append((buyButton,icon))


#game loop
while running:  

    display.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
    for i,icon in enumerate(unOwnedIcons):
        Player.drawtext("5000",font,(255,255,255),125*i + 175,550)
        display.blit(iconImages[int(icon)-1],(125*i+150,450))
    
    for i,buttonAndIcon in enumerate(helperArray):
        if buttonAndIcon[0].draw(display):
            if money <50:
                Player.drawtext("Not enough money",font,(255,0,0),450,700)
            else:
                money -=50
                lastOwnedIconsString +=buttonAndIcon[1]
                cursor.execute("INSERT OR REPLACE INTO Ownership VALUES(?,?,?,?)",(username,lastOwnedIconsString,str(datetime.datetime.now()),money))
                connection.commit()
                helperArray.remove(buttonAndIcon)         

    
    if backButton.draw(display):
        os.startfile("mainmenu.py")
        running = False
    
    Player.drawtext(f"Money: {money}",font,(0,0,0),300,100)
    pygame.display.update()
