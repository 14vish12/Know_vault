from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")



def change_to_vector(text):
    embeddings = model.encode(text).tolist()
    return embeddings




def embed_chunks(newlist: list) -> list:
    embedded_chunks = []
    for chunk in newlist:
        chunk_text = chunk["text"]
        vector = change_to_vector(chunk_text)
        embedded_chunks.append({
            "id": chunk["id"],
            "text": chunk["text"],
            "embedding": vector
        })
    return embedded_chunks

