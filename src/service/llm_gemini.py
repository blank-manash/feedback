from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.constants import config
from src.models import CreateResponse, TextResponse
from src.prompts import CUSTOMER_SERVICE, CREATE_FLOW, SANITIZE_TEXT
from langchain.output_parsers import PydanticOutputParser
from global_utils import get_logger
from retry import retry

logger = get_logger(__name__)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=config.get("GOOGLE_API_KEY"),
)


@retry(tries=3, backoff=2, delay=1)
def create_card(point_content: str) -> CreateResponse:
    """
    Create a card from user feedback.

    This function uses the Gemini model to parse the user feedback and generate a card
    title and point content. The response is a CreateResponse object with the card title
    and point content.

    Args:
        point_content (str): The user feedback to parse.

    Returns:
        CreateResponse: A CreateResponse object with the card title and point content.
    """
    parser = PydanticOutputParser(pydantic_object=CreateResponse)
    prompt = PromptTemplate(
        template=CREATE_FLOW,
        input_variables=["user_feedback"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    )
    chain = prompt | llm | parser
    logger.info("Calling LLM to create card")
    return chain.invoke({"user_feedback": point_content})


@retry(tries=3, backoff=2, delay=1)
def sanitize_text(text: str):
    """
    Sanitize the given text, removing profanity and rephrasing it to be more informative.

    Args:
        text (str): The text to sanitize.

    Returns:
        TextResponse: The sanitized text.
    """
    parser = PydanticOutputParser(pydantic_object=TextResponse)
    prompt = PromptTemplate(
        template=SANITIZE_TEXT,
        input_variables=["user_feedback"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    )
    chain = prompt | llm | parser
    logger.info("Calling LLM to sanitize text")
    return chain.invoke({"user_feedback": text})
