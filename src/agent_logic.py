from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from src.tools import query_hive_tool

def setup_agent():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    tools = [query_hive_tool]
    
    # Bajamos un prompt estándar de la comunidad para agentes que razonan (ReAct)
    prompt = hub.pull("hwchase17/react")
    
    # Instrucciones específicas sobre el Titanic (basado en tu documento)
    instrucciones = """Eres un experto en Big Data sobre AWS EMR. 
    Tienes acceso a una tabla llamada 'titanic' con columnas: 
    PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.
    Responde las preguntas del usuario generando SQL para Hive."""
    
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)