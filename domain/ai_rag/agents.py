from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from core.config import settings

def get_financial_assistant_agent():
    """
    Creates a RAG agent capable of answering natural language questions
    about M-Pesa transactions stored in PostgreSQL.
    """
    db = SQLDatabase.from_uri(settings.DATABASE_URL)
    llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
    
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor

# Example usage: agent.run("What was the total M-Pesa revenue for March 2026?")
