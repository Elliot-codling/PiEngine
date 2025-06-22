import pygame
from .vector import *
from .sharedObjectClass import *
# Initialise font
pygame.font.init()

class transform:
    def setPosition(self, position: vector2f) -> None:
        self.m_position = position

    def incrementPosition(self, position: vector2f) -> None:
        self.m_position += position

    def getPosition(self) -> vector2f:
        return self.m_position

    def getSize(self) -> vector2i:
        return vector2i(self.m_texture.get_width(), self.m_texture.get_height())

class textObject(sharedData, transform):
    # === Define text object ===
    def __init__(self, objectID: str, message: str, position: vector2f, fontSize: int, textColor = (255, 255, 255), layer = 0) -> "textObject":
        super().__init__()
        self.setID(objectID)
        self.m_text = message
        self.m_position = position
        self.m_color = textColor
        self.setLayer(layer)

        self.m_font = pygame.font.SysFont(None, fontSize)
        self.m_texture = self.m_font.render(message, True, pygame.Color(textColor))
    
        self.initialiseObject()

    def replaceText(self, message: str) -> None:
        self.m_texture = self.m_font.render(message, True, pygame.Color(self.m_color))
    # === Render text ===
    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.m_texture, [self.m_position.x, self.m_position.y])
