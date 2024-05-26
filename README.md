Changes to the preview build:

- Added SFX class
    - Used for sounds such as walking, jumping etc
    - Define by PiEngine_9_0_0.sfx()
    - Choose the file location of the sound
    - Choose which channel the sound will be played on
    - PiEngine_9_0_0.sfx.playSound() will play the sound

- Music class has been modified to use pygame.mixer.channel
    - You can define a music object with PiEngine_9_0_0.music()
    - Track requries [], inside will be a directory of the track
    - Choose which channel to play on 
    - Can be looped through the track indefinitly
    - If loop is true, the songs can be chosen from randomly
    - PiEngine_9_0_0.music.play() can play a specific song from a track
    - PiEngine_9_0_0.music.stop() will stop the channel from playing

- New event class has been created:
    - Called by PiEngine_9_0_0.event.update()
    - gets the current keys pressed
    - keys can be detected by PiEngine_9_0_0.keys[]
    - updates the events recieved (e.g close button pressed)
    - Called once per clock.tick cycle
    - Can check if the game is still running with PiEngine_9_0_0.run

- alpha attrtibute to properties_object() is now default False

- properties_text.reload_text requires self, it does not return a value instead changing texture with self.texture

- window.writeDebug_file() has been removed

- window.update debug functions now correctly work without using counter.update()
    - debug attribute requires the following: [layer, clock, color]
    - Layer will highlight objects that have that assigned layer
    - Clock will get the frametime stats
    - Color will Change the frametime text and the highlighted objects color
    - Debug is the last process in the update method
    - To reset frametime stats, press F1.

- window.delete_layer has been improved. This does not affect its input or output

- Addded PiEngine_9_0_0.initDebug() which will reset the frametime stats

- Removed import time

- Added PiEngine_9_0_0.directory to get the current directory of the code execution