from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_curr_time()->dict:
    # this is called doc string, it is used by llm to understand wether to call the tool or not 
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent= Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools: 
    -google_search                  
    """,
    tools=[google_search],
    # tools=[get_curr_time],

) # before running curr time  change -google_search to -get_curr_time in instructions 