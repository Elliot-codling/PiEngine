from ..scene.Scene import *

class SceneManager:
    def __init__(self):
        self.m_activeScene = None

    def createScene(self, sceneName: str) -> "Scene":
        self.m_activeScene = Scene(sceneName)
        return self.m_activeScene