import unittest
from src.mood_detector.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_happy_mood(self):
        result = self.analyzer.analyze_mood("I love sunny days and good vibes!")
        self.assertEqual(result["mood"], "happy")

    def test_sad_mood(self):
        result = self.analyzer.analyze_mood("I feel terrible and lonely.")
        self.assertEqual(result["mood"], "sad")

    def test_neutral_mood(self):
        result = self.analyzer.analyze_mood("I am sitting here.")
        self.assertEqual(result["mood"], "neutral")

    def test_empty_text(self):
        result = self.analyzer.analyze_mood("")
        self.assertEqual(result["mood"], "neutral")

if __name__ == "__main__":
    unittest.main()
