import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.mood_detector.sentiment_analyzer import SentimentAnalyzer

def run_demo():
    analyzer = SentimentAnalyzer()
    test_texts = [
        "I'm feeling fantastic and joyful today!",
        "I am so down and depressed right now.",
        "It's just an ordinary day, nothing special.",
        "I am very frustrated and upset about this."
    ]
    print("Mood Detection Demo\n" + "-"*40)
    for text in test_texts:
        result = analyzer.analyze_mood(text)
        print(f"Text: {text}")
        print(f"Mood: {result['mood']} (Confidence: {result['confidence']:.2f})")
        print("-"*40)

if __name__ == "__main__":
    run_demo()
