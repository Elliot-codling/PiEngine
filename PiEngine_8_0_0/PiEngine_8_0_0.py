#BY ELLIOT CODLING
#PiEngine 8.0.0

#used for sfx sounds
class sfx:
    def __init__(self, soundDirectory, channel):        #laods the song, and adds it to a channel
        self.sound = pygame.mixer.Sound(soundDirectory)
        self.channel = channel

    #play sfx sound
    def playSound(self, playIfBusy=False):
        #if the playIfBusy is true, then overwrite the channel even if it is busy
        if pygame.mixer.Channel(self.channel).get_busy() and playIfBusy == False:
            return
        pygame.mixer.Channel(self.channel).play(self.sound)

    

#used for music
class music:
    def __init__(self, track, channel=0):
        #define a track with [], it can have multiple songs
        #choose a channel to play on
        #can loop through if the track gets to the end
        self.track = track
        self.channel = channel
        self.currentTrack = 0

    #used to go through a whole track
    def loop(self, shuffle):
        if pygame.mixer.Channel(self.channel).get_busy():
            return
        if shuffle:
            self.currentTrack = random.randint(0, len(self.track) - 1)
        pygame.mixer.Channel(self.channel).play(pygame.mixer.Sound(self.track[self.currentTrack]))

        if self.currentTrack + 1 == len(self.track):
            self.currentTrack = 0
        else:
            self.currentTrack += 1

    #used to play just one song on a track
    def play(self, trackNumber, playIfBusy=False):
        #if the playIfBusy is true, then overwrite the channel even if it is busy
        if pygame.mixer.Channel(self.channel).get_busy() and playIfBusy == False:
            return
        
        pygame.mixer.Channel(self.channel).play(pygame.mixer.Sound(self.track[trackNumber]))

    #used to stop the channel playing
    def stop(self):
        pygame.mixer.Channel(self.channel).stop()



#keeps track of the frames that have been passed
#used for animation
class counter:  
    def update():
        global frames
        frames += 1

#updates the events of the program
#checks if the close button has been pressed as well as updates the current key pressed
class event:
    def update():
        global keys, run
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        return events

    def getKeydown(events, pygameEvent):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygameEvent:
                    return True

    def getKeyUp(events, pygameEvent):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygameEvent:
                    return True

#manipulate an object
class object:
    def setAngle(self, angle):          #set a specific angle for the object to look in
        texture = pygame.image.load(self.loaded_texture)
        self.texture = pygame.transform.rotate(pygame.transform.scale(texture, (self.width, self.height)), angle)             #rotates the object and setss its new angle
        self.rotation = angle    
        self.mask = pygame.mask.from_surface(self.texture)    

    def animate(self, animationList, frameWait, flipX = 0, flipY = 0):
        if frames >= self.animationTime:            #check if it is the right time to change the texture
            properties_object.reload_texture(self, animationList[self.animationStage], self.width, self.height)            #change the texture of the object
            self.texture = pygame.transform.flip(self.texture, flipX, flipY)
            self.animationTime = frames + frameWait         #update when the object should change texture next
        
            if self.animationStage == len(animationList) - 1:           #if we are at the end of the list, change the animationStage to 0
                self.animationStage = 0
            else:
                self.animationStage += 1                    #else continue on increasing
                
    def collision_rect(self, display, index):     #get the object pos, the collision list and the index to check if collided
        #check to see if its within the x coord position
        if not self.x + self.width >= display[index].x:
            return None
        elif not self.x <= display[index].x + display[index].width:
            return None
        elif not self.y + self.height >= display[index].y:
            return None
        elif not self.y <= display[index].y + display[index].height:
            return None
        else:
            #collision has occured
            return display[index].id

    def collision_mask(self, display, collidableLayers=[]):        #finds objects in the list
        for object in display:
            collidable = False
            for layer in collidableLayers:
                if object.layer == layer:
                    collidable = True
                    break

            if not collidable:
                continue
            offsetX = object.x - self.x             #offsets the object by the player position
            offsetY = object.y - self.y
            if self.mask.overlap(object.mask, (offsetX, offsetY)) and object.id != self.id:          #checks for overlap
                return object.id

    def left(self, vel, border):
        #check if the object x coord is hitting the border - reports true if hit a border
        if self.x > border:
            self.x -= vel
            return False            
        else:
            return True

    def right(self, vel, border):
        if self.x < border:
            self.x += vel
            return False
        else:
            return True

    def up(self, vel, border):
        if self.y > border:
            self.y -= vel
            return False
        else:
            return True 

    def down(self, vel, border):
        if self.y < border:
            self.y += vel
            return False            
        else:       
            return True

#gives basic properties to objects
class properties_object(object):            #this is to define the properties of a sprite
    def __init__(self, id, loaded_texture, x, y, width, height, alpha=False, layer=0, rotation = 0):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.animationTime = 0          #how long the animation should last
        self.animationStage = 0        #what is the current state the animation is in
        self.rotation = rotation            #set the angle at which the object is facing
        self.layer = layer          #sets which layer of the screen the object will be drawn to

        #transform the texture to correct size when creating object
        self.loaded_texture = loaded_texture
        if type(loaded_texture) == str:
            loaded_texture = pygame.image.load(loaded_texture)
        
        #scale the texture to the width and height
        texture = pygame.transform.scale(loaded_texture, (width, height))
        self.texture = texture
        
        #include alpha channel
        self.alpha = alpha
        if alpha == True:
            pass
        elif alpha == False:
            self.texture = texture.convert()

        self.mask = pygame.mask.from_surface(self.texture)          #create a mask for the texture used

    def reload_texture(self, loaded_texture, width, height):          #reloads the texture and can resize it all in one line!
        if type(loaded_texture) == str:                             #check if the tetxure coming ahs already been loaded or is a request for a new file location
            loaded_texture = pygame.image.load(loaded_texture)
        
        self.texture = pygame.transform.scale(loaded_texture, (width, height))           #scale this object accordingly
        self.mask = pygame.mask.from_surface(self.texture)          #recreates the mask that has initially been made
        #no longer needed to return the texture



#class for defining text
class properties_text:          #this is to define properties of text
    def __init__(self, id, text, color, x, y, font_size, snapCentre = False, layer=0):
        self.id = id        #define all of the variables
        self.text = text
        
        self.font_size = font_size
        self.color = color  
        self.snapCentre = snapCentre
        self.layer = layer
        
        font = pygame.font.SysFont(None, font_size)
        texture = font.render(text, True, pygame.Color(color))
        if snapCentre == True:          #can snap to the centre of the screen, x and y are turned into the width and height of window
            centre_coords = texture.get_rect(center=(x/2, y/2))
            self.x = centre_coords[0]
            self.y = centre_coords[1]
        else:
            self.x = x
            self.y = y
        self.texture = texture

    def reload_text(self, text, color, font_size):            #reload the texture to text
        font = pygame.font.SysFont(None, font_size)
        self.texture = font.render(text, True, pygame.Color(color))  


#mouse capability
class mouse():          
    def collision(objectId, display, mouseX = 0, mouseY = 0):
        if mouseX == 0 or mouseY == 0:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            #gets the mouse positions and checks to see if it hits a box with a given id
        #if yes then returns true
        #else returns false
        x, y = None, None
        #find the id of the object
        for object in display:
            if object.id == objectId:
                #find coords of sprite
                x = object.x
                y = object.y
                width = object.width
                height = object.height
        #return false if no x or y coord is found
        if x == None and y == None:
            return False
        #check to see if the mouse position contains within the box
        if not mouseX >= x:
            return False
        elif not mouseX <= x+width:
            return False
        elif not mouseY >= y:
            return False
        elif not mouseY <= y+height:
            return False
        else:
            return True


#interaction with the screen
class window:
    #window is now an object and can add properties to the window
    def __init__(self, name, w, h, color = (0, 0, 0), flags=0, vsync=0):
        if vsync == 0:    #create window
            self.surface = pygame.display.set_mode((w, h), flags)        
        elif vsync == 1:
            self.surface = pygame.display.set_mode((w, h), flags, vsync=1)   
        self.color = color      
        pygame.display.set_caption(name)                        #create name
    
    def music_debug():          #print out the error if an audio driver hasnt been found
        print("It seems like there is no Audio Driver installed on your device.")
        print("Sound will be deactivated.")

    def pygame_debug():         #pygame debug help
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
        
    #update the screen
    def update(window, display = None, debug=[None]):                #update routine
        global minFPS, maxFPS
        #fill the screen with the color selected
        window.surface.fill(window.color)
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
                
                window.surface.blit(texture, [x, y])

        #debug - anything in the display will be highlighted at the start to allow overlap
        #also a frame rate counter will be in the top left showing the current, minimum and maximum fps 
        if debug[0] != None:
            layer = debug[0]
            clock = debug[1]
            color = debug[2]

            if keys[pygame.K_F1]:
                initDebug()
            if display != None:
                for object in display:
                    if object.layer != layer:
                        continue
                    
                    x = object.x
                    y = object.y
                    width = object.texture.get_width()
                    height = object.texture.get_height()

                    pygame.draw.rect(window.surface, color, pygame.Rect(x, y, width, height))

            if int(clock.get_fps()) < minFPS:
                minFPS = int(clock.get_fps())
            if int(clock.get_fps()) > maxFPS:
                maxFPS = int(clock.get_fps())

            minFpsText.reload_text(f"Min FPS: {minFPS}", color, 20)
            maxFpsText.reload_text(f"Max FPS: {maxFPS}", color, 20)
            currentFpsText.reload_text(f"FPS: {int(clock.get_fps())}", color, 20)

            pygame.draw.rect(window.surface, (0, 0, 0), pygame.Rect(minFpsText.x - 10, minFpsText.y - 10, currentFpsText.x + 80, currentFpsText.y + 10))
            window.surface.blit(minFpsText.texture, [minFpsText.x, minFpsText.y])
            window.surface.blit(maxFpsText.texture, [maxFpsText.x, maxFpsText.y])
            window.surface.blit(currentFpsText.texture, [currentFpsText.x, currentFpsText.y])

       
        #update
        pygame.display.flip()     #update all of the screen

    #go through the display list
    #remove any items with the selected layer
    def delete_layer(display, layer):
        for object in display:
            if object.layer == layer:
                display.remove(object)

        return display

#try to import pygame, if that is not successful then 
#help the user to try to install pygame onto their computer
try:
    import pygame
    pygame.font.init()
except ModuleNotFoundError:
    window.pygame_debug()

try:
    pygame.mixer.init()         #initilise music
    activate_music = True
except pygame.error:
    window.music_debug()            #if the audio driver hasn't been found
    activate_music = False

# ------------------------------------------------------------------------------------------------------------------------------------------
#This part of the code is for all uses to access specific variables
#can be used by calling engine.x

#used for debugging, sets the min and max frames to be out of bounds so that the comparison will overide the values
#call frames by engine.frames
def initDebug():
    global frames, minFPS, maxFPS
    frames = 0
    minFPS, maxFPS = 1000000000, -1
initDebug()
minFpsText = properties_text("minFPS", "Min FPS: ", "WHITE", 20, 20, 20)
maxFpsText = properties_text("maxFPS", "Max FPS: ", "WHITE", 20, 35, 20)
currentFpsText = properties_text("currentFPS", "FPS: ", "WHITE", 20, 50, 20)

#sets the main body while loop to be running, call with engine.run
global run
run = True

#finds the current directory of the engine
import os, random
directory = os.getcwd()
