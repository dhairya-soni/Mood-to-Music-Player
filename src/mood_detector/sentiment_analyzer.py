from transformers import pipeline
import logging

class SentimentAnalyzer:
    def __init__(self):
        try:
            self.sentiment_pipeline = pipeline(
                "sentiment-analysis",
                model="cardiffnlp/twitter-roberta-base-sentiment-latest"
            )
            logging.info("SentimentAnalyzer initialized successfully.")
        except Exception as e:
            logging.error(f"Failed to initialize SentimentAnalyzer: {e}")
            raise

    def analyze_mood(self, text):
        if not text or not text.strip():
            return {"mood": "neutral", "confidence": 0.0}
        try:
            result = self.sentiment_pipeline(text)[0]
            mood = self._map_label_to_mood(result["label"])
            return {"mood": mood, "confidence": result["score"], "raw_label": result["label"]}
        except Exception as e:
            logging.error(f"Error during mood analysis: {e}")
            return {"mood": "neutral", "confidence": 0.0}

    def _map_label_to_mood(self, label):
        mapping = {
            "LABEL_0": "sad",      # Negative
            "LABEL_1": "neutral",  # Neutral
            "LABEL_2": "happy"     # Positive
        }
        return mapping.get(label, "neutral")
