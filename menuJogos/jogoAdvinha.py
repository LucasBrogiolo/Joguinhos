def jogar():
    from random import randint
    import sys

    numero = randint(0, 100)
    tentativas = []
    contador = 7
    print("\n*******************************")
    print("******* Acerte o número *******")
    print("*******************************\n")
    while contador != 0:
        try:
            chute = float(input("\nDigite um numero: "))
            tentativas.append(int(chute))
            print("\n************************************")
            print("***** Placar ************************")
            print(f"***** Tentativas Restantes: {contador}")
            print(f"***** Suas tentativas foram {tentativas}")
            print("************************************")
            acertou = numero == chute
            maior = chute > numero
            menor = chute < numero
            if acertou:
                print("\nParabéns!! Você acertou\n")
                sys.exit()
            elif maior:
                print("\nErrou, seu chute foi maior que o numero secreto\n")
            elif menor:
                print("\nErrou, seu chute foi menor que o numero secreto\n")
        except:
            if acertou:
                sys.exit()
            else:
                print("digite um valor valido")
        contador-=1

    print("\n********************************")
    print("*** Suas tentativas acabaram ****")
    print("********************************\n")