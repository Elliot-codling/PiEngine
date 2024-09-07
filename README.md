Changes to the preview branch:

- update in event class now takes window

- "run" and "directory" variables are no longer accessible variables
- To access the directory use: engine.directory() which will return the location of the application directory
- To access if the application is running use: window.isRunning()
- To set the current status of the application use: engine.setRunStatus(status)
- To find if music is available to play, use: music.isActive() -> Bool

- New class has been created called debug()
- This should not be accessed directory, these functions are for the engines use not your application
- All debugging functions from window.update() have been moved to debug() class
- Added checkMusic() -> Used for the music class only

- Updated PiEngine Documentation

- PiEngine has been seperated into several files to reduce complexity
- To import PiEngine type: import PiEngine. This must be done outside of the folder PiEngine

- Added options to save / load varibales
- Saves to a CSV file called "data.csv"
- deleteAll() -> Deletes all current keys
- deleteKey(name) -> Deletes a specific key
- getVariable(name) -> Returns the value of a key
- setVariable(name, data) -> Saves a variable with its name and data
- hasKey(name) -> Returns if a key exists in the database
- getKyes() -> Returns all current keys in the database

- Added engine.appendForDeletion(object)
- Added deleteObjects(display) -> display
- You can add items to a list to be deleted later in the display list

- Updated engine.counter to be an object instead of a variable
- To define the counter: counter = engine.counter()
- To update the counter: counter.update()
- To get the current frames that have passed: counter.frames
- Updated object.animate so that it works with the new counter() class and the updaed reload texture
- Updated properties_object.reload_texture()
- Now takes alpha as an option argument

- To reduce the performance impact of the debugger, an interval has been added.
- The interval is the number of frames that is required to pass before updating the text.