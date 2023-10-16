from fastapi import FastAPI

# from src.utilities.db import DB



app = FastAPI()

@app.get("/")
async def root():
    # db = DB()
    # db.insert("BANK", {"id": "BC", "name": "Bancolombia", "website": "https://www.grupobancolombia.com", "favicon": "https://www.grupobancolombia.com/favicon.ico"})
    return {"message": "Hello World"}
