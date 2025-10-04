# === External libs ===
import pygame
# === Inherited classes ===
# === Internal classes ===
from ..sprite.Transform import * 

# === Collision statements ===
# Returns a bool
class Collision(Transform):
    # === Check position of object compared to predefinied border ===
    def leftBorder(self, relativePosition: vector2i, borderLeft: int) -> bool:
        return relativePosition.x <= borderLeft
    
    def rightBorder(self, relativePosition: vector2i, borderRight: int) -> bool:
        return relativePosition.x >= borderRight
    
    def topBorder(self, relativePosition: vector2i, borderTop: int) -> bool:
        return relativePosition.y <= borderTop
    
    def bottomBorder(self, relativePosition: vector2i, borderBottom: int) -> bool:
        return relativePosition.y >= borderBottom
    
    # === Collision boxes ===
    # Return true if the current object collides with the object passed
    # Else return false
    def collideBoxByObject(self, object: "Sprite") -> bool:        
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
    def collideBoxByID(self, renderQueue: list, objectID: str) -> Union["spriteObject", None]:
        for object in renderQueue:
            if object.getID() != objectID:
                continue

            if self.collideBoxByObject(object):
                return object
            
        return None
    
    # Same as 'collideBoxByObject' however it uses a mask instead for more accurate collision
    # Returns a bool if the object is collided with
    def collideMaskByObject(self, object: "Sprite") -> bool:
        if self.m_mask == None or object.m_mask == None:
            return False
        
        offsetX = object.getPosition().x - self.getPosition().x
        offsetY = object.getPosition().y - self.getPosition().y
        return self.m_mask.overlap(object.m_mask, (offsetX, offsetY)) != None
    
    # Same as 'collideBoxByID' however it uses a mask instead for more accurate collision
    # Returns the object if it has been collided with
    # Else return 'None'
    def collideMaskByID(self, renderQueue: list, objectID: str) -> Union["spriteObject", None]:
        for object in renderQueue:
            if object.getID() != objectID:
                continue
                        
            if self.collideMaskByObject(object):
                return object
        return None