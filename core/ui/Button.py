# Used for creating a simple button
# Consists of a textObject and a spriteObject
# textObject is the text of the button while the spriteObject is to allow collision
# Sprite allows for a better collision as text collision only works if the mouse is over colored pixels

# Import required scripts
from .sprite import *
from .text import *
from .sharedObjectClass import *
from .vector.vector import *
from ..log.Logger import *
from .. import Application as system

# === Transform the object ===
class transform:
    # === Transform positions ===
    def setPosition(self, position: vector2f) -> None:
        self.m_text.setPosition(position)
        # Account for the padding size
        self.m_spriteObject.setPosition(position - vector2f(self.m_paddingSize, self.m_paddingSize))

    def incrementPosition(self, position: vector2f) -> None:
        self.m_textObject.incrementPosition(position)
        self.m_spriteObject.incrementPosition(position)

    def getPosition(self) -> vector2f:
        return self.m_spriteObject.getPosition()

    # === Sizes ===
    # Size is determined by padding as well as text size
    def getSize(self) -> vector2i:
        return self.m_spriteObject.getSize()
    
# === Flag statements ===
# Returns a bool
class flags:
    # Determine if the button has been pressed, return a bool
    def isClicked(self, window: "system.window") -> bool:
        if not window.mouseButtonClicked("LEFT"):
            return False
        
        if window.getMouseCollisionByObject(self.m_spriteObject):
            return True
        return False


class button(sharedData, flags, transform):
    # === Create button ===
    def __init__(self, objectID: str, content: str, position: vector2f, fontSize: int, textColor = (255, 255, 255), layer = 0) -> "button":
        # Since this is an object it needs a layer, id and requires to be initialised
        super().__init__()
        self.setID(objectID)

        # Create both the text and sprite objects
        self.m_textObject = textObject(f"{objectID}Text", content, position, fontSize, textColor, layer)
        self.m_spriteObject = spriteObject(f"{objectID}Sprite", "core/assets/invisable_button.png", position, self.m_textObject.getSize(), False, layer)

        self.setLayer(layer)

        # Padding around the text in pixels
        self.m_paddingSize = 0

        # Initialise object
        self.initialiseObject()

    # Replace the text of the button
    def replaceText(self, content: str) -> None:
        self.m_textObject.replaceText(content)
        self.m_spriteObject.setSize(self.m_textObject.getSize())

    # Change the padding size around the text
    def setTextPadding(self, padding: int) -> None:
        self.m_spriteObject.incrementPosition(vector2f(-padding, -padding))
        newSpriteSize = self.m_spriteObject.getSize() + vector2i(padding * 2, padding * 2)
        self.m_spriteObject.setSize(newSpriteSize)

        self.m_paddingSize = padding

    # Render the button
    def render(self, surface: pygame.Surface) -> None:
        self.m_spriteObject.render(surface)
        self.m_textObject.render(surface)