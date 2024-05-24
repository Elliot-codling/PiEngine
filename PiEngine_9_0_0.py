#BY ELLIOT CODLING
# I am creating a change to the main PiEngine file on github from VScode
#PiEngine 9.0.0
class music:
    # volume is what the volume of what it is now
    #end volume is what it will get to
    def fade_out(volume, end_volume, wait):
        if activate_music:
            pre_volume = 0
            pre_volume += volume
            for _ in range(int(end_volume * 10), int(volume * 10)):
                pygame.mixer.music.set_volume(volume)       #set volume of the music
                volume -= 0.1                   #slowly decrease the music
                time.sleep(wait)                 #tell it to stop so that it slowly fades out

            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(pre_volume)

    #stop the music only if an audio driver has been detected
    def stop():
        if activate_music:
            pygame.mixer_music.stop()

#keeps track of the frames that have been passed
#used for animation
class counter:  
    def updateCounter():
        global frames
        frames += 1

#updates the events of the program
#checks if the close button has been pressed as well as updates the current key pressed
class event:
    def update():
        global run, keys
        run = True
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False


#gives basic properties to objects
class properties_object:            #this is to define the properties of a sprite
    def __init__(self, name, loaded_texture, x, y, width, height, alpha, layer=0, rotation = 0):
        self.name = name
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



#updates text
class properties_text:          #this is to define properties of text
    def __init__(self, name, text, color, x, y, font_size, snapCentre = False):
        self.name = name        #define all of the variables
        self.text = text
        
        self.font_size = font_size
        self.color = color  
        self.snapCentre = snapCentre
        
        font = pygame.font.SysFont(None, font_size)
        texture = font.render(text, True, pygame.Color(color))
        if snapCentre == True:          #can snap to the centre of the screen, x and y are turned into the width and height
            centre_coords = texture.get_rect(center=(x/2, y/2))
            self.x = centre_coords[0]
            self.y = centre_coords[1]
        else:
            self.x = x
            self.y = y
        self.texture = texture

    def reload_text(text, color, font_size):            #relaod the texture to text
        font = pygame.font.SysFont(None, font_size)
        texture = font.render(text, True, pygame.Color(color))
        return texture


#mouse capability
class mouse():          
    def collision(boxName, display, mouseX = 0, mouseY = 0):
        if mouseX == 0 or mouseY == 0:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            #gets the mouse positions and checks to see if it hits a box with a given name
        #if yes then returns true
        #else returns false
        x, y = None, None
        #find the name of the box/sprite
        for sprite in display:
            if sprite.name == boxName:
                #find coords of sprite
                x = sprite.x
                y = sprite.y
                width = sprite.width
                height = sprite.height
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
            print("Type: pip3 install pygame")
            print("IF PIP IS NOT RECOGNISED / INSTALLED:")
            print("")
            print("Type 1: sudo apt install python3-pip")
        else:
            print("Invalid")

        input("Enter to exit. ")
        sys.exit()

    #update the screen
    def update(window, display = None, clock = 0, layer = 0):                #update routine
        global minFPS, maxFPS
        #fill the screen with the color selected
        window.surface.fill(window.color)

        #debug - anything in the display will be highlighted at the start to allow overlap
        #also a frame rate counter will be in the top left showing the current, minimum and maximum fps
        if clock == 0:
            pass
        elif display != None:
            for object in display:
                if object.layer != layer:
                    continue
                    
                x = object.x
                y = object.y

                pygame.draw.rect(window.surface, (255, 255, 0), pygame.Rect(x, y, object.width, object.height))          
                #create the debug rectangle to show where the hitbox is on sprites
            
            #sets the new max and min fps
            counter.update()
            if frames > 30:
                if int(clock.get_fps()) < minFPS:
                    minFPS = int(clock.get_fps())
                if int(clock.get_fps()) > maxFPS:
                    maxFPS = int(clock.get_fps())

            pygame.draw.rect(window.surface, (255, 255, 0), pygame.Rect(0, 0, 75, 50))
            window.surface.blit(properties_text.reload_text(f"FPS: {int(clock.get_fps())}", "BLACK", 20), [10, 10])
            window.surface.blit(properties_text.reload_text(f"Min: {minFPS}", "BLACK", 20), [10, 20])
            window.surface.blit(properties_text.reload_text(f"max: {maxFPS}", "BLACK", 20), [10, 30])


        #sort the list from smallest layer value to largest
        display.sort(key=lambda x: x.layer)
        #get the texture and find it's x + y
        if display != None:
            for object in display:
                #find the texture
                texture = object.texture

                #find the coords
                x = object.x
                y = object.y
                
                window.surface.blit(texture, [x, y])

        #update
        pygame.display.flip()     #update all of the screen

    #go through the display list
    #remove any items with the selected layer
    def delete_layer(display, layer):
        for index in range(len(display)):
            if display[index].layer == layer:
                del display[index]

        return display



#manipulate an object
class object:
    def setAngle(self, angle):          #set a specific angle for the object to look in
        self.texture = pygame.transform.rotate(self.texture, self.rotation - angle)             #rotates the object and setss its new angle
        self.rotation = angle   #sets the current new angle for the object

    def animate(self, animationList, frameWait, flipX = 0, flipY = 0):
        if frames >= self.animationTime:            #check if it is the right time to change the texture
            properties_object.reload_texture(self, animationList[self.animationStage], self.width, self.height)            #change the texture of the object
            self.texture = pygame.transform.flip(self.texture, flipX, flipY)
            self.animationTime = frames + frameWait         #update when the object should change texture next
        
            if self.animationStage == len(animationList) - 1:           #if we are at the end of the list, change the animationStage to 0
                self.animationStage = 0
            else:
                self.animationStage += 1                    #else continue on increasing
                
    def collision_rect(self, box_list, index):     #get the object pos, the collision list and the index to check if collided
        #check to see if its within the x coord position
        if not self.x + self.width >= box_list[index].x:
            return None
        elif not self.x <= box_list[index].x + box_list[index].width:
            return None
        elif not self.y + self.height >= box_list[index].y:
            return None
        elif not self.y <= box_list[index].y + box_list[index].height:
            return None
        else:
            #collision has occured
            return box_list[index].name

    def collision_mask(self, box_list):        #finds objects in the list
        for object in box_list:
            offsetX = object.x - self.x             #offsets the object by the player position
            offsetY = object.y - self.y
            if self.mask.overlap(object.mask, (offsetX, offsetY)) and object.name != self.name:          #checks for overlap
                return object.name

    def left(object, vel, border):
        #check if the object x coord is hitting the border - reports true if hit a border
        if object.x > border:
            object.x -= vel
            return False            
        else:
            return True

    def right(object, vel, border):
        if object.x < border:
            object.x += vel
            return False
        else:
            return True

    def up(object, vel, border):
        if object.y > border:
            object.y -= vel
            return False
        else:
            return True 

    def down(object, vel, border):
        if object.y < border:
            object.y += vel
            return False            
        else:       
            return True

#try to import pygame, if that is not successful then 
#help the user to try to install pygame onto their computer
try:
    import pygame, time
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
global frames, minFPS, maxFPS
frames = 0
minFPS, maxFPS = 1000000000, -1

#sets the main body while loop to be running, call with engine.run
global run
run = True

#finds the current directory of the engine
import os
directory = os.getcwd()
