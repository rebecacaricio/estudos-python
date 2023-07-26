import random


print("**********************************")
print("Bem vindo ao Jogo de adivinhação")
print ("*********************************")

numero_secreto = round (random.randrange (1, 101))
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int (input ("Defina um nível:"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print(numero_secreto)
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    chute_str= input("Digite um número entre 1 e 100:")
    print ("Você digitou:", chute_str)
    chute = int(chute_str)

    if (chute <1 or chute > 100):
        print ("Você deve digitar um número entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("você errou!o seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! o seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    rodada = rodada + 1

print("fim do jogo")



