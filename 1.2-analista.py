from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Groq("llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto",
)

agent.print_response("qual a cotação da apple atual?", stream=True)
