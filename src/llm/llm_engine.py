from langchain_openai import ChatOpenAI
from src.config.settings import OPENAI_API_KEY

def load_llm():

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY missing in .env"
        )

    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model="gpt-3.5-turbo",
        temperature=0
    )

    return llm