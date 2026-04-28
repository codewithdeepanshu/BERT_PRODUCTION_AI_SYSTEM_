from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.analysis import router as analysis_router

app = FastAPI(
    title="Social Media Opinion Analysis API",
    version="1.0.0",
    description="Production-style API for live thread sentiment analysis."
)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(analysis_router, prefix="/analysis", tags=["analysis"])
