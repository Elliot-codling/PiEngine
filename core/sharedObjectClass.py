# Sprites and text have similar functions
# This class prevents functions from being dulicated in code
class sharedData:
    # === Set m_initialised as false ===
    def __init__(self) -> "sharedData":
        self.m_initialised = False

    # === Set functions ===
    def setID(self, objectID: str) -> None:
        self.m_objectID = objectID

    def setLayer(self, layer: int) -> None:
        # Lower number = closer to camera
        self.m_layer = layer

    # === Get functions ===
    def getID(self) -> str:
        return self.m_objectID
    
    def getLayer(self) -> int:
        return self.m_layer
    
    # === Initialiser ===
    def initialiseObject(self) -> None:
        self.m_initialised = True

    def isInitialised(self) -> bool:
        return self.m_initialised
    