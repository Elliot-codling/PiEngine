import pygame
from .sprite import *
from .vector import *
from .debugHandler import *
from typing import Union

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

class windowInput: 
    def getKey(self, keyType: str) -> bool:
        # Return a bool if the key has been pressed
        keys = pygame.key.get_pressed()
        try:
            keyPressed = getattr(pygame, f"K_{keyType}")
        except AttributeError:
            printWarningInfo(f"Key name: '{keyType}' could not be found")
            return False 

        return keys[keyPressed]
    
    def getMousePosition(self) -> vector2i:
        return vector2i(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    
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
        
    def getMouseCollisionByID(self, renderQueue: list, objectID: str, mouseX = 0, mouseY = 0) -> Union[spriteObject, textObject, None]:
        if mouseX == 0  or mouseY == 0:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
        
        matchFound = False
        for object in renderQueue:
            if object.getID() == objectID:
                matchFound = self.getMouseCollisionByObject(object, mouseX, mouseY)
            if matchFound:
                return object
            
        return None
