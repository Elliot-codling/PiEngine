# Mainscript which is where the game runs
import core as system

# Square box
squareBox = system.spriteObject("box", "examples/assets/textures/red.png", system.vector2f(0, 0), system.vector2i(250, 250))
greenTex = system.loadImage("examples/assets/textures/green.png")
redTex = system.loadImage("examples/assets/textures/red.png")

# Asteroid
asteroid = system.spriteObject("rock", "examples/assets/textures/rock_brown.png", system.vector2f(0, 0), system.vector2i(250, 250), True)
asteroidBox = system.spriteObject("rockBox", redTex, system.vector2f(0, 0), system.vector2i(250, 250))

# Collision with the asteroid code
def collisionWithMask(window: system.window):
    if window.mouseCollideMaskByObject(asteroid):
        asteroidBox.replaceTexture(greenTex, system.vector2f(250, 250))
        return
    
    asteroidBox.replaceTexture(redTex, system.vector2f(250, 250))
    
# Collision with the box code
def collisionWithBox(window: system.window):
    if window.mouseCollideBoxByObject(squareBox):
        squareBox.replaceTexture(greenTex, system.vector2f(250, 250))
        return
    
    squareBox.replaceTexture(redTex, system.vector2f(250, 250))

# Runs only once
def start(window: system.window) -> None:
    # Set the square y position to the middle of the screen
    squareBoxPosition = system.vector2f(100, window.getHeight() / 2 - squareBox.getSize().y / 2)
    squareBox.setPosition(squareBoxPosition)
    window.pushToQueue(squareBox)

    asteroidPosition = system.vector2f(window.getWidth() - (100 + asteroid.getSize().x), window.getHeight() / 2 - asteroid.getSize().y / 2)
    asteroid.setPosition(asteroidPosition)
    asteroidBox.setPosition(asteroid.getPosition())
    window.pushToQueue(asteroidBox)
    window.pushToQueue(asteroid)
    
    window.setTargetFramerate(60)

# Runs every frame
def update(window: system.window) -> None:
    window.renderObjects()

    collisionWithBox(window)
    collisionWithMask(window)


# Runs at 60fps (16.666... ms)
def fixedUpdate(window: system.window, deltaTime: float) -> None:
    window.updateEvents()

    if window.getEvent("QUIT") or window.getKey("ESCAPE"):
        window.stopRunning()
    
# Runs once at the end
def end() -> None:
    pass

