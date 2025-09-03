import pygame
from pygame.locals import *
display = pygame.display.set_mode((1000,1000))
defaultTileSize = (20,20)
class Level:
    def __init__(self,data):
        dirt = pygame.image.load('images/tiles/0.png').convert_alpha()
        grass = pygame.image.load('images/tiles/1.png').convert_alpha()
        stone = pygame.image.load('images/tiles/2.png').convert_alpha()
        lava = pygame.image.load('images/tiles/3.png').convert_alpha()
        water = pygame.image.load('images/tiles/4.png').convert_alpha()
        sand = pygame.image.load('images/tiles/5.png').convert_alpha()
        slime = pygame.image.load('images/tiles/6.png').convert_alpha()
        levelEnd = pygame.image.load('images/tiles/7.png').convert_alpha()
        money = pygame.image.load('images/tiles/8.png').convert_alpha()
        rowCounter = 0
        self.tileList = []
        self.grassTileList = []
        self.dirtTileList = []
        self.stoneTileList = []
        self.lavaTileList = []
        self.waterTileList = []
        self.sandTileList = []
        self.slimeTileList = []
        self.levelEndTileList = []
        self.moneyTileList = []
        for row in data:
            columnCounter = 0
            for tile in row:
                if  tile ==0:
                    dirtImage = pygame.transform.scale(dirt, defaultTileSize)
                    dirtImageRect = dirtImage.get_rect()
                    dirtImageRect.x = columnCounter*20
                    dirtImageRect.y = rowCounter*20
                    dirtTile = (dirtImage,dirtImageRect)
                    self.tileList.append(dirtTile)
                    self.dirtTileList.append(dirtTile)
                if tile ==1:
                    grassImage = pygame.transform.scale(grass , defaultTileSize)
                    grassImageRect = grassImage.get_rect()
                    grassImageRect.x = columnCounter*20
                    grassImageRect.y = rowCounter*20
                    grassTile = (grassImage,grassImageRect)
                    self.tileList.append(grassTile)
                    self.grassTileList.append(grassTile)
                if tile ==2:
                    stoneImage = pygame.transform.scale(stone , defaultTileSize)
                    stoneImageRect = stoneImage.get_rect()
                    stoneImageRect.x = columnCounter*20
                    stoneImageRect.y = rowCounter*20
                    stoneTile = (stoneImage,stoneImageRect)
                    self.tileList.append(stoneTile)
                    self.stoneTileList.append(stoneTile)
                if tile == 3:
                    lavaImage = pygame.transform.scale(lava , defaultTileSize)
                    lavaImageRect = lavaImage.get_rect()
                    lavaImageRect.x = columnCounter*20
                    lavaImageRect.y = rowCounter*20
                    lavaTile = (lavaImage,lavaImageRect)
                    self.tileList.append(lavaTile)
                    self.lavaTileList.append(lavaTile)
                if tile ==4:
                    waterImage = pygame.transform.scale(water , defaultTileSize)
                    waterImageRect = waterImage.get_rect()
                    waterImageRect.x = columnCounter*20
                    waterImageRect.y = rowCounter*20
                    waterTile = (waterImage,waterImageRect)
                    self.tileList.append(waterTile)
                    self.waterTileList.append(waterTile)
                if tile ==5:
                    sandImage = pygame.transform.scale(sand, defaultTileSize)
                    sandImageRect = sandImage.get_rect()
                    sandImageRect.x = columnCounter*20
                    sandImageRect.y = rowCounter*20
                    sandTile = (sandImage,sandImageRect)
                    self.tileList.append(sandTile)
                    self.sandTileList.append(sandTile)
                if tile ==6:
                    slimeImage = pygame.transform.scale(slime , defaultTileSize)
                    slimeImageRect = slimeImage.get_rect()
                    slimeImageRect.x = columnCounter*20
                    slimeImageRect.y = rowCounter*20
                    slimeTile = (slimeImage,slimeImageRect)
                    self.tileList.append(slimeTile)
                    self.slimeTileList.append(slimeTile)
                if tile==7:
                    levelEndImage = pygame.transform.scale(levelEnd , defaultTileSize)
                    levelEndImageRect = levelEndImage.get_rect()
                    levelEndImageRect.x = columnCounter*20
                    levelEndImageRect.y = rowCounter*20
                    levelEndTile = (levelEndImage,levelEndImageRect)
                    self.tileList.append(levelEndTile)
                    self.levelEndTileList.append(levelEndTile)
                if tile ==8:
                    moneyImage = pygame.transform.scale(money , defaultTileSize)
                    moneyImageRect = moneyImage.get_rect()
                    moneyImageRect.x = columnCounter*20
                    moneyImageRect.y = rowCounter*20
                    moneyTile = (moneyImage,moneyImageRect)
                    self.tileList.append(moneyTile)
                    self.moneyTileList.append(moneyTile)
                columnCounter +=1
            rowCounter +=1
    def draw(self):
        for tile in self.tileList:
            display.blit(tile[0],tile[1])