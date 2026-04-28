from dataclasses import dataclass
from src.utils.preprocess import clean_text

LABELS = ["Negative", "Neutral", "Positive"]

@dataclass
class PredictionResult:
    label: str
    confidence: float

class SentimentModel:
    def __init__(self, model_name: str = "bert-base-uncased"):
        self.model_name = model_name

    def predict(self, text: str) -> PredictionResult:
        text = clean_text(text).lower()
        positive_words = ["good", "great", "love", "excellent", "amazing", "happy", "best"]
        negative_words = ["bad", "worst", "hate", "terrible", "awful", "angry", "poor"]

        pos = sum(word in text for word in positive_words)
        neg = sum(word in text for word in negative_words)

        if pos > neg:
            return PredictionResult(label="Positive", confidence=0.82)
        if neg > pos:
            return PredictionResult(label="Negative", confidence=0.84)
        return PredictionResult(label="Neutral", confidence=0.71)
