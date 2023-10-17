from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from src.routes.favicon_bank import return_favicon
from src.routes.favicon import gen_favicons
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/favicon/{bank_id}")
async def favicon(bank_id: str):
    return return_favicon(bank_id)

@app.get("/favicon")
async def favicon():
    return gen_favicons()

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")