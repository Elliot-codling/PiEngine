#BY ELLIOT CODLING
class music():
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

#gives basic properties to objects
class properties_object:            #this is to define the properties of a sprite
    def __init__(self, name, loaded_texture, x, y, width, height, alpha, animationTime = 0, animationStage = 0):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.animationTime = animationTime          #how long the animation should last
        self.animationStage = animationStage        #what is the current state the animation is in

        #transform the texture to correct size when creating object
        self.loaded_texture = loaded_texture
        if type(loaded_texture) == str:
            loaded_texture = pygame.image.load(loaded_texture)
        
        texture = pygame.transform.scale(loaded_texture, (width, height))
        self.texture = texture
        
        #include alpha channel
        self.alpha = alpha
        if alpha == True:
            pass
        elif alpha == False:
            self.texture = texture.convert()

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

class mouse():          #mouse capability
    def collision(boxName, foreground, mouseX = 0, mouseY = 0, ):
        if mouseX == 0 or mouseY == 0:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            #gets the mouse positions and checks to see if it hits a box with a given name
        #if yes then returns true
        #else returns false
        x, y = None, None
        #find the name of the box/sprite
        for sprite in foreground:
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

#interaction wit the screen
class window:
    def music_debug():
        print("It seems like there is no Audio Driver installed on your device.")
        print("Sound will be deactivated.")
    def pygame_debug():
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
    def list_debug(display, display_sprite, foreground, text_foreground, clock):             #this is debug, needs display, sprite and foreground + text_foreground
        print("Number of items in display: {}".format(len(display)))            #items in background
        print("Number of items in display sprite: {}".format(len(display_sprite)))          #items in sprites
        print("Number of items in foreground: {}".format(len(foreground)))              #items in foreground
        print("Number of items in text_foreground: {}".format(len(text_foreground)))
        print("")
        print("Display: {}".format(display))            #print the arrays, leave enough room between each
        print("")
        print("")
        print("Display sprite: {}".format(display_sprite))
        print("")
        print("")
        print("Foreground: {}".format(foreground))
        print("")
        print("")
        print("Text_foreground: {}".format(text_foreground))
        fps = int(clock.get_fps())
        print("FPS: {}".format(fps))
        pygame.time.delay(100)              #stop game for 0.1 seconds

    def define(name, w, h, flags=0, vsync=0):             #define the window   
        if vsync == 0:    #create window
            window = pygame.display.set_mode((w, h), flags)        
        elif vsync == 1:
            window = pygame.display.set_mode((w, h), flags, vsync=1)         
        pygame.display.set_caption(name)                        #create name
        return window

    def update(window, display, display_sprite, foreground, text_foreground, clock, debug):                #update routine
        #get the texture and find it's x + y
        #v standing for variable
        for v in range(len(display)):
            #find the texture
            texture = display[v].texture

            #find the coords
            x = display[v].x
            y = display[v].y
            
            window.blit(texture, [x, y])

        #for creating sprites
        for v in range(len(display_sprite)):
            #find the texture
            texture = display_sprite[v].texture

            #find the coords
            x = display_sprite[v].x
            y = display_sprite[v].y
            
            window.blit(texture, [x, y])

        #foreground
        #v standing for variable
        for v in range(len(foreground)):
            #find the texture
            texture = foreground[v].texture           #find the texture

            #find the coords
            x = foreground[v].x              #find the x coord
            y = foreground[v].y               #find the x coord
            
            window.blit(texture, [x, y])            #paste that onto the screen

        #text_foreground
        #v standing for variable
        for v in range(len(text_foreground)):
            #find the texture
            texture = text_foreground[v].texture            #find the texture

            #find the coords
            x = text_foreground[v].x               #find the x coord
            y = text_foreground[v].y               #find the x coord
            
            window.blit(texture, [x, y])            #paste that onto the screen

        #debug
        if debug:
            color = (255, 255, 0)
            length = len(display_sprite)            #find the length of the foreground
            length = int(length)                #change to int
            
            for v in range(length):
                x = display_sprite[v].x
                y = display_sprite[v].y
                width = display_sprite[v].width
                height = display_sprite[v].height

                pygame.draw.rect(window, color, pygame.Rect(x, y, width, height))          
                #create the debug rectangle to show where the hitbox is on sprites
            
            fps = int(clock.get_fps())
            font = pygame.font.SysFont(None, 30)
            fps_text = font.render("FPS: {}".format(fps), True, pygame.Color("YELLOW"))
            window.blit(fps_text, [20, 40])
            
        #update
        pygame.display.update()     #only update the screen at this time

class player:
    def collisions(player, box_list, index):     #get the player pos, the collision list and the index to check if collided
        #check to see if its within the x coord position
        if not player.x + player.width >= box_list[index].x:
            return None
        elif not player.x <= box_list[index].x + box_list[index].width:
            return None
        elif not player.y + player.height >= box_list[index].y:
            return None
        elif not player.y <= box_list[index].y + box_list[index].height:
            return None
        else:
            #collision has occured
            return box_list[index].name

    def left(player, vel, border):
        #check if the player x coord is hitting the border
        if player.x > border:
            player.x -= vel
        return player

    def right(player, vel, border):
        if player.x < border:
            player.x += vel
        return player

    def up(player, vel, border):
        if player.y > border:
            player.y -= vel
        return player

    def down(player, vel, border):
        if player.y < border:
            player.y += vel
        return player

try:
    import pygame, time
except ModuleNotFoundError:
    window.pygame_debug()
try:
    pygame.mixer.init()         #initilise music
    activate_music = True
except pygame.error:
    window.music_debug()            #if the audio driver hasn't been found
    activate_music = False