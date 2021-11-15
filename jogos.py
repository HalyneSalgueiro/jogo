import forca
import adivinhacao_nivel

print("*********************************")
print("******Escolhe o seu jogo!********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao_nivel.jogar_adivinhacao()


print("Fim de jogo")