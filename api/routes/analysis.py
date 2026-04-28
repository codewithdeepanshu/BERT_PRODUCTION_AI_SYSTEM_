from fastapi import APIRouter
from api.schemas.analysis import TextAnalysisRequest, ThreadRequest
from src.services.analysis_service import AnalysisService

router = APIRouter()
service = AnalysisService()

@router.post("/text")
def analyze_text(payload: TextAnalysisRequest):
    return service.analyze_text(payload.text)

@router.post("/thread")
def analyze_thread(payload: ThreadRequest):
    return service.analyze_thread(payload.tweet_id)
