# Mainscript which is where the game runs
import core as system
from random import randint

bouncyBall = system.spriteObject("cirlce", "examples/assets/textures/circle.png", system.vector2f(0, 0), system.vector2i(50, 50))
velocity = system.vector2i(randint(2, 5), randint(2, 5))

def wallBounce(window: system.window):
    global velocity
    if bouncyBall.leftBorder(bouncyBall.getPosition(), 0):
        velocity.x *= -1

    if bouncyBall.rightBorder(bouncyBall.getPosition(), window.getWidth() - bouncyBall.getSize().x):
        velocity.x *= -1

    if bouncyBall.topBorder(bouncyBall.getPosition(), 0):
        velocity.y *= -1

    if bouncyBall.bottomBorder(bouncyBall.getPosition(), window.getHeight() - bouncyBall.getSize().y):
        velocity.y *= -1


# Runs only once
def start(window: system.window) -> None:
    window.pushToQueue(bouncyBall)
    window.setTargetFramerate(60)

# Runs every frame
def update(window: system.window) -> None:
    window.renderObjects()

# Runs at 60fps (16.666... ms)
def fixedUpdate(window: system.window, deltaTime: float) -> None:
    window.updateEvents()

    if window.getEvent("QUIT") or window.getKey("ESCAPE"):
        window.stopRunning()

    # Update the position of the ball
    bouncyBall.incrementPosition(velocity)  

    # Change the velocity of the ball if it hits a wall
    wallBounce(window)

# Runs once at the end
def end() -> None:
    pass

