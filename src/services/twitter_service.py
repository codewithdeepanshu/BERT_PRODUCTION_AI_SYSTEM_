from typing import List
from src.utils.config import TWITTER_BEARER_TOKEN

class TwitterService:
    def __init__(self, bearer_token: str | None = None):
        self.bearer_token = bearer_token or TWITTER_BEARER_TOKEN

    def fetch_thread(self, tweet_id: str) -> List[str]:
        # Production stub:
        # Replace with tweepy.Client(bearer_token=...) and conversation search flow.
        # This fallback lets the UI and API run without external credentials.
        return [
            f"Root tweet for thread {tweet_id}",
            "This product update looks good and very useful.",
            "Some users still hate the new changes.",
            "Overall reaction seems mixed but improving."
        ]
