from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running. Visit /get-file to download the file."}

@app.get("/get-file")
def get_file():
    return {"message": "This API works fine."}

@app.get("/get-name")
def get_file():
    return {"message": "three idiots."}

