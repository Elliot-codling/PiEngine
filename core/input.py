import pygame
from .sprite import *
from .vector import *
from .debugHandler import *
from typing import Union

# === Used for window events ===
class windowEvents:
    def __init__(self) -> "windowEvents":
        self.m_currentEvents = []

    def updateEvents(self) -> None:
        # Update events that have occured in the frame
        events = pygame.event.get()

        self.m_currentEvents = []
        for event in events:
            self.m_currentEvents.append(event.type)
    
    def getEvent(self, eventType: str) -> bool:
        # Return a bool if the specified eventType matches what has happened in a frame
        try:
            eventTriggered = getattr(pygame, eventType)
        except AttributeError:
            return False
        
        for event in self.m_currentEvents:
            if event == eventTriggered:
                return True
            
        return False

# === Used for keyboard or mouse inputs ===
class windowInput: 
    # Find an attribute for a given string and return a bool if it has been pressed
    def getKey(self, keyType: str) -> bool:
        # Return a bool if the key has been pressed
        keys = pygame.key.get_pressed()
        try:
            keyPressed = getattr(pygame, f"K_{keyType}")
        except AttributeError:
            # Throw a warning if the specified key type has not been found
            printWarningInfo(f"Key name: '{keyType}' could not be found")
            return False 

        return keys[keyPressed]
    
    # Return a vector2i of the mouse position relative to the pygame window
    def getMousePosition(self) -> vector2i:
        return vector2i(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    
    # Return a bool if the specified mouse button has been pressed
    def mouseButtonClicked(self, button: str) -> bool:
        if button == "LEFT":
            return pygame.mouse.get_pressed()[0]
        
        elif button == "RIGHT":
            return pygame.mouse.get_pressed()[2]
        
        elif button == "MIDDLE":
            return pygame.mouse.get_pressed()[1]
        
        # Throw a warning if the specified mouse button could not be found
        printWarningInfo(f"Mouse button name: '{button}' could not be found")
        return False
        
    # Return a bool if the mouse has hit an object
    # Object passed into function
    # Uses axies aligned collision
    def getMouseCollisionByObject(self, object: "spriteObject", mouseX = 0, mouseY = 0) -> bool:
        if mouseX == 0  or mouseY == 0:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
        
        if not mouseX >= object.getPosition().x:
            return False
        elif not mouseX <= object.getPosition().x + object.getSize().x:
            return False
        elif not mouseY >= object.getPosition().y:
            return False
        elif not mouseY <= object.getPosition().y + object.getSize().y:
            return False
        else:
            return True
    
    # Return an object if the mouse has hit an object based on the ID
    # If not it will return 'None'
    def getMouseCollisionByID(self, renderQueue: list, objectID: str, mouseX = 0, mouseY = 0) -> Union[spriteObject, textObject, None]:
        if mouseX == 0  or mouseY == 0:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
        
        # Return if a collision is found with the specified ID
        for object in renderQueue:
            if object.getID() != objectID:
                continue

            if self.getMouseCollisionByObject(object, mouseX, mouseY):
                return object
            
        return None
