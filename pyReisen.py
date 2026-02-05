#Script original

import random
import time

print("🎮 Bem-vindo ao Jokenpô PyReisen!")

lista_jogadas = ["PEDRA", "PAPEL", "TESOURA"]
regras = {
    "PEDRA": "TESOURA",
    "TESOURA": "PAPEL",
    "PAPEL": "PEDRA"
}

def obter_jogadas() :
   while True :
     jogada_usuario = input("\n Digite sua escolha:").upper().strip()
     if valida_jogada(jogada_usuario) :
         break
   jogada_sistema = random.choice(lista_jogadas)
   return jogada_usuario, jogada_sistema 

def valida_jogada(jogada) : 
    if not jogada or jogada not in lista_jogadas :
      print("Jogada invalida! \n Escolha entre Pedra, Papel ou Tesoura.")
      return False 
    return True 
   
def jokempo() :
  jogador = 0 
  sistema = 0
  partida = 3
  
  for i in range(partida) :
    print(f"\n **Rodada: {i+1} de {partida}**")
    jogada_usuario , jogada_sistema = obter_jogadas()    
     
    print(f"\n 🧑 Sua escolha: {jogada_usuario} \n 🤖 Escolha do Sistema: {jogada_sistema}")
    
    if jogada_usuario == jogada_sistema:
       print("😐 --- Empatou ---")
    elif regras.get(jogada_usuario)== jogada_sistema:
         print("🏆💥 Você Venceu! 💥🏆")
         jogador += 1
    else : 
        print("💀❌ Você Perdeu! ❌💀")
        sistema += 1
  return jogador, sistema 
  
inicio = time.time()
jogador, sistema = jokempo()
fim = time.time()        
        
print("\n📊 RESULTADO FINAL")
print(f"Jogador: {jogador}")
print(f"Sistema: {sistema}")
print(f"⏱️ Tempo total da partida: {fim - inicio:.2f} segundos")          

         

         



 

