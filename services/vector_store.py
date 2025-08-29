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

   

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return collection.get(
        ids=[ids[0]]
    )
