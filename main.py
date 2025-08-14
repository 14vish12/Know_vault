import docx
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.upload import upload_file_router



new_app = FastAPI()

# Root page with HTML upload form
@new_app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <head>
            <title>Upload File</title>
        </head>
        <body>
            <h2>Upload a File</h2>
            <form action="/upload/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

new_app.include_router(upload_file_router)
