from src.models.sentiment_model import SentimentModel
from src.services.twitter_service import TwitterService
from src.db.repository import save_analysis

class AnalysisService:
    def __init__(self):
        self.model = SentimentModel()
        self.twitter = TwitterService()

    def analyze_text(self, text: str):
        pred = self.model.predict(text)
        return {
            "text": text,
            "sentiment": pred.label,
            "confidence": pred.confidence
        }

    def analyze_thread(self, tweet_id: str):
        tweets = self.twitter.fetch_thread(tweet_id)
        results = []
        for tweet in tweets:
            pred = self.model.predict(tweet)
            results.append({
                "text": tweet,
                "sentiment": pred.label,
                "confidence": pred.confidence
            })
        save_analysis(tweet_id, results)
        return {"tweet_id": tweet_id, "predictions": results}
