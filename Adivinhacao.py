import random

def jogar():

    print(11 * "-=")
    print(" JOGO DA ADIVINHAÇÃO")
    print(11 * "-=")

    numeroSecreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("1 - Fácil \n2 - Médio \n3 - Difícil")
    nivel = int(input("Defina o nivel do jogo: "))

    if(nivel == 1):
        tentativas = 15
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, tentativas))
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("Você chutou o numero: ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numeroSecreto

        if(acertou):
            print("\nVOCÊ ACERTOU!!!\nSua pontuação: {}".format(pontos))
            break
        else:
            if(chute > numeroSecreto):
                print("O seu chute foi MAIOR que o numero secreto!")
            elif(chute < numeroSecreto):
                print("Seu chute foi MENOR que o numero secreto")
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos
    print("\nO numero secreto é: ",numeroSecreto)

    print(15 * "=")
    print("Fim de jogo!")
    print(15 * "=")

if(__name__ == "__main__"):
    jogar()