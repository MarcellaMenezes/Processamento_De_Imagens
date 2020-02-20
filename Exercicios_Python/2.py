import random

jogo = ['pedra', 'papel', 'tesoura']
ganhou = -1

while(ganhou!=1):
    jogada_pc = random.randint(0,2)

    jogada_user = input("Digite sua opcao: ")
    jogada_user_posi = jogo.index(jogada_user)

    print("Pc escolheu: ", jogo[jogada_pc])

    #PC PEDRA
    if(jogada_pc == 0 and jogada_user_posi == 1):
        ganhou=1
    elif(jogada_pc == 0 and jogada_user_posi == 2):
        print("Voce perdeu !")
        
    #PC PAPEL
    elif(jogada_pc == 1 and jogada_user_posi == 0):
        print("Voce perdeu !")
    elif(jogada_pc == 1 and jogada_user_posi == 2):
       ganhou=1

    #PC TESOURA
    elif(jogada_pc == 2 and jogada_user_posi == 0):
        ganhou=1
    elif(jogada_pc == 2 and jogada_user_posi == 1):
        print("Voce perdeu !") 
    
    #EMPATES
    elif(jogada_pc == 0 and jogada_user_posi == 0):
        print("Empate !")
    elif(jogada_pc == 1 and jogada_user_posi == 1):
        print("Empate !")
    elif(jogada_pc == 2 and jogada_user_posi == 2):
        print("Empate !") 

print("Parabéns! Você ganhou de um pc!")
