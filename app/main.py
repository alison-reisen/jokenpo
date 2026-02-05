from fastapi import FastAPI
from pydantic import BaseModel
from .routers import jokenpo

app = FastAPI()

app.include_router(jokenpo.router)

@app.get("/")
def home():
    return {"mensagem": "API Jokenpô PyReisen Online! 🚀 Use a rota /jogar para desafiar o sistema."}

