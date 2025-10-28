import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        self.music_dir = music_dir
        pygame.mixer.init()

    def play_music_by_mood(self, mood):
        mood_folder = os.path.join(self.music_dir, mood)
        if not os.path.exists(mood_folder):
            print("No music found for this mood.")
            return
        
        songs = [f for f in os.listdir(mood_folder) if f.endswith('.mp3')]
        if not songs:
            print("No songs found in this mood folder.")
            return
        
        song_path = os.path.join(mood_folder, songs[0])
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()
