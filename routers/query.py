from fastapi import APIRouter
import chromadb
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
# ------------------------
# ChromaDB + Model Setup
# ------------------------
client = chromadb.Client()
collection = client.get_or_create_collection(name="documents")
model = SentenceTransformer("all-MiniLM-L6-v2")

query_router = APIRouter()  # ✅ This is important
class QueryRequest(BaseModel):
    query: str
    top_k: int = 3  # default return top 3 results


async def search_documents(request: QueryRequest):
    # Convert query to embedding
    query_vector = model.encode(request.query).tolist()

    # Query ChromaDB
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=request.top_k,
        include=["documents", "metadatas", "distances"]
    )

    # Clean JSON response
    return {
        "query": request.query,
        "results": [
            {
                "document": doc,
                "metadata": meta,
                "distance": dist
            }
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            )
        ]
    }