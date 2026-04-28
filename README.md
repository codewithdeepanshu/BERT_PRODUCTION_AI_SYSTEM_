# Social Media Opinion Analysis with BERT — Production AI System

A production-style starter project for live Twitter/X thread sentiment and opinion analysis using a BERT-based pipeline, FastAPI backend, Streamlit dashboard, SQLite storage, analytics, exports, and Docker support.

## Features
- FastAPI backend with health and analysis routes
- Streamlit dashboard with multi-page UI
- SQLite database for storing analyses
- CSV export support
- Sentiment analytics with charts
- Twitter/X fetch service stub
- Clean project structure for VS Code
- Docker and docker-compose ready
- VS Code launch and settings included
- Unit test starter files

## Folder Structure
```text
BERT_PRODUCTION_AI_SYSTEM/
├── api/
│   ├── main.py
│   ├── routes/
│   │   ├── health.py
│   │   └── analysis.py
│   └── schemas/
│       └── analysis.py
├── src/
│   ├── db/
│   │   ├── database.py
│   │   └── repository.py
│   ├── models/
│   │   └── sentiment_model.py
│   ├── services/
│   │   ├── twitter_service.py
│   │   ├── analysis_service.py
│   │   └── reporting_service.py
│   └── utils/
│       ├── preprocess.py
│       └── config.py
├── ui/
│   ├── Home.py
│   ├── pages/
│   │   ├── 1_Live_Thread_Analysis.py
│   │   ├── 2_History_and_Exports.py
│   │   └── 3_System_Status.py
│   └── assets/
│       └── custom.css
├── configs/
│   ├── launch.json
│   ├── settings.json
│   └── .env.example
├── tests/
│   ├── test_api.py
│   └── test_preprocess.py
├── data/sample/
│   └── sample_threads.csv
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

## Quick Start

### 1) Create virtual environment
```bash
python -m venv venv
```

### 2) Activate environment
**Windows**
```bash
venv\Scripts\activate
```

**Linux/macOS**
```bash
source venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure environment
Copy:
```bash
configs/.env.example
```
to:
```bash
.env
```
and add your Twitter/X Bearer token.

### 5) Run backend
```bash
uvicorn api.main:app --reload
```

### 6) Run dashboard
```bash
streamlit run ui/Home.py
```

## Notes
- `twitter_service.py` is structured for live thread fetching. Replace the stub logic with your verified Twitter/X API credentials and query flow.
- `sentiment_model.py` currently contains a production-ready interface with a lightweight fallback predictor. You can plug in your trained BERT checkpoint later.
- SQLite database file is created automatically on first run.

## Future Upgrade Ideas
- Real fine-tuned BERT checkpoint loading
- Celery or RQ for async jobs
- Redis caching
- Authentication and roles
- Grafana/Prometheus monitoring
- Cloud deployment (Render, Railway, AWS, Azure)
