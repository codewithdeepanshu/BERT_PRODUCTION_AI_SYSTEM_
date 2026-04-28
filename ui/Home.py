import streamlit as st

st.set_page_config(page_title="Opinion Analysis Dashboard", layout="wide")

st.title("Social Media Opinion Analysis with BERT")
st.write("Production-style dashboard for live thread analysis, history, exports, and API-backed workflows.")

st.markdown("""
### Included Pages
- **Live Thread Analysis**
- **History and Exports**
- **System Status**

Use the sidebar to navigate between pages.
""")
