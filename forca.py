def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        letras_faltando = str(letras_acertadas.count('_'))
        if (letras_faltando == "0"):
            print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))
            acertou = True
        else:
            print(letras_acertadas)
            print('Ainda faltam acertar {} letras'.format(letras_faltando))

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()