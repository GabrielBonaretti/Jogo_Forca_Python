from jogo_forca_funcoes import dificil
from jogo_forca_funcoes import medio
from jogo_forca_funcoes import facil
from jogo_forca_funcoes import menu
from time import sleep
import os


def main():
    while True:
        os.system('cls')
        escolha_dificuldade = menu(escolha_dificuldade_param=0)
        os.system('cls')

        if escolha_dificuldade == "Fácil":
            facil()

        elif escolha_dificuldade == "Médio":
            medio()

        elif escolha_dificuldade == "Difícil":
            dificil()

        elif escolha_dificuldade == "Sair":
            print("Obrigado por jogar \033[31m♥♥♥♥\033[m")
            sleep(2)
            break


if __name__ == '__main__':
    main()