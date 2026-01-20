"""LangGraph multi-agent workflow definition."""

from typing import Annotated, TypedDict

from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """State for the multi-agent workflow."""

    messages: Annotated[list, add_messages]
    current_agent: str
    context: dict


def create_agent_graph() -> StateGraph:
    """Create and return the multi-agent workflow graph.

    Returns:
        Compiled LangGraph workflow.
    """
    workflow = StateGraph(AgentState)

    # Define agent nodes
    def router(state: AgentState) -> AgentState:
        """Route to appropriate agent based on context."""
        return state

    def analyst(state: AgentState) -> AgentState:
        """Analysis agent for market data."""
        return state

    def strategist(state: AgentState) -> AgentState:
        """Strategy agent for trading decisions."""
        return state

    # Add nodes
    workflow.add_node("router", router)
    workflow.add_node("analyst", analyst)
    workflow.add_node("strategist", strategist)

    # Set entry point
    workflow.set_entry_point("router")

    # Define edges
    workflow.add_edge("router", "analyst")
    workflow.add_edge("analyst", "strategist")
    workflow.add_edge("strategist", END)

    return workflow.compile()
