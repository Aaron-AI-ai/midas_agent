"""Chart components."""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from pandas import DataFrame


def render_line_chart(
    data: DataFrame,
    x: str,
    y: str,
    title: str = "",
) -> None:
    """Render a line chart.

    Args:
        data: DataFrame with chart data.
        x: Column name for x-axis.
        y: Column name for y-axis.
        title: Chart title.
    """
    fig = px.line(data, x=x, y=y, title=title)
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        hovermode="x unified",
    )
    st.plotly_chart(fig, use_container_width=True)


def render_pie_chart(
    data: DataFrame,
    names: str,
    values: str,
    title: str = "",
) -> None:
    """Render a pie chart.

    Args:
        data: DataFrame with chart data.
        names: Column name for labels.
        values: Column name for values.
        title: Chart title.
    """
    fig = px.pie(data, names=names, values=values, title=title)
    st.plotly_chart(fig, use_container_width=True)
