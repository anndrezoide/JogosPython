import Adivinhacao
import Forca

def escolherJogo():
    print(20 * "-=")
    print("             MENU DE JOGOS")
    print(20 * "-=")

    print("1 - ADIVINHAÇÃO \n2 - FORCA")
    jogo = int(input("Informe: "))

    if(jogo == 1):
        Adivinhacao.jogar()
    else:
        Forca.jogar()

if(__name__ == "__main__"):
    escolherJogo()