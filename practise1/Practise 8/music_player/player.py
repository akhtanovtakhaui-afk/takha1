import pygame
import os


class MusicPlayer:
    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist
        self.current_index = 0
        self.is_playing = False

    def load_track(self):
        pygame.mixer.music.load(self.playlist[self.current_index])

    def play(self):
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track_name(self):
        return os.path.basename(self.playlist[self.current_index])

    def get_position_seconds(self):
        if not self.is_playing:
            return 0

        pos = pygame.mixer.music.get_pos()
        if pos < 0:
            return 0

        return pos // 1000