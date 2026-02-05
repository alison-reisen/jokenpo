from fastapi import APIRouter
from app.services import regras_jogo


router = APIRouter()

@router.get("/jogar/{escolha}")
async def jogar(escolha: str):
    escolha_usuario = escolha
    print(escolha_usuario)
    resultado = regras_jogo.jokenpo(escolha_usuario)
    print(resultado)
    return resultado
    
