#input file
import pygame

#updates the events of the program
#checks if the close button has been pressed as well as updates the current key pressed
class event:
    def update(window):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                window.setRunStatus(False)

        return events, keys

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

#mouse capability
class mouse:          
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
        
