import random

numero_sorteado = random.randint(0,20)
numero_chutado = -2

numero_chutado = int(input("Digite um numero: "))
while(numero_chutado!=numero_sorteado):
    
    if(numero_chutado>numero_sorteado):
        numero_chutado = int(input("Digite um valor menor: "))
    else:
        numero_chutado = int(input("Digite um valor maior: "))
print("Voce acertou, o numero sorteado era ", numero_sorteado)         
    
