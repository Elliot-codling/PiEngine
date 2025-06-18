import pygame, random
pygame.mixer.init()

# === SFX class ===
# Used for in game sounds, e.g: a door opening
class sfx:
    # === Create the sound ===
    def __init__(self, sfxDirectory: str, channelNumber: int) -> "sfx":
        self.m_vfxSound = pygame.mixer.Sound(sfxDirectory)
        self.m_channelNumber = channelNumber

    # === Play the SFX sound ===
    def playSound(self, playIfBusyChannel = False) -> None:
        if pygame.mixer.Channel(self.m_channelNumber).get_busy() and not playIfBusyChannel:
            return
        pygame.mixer.Channel(self.m_channelNumber).play(self.m_vfxSound)

# === Music class ===
# Used for background music or game tracks
class music:
    # === Create music track ===
    def __init__(self, musicTrack: list, channelNumber: int) -> "music":
        # Music track
        self.m_musicTrack = musicTrack
        # Channel number
        self.m_channelNumber = channelNumber
        # Keeps track of which music piece in the track is playing
        self.m_currentTrackNumber = 0
        
    # === Audio controls ===
    # Used to play a specific piece of music within the sound track
    def play(self, trackNumber: int, overWriteChannel = False) -> None:
        if pygame.mixer.Channel(self.m_channelNumber).get_busy() and not overWriteChannel or trackNumber > len(self.m_musicTrack) - 1:
            return 
        pygame.mixer.Channel(self.m_channelNumber).play(pygame.mixer.Sound(self.m_musicTrack[trackNumber]))

    # Loop the sound track
    # Can be shuffled and tracks can be picked at random
    def loop(self, shuffle = False) -> None:
        
        if pygame.mixer.Channel(self.m_channelNumber).get_busy():
            return
        if shuffle:
            self.m_currentTrackNumber = random.randint(0, len(self.m_musicTrack) - 1)

        # Play music if the channel is not busy
        pygame.mixer.Channel(self.m_channelNumber).play(pygame.mixer.Sound(self.m_musicTrack[self.m_currentTrackNumber]))

        # Increase the track number
        if self.m_currentTrackNumber == len(self.m_musicTrack) - 1:
            self.m_currentTrackNumber = 0
        else:
            self.m_currentTrackNumber += 1

    # Stop all sounds
    def stop(self) -> None:
        pygame.mixer.Channel(self.m_channelNumber).stop()

    