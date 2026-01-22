"""Analysis page."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import streamlit as st

st.set_page_config(
    page_title="Analysis - Midas",
    page_icon=None,
    layout="wide",
)

st.title("Analysis")
st.markdown("---")

# Market Analysis
st.subheader("Market Analysis")

tab1, tab2 = st.tabs(["Chart", "Data"])

with tab1:
    st.info("Chart will be displayed here.")

with tab2:
    st.info("Market data will be displayed here.")
