import random

def jogar_forca():

    abertura_do_jogo()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    errou = 0


    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas, palavra_secreta)
        else:
            errou += 1
            desenha_forca(errou)
        enforcou = errou == 7
        acertou = "_" not in letras_acertadas
        tentativas = 7 - errou
        print("Você possui mais {} tentativas".format(tentativas))

        print("\nCom seu chute a palavra ficou assim:")
        print(letras_acertadas)

    if(acertou):
        vencedor()

    else:
        perdedor(palavra_secreta)





def abertura_do_jogo():
    print("********************************")
    print("***Bem vindo no jogo de forca***")
    print("********************************")
    print("\n-Você possui 6 tentativas,GL HF-\n")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_das_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_das_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista_das_palavras))
    palavra_secreta = lista_das_palavras[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavras):
    return ["_" for letra in palavras]

def pede_chute():
    chute = input("Chute uma letra :D\n")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1



def desenha_forca(errou):
    print("  _______     ")
    print(" |/      |    ")

    if(errou == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errou == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errou == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errou == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errou == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errou == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errou == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()







def vencedor():
    print("\nParabéns, você acertou a palavra!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor(palavra_secreta):
    print("\nNão foi dessa vez, tente novamente :D")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar_forca()
