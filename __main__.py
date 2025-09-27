# Starts the program if python3 ./PiEngine is called
def main():
    # Create runtime
    from main import Runtime
    app = Runtime.Runtime("main.src.mainScript", "Pygame Window", 1280, 720)

    # Call the update function
    app.update()

    # Call the end function
    app.end()

# Run if the file name is __main__
if __name__ == "__main__":
    main()