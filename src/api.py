from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from src.routes.favicon import gen_favicons
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/favicon/{bank_id}")
async def favicon(bank_id: str):
    # check if file exists
    if not os.path.isfile(f"src/assets/{bank_id}.ico"):\
        return Response(status_code=404, content="{\"status\": \"error\", \"message\": \"File not found\"}")
    
    # return file
    return FileResponse(f"src/assets/{bank_id}.ico")

@app.get("/favicon")
async def favicon():
    return gen_favicons()