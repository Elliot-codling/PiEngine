# Starts the program if python3 ./GameTemplate is called
def main():
    # Create runtime
    from src import runtime as system
    runtimeWindow = system.runtime("Pygame Window", 1280, 720, (0, 0, 0))

    # Call the update function
    runtimeWindow.update()

    # Call the end function
    runtimeWindow.end()

# Run if the file name is __main__
if __name__ == "__main__":
    main()