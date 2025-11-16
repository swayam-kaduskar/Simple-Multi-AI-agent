from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, google_search
from google.genai import types
from typing import Any
from collections.abc import Callable

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# Research Agent
research_agent = Agent(
    name="ResearchAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite", 
        retry_options=retry_config,
        ),
    tools=[google_search],
    output_key="research_findings",
)

# Summarizer Agent
summarizer_agent = Agent(
    name="SummarizerAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite", 
        retry_options=retry_config,
        ),
    tools = [google_search]
    output_key="final_summary",
)

# Root/Coordinator Agent
root_agent = Agent(
    name="ResearchCoordinator",
    model=Gemini(
        model="gemini-2.5-flash-lite", 
        retry_options=retry_config,
        ),
    tools=[AgentTool(research_agent), AgentTool(summarizer_agent)],
)