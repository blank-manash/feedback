from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.constants import config
from src.prompts import CUSTOMER_SERVICE

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=config.get("GOOGLE_API_KEY"),
)


def get_response(text: str):
    prompt = PromptTemplate.from_template(CUSTOMER_SERVICE)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"context": text})
