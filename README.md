Changes to the preview build:

- Added SFX class
    - Used for sounds such as walking, jumping etc
    - Define by PiEngine_8_0_0.sfx()
    - Choose the file location of the sound
    - Choose which channel the sound will be played on
    - PiEngine_8_0_0.sfx.playSound() will play the sound

- Music class has been modified to use pygame.mixer.channel
    - You can define a music object with PiEngine_8_0_0.music()
    - Track requries [], inside will be a directory of the track
    - Choose which channel to play on 
    - To loop songs, use your [loop object].loop()  Additionally, these songs can be shuffled to randomise the next song
    - PiEngine_8_0_0.music.play() can play a specific song from a track
    - PiEngine_8_0_0.music.stop() will stop the channel from playing

- New event class has been created:
    - Called by PiEngine_8_0_0.event.update()
    - Used to get keys that are being pressed
    - returns events
    - keys can be detected by PiEngine_8_0_0.keys[]
    - updates the events recieved (e.g close button pressed)
    - Called once per clock.tick cycle
    - Can check if the game is still running with PiEngine_8_0_0.run
    - event.getKeydown() and event.getKeyup() requires the events variable. To check the required key, use pygame.[KEY] (Look at pygame docs for key types)
    - This returns true if the key specified has been pressed

- object.setAngle() has been modifed so that non-right angles specified work correctly

- object.collision_rect() box_list parameter changed to display

- object.collision_mask() box_list parameter changed to display
- added collidableLayers[] parameter, that specifies what layers the object provided can collide with

- Removed canvas offset values from [left, right, up, down] functions in object() class

- properties_object() now inherits the object() class

- name parameter in properties_object() has been renamed to id

- alpha attrtibute to properties_object() is now default False

- name parameter in properties_text() has been renamed to id

- properties_text.reload_text requires self, it does not return a value instead changing texture with self.texture

- objectname parameter in mouse() class has been renamed to objectId
- boxName parameter in mouse() class has been renamed to objectName

- window.writeDebug_file() has been removed

- window.update debug functions now correctly work without using counter.update()
    - debug attribute requires the following: [layer, clock, color]
    - Layer will highlight objects that have that assigned layer
    - Clock will get the frametime stats
    - Color will Change the frametime text and the highlighted objects color
    - Debug is the last process in the update method
    - To reset frametime stats, press F1.

- window.delete_layer has been improved. This does not affect its input or output

- Removed Canvas

- Addded PiEngine_8_0_0.initDebug() which will reset the frametime stats

- Removed import time

- Added PiEngine_8_0_0.directory to get the current directory of the code execution