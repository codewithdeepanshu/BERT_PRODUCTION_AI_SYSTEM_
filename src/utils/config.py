import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")
MODEL_NAME = os.getenv("MODEL_NAME", "bert-base-uncased")
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
DB_URL = "sqlite:///analysis.db"
