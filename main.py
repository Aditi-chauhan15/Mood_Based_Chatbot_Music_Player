import tkinter as tk
from mood_detector import MoodDetector
from music_player import MusicPlayer
from chatbot_ui import ChatbotUI

if __name__ == "__main__":
    music_directory = "music_directory"  

    mood_detector = MoodDetector()
    music_player = MusicPlayer(music_directory)

    root = tk.Tk()
    app = ChatbotUI(root, mood_detector, music_player)
    root.mainloop()
