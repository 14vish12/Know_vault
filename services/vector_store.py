import chromadb

client = chromadb.Client()
collection = client.create_collection(name="documents")
def add_data_to_database(File_name,embeding_list :list) ->list:
    for item in embeding_list:
      unique_id = item["id"]
      original_text = item["text"]
      embeding_text = item[["embedding"]]

      metadata = [{"File_Name":File_name}]
      collection.add(
      ids = unique_id,
      documents=  original_text,
      embeddings= embeding_text,
      metadatas=metadata
      )
    
    return collection.get(ids=["file_chunk_0"],include=["embeddings", "documents", "metadatas"])
    
