# Used to create a pygame window and manager the events for the window

# Import required files - global
from .sprite import *
from .textObject import *
from .vector import *
from .input import *
from .ssp import *
from .audio import *
from .debugHandler import *
from .button import *
from typing import Union

# Goes through a list of strings which it tries to find an equivalent value for
# For example: 'SCALED' => 'pygame.SCALED'
# 'pygame.SCALED' + 'pygame.RESIZABLE' = 528, therefore it returns the int 528
# Any values it could not find an attribute for it throws a warning and then returns 0
def getAttributes(flags: list) -> int:
    attributeInt = 0
    for flag in flags:
        try:
            attributeInt += getattr(pygame, flag)
        except AttributeError:
            printWarningInfo(f"Could not find attribute: '{flag}'")
            return 0
        
    return attributeInt

class window(windowEvents, windowInput):
    # === Manage and define the window functions ===
    def __init__(self, name: str, width: int, height: int, clock: pygame.time.Clock, color = (0, 0, 0), flags = [], vsync = False) -> "window":
        import pygame, platform
        if platform.system().lower() == "windows":
            import ctypes
            ctypes.windll.user32.SetProcessDPIAware()
        # Create window
        self.m_clock = clock
        self.m_targetFramerate = 0

        # Enable vsync if the bool is set. 'SCALED' flag is required to enable this feature
        # If user types, 'SCALED' it will be converted to 'pygame.SCALED'     
        if vsync:
            self.m_surface = pygame.display.set_mode((width, height), getAttributes(flags), vsync = 1)
        else:
            self.m_surface = pygame.display.set_mode((width, height), getAttributes(flags))

        # Output to log
        printInfo(f"Created Pygame window: '{name}'")
        pygame.display.set_caption(name)

        # Create render queues
        self.m_renderQueue = []

        # Define the colour of the display background
        self.m_color = color
        self.m_windowOpen = True

    # === Window control ===
    def isRunning(self) -> bool:
        return self.m_windowOpen
    
    def stopRunning(self) -> None:
        self.m_windowOpen = False

    # === Sizes ===
    def getWidth(self):
        return self.m_surface.get_width()
    
    def getHeight(self):
        return self.m_surface.get_height()

    # === Framerate ===
    def setTargetFramerate(self, targetFPS: int) -> None:
        self.m_targetFramerate = targetFPS

    def getTargetFramerate(self) -> int:
        return self.m_targetFramerate
    
    def getFramerate(self) -> float:
        return self.m_clock.get_fps()
    
    # === object layers ===
    def clearLayer(self, layerNumber: int) -> None:
        for object in self.m_renderQueue:
            if object.getLayer() == layerNumber:
                self.popFromQueue(object)
        


    # === Render queue ===
    def pushToQueue(self, object: Union[spriteObject, textObject]) -> None:
        if object.isInitialised():
            self.m_renderQueue.append(object)
            return
        printWarningInfo(f"Object: '{object.getID()}' not added to the render queue. Object is not initialised")

    def popFromQueue(self, object: Union[spriteObject, textObject]) -> None:
        self.m_renderQueue.remove(object)

    def getQueue(self) -> list:
        return self.m_renderQueue

    def sortQueue(self) -> None:
        self.m_renderQueue.sort(key = lambda object: object.getLayer(), reverse=True)

    # === Render Objects ===
    def renderObjects(self) -> None:
        self.m_surface.fill(self.m_color)

        self.sortQueue()
        
        for object in self.m_renderQueue:   
            if object.isInitialised():
                object.render(self.m_surface)

        pygame.display.flip()

    