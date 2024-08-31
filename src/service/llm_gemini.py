from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    ChatMessagePromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from src.constants import config

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=config.get("GOOGLE_API_KEY"),
)


def get_response(text: str):
    messages = [
        SystemMessagePromptTemplate.from_template(
            "You are expert Customer Behaviour Analyzer"
        ),
        HumanMessagePromptTemplate.from_template(text),
    ]

    return llm.invoke(messages).content
