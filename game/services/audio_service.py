import pygame
class AudioService:
    """An audio service inteface.

    The responsibility of AudioService is to handle the audio assets for a game.
    """

    def initialize(self):
        """Initializes the mixer to play sounds"""
        pygame.mixer.init()

    def stop(self):
        pygame.mixer.stop()
        
    def playsound(self, sound):
        playsound = pygame.mixer.Sound(sound)
        playsound.play()
        