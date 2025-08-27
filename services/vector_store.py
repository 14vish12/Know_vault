import chromadb
client = chromadb.Client()
collection = client.create_collection(name="documents")
def add_data_to_database(embeding_list :list) ->list:
    for item in embeding_list:
        unique_id = item["id"]
        original_text = item["text"]
        embeding_text = item["embeding"]
    collection.add(
      unique_id = unique_id,
      original_text = original_text,
      embedding_text = embeding_text
    )
    
