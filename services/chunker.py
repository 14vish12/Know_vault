
async def chunk_text(text: str, chunk_size: int = 500, file_id: str = "file") -> list:
    words = text.strip().split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

    return [
        {"id": f"{file_id}_chunk_{i}", "text": chunk}
        for i, chunk in enumerate(chunks)
    ]

