import random
import time

print("🎮 Bem-vindo ao Jokenpô PyReisen!")

lista_jogadas = ["PEDRA", "PAPEL", "TESOURA"]
regras = {
    "PEDRA": "TESOURA",
    "TESOURA": "PAPEL",
    "PAPEL": "PEDRA"
}

historico_partidas = []

def instrucoes():
    return {
        "mensagem": "Use /jogar/pedra, /jogar/papel ou /jogar/tesoura para jogar."
    }
   
def jokenpo(jogada) :
   jogador = 0 
   sistema = 0
   jogada_usuario = ""
   jogada_sistema = ""
   vencedor = ""

   jogada_usuario = jogada.upper().strip()
  


   if not jogada_usuario or jogada_usuario not in lista_jogadas :
      return {
            "erro": True,
            "mensagem": "Jogada inválida! Escolha entre PEDRA, PAPEL ou TESOURA."
   }
  
   jogada_sistema = random.choice(lista_jogadas)   
     

    
   if jogada_usuario == jogada_sistema:
       mensagem = "😐 --- Empatou ---"
       vencedor = "empate"
   elif regras.get(jogada_usuario)== jogada_sistema:
       mensagem = "🏆💥 Você Venceu! 💥🏆"
       jogador += 1
       vencedor = "jogador"
   else : 
       mensagem = "💀❌ Você Perdeu! ❌💀"
       sistema += 1
       vencedor = "sistema"
 
   resultado_atual = {
            "rodada": len(historico_partidas) + 1,
            "sua_escolha": jogada_usuario,
            "escolha_sistema": jogada_sistema,
            "vencedor": vencedor
        }
        
   historico_partidas.append(resultado_atual)
   print(historico_partidas)

   resumo_final = None
   if len(historico_partidas) >= 3:
            resumo_final = historico_partidas[:] 
            historico_partidas.clear() 
   return {
            "resultado_rodada": mensagem,
            "dados": resultado_atual,
            "torneio_completo": resumo_final 
        }






 

