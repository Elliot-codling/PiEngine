# Starts the program if python3 ./PiEngine is called
def main():
    # Create runtime
    import runtime as system
    runtimeWindow = system.runtime("src.mainScript", "Pygame Window", 1280, 720)

    # Call the update function
    runtimeWindow.update()

    # Call the end function
    runtimeWindow.end()

# Run if the file name is __main__
if __name__ == "__main__":
    main()