# === External libs ===
import pygame
# === Inherited classes ===
# === Internal classes ===
from ..scene.Scene import *

class Renderer():
    def renderBlankScene(self, surface, color):
        surface.fill(color)
        pygame.display.flip()

    def renderScene(self, surface, color, scene: "Scene"):
        surface.fill(color)

        #self.sortQueue()
        spriteList = scene.getSpriteQueue()
        textList = scene.getTextQueue()
        spriteRenderList = scene.getSpriteRenderQueue()
        
        for object in spriteList:   
            if object.isInitialised():
                object.render(surface)

        for object in textList:
            if object.isInitialised():
                object.render(surface)
        
        pygame.display.flip()