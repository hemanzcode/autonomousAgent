from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq("llama-3.3-70b-versatile"),
    instructions="You are a helpful assistant.",
)

response = agent.run("hello world")

print(response)
