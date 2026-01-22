"""Settings page."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import streamlit as st

from app.core import settings

st.set_page_config(
    page_title="Settings - Midas",
    page_icon=None,
    layout="wide",
)

st.title("Settings")
st.markdown("---")

# API Settings
st.subheader("API Configuration")

brain_url = st.text_input(
    "Midas Brain API URL",
    value=settings.brain_api_url,
    help="URL for the Midas Brain AI Agent service",
)

if st.button("Test Connection"):
    st.info(f"Testing connection to {brain_url}...")
    # TODO: Implement connection test

st.markdown("---")

# Display Settings
st.subheader("Display Settings")

theme = st.selectbox("Theme", ["Light", "Dark", "System"])
language = st.selectbox("Language", ["English", "Korean"])

if st.button("Save Settings"):
    st.success("Settings saved!")
