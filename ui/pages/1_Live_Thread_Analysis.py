import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from collections import Counter

API_URL = "http://localhost:8000/analysis/thread"

st.title("Live Thread Analysis")

tweet_id = st.text_input("Enter Tweet ID")

if st.button("Fetch and Analyze"):
    if tweet_id.strip():
        response = requests.post(API_URL, json={"tweet_id": tweet_id}, timeout=30)
        data = response.json()

        rows = data["predictions"]
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)

        counts = Counter(df["sentiment"])
        fig, ax = plt.subplots()
        ax.bar(list(counts.keys()), list(counts.values()))
        ax.set_title("Sentiment Distribution")
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.warning("Please enter a tweet ID.")
