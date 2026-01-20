"""Sidebar component."""

import streamlit as st


def render_sidebar() -> None:
    """Render the sidebar navigation."""
    with st.sidebar:
        st.header("Midas Dashboard")
        st.markdown("---")

        st.subheader("Navigation")
        st.page_link("app/main.py", label="Home", icon="🏠")
        st.page_link("app/pages/1_dashboard.py", label="Dashboard", icon="📊")
        st.page_link("app/pages/2_analysis.py", label="Analysis", icon="📈")
        st.page_link("app/pages/3_settings.py", label="Settings", icon="⚙️")

        st.markdown("---")
        st.caption("Midas Agent v0.1.0")
