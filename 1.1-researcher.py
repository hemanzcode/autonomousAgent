from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

agent = Agent(
    model=Groq("llama-3.3-70b-versatile"),
    tools=[TavilyTools()],
    debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura atual em Nova York.")
