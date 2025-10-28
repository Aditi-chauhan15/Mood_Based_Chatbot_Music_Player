import tkinter as tk

class ChatbotUI:
    def __init__(self, root, mood_detector, music_player):
        self.root = root
        self.mood_detector = mood_detector
        self.music_player = music_player
        
        self.root.title("Mood-based Chatbot Music Player")
        
        self.chat_label = tk.Label(root, text="Enter your mood:")
        self.chat_label.pack(pady=5)
        
        self.user_input = tk.Entry(root, width=40)
        self.user_input.pack(pady=5)
        
        self.submit_btn = tk.Button(root, text="Detect Mood and Play Music", command=self.process_input)
        self.submit_btn.pack(pady=5)
        
        self.output_label = tk.Label(root, text="", fg="blue")
        self.output_label.pack(pady=5)
        
        self.stop_btn = tk.Button(root, text="Stop Music", command=self.music_player.stop_music)
        self.stop_btn.pack(pady=5)
    
    def process_input(self):
        user_text = self.user_input.get()
        detected_mood = self.mood_detector.detect_mood(user_text)
        self.output_label.config(text=f"Detected Mood: {detected_mood.capitalize()}")
        self.music_player.play_music_by_mood(detected_mood)
