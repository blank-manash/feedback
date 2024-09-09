from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.constants import config
from src.models import CreateResponse
from src.prompts import CUSTOMER_SERVICE, CREATE_FLOW
from langchain.output_parsers import PydanticOutputParser


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=config.get("GOOGLE_API_KEY"),
)


def create_card(point_content: str) -> CreateResponse:
    parser = PydanticOutputParser(pydantic_object=CreateResponse)
    prompt = PromptTemplate(
        template=CREATE_FLOW,
        input_variables=["user_feedback"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    )
    chain = prompt | llm | parser
    return chain.invoke({"user_feedback": point_content})


def merge_point(user_point: str, reference_point: str):
    # Make sure to limit the number of words
    pass


def get_response(text: str):
    prompt = PromptTemplate.from_template(CUSTOMER_SERVICE)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"context": text})
