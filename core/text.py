import pygame
from .vector import *
from .sharedObjectClass import *

# Initialise font
pygame.font.init()
class textObject(sharedData):
    # === Define text object ===
    def __init__(self, objectID, message, position: vector2f, fontSize, textColor = (255, 255, 255), layer = 0):
        super().__init__()
        self.setID(objectID)
        self.m_text = message
        self.m_position = position
        self.m_color = textColor
        self.setLayer(layer)

        self.m_font = pygame.font.SysFont(None, fontSize)
        self.m_texture = self.m_font.render(message, True, pygame.Color(textColor))

        self.initialiseObject()

    def replaceText(self, message):
        self.m_texture = self.m_font.render(message, True, pygame.Color(self.m_color))
    # === Render text ===
    def render(self, surface):
        surface.blit(self.m_texture, [self.m_position.x, self.m_position.y])
