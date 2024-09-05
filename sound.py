#Sound file
import pygame, random
#used for sfx sounds
class sfx:
    def __init__(self, soundDirectory, channel):        #laods the song, and adds it to a channel
        self.sound = pygame.mixer.Sound(soundDirectory)
        self.channel = channel

    #play sfx sound
    def playSound(self, playIfBusy=False):
        #if the playIfBusy is true, then overwrite the channel even if it is busy
        if pygame.mixer.Channel(self.channel).get_busy() and playIfBusy == False:
            return
        pygame.mixer.Channel(self.channel).play(self.sound)

    

#used for music
class music:
    def __init__(self, track, channel=0):
        #define a track with [], it can have multiple songs
        #choose a channel to play on
        #can loop through if the track gets to the end
        self.track = track
        self.channel = channel
        self.currentTrack = 0
        self.active = debug.checkMusic()

    #used to go through a whole track
    def loop(self, shuffle):
        if pygame.mixer.Channel(self.channel).get_busy():
            return
        if shuffle:
            self.currentTrack = random.randint(0, len(self.track) - 1)
        pygame.mixer.Channel(self.channel).play(pygame.mixer.Sound(self.track[self.currentTrack]))

        if self.currentTrack + 1 == len(self.track):
            self.currentTrack = 0
        else:
            self.currentTrack += 1

    #used to play just one song on a track
    def play(self, trackNumber, playIfBusy=False):
        #if the playIfBusy is true, then overwrite the channel even if it is busy
        if pygame.mixer.Channel(self.channel).get_busy() and playIfBusy == False:
            return
        
        pygame.mixer.Channel(self.channel).play(pygame.mixer.Sound(self.track[trackNumber]))

    #used to stop the channel playing
    def stop(self):
        pygame.mixer.Channel(self.channel).stop()

    #returns bool if the music is active
    def isActive(self):
        return self.active
    

class debug:
    #used with the music class only
    #returns mbool if the music is active
    #if false sends an error out to the user
    def checkMusic():
        try:
            pygame.mixer.init()         #initilise music
            return True
        except pygame.error:
            debug.music()            #if the audio driver hasn't been found
            return False
        
    def music():          #print out the error if an audio driver hasnt been found
        print("It seems like there is no Audio Driver installed on your device.")
        print("Sound will be deactivated.")