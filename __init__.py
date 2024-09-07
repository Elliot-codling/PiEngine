#BY ELLIOT CODLING
#PiEngine 8.1.0
from .sound import *
from .input import *
from .object import *
from .ssp import *

#deleted objects in the display list
#add item to the deletion list
def appendForDeletion(object):
    global deletedObjects
    deletedObjects += [object]

#Delete items from the deletion list in the display list
def deleteObjects(display):
    global deletedObjects
    for object in display:
        display.remove(object)

    deletedObjects = []
    return display

#interaction with the screen
class window:
    #window is now an object and can add properties to the window
    def __init__(self, name, w, h, color = (0, 0, 0), flags=0, vsync=0):
        if vsync == 0:    #create window
            self.surface = pygame.display.set_mode((w, h), flags)    
        elif vsync == 1:
            self.surface = pygame.display.set_mode((w, h), flags, vsync=1)   
        self.color = color   
        self.run = True   
        pygame.display.set_caption(name)                        #create name
    
    def isRunning(self):    #Returns a boolean value if the window is running
        return self.run
    
    def setRunStatus(self, status):      
        self.run = status
        
    #update the screen
    def update(self, display = None, debugParameters=[None]):                #update routine
        #fill the screen with the color selected
        self.surface.fill(self.color)
        #get the texture and find it's x + y
        if display != None:
             #sort the list from smallest layer value to largest
            display.sort(key=lambda x: x.layer)
            for object in display:
                #find the texture
                texture = object.texture

                #find the coords
                x = object.x
                y = object.y
                
                self.surface.blit(texture, [x, y])

        #debug - anything in the display will be highlighted at the start to allow overlap
        #also a frame rate counter will be in the top left showing the current, minimum and maximum fps 
        if debugParameters[0] != None:
            debug.application(self, display, debugParameters)
            
        #update
        pygame.display.flip()     #update all of the screen

    #go through the display list
    #remove any items with the selected layer
    def delete_layer(display, layer):
        for object in display:
            if object.layer == layer:
                display.remove(object)

        return display


#class used for debugging purposes
class debug:
    def pygame():         #pygame debug help
        import sys              #import system files
        #steps on installing pygame / pip onto os
        print("It seems like Pygame is not installed. What OS are you using?")
        print("")
        print("Windows (1)")
        print("Mac OS or Linux (2)")
        print("")
        os_select = input(":")
        if os_select == "1":
            print("")
            print("Open Terminal / CMD")
            print("")
            print("Type: pip3 install pygame")
            print("IF PIP IS NOT RECOGNISED / INSTALLED:")
            print("")
            print("Type 1: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
            print("")
            print("Type 2: py get-pip.py")
        elif os_select == "2":
            print("")
            print("Open Terminal")
            print("")
            print("Type: sudo apt install python3-pygame")
            print("IF PIP IS NOT RECOGNISED / INSTALLED:")
            print("")
            print("Type 1: sudo apt install python3-pip")
        else:
            print("Invalid")

        input("Enter to exit. ")
        sys.exit()

    #debugging the application
    #debug parameters: 1 - layer, 2 - clock, 3 - color
    def application(window, display, debugParameters=[]):
        global minFPS, maxFPS, wait
        layer = debugParameters[0]
        clock = debugParameters[1]
        color = debugParameters[2]
        interval = debugParameters[3]
        
        #used to reset the fps stats
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F1]:
            initConfig()
        #highlight over a layer with a specific color
        if display != None:
            for object in display:
                if object.layer != layer:
                    continue
                
                x = object.x
                y = object.y
                width = object.texture.get_width()
                height = object.texture.get_height()

                pygame.draw.rect(window.surface, color, pygame.Rect(x, y, width, height))

        #set min and max fps
        if int(clock.get_fps()) < minFPS:
            minFPS = int(clock.get_fps())
        if int(clock.get_fps()) > maxFPS:
            maxFPS = int(clock.get_fps())
        
        #update the text in for the fps stats
        internalTimer.update()
        if internalTimer.frames >= wait:
            wait = internalTimer.frames + interval
            minFpsText.reload_text(f"Min FPS: {minFPS}", color, 20)
            maxFpsText.reload_text(f"Max FPS: {maxFPS}", color, 20)
            currentFpsText.reload_text(f"FPS: {int(clock.get_fps())}", color, 20)

        #manually draw to the screen
        pygame.draw.rect(window.surface, (0, 0, 0), pygame.Rect(minFpsText.x - 10, minFpsText.y - 10, currentFpsText.x + 80, currentFpsText.y + 10))
        window.surface.blit(minFpsText.texture, [minFpsText.x, minFpsText.y])
        window.surface.blit(maxFpsText.texture, [maxFpsText.x, maxFpsText.y])
        window.surface.blit(currentFpsText.texture, [currentFpsText.x, currentFpsText.y])

#try to import pygame, if that is not successful then 
#help the user to try to install pygame onto their computer
try:
    import pygame
    pygame.font.init()
except ModuleNotFoundError:
    debug.pygame()
try:
    pygame.mixer.init()         #initilise music
except pygame.error:
    pass

# ------------------------------------------------------------------------------------------------------------------------------------------
#used for config, sets the min and max frames to be out of bounds so that the comparison will overide the values
internalTimer = counter()
def initConfig():
    global minFPS, maxFPS, deletedObjects, wait
    minFPS, maxFPS, wait = 1000000000, -1, 0
    deletedObjects = []
initConfig()

#finds the current directory of the engine
import os
def directory():
    return os.getcwd()

minFpsText = properties_text("minFPS", "Min FPS: ", "WHITE", 20, 20, 20)
maxFpsText = properties_text("maxFPS", "Max FPS: ", "WHITE", 20, 35, 20)
currentFpsText = properties_text("currentFPS", "FPS: ", "WHITE", 20, 50, 20)