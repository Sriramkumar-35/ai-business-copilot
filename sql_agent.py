"""
sql_agent.py
------------
Sets up a LangChain SQL Agent backed by a local Ollama model (Llama 3.1)
and the local SQLite database (sales.db).

Requires:
    - Ollama installed and running (https://ollama.com)
    - Model pulled locally:  ollama pull llama3.1
    - sales.db created (run db_setup.py first)
"""

from langchain_community.utilities import SQLDatabase
from langchain_community.llms import Ollama
from langchain_community.agent_toolkits import create_sql_agent

DB_PATH = "sales.db"
MODEL_NAME = "llama3.1"  # swap to "phi3" for a lighter/faster model


def get_agent(verbose: bool = True):
    """Builds and returns a LangChain SQL agent ready to answer questions."""

    db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
    llm = Ollama(model=MODEL_NAME, temperature=0)

    agent = create_sql_agent(
        llm=llm,
        db=db,
        verbose=verbose,
    )
    return agent


def ask(question: str) -> str:
    """Convenience function: ask a single natural-language question, get an answer."""
    agent = get_agent(verbose=False)
    result = agent.invoke({"input": question})
    return result.get("output", str(result))


if __name__ == "__main__":
    # Quick manual test from the command line
    test_questions = [
        "What are the top 5 products by total revenue?",
        "Which region had the highest sales in March 2025?",
        "What is the total revenue for the Electronics category?",
    ]

    agent = get_agent(verbose=True)
    for q in test_questions:
        print("\n--- QUESTION:", q)
        response = agent.invoke({"input": q})
        print("--- ANSWER:", response.get("output", response))
