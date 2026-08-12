from langgraph.graph import StateGraph, START, END
from .state import FarmState
from .soil_agent import soil_agent
from .crop_agent import crop_agent
from .fertilizer_agent import fertilizer_agent
from .risk_agent import risk_agent
from .final_agent import final_agent

graph = StateGraph(FarmState)

graph.add_node("soil", soil_agent)
graph.add_node("crop", crop_agent)
graph.add_node("fertilizer", fertilizer_agent)
graph.add_node("risk", risk_agent)
graph.add_node("final", final_agent)

graph.add_edge(START, "soil")
graph.add_edge("soil", "crop")
graph.add_edge("crop", "fertilizer")
graph.add_edge("fertilizer", "risk")
graph.add_edge("risk", "final")
graph.add_edge("final", END)

agri_graph = graph.compile()
