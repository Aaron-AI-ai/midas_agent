"""Streamlit application entry point."""

import streamlit as st

from app.core import settings

st.set_page_config(
    page_title=settings.page_title,
    page_icon=settings.page_icon,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 Midas Dashboard")
st.markdown("---")

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Portfolio Value", value="$0.00", delta="0.00%")

with col2:
    st.metric(label="Daily P&L", value="$0.00", delta="0.00%")

with col3:
    st.metric(label="Total Return", value="0.00%", delta="0.00%")

st.markdown("---")

st.info("👈 사이드바에서 페이지를 선택하세요.")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.page_link("app/main.py", label="Home", icon="🏠")
    st.page_link("app/pages/1_dashboard.py", label="Dashboard", icon="📊")
    st.page_link("app/pages/2_analysis.py", label="Analysis", icon="📈")
    st.page_link("app/pages/3_settings.py", label="Settings", icon="⚙️")
