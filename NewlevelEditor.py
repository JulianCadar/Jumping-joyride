import pygame
from buttonClass import Button
from pygame.locals import *
import os
from playerClass import Player
pygame.init()
with open("signedInAs.txt", "r") as usernameFile:
    if usernameFile.read() == "":
        os.startfile("loginGui.py")
        quit()
running = True
playButtonImage = pygame.image.load('images/buttons/new_play_button.PNG').convert_alpha()
playButtonImage = pygame.transform.scale(playButtonImage,(100,100))
playbutton = Button(920,600,playButtonImage)
errorFont = pygame.font.SysFont("arial",25)
#display varaibles
displayWidth = 900
displayHeight = 900
sideMargin = 300
defaultTileSize = (20,20)
tileTypes = 9
currentTile = 0
display = pygame.display.set_mode((displayWidth + sideMargin, displayHeight))
pygame.display.set_caption('Level editor')
rows = 45
collumns = 45
tileSize = 20
backButtonImage = pygame.image.load("images/buttons/BackButton.PNG")
backButtonImage = pygame.transform.scale(backButtonImage,(50,50))
backButton = Button(975,825,backButtonImage)
clearGridImage = pygame.image.load("images/buttons/ClearGrid.png")
clearGridImage = pygame.transform.scale(clearGridImage,(100,50))
clearGridButton = Button(975,540,clearGridImage)
#scrolling variables
#create empty tile list
levelData = []
for row in range(rows):
    levelRow = [-1]*collumns
    levelData.append(levelRow)
# for row in range(rows):
#     levelRow = [-1]*collumns
#     levelData.append(levelRow)

#background
background = pygame.image.load('images/background.png').convert_alpha()
background = pygame.transform.scale(background, (900 , 900))
def drawBackground():
    backgroundWidth = background.get_width()
    for i in range(5):
        display.blit(background, ((i*backgroundWidth), 0))
#grid
def drawGrid():
    #vertical lines
    for y in range(collumns+1):
        pygame.draw.line(display, (255,255,255), (y*tileSize, 0), (y*tileSize, displayHeight))
    #horizontal lines
    for x in range(rows+1):
        pygame.draw.line(display, (255,255,255), (0, x*tileSize), (displayWidth, x*tileSize))
#drawing level tiles
def drawLevel():
    for y, row in enumerate(levelData):
        for x,tile in enumerate(row):
            if tile >= 0:
                display.blit(tileList[tile], (x*tileSize, y*tileSize))
#loading and scaling game tiles
tileList = []
for x in range(tileTypes):
    tile = pygame.image.load(f'images/tiles/{x}.PNG').convert_alpha()
    tile = pygame.transform.scale(tile, defaultTileSize)
    tileList.append(tile)
#create buttons
#make button list
buttonList = []
buttonRow = 0
buttonCollumn = 0
#import previous tile list button
importPrev = pygame.image.load("images/buttons/ImportPreviousTileList.png")
importPrev = pygame.transform.scale(importPrev,(175,75))
importPrevButton = Button(displayWidth+50,450,importPrev)
for i in range(len(tileList)):
    tileButton = Button(displayWidth + (75*buttonCollumn) + 50, (75*buttonRow) + 50, tileList[i])
    buttonList.append(tileButton)
    buttonCollumn +=1
    if buttonCollumn == 3:
        buttonRow +=1
        buttonCollumn =0
while running:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #add new tiles to the screen
    #get mouse pos
    
    mousePos = pygame.mouse.get_pos()
    x = (mousePos[0])//tileSize
    y = mousePos[1]//tileSize
    #check if co-ordinate of mouse position is in the grid
    if mousePos[0]<displayWidth and mousePos[1]<displayHeight:
        #update tile value
        if pygame.mouse.get_pressed()[0]:
            if levelData[y][x] != currentTile:
                levelData[y][x] = currentTile
        if pygame.mouse.get_pressed()[2]:
            levelData[y][x] = -1
    drawBackground()
    drawGrid()
    drawLevel()
    
    #draw a panel for tiles, and draw the tiles themselves
    pygame.draw.rect(display, (174, 198, 207), Rect(displayWidth,0,sideMargin,displayHeight))
    #choose a tile
    buttonCount =0
    for buttonCount, button in enumerate(buttonList):
        if button.draw(display):
            currentTile = buttonCount
    #highlight selected tile
    #clear grid button
    if clearGridButton.draw(display):
        levelData = [[-1 for i in range(rows)] for i in range(collumns)]
    pygame.draw.rect(display, (255,0,0), buttonList[currentTile].rect,3)
    #import previously stored tile list
    if importPrevButton.draw(display):
        from leveldatatext import levelData
    #test level
    if playbutton.draw(display):
        for levelRow in levelData:
            if 7 in levelRow:
                with open("leveldatatext.py","w") as file:
                    file.write(f"levelData = {levelData}")
                os.startfile("leveltester.py")
                quit()
        else:
            Player.drawtext("Level needs an end jewel",errorFont,(255,0,0),200,450)
    if backButton.draw(display):
        os.startfile("mainMenu.py")
        quit()
    
    pygame.display.update()  
print(levelData)
pygame.quit()