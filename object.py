#object file
import pygame

#keeps track of the frames that have been passed
#used for animation, must create a counter object
class counter:
    def __init__(self):
        self.frames = 0

    #update the frames by 1
    def update(self):
        self.frames += 1

#manipulate an object
class object:
    def setAngle(self, angle):          #set a specific angle for the object to look in
        texture = pygame.image.load(self.loaded_texture)
        self.texture = pygame.transform.rotate(pygame.transform.scale(texture, (self.width, self.height)), angle)             #rotates the object and setss its new angle
        self.rotation = angle    
        self.mask = pygame.mask.from_surface(self.texture)    

    def animate(self, animationList, frameWait, counter, flipX = 0, flipY = 0, alpha = False):
        if counter.frames >= self.animationTime:            #check if it is the right time to change the texture
            properties_object.reload_texture(self, animationList[self.animationStage], self.width, self.height, alpha)            #change the texture of the object
            self.texture = pygame.transform.flip(self.texture, flipX, flipY)
            self.animationTime = counter.frames + frameWait         #update when the object should change texture next
        
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

    def reload_texture(self, loaded_texture, width, height, alpha=False):          #reloads the texture and can resize it all in one line!
        if type(loaded_texture) == str:                             #check if the tetxure coming ahs already been loaded or is a request for a new file location
            loaded_texture = pygame.image.load(loaded_texture)
        
        self.texture = pygame.transform.scale(loaded_texture, (width, height))           #scale this object accordingly
        self.mask = pygame.mask.from_surface(self.texture)          #recreates the mask that has initially been made
        #no longer needed to return the texture

        #include alpha channel
        self.alpha = alpha
        if alpha == True:
            pass
        elif alpha == False:
            self.texture = self.texture.convert()
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
