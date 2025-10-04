# === External libs ===
import pygame
# === Inherited classes ===
# === Internal classes ===
from ..vector.Vector import *

# === Transform the object ===
class Transform:
    # === Origin ===
    def setOrigin(self, position: vector2i) -> None:
        self.m_origin = position

    # === Rotation (clockwise) ===
    def setAngle(self, angle: float) -> None:
        self.m_texture = pygame.transform.rotate(self.c_texture, -angle)
        self.m_rotation = angle

        self.m_mask = pygame.mask.from_surface(self.m_texture)
    
    def incrementAngle(self, angle: float) -> None:
        self.m_rotation += angle
        self.m_texture = pygame.transform.rotate(self.c_texture, -self.m_rotation)

        self.m_mask = pygame.mask.from_surface(self.m_texture)
    
    # === Transform positions ===
    def setPosition(self, position: vector2f) -> None:
        self.m_position = position
        
    def incrementPosition(self, position: vector2f) -> None:
        self.m_position += position

    def getPosition(self) -> vector2f:
        return self.m_position
    
    # === Sizes ===
    def setSize(self, size: vector2i) -> None:
        self.m_size = size
        self.m_texture = pygame.transform.scale(self.m_texture, (size.x, size.y))
        self.c_texture = pygame.transform.scale(self.c_texture, (size.x, size.y))
        
    def getSize(self) -> vector2i:
        return vector2i(self.m_texture.get_rect().right, self.m_texture.get_rect().bottom)
