# Mainscript which is where the game runs
import core as engine

# Runs only once
def start(window: engine.window) -> None:
    pass
    

# Runs every frame
def update(window: engine.window) -> None:
    window.renderObjects()

# Runs at 60fps (16.666... ms)
def fixedUpdate(window: engine.window, deltaTime: float) -> None:
    window.updateEvents()

    if window.getEvent("QUIT") or window.getKey("ESCAPE"):
        window.stopRunning()
    
# Runs once at the end
def end() -> None:
    pass

