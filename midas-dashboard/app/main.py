"""Quant Market Dashboard - Main Application."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import plotly.graph_objects as go
import streamlit as st
import numpy as np

from app.core import settings

st.set_page_config(
    page_title="Quant Market Dashboard",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for dark theme styling
st.markdown(
    """
<style>
    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main container styling */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }

    /* Custom header */
    .dashboard-header {
        background: linear-gradient(90deg, #0D1117 0%, #161B22 100%);
        padding: 12px 24px;
        border-radius: 8px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .dashboard-title {
        color: #E6EDF3;
        font-size: 20px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .dashboard-title .logo {
        width: 28px;
        height: 28px;
        background: linear-gradient(135deg, #00D4AA 0%, #00A080 100%);
        border-radius: 6px;
    }

    /* Navigation tabs */
    .nav-tabs {
        display: flex;
        gap: 8px;
    }

    .nav-tab {
        padding: 8px 16px;
        border-radius: 6px;
        color: #8B949E;
        font-size: 14px;
        cursor: pointer;
        transition: all 0.2s;
    }

    .nav-tab.active {
        background-color: #21262D;
        color: #E6EDF3;
    }

    .nav-tab:hover {
        color: #E6EDF3;
    }

    /* Section headers */
    .section-header {
        color: #E6EDF3;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Market card styling */
    .market-card {
        background-color: #161B22;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #30363D;
    }

    .market-label {
        color: #8B949E;
        font-size: 12px;
        margin-bottom: 4px;
    }

    .market-value {
        color: #E6EDF3;
        font-size: 24px;
        font-weight: 600;
    }

    .market-change {
        font-size: 12px;
        margin-top: 4px;
    }

    .positive { color: #00D4AA !important; }
    .negative { color: #F85149 !important; }

    /* Card containers */
    .card {
        background-color: #161B22;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #30363D;
        height: 100%;
    }

    .card-header {
        color: #E6EDF3;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Tags */
    .tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 12px;
        margin: 4px;
        background-color: #21262D;
        color: #8B949E;
        border: 1px solid #30363D;
    }

    .tag.hot {
        background-color: rgba(248, 81, 73, 0.2);
        color: #F85149;
        border-color: #F85149;
    }

    .tag.trending {
        background-color: rgba(0, 212, 170, 0.2);
        color: #00D4AA;
        border-color: #00D4AA;
    }

    /* Feed items */
    .feed-item {
        padding: 12px 0;
        border-bottom: 1px solid #30363D;
    }

    .feed-item:last-child {
        border-bottom: none;
    }

    .feed-source {
        color: #00D4AA;
        font-size: 11px;
        font-weight: 600;
    }

    .feed-text {
        color: #E6EDF3;
        font-size: 13px;
        margin-top: 4px;
        line-height: 1.4;
    }

    /* Sentiment gauge */
    .sentiment-value {
        font-size: 48px;
        font-weight: 700;
        color: #00D4AA;
        text-align: center;
    }

    .sentiment-label {
        color: #00D4AA;
        font-size: 14px;
        text-align: center;
    }

    /* Strategic comparison */
    .comparison-card {
        background-color: #161B22;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #30363D;
    }

    .comparison-header {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
    }

    .confidence-bar {
        height: 8px;
        background-color: #21262D;
        border-radius: 4px;
        overflow: hidden;
        margin: 8px 0;
    }

    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, #00D4AA 0%, #00A080 100%);
        border-radius: 4px;
    }

    .sector-tag {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 11px;
        margin: 2px;
        background-color: #21262D;
        color: #8B949E;
    }

    .sector-tag.highlight {
        background-color: rgba(0, 212, 170, 0.2);
        color: #00D4AA;
    }

    /* Analysis perspective */
    .perspective-item {
        padding: 8px 0;
        border-bottom: 1px solid #30363D;
    }

    .perspective-bullet {
        color: #00D4AA;
        margin-right: 8px;
    }

    .perspective-text {
        color: #8B949E;
        font-size: 12px;
    }

    /* Target price */
    .target-price-label {
        color: #8B949E;
        font-size: 12px;
        margin-bottom: 4px;
    }

    .target-price-value {
        color: #E6EDF3;
        font-size: 20px;
        font-weight: 600;
    }

    /* Hide streamlit metric labels if needed */
    [data-testid="stMetricLabel"] {
        color: #8B949E !important;
    }

    [data-testid="stMetricValue"] {
        color: #E6EDF3 !important;
    }

    /* Status badge */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
    }

    .status-cautious {
        background-color: rgba(210, 153, 34, 0.2);
        color: #D29922;
    }

    /* View more link */
    .view-more {
        color: #58A6FF;
        font-size: 12px;
        text-align: center;
        margin-top: 12px;
        cursor: pointer;
    }
</style>
""",
    unsafe_allow_html=True,
)


def create_sparkline(values, color="#00D4AA", height=40):
    """Create a sparkline chart."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=values,
        mode='lines',
        line=dict(color=color, width=2),
        fill='tozeroy',
        fillcolor=f'rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1)',
        showlegend=False,
    ))

    fig.update_layout(
        height=height,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )

    return fig


def create_donut_chart(value, max_value=100):
    """Create a donut chart for sentiment."""
    fig = go.Figure()

    fig.add_trace(go.Pie(
        values=[value, max_value - value],
        hole=0.7,
        marker=dict(colors=['#00D4AA', '#21262D']),
        textinfo='none',
        showlegend=False,
    ))

    fig.update_layout(
        height=180,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        annotations=[
            dict(
                text=f'<b>{value}</b>',
                x=0.5, y=0.55,
                font=dict(size=36, color='#00D4AA'),
                showarrow=False,
            ),
            dict(
                text='Bullish',
                x=0.5, y=0.35,
                font=dict(size=14, color='#00D4AA'),
                showarrow=False,
            ),
        ],
    )

    return fig


# Header
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-title">
        <div class="logo"></div>
        Quant Market Dashboard
    </div>
    <div class="nav-tabs">
        <div class="nav-tab active">Overview</div>
        <div class="nav-tab">Portfolio</div>
        <div class="nav-tab">Advanced Analysis</div>
        <div class="nav-tab">Backtesting</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Global Market Indices Section
st.markdown('<div class="section-header">Global Market Indices</div>', unsafe_allow_html=True)

# Market data
market_indices = [
    {"name": "KOSPI", "value": "2,560.12", "change": "+1.24%", "change_val": "+31.45", "positive": True},
    {"name": "S&P 500", "value": "5,026.73", "change": "+0.85%", "change_val": "+42.31", "positive": True},
    {"name": "NASDAQ", "value": "16,128.50", "change": "+1.12%", "change_val": "+178.65", "positive": True},
    {"name": "BTC / USD", "value": "68,432.10", "change": "+2.34%", "change_val": "+1,562.80", "positive": True},
]

# Generate sample sparkline data
np.random.seed(42)
sparkline_data = [
    np.cumsum(np.random.randn(20) * 0.5 + 0.1),
    np.cumsum(np.random.randn(20) * 0.3 + 0.05),
    np.cumsum(np.random.randn(20) * 0.4 + 0.08),
    np.cumsum(np.random.randn(20) * 0.6 + 0.15),
]

cols = st.columns(4)
for i, (col, market, sparkline) in enumerate(zip(cols, market_indices, sparkline_data)):
    with col:
        st.markdown(f"""
        <div class="market-card">
            <div class="market-label">{market['name']}</div>
            <div class="market-value">{market['value']}</div>
            <div class="market-change {'positive' if market['positive'] else 'negative'}">
                {market['change_val']} ({market['change']})
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.plotly_chart(create_sparkline(sparkline), use_container_width=True, config={'displayModeBar': False})

st.markdown("<br>", unsafe_allow_html=True)

# Middle Section: Trending Keywords, Live Alpha Feed, Sentiment Analysis
col1, col2, col3 = st.columns([1, 1.5, 1])

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            Trending Keywords
        </div>
        <div>
            <span class="tag hot">Hot Rate</span>
            <span class="tag trending">NVIDIA Hype</span>
        </div>
        <div>
            <span class="tag">EV Demand</span>
            <span class="tag">Oil Volatility</span>
        </div>
        <div>
            <span class="tag">Semiconductors</span>
            <span class="tag">CPI Data</span>
        </div>
        <div style="margin-top: 8px;">
            <span class="tag">Quantum Computing</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            Live Alpha Feed
            <span style="color: #8B949E; font-size: 12px; font-weight: normal;">Show Filter</span>
        </div>
        <div class="feed-item">
            <div class="feed-source">ECB</div>
            <div class="feed-text">ECB signals potential rate cut in June as inflation targets near 2% goal.</div>
        </div>
        <div class="feed-item">
            <div class="feed-source">NVIDIA</div>
            <div class="feed-text">NVIDIA partners with major cloud providers for H200 chip rollout in Asia markets.</div>
        </div>
        <div class="feed-item">
            <div class="feed-source">CRUDE OIL</div>
            <div class="feed-text">Crude oil prices stabilize as middle-east supply chain disruptions ease.</div>
        </div>
        <div class="view-more">View Full Feed</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            Sentiment Analysis
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.plotly_chart(create_donut_chart(74), use_container_width=True, config={'displayModeBar': False})

st.markdown("<br>", unsafe_allow_html=True)

# Strategic Comparison Section
st.markdown('<div class="section-header">Strategic Comparison</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="comparison-card">
        <div class="comparison-header">
            <span style="color: #E6EDF3; font-weight: 600;">AI Agent Insight</span>
        </div>
        <div style="color: #8B949E; font-size: 12px; margin-bottom: 12px;">Based on quantitative models</div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="color: #8B949E; font-size: 12px;">Confidence</span>
            <span style="color: #00D4AA; font-size: 14px; font-weight: 600;">68.4%</span>
        </div>
        <div class="confidence-bar">
            <div class="confidence-fill" style="width: 68.4%;"></div>
        </div>

        <div style="margin-top: 16px; margin-bottom: 8px; color: #8B949E; font-size: 12px;">RECOMMENDED SECTORS</div>
        <div>
            <span class="sector-tag highlight">AAPL</span>
            <span class="sector-tag">TSLA</span>
            <span class="sector-tag highlight">NVDA</span>
            <span class="sector-tag">AMZN</span>
            <span class="sector-tag">META</span>
            <span class="sector-tag">GOOGL</span>
        </div>
        <div style="margin-top: 4px;">
            <span class="sector-tag highlight">TAT.NS</span>
            <span class="sector-tag">0.09%</span>
            <span class="sector-tag">SAN.PA</span>
            <span class="sector-tag">0.02%</span>
        </div>

        <div style="margin-top: 16px; margin-bottom: 8px; color: #8B949E; font-size: 12px;">ANALYSIS PERSPECTIVE</div>
        <div class="perspective-item">
            <span class="perspective-bullet">●</span>
            <span class="perspective-text">Deep learning pattern recognition identifies 7-year fractal similarity in tech sector accumulation.</span>
        </div>
        <div class="perspective-item">
            <span class="perspective-bullet">●</span>
            <span class="perspective-text">Volatility clustering indicates imminent upward breakout from current consolidation range.</span>
        </div>
        <div class="perspective-item">
            <span class="perspective-bullet">●</span>
            <span class="perspective-text">Cross-asset correlation analysis shows divergence in bond yields supporting equity momentum.</span>
        </div>

        <div style="margin-top: 20px; display: flex; gap: 40px;">
            <div>
                <div class="target-price-label">TARGET PRICE</div>
                <div class="target-price-value">17,450</div>
            </div>
            <div>
                <div class="target-price-label">STOP LOSS</div>
                <div class="target-price-value">15,820</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="comparison-card">
        <div class="comparison-header">
            <span style="color: #E6EDF3; font-weight: 600;">Human Expert Logic</span>
        </div>
        <div style="color: #8B949E; font-size: 12px; margin-bottom: 12px;">Based on fundamental analysis</div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="color: #8B949E; font-size: 12px;">RECOMMENDATION</span>
            <span class="status-badge status-cautious">CAUTIOUS</span>
        </div>

        <div style="margin-bottom: 8px; color: #8B949E; font-size: 12px;">RECOMMENDED SECTORS</div>
        <div>
            <span class="sector-tag">AAPL</span>
            <span class="sector-tag highlight">TSLA</span>
            <span class="sector-tag">NVDA</span>
            <span class="sector-tag highlight">AMZN</span>
            <span class="sector-tag">META</span>
            <span class="sector-tag">GOOGL</span>
        </div>
        <div style="margin-top: 4px;">
            <span class="sector-tag">TAT.NS</span>
            <span class="sector-tag">1.6%</span>
            <span class="sector-tag">SAN.PA</span>
            <span class="sector-tag">1.4%</span>
        </div>

        <div style="margin-top: 16px; margin-bottom: 8px; color: #8B949E; font-size: 12px;">ANALYSIS PERSPECTIVE</div>
        <div class="perspective-item">
            <span class="perspective-bullet" style="color: #F85149;">●</span>
            <span class="perspective-text">Stagnant container volume in the Red Sea could lead to unexpected freight cost spikes, affecting margin outlook.</span>
        </div>
        <div class="perspective-item">
            <span class="perspective-bullet" style="color: #F85149;">●</span>
            <span class="perspective-text">Election cycle volatility usually peaks in Q2; historical data suggests a wait-and-see approach is prudent.</span>
        </div>
        <div class="perspective-item">
            <span class="perspective-bullet" style="color: #F85149;">●</span>
            <span class="perspective-text">Concentration risk in Top-7 mega-cap tech stocks is at decadal highs, raising concerns about market breadth.</span>
        </div>

        <div style="margin-top: 20px; display: flex; gap: 40px;">
            <div>
                <div class="target-price-label">TARGET PRICE</div>
                <div class="target-price-value">15,900</div>
            </div>
            <div>
                <div class="target-price-label">STOP LOSS</div>
                <div class="target-price-value">12,700</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #8B949E; font-size: 12px; padding: 20px 0;">
    Data is delayed and for demonstration purposes only. | Quant Market Dashboard v1.0.0
</div>
""", unsafe_allow_html=True)
