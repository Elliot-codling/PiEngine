#game engine v0.0.2
#BY ELLIOT CODLING
import pygame

class update():
    global debug_state
    debug_state = False
    def list_debug(display, display_sprite, foreground, clock):             #this is debug, needs display, sprite and foreground
        print("NUmber of items in display: {}".format(len(display)))            #items in background
        print("NUmber of items in display sprite: {}".format(len(display_sprite)))          #items in sprites
        print("NUmber of items in foreground: {}".format(len(foreground)))              #items in foreground
        print("")
        print("Display: {}".format(display))            #print the arrays, leave enough room between each
        print("")
        print("")
        print("Display sprite: {}".format(display_sprite))
        print("")
        print("")
        print("Foreground: {}".format(foreground))
        fps = int(clock.get_fps())
        print("FPS: {}".format(fps))
        pygame.time.delay(100)              #stop game for 0.1 seconds

    def debug(debug, x1, x2, y, y2):            #state if debug needs to be activated, give player x and y coords
        global debug_state
        debug_state = debug

        global player_x, player_x_2, player_y, player_y_2
        player_x = x1               #top left x coords
        player_x_2 = x2             #bottom right x coord
        player_y = y                #top left y coord
        player_y_2 = y2             #bottom right y coord

    def define(name, w, h):             #define the window
        global window                   #need to globalise to update            
        window = pygame.display.set_mode((w, h))                #create window  
        pygame.display.set_caption(name)                        #create name

    def window(display, display_sprite, foreground, clock):                #update routine
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

        #debug
        if debug_state == True:
            color = (255, 255, 0)
            pygame.draw.rect(window, color, pygame.Rect(player_x, player_y, player_x_2 - player_x, player_y_2 - player_y))          
            #create the debug rectangle to show where the hitbox is on sprites
        
        
            fps = int(clock.get_fps())
            font = pygame.font.SysFont(None, 30)
            fps_text = font.render("FPS: {}".format(fps), True, pygame.Color("WHITE"))
            window.blit(fps_text, (20, 40))
            
        #update
        pygame.display.update()     #only update the screen at this time





class player():
    def left(player_screenx, player_screenx_2, player_x, player_x_2, vel):
        #stop the players screen x coord if it gets too close to the left border
        #return the values of the player's x coord and the players screen x coord 
        if player_screenx > left_border:
            player_screenx -= vel
            player_screenx_2 -= vel
            player_x -= vel
            player_x_2 -= vel

        return player_screenx, player_x, player_screenx_2, player_x_2

    def right(player_screenx, player_screenx_2, player_x, player_x_2, vel):
        #stop the players screen x coord if it gets too close to the right border
        #return the values of the player's x coord and the players screen x coord 
        if player_screenx < right_border:
            player_screenx += vel
            player_screenx_2 += vel
            player_x += vel
            player_x_2 += vel

        return player_screenx, player_x, player_screenx_2, player_x_2

    def up(player_screeny, player_screeny_2, player_y, player_y_2, vel):
        #stop the player screen y coord if it gets too close to the top border
        #return the values of the players x coord and the players screen x coord
        if player_screeny > top_border:
            player_screeny -= vel
            player_screeny_2 -= vel
            player_y -= vel
            player_y_2 -= vel

        return player_screeny, player_y, player_screeny_2, player_y_2

    def down(player_screeny, player_screeny_2, player_y, player_y_2, vel):
        #stop the player screen y coord if it gets too close to the bottom border
        #return the values of the players x coord and the players screen x coord
        if player_screeny < bottom_border:
            player_screeny += vel
            player_screeny_2 += vel
            player_y += vel
            player_y_2 += vel

        return player_screeny, player_y, player_screeny_2, player_y_2

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