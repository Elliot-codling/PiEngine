from typing import Union
import pygame
from ..vector import *
from ..sprite.Sprite import *

class Scene:    
    def __init__(self, sceneName: str):
        self.m_sceneName = sceneName
        self.m_spriteList = []
        self.m_spriteRenderList = []
        self.m_textList = []

    def getSpriteQueue(self):
        return self.m_spriteList
    
    def getTextQueue(self):
        return self.m_textList
    
    def getSpriteRenderQueue(self):
        return self.m_spriteRenderList


    def createSprite(self, objectID: str, texture: Union[str, pygame.Surface], position: vector2f, size: vector2i, alpha = False, layer = 0) -> "Sprite":
        newSprite = Sprite(objectID, texture, position, size, alpha, layer)
        self.m_spriteList.append(newSprite)
        return newSprite


    def clearLayer(self, layerNumber: int) -> None:
        pass