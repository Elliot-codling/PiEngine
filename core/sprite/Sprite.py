# Sprite file used to handle sprites

# === External libs ===
import pygame
from typing import Union
# === Inherited classes ===
from ..sprite.Transform import *
from ..sprite.Collision import *
# === Internal classes ===
from ..vector.Vector import *
from ..sharedObjectClass.SharedObjectClass import *
from ..window.Application import *
from ..storage.SSP import loadImage 
from ..log.Logger import *

# TODO LIST:
# - Add animation:
# Use a json file instead and just point to where the file is for each frame. Example:
# {
#   {
#       "textureFile": "file"
#       "x": 10
#       "y": 10
#       "width": 64
#       "height": 64
#   }
# }
# Then with each, load the image, set the position and size
#
# Add the option to use a spritesheet instead:
# Use the same json file format however each textureFile must be the same file, in that case only load it once
# The width and height determines the size of the ALL frames
# The x and y will be disgarded
# When using spriteSheet, the colums and rows will have to be pre-determined in code
# Possibly the json file at the start could tell the program that its either a spritesheet or seperate images

    

class Sprite(Collision, Transform, SharedData):
    # === Define spriteObject ===
    def __init__(self, objectID: str, texture: Union[str, pygame.Surface], position: vector2f, size: vector2i, alpha = False, layer = 0) -> "Sprite":
        super().__init__()
        self.setID(objectID)
        # m_texture = current texture to render
        # c_texture = loaded texture
        # c_texture is only changed if a new texture has been loaded
        # c_texture does not change in any other 
        # m_texture is used for render, but can be replaced by rotations etc
        # rotations are based on c_texture but the output it stored to m_texture
        
        if type(texture) == str:
            self.m_texture = loadImage(texture)
            self.c_texture = self.m_texture
        else:
            self.m_texture = texture
            self.c_texture = texture
        
        if self.m_texture == None or self.c_texture == None:
            Logger.warn("sprite/Sprite", f"Sprite Object: '{self.getID()}' is not initialised")
            return None
        
        self.m_position = position
        self.m_size = size
        self.setLayer(layer)
        
        ## TODO: Complete origin calculations
        # Rotations
        self.m_rotation = 0
        self.m_origin = vector2i(0, 0)
        
        # Scale texture
        self.m_texture = pygame.transform.scale(self.m_texture, (size.x, size.y))
        self.c_texture = pygame.transform.scale(self.c_texture, (size.x, size.y))

        # Remove alpha of texture if alpha is false
        if not alpha:
            self.m_texture = self.m_texture.convert()
            self.c_texture = self.c_texture.convert()
            self.m_mask = None
        else:
            self.m_texture = self.m_texture.convert_alpha()
            self.c_texture = self.c_texture.convert_alpha()
            self.m_mask = pygame.mask.from_surface(self.m_texture)
        
        self.initialiseObject()

    # === Replace texture ===
    def replaceTexture(self, texture: Union[str, pygame.Surface], size: vector2f, alpha = False) -> None:
        # Check if 'newTexture' is a string or a loaded texture
        if type(texture) == str:
            newTexture = loadImage(texture)             
        else:
            newTexture = texture

        # Return and do not apply new texture if it could not be loaded
        if newTexture == None:
            return
        else:
            self.m_texture = newTexture
        
        self.m_texture = pygame.transform.scale(self.m_texture, (size.x, size.y))
        if not alpha:
            self.m_texture = self.m_texture.convert()    

        self.m_mask = pygame.mask.from_surface(self.m_texture)

    # === Render Object ===
    def render(self, surface: pygame.surface) -> None:
        surface.blit(self.m_texture, [self.m_position.x, self.m_position.y])
