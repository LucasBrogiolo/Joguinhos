def jogar():
    from random import randint

    letrasErradas = []
    erro = 0
    IMG = [
    '''
    +___+
    |   |
    |
    |
    |
    ''', 
    '''
    +___+
    |   |
    |   O
    |
    |
    ''',
    '''
    +___+
    |   |
    |   O
    |   |
    |
    ''',
    '''
    +___+
    |   |
    |   O
    |  /|
    |
    ''',
    '''
    +___+
    |   |
    |   O
    |  /|\\
    |
    ''',
    '''
    +___+
    |   |
    |   O
    |  /|\\
    |  /
    ''',
    '''
    +___+
    |   |
    |   O
    |  /|\\
    |  / \\
    ''']
    def listToString(l):
        str1 = ""
        for letra in l:
            str1 += letra
        return str1

    def palavraSecret():
        grupo = ["arroz", "farofa", "hoverboard", "cachorro", "floresta", "geleira", "bolota"]
        indice = randint(0, len(grupo) - 1)
        return grupo[indice]

    def palavraAcert(x):
        vazia = []
        escolhida = range(len(x))
        for i in escolhida:
            vazia.append("_ ")
        return vazia

    palavraSecreta = palavraSecret()
    letrasAcertadas = palavraAcert(palavraSecreta)    
    print("\n********************************")
    print("*******   JOGO DA FORCA   *******")
    print("********************************\n")

    while True:
        print(IMG[erro])
        palavraFormada = listToString(letrasAcertadas)
        print(palavraFormada.upper())
        if palavraSecreta == listToString(letrasAcertadas):
            print("**********\nVocê Acertou\n**********")
            print("\nFIM DO JOGO\n")
            break
        elif erro == 6:
            print("**********\nAcabou suas chances\n**********")
            print("\nFIM DO JOGO\n")
            break
        chute = input("\nQual a letra?")
        posicao = 0
        if chute not in palavraSecreta:
            letrasErradas.append(chute)
            erro += 1
        else:
            for letra in palavraSecreta:
                if (chute.upper() == letra.upper()):
                    letrasAcertadas[posicao] = letra
                posicao += 1      
        print(f"\nas letras erradas são: {letrasErradas}\n")