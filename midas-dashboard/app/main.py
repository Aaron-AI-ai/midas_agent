"""Streamlit application entry point."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from app.core import settings

st.set_page_config(
    page_title=settings.page_title,
    page_icon=settings.page_icon,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for TradingView-like styling
st.markdown(
    """
<style>
    .market-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .positive { color: #26a69a; }
    .negative { color: #ef5350; }
    .stMetric label { font-size: 14px; }
</style>
""",
    unsafe_allow_html=True,
)


# Market Summary Section
st.subheader("Market Summary")

# Sample market data (실제로는 API에서 가져올 데이터)
market_data = {
    "indices": [
        {"name": "KOSPI", "value": "2,687.45", "change": "+0.85%", "positive": True},
        {"name": "KOSDAQ", "value": "868.32", "change": "-0.42%", "positive": False},
        {"name": "S&P 500", "value": "5,234.18", "change": "+1.02%", "positive": True},
        {"name": "NASDAQ", "value": "16,428.82", "change": "+1.35%", "positive": True},
    ],
    "crypto": [
        {"name": "BTC/USD", "value": "67,234.50", "change": "+2.15%", "positive": True},
        {"name": "ETH/USD", "value": "3,456.78", "change": "+1.89%", "positive": True},
    ],
    "forex": [
        {"name": "USD/KRW", "value": "1,345.20", "change": "-0.32%", "positive": False},
        {"name": "EUR/USD", "value": "1.0845", "change": "+0.15%", "positive": True},
    ],
    "commodities": [
        {"name": "Gold", "value": "2,345.60", "change": "+0.45%", "positive": True},
        {"name": "WTI Oil", "value": "78.45", "change": "-1.23%", "positive": False},
    ],
}

# Market Summary Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**Indices**")
    for item in market_data["indices"]:
        change_color = "green" if item["positive"] else "red"
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee;">
                <span>{item["name"]}</span>
                <span style="color: {change_color};">{item["value"]} ({item["change"]})</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col2:
    st.markdown("**Crypto**")
    for item in market_data["crypto"]:
        change_color = "green" if item["positive"] else "red"
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee;">
                <span>{item["name"]}</span>
                <span style="color: {change_color};">{item["value"]} ({item["change"]})</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col3:
    st.markdown("**Forex**")
    for item in market_data["forex"]:
        change_color = "green" if item["positive"] else "red"
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee;">
                <span>{item["name"]}</span>
                <span style="color: {change_color};">{item["value"]} ({item["change"]})</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col4:
    st.markdown("**Commodities**")
    for item in market_data["commodities"]:
        change_color = "green" if item["positive"] else "red"
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee;">
                <span>{item["name"]}</span>
                <span style="color: {change_color};">{item["value"]} ({item["change"]})</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# Chart Section
st.subheader("Price Chart")

chart_col1, chart_col2 = st.columns([3, 1])

with chart_col1:
    # Sample candlestick data
    dates = pd.date_range(start="2024-01-01", periods=60, freq="D")

    # Generate sample OHLC data
    import random
    random.seed(42)

    open_prices = [100]
    for _ in range(59):
        open_prices.append(open_prices[-1] * (1 + random.uniform(-0.02, 0.02)))

    high_prices = [o * (1 + random.uniform(0, 0.015)) for o in open_prices]
    low_prices = [o * (1 - random.uniform(0, 0.015)) for o in open_prices]
    close_prices = [random.uniform(l, h) for l, h in zip(low_prices, high_prices)]

    df = pd.DataFrame({
        "Date": dates,
        "Open": open_prices,
        "High": high_prices,
        "Low": low_prices,
        "Close": close_prices,
    })

    # Create candlestick chart
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["Date"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                increasing_line_color="#26a69a",
                decreasing_line_color="#ef5350",
            )
        ]
    )

    fig.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_rangeslider_visible=False,
        xaxis_title="",
        yaxis_title="Price",
        template="plotly_white",
    )

    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    st.markdown("**Symbol**")
    symbol = st.selectbox(
        "Select",
        ["KOSPI", "KOSDAQ", "S&P 500", "NASDAQ", "BTC/USD", "ETH/USD"],
        label_visibility="collapsed",
    )

    st.markdown("**Timeframe**")
    timeframe = st.selectbox(
        "Timeframe",
        ["1D", "1W", "1M", "3M", "1Y"],
        label_visibility="collapsed",
    )

    st.markdown("---")

    st.markdown("**Key Stats**")
    st.metric("Open", "2,680.12")
    st.metric("High", "2,695.34")
    st.metric("Low", "2,675.88")
    st.metric("Volume", "485.2M")

st.markdown("---")

# Portfolio Summary and Agent Section
portfolio_col, agent_col = st.columns(2)

with portfolio_col:
    st.subheader("Portfolio Summary")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Value", "$125,430.50", "+$2,340.25")
    with col2:
        st.metric("Daily P&L", "+$1,234.56", "+0.99%")
    with col3:
        st.metric("Total Return", "+18.45%", "+2.3%")

    # Holdings table
    holdings_data = pd.DataFrame({
        "Symbol": ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA"],
        "Shares": [50, 20, 30, 15, 25],
        "Avg Cost": [175.50, 142.30, 378.20, 245.80, 485.60],
        "Current": [182.30, 148.50, 395.40, 238.20, 512.80],
        "P&L %": ["+3.87%", "+4.36%", "+4.55%", "-3.09%", "+5.60%"],
    })

    st.dataframe(holdings_data, use_container_width=True, hide_index=True)

with agent_col:
    st.subheader("AI Agent")

    # Agent status
    st.markdown("**Status:** Online")

    # Simple chat interface
    st.markdown("**Recent Analysis**")

    with st.container():
        st.info("KOSPI 지수가 2,700 저항선에 근접했습니다. 단기 조정 가능성에 유의하세요.")
        st.success("BTC/USD가 강한 상승 모멘텀을 보이고 있습니다. RSI 지표는 아직 과매수 구간에 진입하지 않았습니다.")
        st.warning("USD/KRW 환율이 1,350원 지지선을 테스트 중입니다. 환율 변동에 따른 포트폴리오 영향을 모니터링하세요.")

    # Quick action buttons
    st.markdown("**Quick Actions**")
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        st.button("Market Analysis", use_container_width=True)
    with btn_col2:
        st.button("Risk Report", use_container_width=True)
    with btn_col3:
        st.button("Ask Agent", use_container_width=True)

st.markdown("---")

# Footer
st.caption("Data is delayed and for demonstration purposes only. | Midas Agent v0.1.0")
