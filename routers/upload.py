from fastapi import APIRouter, File, UploadFile
import os, shutil
from datetime import datetime
from services.parser import extract_text_from_files
from services.chunker import chunk_text
from services.embeding import embed_chunks
from services.vector_store import add_data_to_database

upload_file_router = APIRouter()  # ✅ This is important

UPLOAD_DIR = "processed_file"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@upload_file_router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    custom_filename = f"uploaded_{timestamp}.{ext}"
    file_location = os.path.join(UPLOAD_DIR, custom_filename)

    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = await extract_text_from_files(file_location)
    chunkwise_text = await chunk_text(result)
   
    vector_text = embed_chunks(chunkwise_text)
    vector_store = add_data_to_database(ext,vector_text)
    return {
        "status": "success",
        "filename": custom_filename,
        "saved_to": file_location,
        # "chunks": chunkwise_text,
        # "vectors": vector_text
        "Database" : vector_store
    }
