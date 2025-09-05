import pygame
from pygame.locals import *
import datetime
from levelClass import Level
pygame.init()
defaultPlayerSize = (25,25)
currentDate = datetime.datetime.now()
import sqlite3
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()
speedx = 5
speedy = 13
display = pygame.display.set_mode((900,900))
font = pygame.font.SysFont("arialblack",25)
sprite = ""


class Player:

    @staticmethod
    def drawtext(text, font, textcolour, x, y):
        txt = font.render(text, True, textcolour)
        display.blit(txt, (x,y))
    def __init__(self,x,y):    
        self.moneySound = pygame.mixer.Sound("sounds/coin_2-89099.mp3")
        self.jumpSound = pygame.mixer.Sound("sounds/maro-jump-sound-effect_1.mp3")
        self.levelCompleteSound = pygame.mixer.Sound("sounds/mixkit-game-level-completed-2059.wav")

        self.moneySound.set_volume(0.05)
        self.jumpSound.set_volume(0.05)
        self.startx = x
        self.starty = y
        with open("selectedsprite.txt","r") as file:
            sprite = file.read()
        sprite = int(sprite)
        username = ""
        with open("signedInAs.txt","r") as file:
            username = file.read()
        moneyArr = []
        for row in cursor.execute("SELECT CurrentBalance FROM Ownership WHERE Username = ?",(username,)):
            moneyArr.append(row)
        playerImage = pygame.image.load(f"images/playerSprites/{sprite}.PNG").convert_alpha()
        self.playerImage = pygame.transform.scale(playerImage,defaultPlayerSize)
        self.playerRect = self.playerImage.get_rect()
        self.playerRect.x = x
        self.playerRect.y = y
        self.speedX = speedx
        self.speedY = 0
        self.playerWidth = self.playerImage.get_width()
        self.playerHeight = self.playerImage.get_height()
        self.jumping = False
        self.money = int(moneyArr[-1][0])
        self.colliding = False
        self.levelCompleted = False
        
    def update(self,levelObject:Level):        
        #get key presses
        userInput = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if userInput[pygame.K_RIGHT] or userInput[pygame.K_d]:
            if self.playerRect.x <875:
                if self.levelCompleted == False:
                    dx += self.speedX
        if userInput[pygame.K_LEFT] or userInput[pygame.K_a]:
            if self.playerRect.x > 0:
                if self.levelCompleted == False:
                    dx -= self.speedX
        #make sure that the player doesnt leave the top of the window:
        if self.playerRect.y < 0:
            self.playerRect.y +=speedy

        #add gravity
        self.speedY+=1
        if self.speedY >speedy:
            self.speedY = speedy
        dy +=self.speedY
        #check for collisions
        #grass tile collision
        for grassTile in levelObject.grassTileList:
            #x collision
            if grassTile[1].colliderect(self.playerRect.x + dx,self.playerRect.y,self.playerWidth,self.playerHeight):
                dx = 0
            # y direction collision
            if grassTile[1].colliderect(self.playerRect.x,self.playerRect.y + dy,self.playerWidth,self.playerHeight):
                #check if it is a downwards collision or an upwards collision
                #upwards collision
                if self.speedY < 0:
                    dy = grassTile[1].bottom - self.playerRect.top
                    self.speedY = 0
                #downwards collision
                elif self.speedY >=0:
                    dy = grassTile[1].top - self.playerRect.bottom
        #dirt tile collision
        for dirtTile in levelObject.dirtTileList:
            if dirtTile[1].colliderect(self.playerRect.x + dx,self.playerRect.y,self.playerWidth,self.playerHeight):
                dx = 0
            # y direction collision
            if dirtTile[1].colliderect(self.playerRect.x,self.playerRect.y + dy,self.playerWidth,self.playerHeight):
                #check if it is a downwards collision or an upwards collision
                #upwards collision
                if self.speedY < 0:
                    dy = dirtTile[1].bottom - self.playerRect.top
                    self.speedY = 0
                #downwards collision
                elif self.speedY >=0:
                    dy = dirtTile[1].top - self.playerRect.bottom
        for stoneTile in levelObject.stoneTileList:
            if stoneTile[1].colliderect(self.playerRect.x + dx,self.playerRect.y,self.playerWidth,self.playerHeight):
                dx = 0
            # y direction collision
            if stoneTile[1].colliderect(self.playerRect.x,self.playerRect.y + dy,self.playerWidth,self.playerHeight):
                #check if it is a downwards collision or an upwards collision
                #upwards collision
                if self.speedY < 0:
                    dy = stoneTile[1].bottom - self.playerRect.top
                    self.speedY = 0
                #downwards collision
                elif self.speedY >=0:
                    dy = stoneTile[1].top - self.playerRect.bottom
        for sandTile in levelObject.sandTileList:
            if sandTile[1].colliderect(self.playerRect.x + dx,self.playerRect.y,self.playerWidth,self.playerHeight):
                dx = 0
            # y direction collision
            if sandTile[1].colliderect(self.playerRect.x,self.playerRect.y + dy,self.playerWidth,self.playerHeight):
                #check if it is a downwards collision or an upwards collision
                #upwards collision
                if self.speedY < 0:
                    dy = sandTile[1].bottom - self.playerRect.top
                    self.speedY = 0
                #downwards collision
                elif self.speedY >=0:
                    dy = sandTile[1].top - self.playerRect.bottom
        for moneyTile in levelObject.moneyTileList:
            if moneyTile[1].colliderect(self.playerRect):
                #when the player touches a piece of money, it collects it and the money is gone, therefore we need to update that both onscreen and in the money tile list
                levelObject.moneyTileList.remove(moneyTile)
                levelObject.tileList.remove(moneyTile)
                self.money += 25
                self.moneySound.play()
        for lavaTile in levelObject.lavaTileList:
            #lava kills you instantly, resets your position, takes 1000 of your money, and doesnt reset the money back to where it used to be, in the future i will add a deathscreen
            if lavaTile[1].colliderect(self.playerRect):
                self.playerRect.x = self.startx
                self.playerRect.y = self.starty
                dx,dy = 0,0
                if self.money >= 250:
                    self.money -= 250
                else:
                    self.money =0
        #in the future i will add a way to register level completion completely, but this is fine for now
        for levelEndTile in levelObject.levelEndTileList:
            if levelEndTile[1].colliderect(self.playerRect):
                self.money +=1000
                self.levelCompleteSound.play()
                self.levelCompleted = True
                username = ""
                with open("signedInAs.txt","r") as file:
                    username = file.read()
                levelObject.levelEndTileList.remove(levelEndTile)
                levelObject.tileList.remove(levelEndTile)
                lastLevelCompleted = ''
                with open("lastLevelCompleted.txt","r") as file:
                    lastLevelCompleted = file.read()
                cursor.execute("INSERT OR REPLACE INTO Progress VALUES(?,?,?)",(username,f"Level {lastLevelCompleted}",currentDate))
                connection.commit()
                iconsOwned = []
                for row in cursor.execute("SELECT ItemOwned FROM Ownership WHERE Username = ?",(username,)):
                    iconsOwned.append(row)
                lastOwnedIcons = []
                for row in iconsOwned[-1]:
                    lastOwnedIcons.append(row)
                lastOwnedIconsString = "".join(set(lastOwnedIcons))
                cursor.execute("INSERT OR REPLACE INTO Ownership VALUES(?,?,?,?)",(username,lastOwnedIconsString,currentDate,str(self.money)))
                connection.commit()
                
        #water makes you bounce up a little bit
        for waterTile in levelObject.waterTileList:
            if waterTile[1].colliderect(self.playerRect):
                dy = -20
        
        #slime will act like a trapdoor that pulls you down like the black orb from geometry dash
        for slimeTile in levelObject.slimeTileList:
            if slimeTile[1].colliderect(self.playerRect.x + dx,self.playerRect.y,self.playerWidth,self.playerHeight):
                dx = 0
                self.speedY += -40
            # y direction collision
            if slimeTile[1].colliderect(self.playerRect.x,self.playerRect.y + dy,self.playerWidth,self.playerHeight):
                #check if it is a downwards collision or an upwards collision
                #upwards collision
                if self.speedY < 0:
                    dy = slimeTile[1].bottom - self.playerRect.top
                    self.speedY = 0
                #downwards collision
                elif self.speedY >=0:
                    self.speedY += -40
        #gravity
        if self.playerRect.bottom > 900:
            self.playerRect.bottom = 900
            dy = 0
        #update onscreen player position
        self.playerRect.x += dx
        self.playerRect.y += dy
        #jumping code 
        if userInput[pygame.K_SPACE] and self.jumping == False and dy == 0 and self.levelCompleted == False:
            self.jumping = True
            self.speedY = -speedy
            self.jumpSound.play()
        if userInput[pygame.K_SPACE] == False:
            self.jumping = False
        #render player
        display.blit(self.playerImage,(self.playerRect.x,self.playerRect.y))
        #display how much money the player has
        Player.drawtext(f"Money: {self.money}",font,(0,0,0),400,30)