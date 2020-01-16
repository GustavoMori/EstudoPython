def jogar_adivinhacao():
    import random


    print("********************************")
    print("Bem vindo no jogo de Adivinhação")
    print("********************************")

    numero_secreto = (random.randrange(1,101))
    tentativas = 0
    pontos = 1000

    print("Você possui inicialmente 1000 pontos")
    print("Selecione o nível de dificuldade:")
    print("1 - fácil\n2 - médio\n3 - difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas+1) :
        print("Tentativa: {} de {}".format(rodada, tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("\nVocê digitou " , chute)

        chute = int(chute)
        if (chute <= 1 or chute >= 100):
            print("\nVocê deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("\nERRRROUUUUUUUUU, o seu chute foi maior que o número secreto.\n")
            elif (menor):
                print("\nERRRROUUUUUUUUU, o seu chute foi menor que o número secreto.\n")
            perdidos = abs(numero_secreto - chute)
            pontos = pontos - perdidos


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()
