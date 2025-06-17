# Used to create a pygame window and manager the events for the window

# Import required files - global
from .sprite import *
from .text import *
from .vector import *
from .input import *
from .ssp import *
from .audio import *

class window(windowEvents, windowInput):
    # === Manage and define the window functions ===
    def __init__(self, name, width, height, clock, color = (0, 0, 0)):
        import pygame
        # Create window
        self.m_clock = clock
        self.m_targetFramerate = 0
        self.m_surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

        # Create render queues
        self.m_renderQueue = []

        # Define the colour of the display background
        self.m_color = color
        self.m_windowOpen = True

    def isRunning(self):
        return self.m_windowOpen
    
    def stopRunning(self):
        self.m_windowOpen = False


    # === Framerate ===
    def setTargetFramerate(self, targetFPS: int):
        self.m_targetFramerate = targetFPS

    def getTargetFramerate(self):
        return self.m_targetFramerate
    
    def getFramerate(self):
        return self.m_clock.get_fps()
    
    # === object layers ===
    def clearLayer(self, layerNumber):
        for object in self.m_renderQueue:
            if object.getLayer() == layerNumber:
                self.popFromQueue(object)
        


    # === Render queue ===
    def pushToQueue(self, object):
        self.m_renderQueue.append(object)

    def popFromQueue(self, object):
        self.m_renderQueue.remove(object)

    def getQueue(self):
        return self.m_renderQueue

    def sortQueue(self):
        self.m_renderQueue.sort(key = lambda object: object.getLayer(), reverse=True)

    # === Render Objects ===
    def renderObjects(self):
        self.m_surface.fill(self.m_color)

        self.sortQueue()
        
        for object in self.m_renderQueue:   
            if object.isInitialised():
                object.render(self.m_surface)

        pygame.display.flip()

    