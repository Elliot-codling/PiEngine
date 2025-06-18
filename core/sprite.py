# Sprite file used to handle sprites

import pygame
from .vector import *
from .sharedObjectClass import *
from .window import *
from .ssp import loadImage
from .debugHandler import *

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

# === Transform the object ===
class transform:
    # === Origin ===
    def setOrigin(self, position: vector2i):
        self.m_origin = position

    # === Rotation (clockwise) ===
    def setAngle(self, angle: float):        
        self.m_texture = pygame.transform.rotate(self.c_texture, -angle)
        self.m_rotation = angle

        self.m_mask = pygame.mask.from_surface(self.m_texture)
    
    def incrementAngle(self, angle: float):
        self.m_rotation += angle
        self.m_texture = pygame.transform.rotate(self.c_texture, -self.m_rotation)

        self.m_mask = pygame.mask.from_surface(self.m_texture)
    
    # === Transform positions ===
    def setPosition(self, position: vector2f):
        self.m_position = position
        
    def incrementPosition(self, position: vector2f):
        self.m_position += position

    def getPosition(self):
        return self.m_position
    
    # === Sizes ===
    def setSize(self, size: vector2i):
        self.m_size = size
        self.m_texture = pygame.transform.scale(self.m_texture, (size.x, size.y))
        self.c_texture = pygame.transform.scale(self.c_texture, (size.x, size.y))
        
    def getSize(self):    
        return vector2f(self.m_texture.get_rect().right, self.m_texture.get_rect().bottom)


# === Flags return a true or false statement ===
class flags(transform):
    # === Check position of object compared to predefinied border ===
    def leftBorder(self, relativePosition: vector2i, borderLeft: int):
        return relativePosition.x >= borderLeft
    
    def rightBorder(self, relativePosition: vector2i, borderRight: int):
        return relativePosition.x <= borderRight
    
    def topBorder(self, relativePosition: vector2i, borderTop: int):
        return relativePosition.y >= borderTop
    
    def bottomBorder(self, relativePosition: vector2i, borderBottom: int):
        return relativePosition.y <= borderBottom
    
    # === Collision boxes ===
    # Return true if the current object collides with the object passed
    # Else return false
    def collideBoxByObject(self, object: "spriteObject"):        
        if not (self.getPosition().x <= object.getPosition().x + object.getSize().x):
            return False
        
        if not (self.getPosition().x + self.getSize().x >= object.getPosition().x):
            return False
        
        if not (self.getPosition().y <= object.getPosition().y + object.getSize().y):
            return False
        
        if not (self.getPosition().y + self.getSize().y >= object.getPosition().y):
            return False
        
        return True
    
    # Go through the list and find matching IDs
    # Some objects may have the same ID, so the whole list is checked
    # Return the collided object if it is found within the current object
    def collideBoxByID(self, renderQueue: list, objectID: str):
        matchFound = False

        for object in renderQueue:
            if object.getID() == objectID:
                matchFound = self.collideBoxByObject(object)

            if matchFound:
                return object
            
        return None
    
    def collideMaskByObject(self, object: "spriteObject"):
        if self.m_mask == None or object.m_mask == None:
            return False
        
        offsetX = object.getPosition().x - self.getPosition().x
        offsetY = object.getPosition().y - self.getPosition().y
        if self.m_mask.overlap(object.m_mask, (offsetX, offsetY)) != None:
            return True
        return False
    
    def collideMaskByID(self, renderQueue: list, objectID: str):
        matchFound = False

        if object in renderQueue:
            if object.getID() == objectID:
                matchFound = self.collideMaskByObject(object)
            
            if matchFound:
                return object
        return None

    

class spriteObject(flags, transform, sharedData):
    # === Define spriteObject ===
    def __init__(self, objectID: str, texture, position: vector2f, size: vector2i, alpha = False, layer = 0):
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
            printWarningInfo(f"Sprite Object: '{self.getID()}' is not initialised")
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
            self.m_mask = None
        else:
            self.m_texture = self.m_texture.convert_alpha()
            self.m_mask = pygame.mask.from_surface(self.m_texture)

        
        self.initialiseObject()

    # === Replace texture ===
    def replaceTexture(self, newTexture, size: vector2f, alpha = False):
        # Check if 'newTexture' is a string or a loaded texture
        if type(newTexture) == str:
            self.m_texture = pygame.image.load(newTexture)
        else:
            self.m_texture = newTexture

        self.m_texture = pygame.transform.scale(self.m_texture, (size.x, size.y))
        if not alpha:
            self.m_texture = self.m_texture.convert()    

        self.m_mask = pygame.mask.from_surface(self.m_texture)

    # === Render Object ===
    def render(self, surface):
        surface.blit(self.m_texture, [self.m_position.x, self.m_position.y])
