import os

from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import Client, create_client

from src.constants import config

os.environ['GOOGLE_API_KEY'] = config.get("GOOGLE_API_KEY")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# See docker command above to launch a postgres instance with pgvector enabled.
supabase_url = config.get("SUPABASE_URL")
supabase_key = config.get("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)
table_name = "points_embedding"
match_function = "match_points"

vector_store = SupabaseVectorStore(
    embedding=embeddings,
    client=supabase,
    table_name=table_name,
    query_name= match_function,
)


print(vector_store.similarity_search_with_relevance_scores(query="external sources data not able to sync with app", k =1))
