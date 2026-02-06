from fastapi import FastAPI
from pydantic import BaseModel
from .routers import jokenpo

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 2. Configura o Middleware logo abaixo do nascimento do app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jokenpo.router)

@app.get("/")
def home():
    return {"mensagem": "API Jokenpô PyReisen Online! 🚀 Use a rota /jogar para desafiar o sistema."}

