import streamlit as st
import pandas as pd
from src.db.repository import list_recent

st.title("History and Exports")

rows = list_recent()
data = [
    {
        "id": r.id,
        "tweet_id": r.tweet_id,
        "text": r.text,
        "sentiment": r.sentiment,
        "confidence": r.confidence
    }
    for r in rows
]

df = pd.DataFrame(data)
if not df.empty:
    st.dataframe(df, use_container_width=True)
    csv_bytes = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", data=csv_bytes, file_name="analysis_history.csv", mime="text/csv")
else:
    st.info("No saved analyses yet.")
