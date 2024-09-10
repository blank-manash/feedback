from typing import Optional
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.constants import config, EMBEDDING_MODEL, CREATE_THRESHOLD
from src.models import SimilarityResponse
from retry import retry
from functools import cache, lru_cache


@cache
def get_embedding_model():
    google_api_key = config.get("GOOGLE_API_KEY")
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL, google_api_key=google_api_key
    )


@cache
def get_vector_store():
    supabase_url = config.get("SUPABASE_URL")
    supabase_key = config.get("SUPABASE_SERVICE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)
    table_name = "point"
    match_function = "get_similarity"

    return SupabaseVectorStore(
        embedding=get_embedding_model(),
        client=supabase,
        table_name=table_name,
        query_name=match_function,
    )


@lru_cache
@retry(tries=3, backoff=2, delay=1)
def create_embedding(query: str) -> list[float]:
    model = get_embedding_model()
    return model.embed_query(text=query)


@lru_cache
def get_similarity(query: str) -> Optional[SimilarityResponse]:
    store = get_vector_store()
    response = store.similarity_search_with_relevance_scores(query)
    doc, score = response[0]
    return SimilarityResponse(
        id=doc.metadata["id"], content=doc.page_content, score=round(score, 2)
    )
