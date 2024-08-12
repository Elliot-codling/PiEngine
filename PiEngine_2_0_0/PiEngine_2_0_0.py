#game engine v0.0.3
#BY ELLIOT CODLING
import pygame
import time
class music():
    # volume is what the volume of what it is now
    #end volume is what it will get to
    def fade_out(volume, end_volume, wait):
        pre_volume = 0
        pre_volume += volume
        for _ in range(int(end_volume * 10), int(volume * 10)):
            pygame.mixer.music.set_volume(volume)       #set volume of the music
            volume -= 0.1                   #slowly decrease the music
            time.sleep(wait)                 #tell it to stop so that it slowly fades out

        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(pre_volume)

class properties_object:            #this is to define the properties of a sprite
    def __init__(self, name, texture, x, y, width, height, alpha):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #include alpha channel
        self.alpha = alpha
        if alpha == True:
            pass
        elif alpha == False:
            self.texture = texture.convert()

        #transform the texture to correct size when creating object
        self.texture = pygame.transform.scale(texture, (width, height))
class properties_text:          #this is to define properties of text
    def __init__(self, name, texture, x, y):
        self.name = name
        self.texture = texture
        self.x = x
        self.y = y

class update:
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

        wait = input("Enter to exit. ")
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


    def define(name, w, h):             #define the window          
        window = pygame.display.set_mode((w, h))                #create window  
        pygame.display.set_caption(name)                        #create name
        return window

    def window(window, display, display_sprite, foreground, text_foreground, clock, debug):                #update routine
        length = len(display)       #find the length of the display array to find how many textures there are to load
        length = int(length)        #turn the str into int

        #get the texture and find it's x + y
        #v standing for variable
        #for creating the background
        #window.fill((255, 255, 255))  
        for v in range(length):

            #find the texture
            texture = display[v].texture

            #find the coords
            x = display[v].x
            y = display[v].y
            
            
            window.blit(texture, [x, y])

        #for creating sprites
        length = len(display_sprite)       #fond the length of the display array to find how many textures there are to load
        length = int(length)        #turn the str into int
        #print(display_sprite)
        for v in range(length):
            #find the texture
            texture = display_sprite[v].texture

            #find the coords
            x = display_sprite[v].x
            y = display_sprite[v].y
            
            window.blit(texture, [x, y])


        #foreground
        length = len(foreground)            #find the length of the foreground
        length = int(length)                #change to int

        #v standing for variable
        for v in range(length):
            #find the texture
            texture = foreground[v].texture           #find the texture

            #find the coords
            x = foreground[v].x              #find the x coord
            y = foreground[v].y               #find the x coord
            
            window.blit(texture, [x, y])            #paste that onto the screen

        
        #text_foreground
        length = len(text_foreground)            #find the length of the text_foreground
        length = int(length)                #change to int

        #v standing for variable
        for v in range(length):
            #find the texture
            texture = text_foreground[v].texture            #find the texture

            #find the coords
            x = text_foreground[v].x               #find the x coord
            y = text_foreground[v].y               #find the x coord
            
            window.blit(texture, [x, y])            #paste that onto the screen
        

        #debug
        if debug == True:
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
            fps_text = font.render("FPS: {}".format(fps), True, pygame.Color("WHITE"))
            window.blit(fps_text, [20, 40])
            
        #update
        pygame.display.update()     #only update the screen at this time

class player:
    def collisions(player_x, player_y, player_width, player_height, list, index):     #get the player pos, the collision list and the index to check if collided
        if player_x <= list[index].x and player_x + player_width >= list[index].x + list[index].width:      #check for x coord if collied with player
            if player_y <= list[index].y and player_y + player_height >= list[index].y + list[index].height:    #check for y coord if collied with player
                return list[index].name

    
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