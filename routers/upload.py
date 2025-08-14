from fastapi import APIRouter, File, UploadFile
import os, shutil
from datetime import datetime
from services.parser import extract_text_from_files
from services.chunker import chunk_text

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
    short_text = await chunk_text(result)
    return {
        "status": "success",
        "filename": custom_filename,
        "saved_to": file_location,
        "chunks": short_text
    }
