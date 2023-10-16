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
    # check if the bank exists in the database
    
    # return file
    return FileResponse(f"https://findata-assets.s3.amazonaws.com/favicon/{bank_id}.ico")

@app.get("/favicon")
async def favicon():
    return gen_favicons()