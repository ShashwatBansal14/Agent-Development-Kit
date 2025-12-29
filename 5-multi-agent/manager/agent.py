from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_curr_time


root_agent=Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manger agent that is responsible for overseeing the work of other agents.

    Always delegate the tast to the appropiate agent. Use your best agent to determine which 
    agent to delegate to.

    You are responsible for delegating the task to the following agents:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_curr_time 
    """,
    sub_agents=[stock_analyst,funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_curr_time,
    ],
)