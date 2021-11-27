def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Qual a letra? ")

        index = 1
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
     jogar()
