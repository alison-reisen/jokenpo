from fastapi import APIRouter
from app.services import regras_jogo


router = APIRouter()

@router.get("/jogar")
async def como_jogar():
    return regras_jogo.instrucoes()

@router.get("/jogar/{escolha}")
async def jogar(escolha: str):
    escolha_usuario = escolha
    
    resultado = regras_jogo.jokenpo(escolha_usuario)
    return resultado
    
