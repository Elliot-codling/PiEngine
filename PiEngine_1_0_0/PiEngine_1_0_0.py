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

class update():
    global debug_state
    debug_state = False
    def pygame_debug():
        import sys              #import system files
        #steps on installing pygame / pip onto os
        print("It seems like Pygame is not installed. What OS are you using?")
        print("")
        print("Windows (1)")
        print("Mac OS & Linux (2)")
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

    def debug(debug, x, y, width, height):            #state if debug needs to be activated, give player x and y coords
        global debug_state
        debug_state = debug

        global player_x, player_y, player_width, player_height
        player_x = x               #top left x coords
        player_y = y             #bottom right x coord
        player_width = width               #top left y coord
        player_height = height             #bottom right y coord

    def define(name, w, h):             #define the window
        global window                   #need to globalise to update            
        window = pygame.display.set_mode((w, h))                #create window  
        pygame.display.set_caption(name)                        #create name

    def window(display, display_sprite, foreground, text_foreground, clock):                #update routine
        length = len(display)       #find the length of the display array to find how many textures there are to load
        length = int(length)        #turn the str into int

        #get the texture and find it's x + y
        #v standing for variable
        #for creating the background
        #window.fill((255, 255, 255))  
        for v in range(length):

            #find the texture
            texture = (display[v][0])

            #find the coords
            x = (display[v][1][0])
            y = (display[v][1][1])
            
            
            window.blit(texture, [x, y])

        #for creating sprites
        length = len(display_sprite)       #fond the length of the display array to find how many textures there are to load
        length = int(length)        #turn the str into int

        for v in range (length):
            #find the texture
            texture = (display_sprite[v][0])

            #find the coords
            x = (display_sprite[v][1][0])
            y = (display_sprite[v][1][1])
            
            window.blit(texture, [x, y])


        #foreground
        length = len(foreground)            #find the length of the foreground
        length = int(length)                #change to int

        #v standing for variable
        for v in range (length):
            #find the texture
            texture = (foreground[v][0])            #find the texture

            #find the coords
            x = (foreground[v][1][0])               #find the x coord
            y = (foreground[v][1][1])               #find the x coord
            
            window.blit(texture, [x, y])            #paste that onto the screen

        
        #text_foreground
        length = len(text_foreground)            #find the length of the text_foreground
        length = int(length)                #change to int

        #v standing for variable
        for v in range (length):
            #find the texture
            texture = (text_foreground[v][0])            #find the texture

            #find the coords
            x = (text_foreground[v][1][0])               #find the x coord
            y = (text_foreground[v][1][1])               #find the x coord
            
            window.blit(texture, [x, y])            #paste that onto the screen
        

        #debug
        if debug_state == True:
            color = (255, 255, 0)
            #pygame.draw.rect(window, color, pygame.Rect(player_x, player_y, player_width, player_height))          
            #create the debug rectangle to show where the hitbox is on sprites
        
            fps = int(clock.get_fps())
            font = pygame.font.SysFont(None, 30)
            fps_text = font.render("FPS: {}".format(fps), True, pygame.Color("WHITE"))
            window.blit(fps_text, (20, 40))
            
        #update
        pygame.display.update()     #only update the screen at this time

class player():
    def collisions(player_x, player_y, player_width, player_height, image_list, v):     #get the player pos, the collision list and the index to check if collided
        image = image_list[v][0]            #specify the image
        image_width = image.get_size()[0]       #x
        image_height = image.get_size()[1]      #y

        image_collided = None         #return nothing
        if player_x <= image_list[v][1][0] + image_width and player_x + player_width >= image_list[v][1][0] and player_y <= image_list[v][1][1] + image_height and player_y + player_height >= image_list[v][1][1]:
            image_collided = image_list[v][0]  #return the image that was collided with      

        return image_collided

    
    def left(player_screenx, player_x, vel):
        #stop the players screen x coord if it gets too close to the left border
        #return the values of the player's x coord and the players screen x coord 
        if player_screenx > left_border:
            player_screenx -= vel
            player_x -= vel

        return player_screenx, player_x

    def right(player_screenx, player_x, vel):
        #stop the players screen x coord if it gets too close to the right border
        #return the values of the player's x coord and the players screen x coord 
        if player_screenx < right_border:
            player_screenx += vel
            player_x += vel

        return player_screenx, player_x

    def up(player_screeny, player_y, vel):
        #stop the player screen y coord if it gets too close to the top border
        #return the values of the players x coord and the players screen x coord
        if player_screeny > top_border:
            player_screeny -= vel
            player_y -= vel

        return player_screeny, player_y

    def down(player_screeny, player_y, vel):
        #stop the player screen y coord if it gets too close to the bottom border
        #return the values of the players x coord and the players screen x coord
        if player_screeny < bottom_border:
            player_screeny += vel
            player_y += vel

        return player_screeny, player_y

    #define the left border of the screen to stop moving
    def left_border(x):
        global left_border
        left_border = x

    #define the right border of the screen to stop moving
    def right_border(x):
        global right_border
        right_border = x

    #define the up border of the screen to stop moving
    def top_border(x):
        global top_border
        top_border = x

    #define the bottom border of the screen to stop moving
    def bottom_border(x):
        global bottom_border
        bottom_border = x