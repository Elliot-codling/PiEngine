# Used to create a pygame window and manager the events for the window
# === External libs ===
from typing import Union
import pygame
# === Inherited classes ===
from ..events.WindowEvents import *
# === Internal classes ===
from ..sprite.Sprite import *
from ..text.Text import *
from ..vector.Vector import *
from ..log.Logger import *
from ..window.Renderer import *

#from ..storage import *
#from ..audio import *
#from ..Button import *


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
            Logger.warn("window/Application", f"Could not find attribute: '{flag}'")
            return 0
        
    return attributeInt   


class Application(WindowEvents, WindowInput):
    # === Manage and define the window functions ===
    def createWindow(self, name: str, width: int, height: int, clock: pygame.time.Clock, color = (0, 0, 0), flags = [], vsync = False) -> None:
        import platform
        # Correction for windows OS
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
        Logger.info("window/Application", f"Created Pygame window: '{name}'")
        pygame.display.set_caption(name)

        # Define the colour of the display background
        self.m_color = color
        self.m_windowOpen = True
        self.m_renderer = Renderer()
        self.m_activeScene = None

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
    # === Scene control ===
    def getActiveScene(self):
        return self.m_activeScene
    
    def setActiveScene(self, scene: "Scene"):
        self.m_activeScene = scene

    # === Display control ===
    def updateBlankDisplay(self):
        self.m_renderer.renderBlankScene(self.m_surface, self.m_color)

    def updateDisplay(self):
        self.m_renderer.renderScene(self.m_surface, self.m_color, self.m_activeScene)
    
    """
    # === object layers ===
    def clearLayer(self, layerNumber: int) -> None:
        for object in self.m_renderQueue:
            if object.getLayer() == layerNumber:
                self.popFromQueue(object)
        

    
    # === Render queue ===
    def sortQueue(self) -> None:
        self.m_renderQueue.sort(key = lambda object: object.getLayer(), reverse=True)
    """
    
    