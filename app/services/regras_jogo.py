import random
import time

print("🎮 Bem-vindo ao Jokenpô PyReisen!")

lista_jogadas = ["PEDRA", "PAPEL", "TESOURA"]
regras = {
    "PEDRA": "TESOURA",
    "TESOURA": "PAPEL",
    "PAPEL": "PEDRA"
}
   
def jokenpo(jogada) :
   jogador = 0 
   sistema = 0
   jogada_usuario = ""
   jogada_sistema = ""

   jogada_usuario = jogada.upper().strip()
  


   if not jogada_usuario or jogada_usuario not in lista_jogadas :
      return {
            "erro": True,
            "mensagem": "Jogada inválida! Escolha entre PEDRA, PAPEL ou TESOURA."
   }
  
   jogada_sistema = random.choice(lista_jogadas)   
     

    
   if jogada_usuario == jogada_sistema:
       menssagem = "😐 --- Empatou ---"
   elif regras.get(jogada_usuario)== jogada_sistema:
       menssagem = "🏆💥 Você Venceu! 💥🏆"
       jogador += 1
   else : 
       menssagem = "💀❌ Você Perdeu! ❌💀"
       sistema += 1
   return {
        "sua_escolha": jogada_usuario,
        "escolha_sistema": jogada_sistema,
        "mensagem": menssagem
    } 
       




 

