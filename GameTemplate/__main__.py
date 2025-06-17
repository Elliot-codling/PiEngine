# Starts the program if python3 ./GameTemplate is called
def main():
    # Create runtime
    from src import runtime as engine
    runtimeWindow = engine.runtime("Pygame Window", 1280, 720)

    # Call the update function
    runtimeWindow.update()

    # Call the end function
    runtimeWindow.end()

# Run if the file name is __main__
if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, f"{os.getcwd()}")    # Get core folder 

    main()