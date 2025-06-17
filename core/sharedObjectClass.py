# Sprites and text have similar functions
# This class prevents functions from being dulicated in code
class sharedData:
    # === Set functions ===
    def setID(self, objectID):
        self.m_objectID = objectID

    def setLayer(self, layer):
        # Lower number = closer to camera
        self.m_layer = layer

    # === Get functions ===
    def getID(self):
        return self.m_objectID
    
    def getLayer(self):
        return self.m_layer
    
    # === Initialiser ===
    def initialiseObject(self):
        self.m_initialised = True

    def isInitialised(self):
        return self.m_initialised
    