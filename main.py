import docx
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from routers.upload import upload_file_router


# ------------------------
# Initialize FastAPI
# ------------------------
app = FastAPI(title="KnowVault", description="A simple knowledge vault API", version="1.0")

# ------------------------
# Include Upload Router
# ------------------------
app.include_router(upload_file_router, prefix="/files", tags=["File Upload"])



# ------------------------
# Root HTML Form
# ------------------------
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <head>
            <title>KnowVault</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background: #fff;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
                    max-width: 500px;
                    width: 100%;
                    text-align: center;
                }
                h1 {
                    color: #444;
                    margin-bottom: 20px;
                }
                form {
                    margin: 20px 0;
                }
                input[type="file"], input[type="text"] {
                    width: 90%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    font-size: 14px;
                }
                input[type="submit"] {
                    background: #667eea;
                    color: white;
                    border: none;
                    padding: 12px 20px;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 15px;
                    transition: background 0.3s ease;
                }
                input[type="submit"]:hover {
                    background: #5a67d8;
                }
                .section {
                    margin-top: 30px;
                    padding-top: 10px;
                    border-top: 1px solid #eee;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📂 KnowVault</h1>
                <p>Upload your files and query them instantly</p>

                <!-- Upload Section -->
                <div class="section">
                    <h2>Upload a File</h2>
                    <form action="/files/upload" enctype="multipart/form-data" method="post">
                        <input name="file" type="file" required>
                        <input type="submit" value="Upload File">
                    </form>
                </div>

                <!-- Search Section -->
                <div class="section">
                    <h2>🔎 Search Query</h2>
                    <form action="/query" method="post">
                        <input name="query" type="text" placeholder="Enter your query..." required>
                        <input type="submit" value="Search">
                    </form>
                </div>
            </div>
        </body>
    </html>
    """

# ------------------------
# Query Endpoint
# ------------------------
@app.post("/query", tags=["Search"])
async def query_endpoint(query: str):
    from routers.query import search_documents, QueryRequest
    request = QueryRequest(query=query)
    return await search_documents(request)
