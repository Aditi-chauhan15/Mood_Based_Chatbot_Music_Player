class MoodDetector:
    def __init__(self):
        self.mood_keywords = {
            "happy": ["happy", "joy", "excited", "great", "good"],
            "sad": ["sad", "down", "unhappy", "depressed", "blue"],
            "relaxed": ["calm", "relaxed", "peaceful", "serene"],
            "energetic": ["energetic", "active", "lively", "burst"]
        }
    
    def detect_mood(self, text):
        text = text.lower()
        for mood, keywords in self.mood_keywords.items():
            for word in keywords:
                if word in text:
                    return mood
        return "neutral"
