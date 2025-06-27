import random
# Biblioteca para efetivar o dorteio do numero, já pronto, apenas iremos informar posteriomente o inter
import os
#biblioteca do sistema operacional, para limpar a tela, se windows cls, no linux clear
erros = 0
sorteado=random.randrange(0,100)
jogador=int(input("digite seu número!  "))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
        erros+=1
        jogador=int(input("digite seu número: " ))
        print("número" + str(jogador) + " , você acertou em: " + str(erros+1) + " tentativas")