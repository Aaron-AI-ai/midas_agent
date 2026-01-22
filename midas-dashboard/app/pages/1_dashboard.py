"""Dashboard page."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import streamlit as st

st.set_page_config(
    page_title="Dashboard - Midas",
    page_icon=None,
    layout="wide",
)

st.title("Dashboard")
st.markdown("---")

# Portfolio Overview
st.subheader("Portfolio Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Holdings")
    st.info("No holdings data available.")

with col2:
    st.markdown("### Performance")
    st.info("No performance data available.")
