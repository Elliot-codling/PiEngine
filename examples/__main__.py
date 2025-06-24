# Starts the program if python3 ./PiEngine/examples is called
# Used for selecting which example program to run
from enum import Enum

class demo(Enum):
    BLANKWINDOW = 1
    BOUNCYBALL = 2
    COLLISION = 3
    BUTTON = 4

def openProgram(programNumber: int):
    import runtime as system
    import sys, os
    sys.path.insert(0, f"{os.getcwd()}")    # Get core folder 
    
    mainDirectory = ""
    if programNumber == demo.BLANKWINDOW.value: mainDirectory = "BlankWindow"
    elif programNumber == demo.BOUNCYBALL.value: mainDirectory = "BouncyBall"
    elif programNumber == demo.COLLISION.value: mainDirectory = "Collision"
    elif programNumber == demo.BUTTON.value: mainDirectory = "Button"
    else:
        print(f"Invalid program number: {programNumber}. Terminating session.")

    runtimeWindow = system.runtime(mainDirectory, mainDirectory, 1280, 720)
    runtimeWindow.update()
    runtimeWindow.end()

def main():    
    print("Welcome to PiEngine examples. These are some demo projects that can help inspire your code.\n")
    for index in range(1, len(demo) + 1):
        print(f"{index}. {demo(index).name.capitalize()}")

    programNumber = 0
    while programNumber == 0:
        try:
            programNumber = int(input(">>> "))
        except:
            print("Invalid input. Try again.")
            programNumber = 0

    openProgram(programNumber)

# Run if the file name is __main__
if __name__ == "__main__":
    main()