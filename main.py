from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running. Visit /get-file to download the file."}

@app.get("/get-file")
def get_file():
    file_path = "sample.txt"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename="sample.txt", media_type='text/plain')
    return {"error": "File not found"}
