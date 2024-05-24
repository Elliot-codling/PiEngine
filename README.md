Changes to the preview build:

- Music class has been modified and will not be currently functional
- New event class has been created:
    - Called by PiEngine_9_0_0.event.update()
    - gets the current keys pressed
    - keys can be detected by PiEngine_9_0_0.keys[]
    - updates the events recieved (e.g close button pressed)
    - Called once per clock.tick cycle
    - Can check if the game is still running with PiEngine.run

- properties_text.reload_text requires self, it does not return a value instead changing texture with self.texture
- window.update debug functions do not currently work
- Added PiEngine_9_0_0.directory to get the current directory of the code execution