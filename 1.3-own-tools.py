from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv
load_dotenv()

# --- TOOL: Especificações ---
def ufo_specifications(type: str) -> str:
    """
    Retorna informações específicas sobre um tipo de óvni.
    Use esta ferramenta sempre que o usuário pedir algum detalhe, curiosidade,
    histórico ou especificação sobre tipos de óvnis.
    """
    
    database = {
        "orbe de luz": "Esferas de luz com variação de intensidade, voo errático e aceleração instantânea.",
        "tamanho": "11 metros de diâmetro.",
        "velocidade": "até 1400 km/h.",
        "laser": "Emite feixes de luz pulsantes para comunicação ou análise."
        
    }
    
    return database.get(type.lower(), "Desconhecido. Não há registros suficientes desse tipo de óvni.")


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[TavilyTools(), ufo_specifications],
    debug_mode=True
)

agent.print_response(
    "Pesquise avistamentos na América do Sul e diga que tipo de óvni é mais comum, depois use sua ferramenta de especificações para descrever esse tipo."
)
