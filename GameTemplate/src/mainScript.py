# Mainscript which is where the game runs
import core as engine

# Runs only once
def start(window: engine.window):
    pass

# Runs every frame
def update(window: engine.window): 
    window.renderObjects()

# Runs at 60fps (16.666... ms)
def fixedUpdate(window: engine.window, deltaTime: float):     
    window.updateEvents()

    if window.getEvent("QUIT") or window.getKey("ESCAPE"):
        window.stopRunning()
        
# Runs once at the end
def end():
    pass

