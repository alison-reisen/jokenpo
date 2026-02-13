from fastapi import APIRouter
from app.services import regras_jogo


router = APIRouter()

#@router.get("/jogar")
  #  return("Escolha um das opções e preencha na url após o / : Pedra, Papel ou tesoura")


@router.get("/jogar/{escolha}")
async def jogar(escolha: str):
    escolha_usuario = escolha
    
    resultado = regras_jogo.jokenpo(escolha_usuario)
    return resultado
    
