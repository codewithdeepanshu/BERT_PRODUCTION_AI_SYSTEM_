import streamlit as st
import requests

st.title("System Status")

try:
    resp = requests.get("http://localhost:8000/health/", timeout=10)
    st.success(f"API Status: {resp.json()}")
except Exception as exc:
    st.error(f"API unavailable: {exc}")

st.code("uvicorn api.main:app --reload", language="bash")
st.code("streamlit run ui/Home.py", language="bash")
