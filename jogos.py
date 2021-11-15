import forca
import adivinhacao_nivel

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação_nivel")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação_nivel")
        adivinhacao_nivel.jogar()

    if (__name__ == "__main__"):
    escolhe_jogo()