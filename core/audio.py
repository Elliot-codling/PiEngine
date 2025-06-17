import pygame, random
pygame.mixer.init()
class sfx:    
    def __init__(self, sfxDirectory, channelNumber):
        
        self.m_vfxSound = pygame.mixer.Sound(sfxDirectory)
        self.m_channelNumber = channelNumber

    def playerSound(self, playIfBusyChannel = False):
        if pygame.mixer.Channel(self.m_channelNumber).get_busy() and not playIfBusyChannel:
            return
        pygame.mixer.Channel(self.m_channelNumber).play(self.m_vfxSound)

class music:
    def __init__(self, musicTrack: list, channelNumber):
        self.m_musicTrack = musicTrack
        self.m_channelNumber = channelNumber
        self.m_currentTrackNumber = 0
        
    def play(self, trackNumber, overWriteChannel = False):
        if pygame.mixer.Channel(self.m_channelNumber).get_busy() and not overWriteChannel or trackNumber > len(self.m_musicTrack) - 1:
            return 
        pygame.mixer.Channel(self.m_channelNumber).play(pygame.mixer.Sound(self.m_musicTrack[trackNumber]))

    def loop(self, shuffle = False):
        if pygame.mixer.Channel(self.m_channelNumber).get_busy():
            return
        if shuffle:
            self.m_currentTrackNumber = random.randint(0, len(self.m_musicTrack) - 1)

        pygame.mixer.Channel(self.m_channelNumber).play(pygame.mixer.Sound(self.m_musicTrack[self.m_currentTrackNumber]))

        if self.m_currentTrackNumber == len(self.m_musicTrack) - 1:
            self.m_currentTrackNumber = 0
        else:
            self.m_currentTrackNumber += 1


    def stop(self):
        pygame.mixer.Channel(self.m_channelNumber).stop()

    