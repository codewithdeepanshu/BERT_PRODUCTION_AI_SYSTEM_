from pydantic import BaseModel
from typing import List

class TextAnalysisRequest(BaseModel):
    text: str

class ThreadRequest(BaseModel):
    tweet_id: str

class TweetPrediction(BaseModel):
    text: str
    sentiment: str
    confidence: float

class ThreadAnalysisResponse(BaseModel):
    tweet_id: str
    predictions: List[TweetPrediction]
