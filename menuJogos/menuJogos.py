import forca
import jogoAdvinha
import sys

print('\n*********************************')
print('**********MENU DE JOGOS**********')
print('*********************************')
print("1. Adivinhação")
print("2. Forca")
print("3. Sair")
escolha = int(input("Qual jogo quer jogar? Digite o número: "))
while True:
    if escolha == 1:
        jogoAdvinha.jogar()
    elif escolha == 2:
        forca.jogar()
    elif escolha == 3:
        print("obrigado por jogar")
        sys.exit()
    else:
        print("escolha uma opcao válida")
        escolha = int(input("Qual jogo quer jogar? Digite o número: "))