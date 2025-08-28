import chromadb

client = chromadb.Client()
collection = client.create_collection(name="documents")
def add_data_to_database(File_name, embeding_list: list) -> list:
    for item in embeding_list:
        unique_id = item["id"]
        original_text = item["text"]
        embeding_text = item["embedding"]

        collection.add(
            ids=[unique_id],                # ✅ list
            documents=[original_text],      # ✅ list
            embeddings=[embeding_text],     # ✅ already wrapped
            metadatas=[{"File_Name": File_name}]
        )
    
    return collection.get(
        ids=["file_chunk_0"], 
        include=["embeddings", "documents", "metadatas"]
    )

    
