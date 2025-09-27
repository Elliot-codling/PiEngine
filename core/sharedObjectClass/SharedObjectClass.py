# Sprites and text have similar functions
# This class prevents functions from being dulicated in code
class SharedData:
    # === Set m_initialised as false ===
    def __init__(self) -> "SharedData":
        self.m_initialised = False
        self.m_objectIsVisible = False

    # === Set functions ===
    def setID(self, objectID: str) -> None:
        self.m_objectID = objectID

    def setLayer(self, layer: int) -> None:
        # Lower number = closer to camera
        self.m_layer = layer

    def setObjectVisable(self, value: bool) -> None:
        self.m_objectIsVisible = value

    # === Get functions ===
    def getID(self) -> str:
        return self.m_objectID
    
    def getLayer(self) -> int:
        return self.m_layer
    
    def isObjectVisable(self) -> bool:
        return self.m_objectIsVisible
    
    # === Initialiser ===
    def initialiseObject(self) -> None:
        self.m_initialised = True

    def isInitialised(self) -> bool:
        return self.m_initialised
    