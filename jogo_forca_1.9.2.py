import jogo_forca_funcoes
import os
from time import sleep


def main():
    while True:
        os.system('cls')
        escolha_dificuldade = jogo_forca_funcoes.tratando_erro_menu()  # "tratando_erro_menu", do menu principal
        os.system('cls')

        if escolha_dificuldade == 1:
            jogo_forca_funcoes.facil(escolha_dificuldade_param=escolha_dificuldade)

        elif escolha_dificuldade == 2:
            jogo_forca_funcoes.medio(escolha_dificuldade_param=escolha_dificuldade)

        elif escolha_dificuldade == 3:
            jogo_forca_funcoes.dificil(escolha_dificuldade_param=escolha_dificuldade)

        elif escolha_dificuldade == 4:
            print("Obrigado por jogar \033[31m♥♥♥♥\033[m")
            sleep(2)
            break

        else:
            jogo_forca_funcoes.menu(0)  # printar o menu principal
            print("Erro, o que você digitou não é uma opção")
            sleep(2)
            os.system('cls')


if __name__ == '__main__':
    main()
