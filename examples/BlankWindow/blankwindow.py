# Mainscript which is where the game runs
import core as system

# Runs only once
def start(window: system.window) -> None:
    window.setTargetFramerate(60)

# Runs every frame
def update(window: system.window) -> None:
    window.renderObjects()

# Runs at 60fps (16.666... ms)
def fixedUpdate(window: system.window, deltaTime: float) -> None:
    window.updateEvents()

    if window.getEvent("QUIT") or window.getKey("ESCAPE"):
        window.stopRunning()
    
# Runs once at the end
def end() -> None:
    pass

