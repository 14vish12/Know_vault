import chromadb

client = chromadb.Client()
collection = client.create_collection(name="documents")




def add_data_to_database(File_name, embeding_list: list) -> list:
    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for item in embeding_list:
        ids.append(item["id"])
        documents.append(item["text"])
        embeddings.append(item["embedding"])  # already a list of floats
        metadatas.append({"File_Name": File_name})

    # return ids,documents,embeddings,metadatas
    for i  in embeddings:
        print(i)
        print(len(i))
        print(type(i))
# result = add_data_to_database("example.txt",vector_list)
# print(result)

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    result = collection.get(ids=["chunk_1"], include=["embeddings", "documents", "metadatas"])
    return {
    "ids": result["ids"],
    "documents": result["documents"],
    "metadatas": result["metadatas"],
    "embeddings": [emb.tolist() if hasattr(emb, "tolist") else emb for emb in result["embeddings"]]
}

