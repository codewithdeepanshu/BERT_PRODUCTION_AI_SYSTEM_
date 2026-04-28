from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from src.utils.config import DB_URL

engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class AnalysisRecord(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    tweet_id = Column(String(128), index=True)
    text = Column(Text)
    sentiment = Column(String(32))
    confidence = Column(Float)

def init_db():
    Base.metadata.create_all(bind=engine)
