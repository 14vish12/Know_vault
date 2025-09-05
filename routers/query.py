from fastapi import APIRouter, Form
from sentence_transformers import SentenceTransformer
import chromadb

# ------------------------
# Initialize
# ------------------------
query_router = APIRouter()

client = chromadb.Client()
collection = client.get_or_create_collection(name="documents")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------------
# Query Endpoint
# ------------------------
@query_router.post("/search")
async def search(query: str = Form(...), top_k: int = Form(3)):
    query_vector = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    return {
        "query": query,
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
