from src.db.database import SessionLocal, AnalysisRecord, init_db

init_db()

def save_analysis(tweet_id: str, predictions):
    db = SessionLocal()
    try:
        for item in predictions:
            row = AnalysisRecord(
                tweet_id=tweet_id,
                text=item["text"],
                sentiment=item["sentiment"],
                confidence=item["confidence"]
            )
            db.add(row)
        db.commit()
    finally:
        db.close()

def list_recent(limit: int = 50):
    db = SessionLocal()
    try:
        return db.query(AnalysisRecord).order_by(AnalysisRecord.id.desc()).limit(limit).all()
    finally:
        db.close()
