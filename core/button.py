from .sprite import *
from .text import *
from .sharedObjectClass import *
from .vector import *
from .input import windowInput
from .debugHandler import *

# TODO: Add comments
class transform:
    def setPosition(self, position: vector2f) -> None:
        self.m_textObject.setPosition(position)
        self.m_spriteObject.setPosition(position - vector2f(self.m_paddingSize, self.m_paddingSize))

    def incrementPosition(self, position: vector2f) -> None:
        self.m_textObject.incrementPosition(position)
        self.m_spriteObject.incrementPosition(position)

    def getPosition(self) -> vector2f:
        return self.m_spriteObject.getPosition()

    def getSize(self) -> vector2i:
        return self.m_spriteObject.getSize()
    

class flags:
    def isClicked(self, window: "engine.window") -> bool:
        if not window.mouseButtonClicked("LEFT"):
            return False
        
        if window.getMouseCollisionByObject(self.m_spriteObject):
            return True
        return False


class button(sharedData, flags, transform):
    def __init__(self, objectID: str, content: str, position: vector2f, fontSize: int, textColor = (255, 255, 255), layer = 0) -> "button":
        super().__init__()
        self.setID(objectID)

        self.m_textObject = textObject(f"{objectID}Text", content, position, fontSize, textColor, layer)
        self.m_spriteObject = spriteObject(f"{objectID}Sprite", "core/assets/invisable_button.png", position, self.m_textObject.getSize(), False, layer)

        self.setLayer(layer)
        self.m_paddingSize = 0

        self.initialiseObject()

    def replaceText(self, content: str) -> None:
        self.m_textObject.replaceText(content)
        self.m_spriteObject.setSize(self.m_textObject.getSize())

    def setTextPadding(self, padding: int) -> None:
        self.m_spriteObject.incrementPosition(vector2f(-padding, -padding))
        newSpriteSize = self.m_spriteObject.getSize() + vector2i(padding * 2, padding * 2)
        self.m_spriteObject.setSize(newSpriteSize)

        self.m_paddingSize = padding

    def render(self, surface: pygame.Surface) -> None:
        self.m_spriteObject.render(surface)
        self.m_textObject.render(surface)