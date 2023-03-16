from random import choice
import csv
import os
from time import sleep


def menu_principal():
    print("---------------------\n"
          "Dificuldade\n"
          "[1] Fácil\n"
          "[2] Médio\n"
          "[3] Difícil\n"
          "[4] Sair\n"
          "---------------------")


def menu_facil():
    print("---------------------------------\n"
          "Opções:\n"
          "[1]Começar o jogo\n"
          "[2]Mostrar lista\n"
          "[3]Sair\n"
          "---------------------------------")


def menu_medio():
    print("---------------------------------\n"
          "Opções:\n"
          "[1]Começar o jogo\n"
          "[2]Adicionar palavra + dica\n"
          "[3]Remover palavra + dica\n"
          "[4]Mostrar lista\n"
          "[5]Sair\n"
          "---------------------------------")


def menu_dificil():
    print("---------------------------------\n"
          "Opções:\n"
          "[1]Começar o jogo\n"
          "[2]Adicionar palavra + dica\n"
          "[3]Remover palavra + dica\n"
          "[4]Mostrar lista\n"
          "[5]Sair\n"
          "---------------------------------")


def mostrar_lista(lista_palavras_param, lista_dicas_param):
    print("A lista de palavras é: {}".format(lista_palavras_param))
    print("A lista de dicas é: {}".format(lista_dicas_param))
    os.system('pause')
    os.system('cls')


def inicio_jogo(lista_palavras_param, lista_dicas_param, vidas_param):
    os.system('cls')
    letras_corretas = []
    letras_erradas = []
    palavra = ''
    palavra_escolhida = choice(lista_palavras_param[:])
    vidas = vidas_param

    separado = palavra_escolhida.split()
    for i in range(len(separado)):
        palavra = palavra + " " + '_' * len(separado[i])
        palavra_arrumada = palavra.strip()

    # aqui a logica acontece de chutar uma letra
    while palavra_arrumada.find('_') != -1:
        print("-" * 30)
        print("Letras corretas: {}".format(letras_corretas))
        print("Letras erradas: {}".format(letras_erradas))
        print("Vidas: {}".format(vidas))
        print(palavra_arrumada)
        tentativa = input("Chute uma letra ou 'dica': ").lower()
        os.system('cls')
        novo_i = 0

        if not tentativa.isalpha():
            print("-" * 30)
            print("Digite novamente, precisa ser uma letra. ")
            sleep(1.5)
            os.system('cls')
            continue

        # ta funcionando a dica
        if tentativa == "dica":
            print("-" * 30)
            print("A dica da palavra é: '{}'".format(lista_dicas_param[lista_palavras_param.index(palavra_escolhida)]))
            sleep(2)
            os.system('cls')

        # nao ta funcionando com duas palavas, so ta funcionando com a primeira palavra
        elif tentativa[0] not in letras_corretas and tentativa[0] not in letras_erradas:
            count = -1
            quantidade_antes = palavra_arrumada.count('_')

            for i in range(len(separado)):
                for x in range(len(separado[i])):
                    if x == 0 and i != novo_i:
                        count += 1
                    count += 1
                    novo_i = i

                    if tentativa[0] == separado[i][x]:
                        palavra_arrumada = palavra_arrumada[:count] + tentativa[0] + palavra_arrumada[
                                                                                     count + 1:]
                        letras_corretas.append(tentativa[0])
                        continue

            quantidade_depois = palavra_arrumada.count('_')
            if quantidade_antes == quantidade_depois:
                letras_erradas.append(tentativa[0])
                vidas -= 1

            if vidas == 0:
                print("-" * 30)
                print("Acabou suas vidas, você perdeu!")
                sleep(1.5)
                os.system('cls')
                break
        else:
            print("-" * 30)
            print("Essa letra já foi digitada!")
            sleep(1.5)
            os.system('cls')

    if palavra_arrumada.find('_') == -1:
        print("-" * 30)
        print("Parabéns! Você acertou a palavra '{}'!".format(palavra_escolhida))
        sleep(1.5)
        os.system('cls')


def acrescentar_lista(lista_palabras_param, lista_dicas_param):
    lista_palabras_param.append(input("Digite a palavra: "))
    lista_dicas_param.append(input("Digite a dica: "))
    print(lista_palabras_param)
    print(lista_dicas_param)
    sleep(2)
    os.system('cls')


def remover_lista(lista_palavras_param, lista_dicas_param):
    palavra_remover = input("Digite a palavra que quer remover+dica: ")
    for i in range(len(lista_palavras_param)):
        if palavra_remover == lista_palavras_param[i - 1]:
            lista_palavras_param.pop(i - 1)
            lista_dicas_param.pop(i - 1)
    print(lista_palavras_param)
    print(lista_dicas_param)
    sleep(2)
    os.system('cls')


def puxando_csv(lista_palavras_param, lista_dicas_param):
    with open("lista.csv", "r") as lista:
        arquivo_csv = csv.reader(lista, delimiter=",")
        for i in arquivo_csv:
            for x in range(2):
                if x == 0:
                    lista_palavras_param.append(i[x])
                else:
                    lista_dicas_param.append(i[x])
    lista.close()


def escrever_csv():
    lista = open("lista.csv", "a", newline="")
    tup = [input("Digite a palavra: "), input("Digite a dica:")]
    writer = csv.writer(lista)
    writer.writerow(tup)
    lista.close()
    print("Palavra e dica registrada com sucesso!")
    sleep(2)
    os.system('cls')


def apagar_csv(lista_palavras_param, lista_dicas_param):
    palavra_remover = input("Digite a palavra que quer remover+dica: ")
    for i in range(len(lista_palavras_param)):
        if palavra_remover == lista_palavras_param[i - 1]:
            palavra_remover_lista = lista_palavras_param[i - 1]
            dica_remover_lista = lista_dicas_param[i - 1]
            lista_palavras_param.pop(i - 1)
            lista_dicas_param.pop(i - 1)

    lista = open("lista.csv", "w")
    for i in range(len(lista_palavras_param)):
        lista.write(lista_palavras_param[i] + ',' + lista_dicas_param[i] + '\n')
    lista.close()
    sleep(2)
    os.system('cls')


def tratando_erro_menu(menu):
    while True:
        try:
            menu
            escolha_dificuldade = int(input("Digite uma das opções: "))
        except ValueError:
            print("-" * 30)
            print("Erro, o que você digitou não é uma opção")
            sleep(2)
            os.system('cls')
            continue
        break
    return escolha_dificuldade


def main():
    while True:
        os.system('cls')
        escolha_dificuldade = tratando_erro_menu(menu=menu_principal())
        os.system('cls')

        if escolha_dificuldade == 1:
            lista_palavras_facil = ["front end", "exame", "ferrari"]
            lista_dicas_facil = ["sinonimo de perder tempo", "teste", "carro de uma cor bem marcante"]

            while True:
                escolha_media = tratando_erro_menu(menu=menu_facil())
                os.system('cls')
                print("-" * 30)

                if escolha_media == 1:
                    inicio_jogo(lista_palavras_param=lista_palavras_facil, lista_dicas_param=lista_dicas_facil,
                                vidas_param=6)

                elif escolha_media == 2:
                    mostrar_lista(lista_palavras_param=lista_palavras_facil, lista_dicas_param=lista_dicas_facil)

                elif escolha_media == 3:
                    break

                else:
                    print("Erro")

        elif escolha_dificuldade == 2:
            lista_palavras_medio = ["front end", "exame", "ferrari"]
            lista_dicas_medio = ["sinonimo de perder tempo", "teste", "carro de uma cor bem marcante"]

            while True:
                escolha_media = tratando_erro_menu(menu=menu_medio())
                os.system('cls')
                print("-" * 30)

                if escolha_media == 2:
                    acrescentar_lista(lista_palabras_param=lista_palavras_medio, lista_dicas_param=lista_dicas_medio)

                elif escolha_media == 3:
                    remover_lista(lista_dicas_param=lista_dicas_medio, lista_palavras_param=lista_palavras_medio)

                elif escolha_media == 4:
                    mostrar_lista(lista_dicas_param=lista_dicas_medio, lista_palavras_param=lista_palavras_medio)

                elif escolha_media == 5:
                    os.system('cls')
                    break

                elif escolha_media == 1:
                    inicio_jogo(lista_palavras_param=lista_palavras_medio, lista_dicas_param=lista_dicas_medio,
                                vidas_param=3)

                else:
                    print("erro")

        elif escolha_dificuldade == 3:
            while True:
                lista_palavras_dificil = []
                lista_dicas_dificil = []
                lista_palavras_dificil.clear()
                lista_dicas_dificil.clear()
                puxando_csv(lista_palavras_param=lista_palavras_dificil, lista_dicas_param=lista_dicas_dificil)

                escolha_media = tratando_erro_menu(menu=menu_dificil())
                os.system('cls')
                print("-" * 30)

                if escolha_media == 2:
                    escrever_csv()

                elif escolha_media == 3:
                    apagar_csv(lista_dicas_param=lista_dicas_dificil, lista_palavras_param=lista_palavras_dificil)

                elif escolha_media == 4:
                    mostrar_lista(lista_palavras_param=lista_palavras_dificil, lista_dicas_param=lista_dicas_dificil)

                elif escolha_media == 5:
                    break

                elif escolha_media == 1:
                    inicio_jogo(lista_dicas_param=lista_dicas_dificil, lista_palavras_param=lista_palavras_dificil,
                                vidas_param=3)

                else:
                    print("erro")

        elif escolha_dificuldade == 4:
            print("Obrigado por jogar.")
            break

        else:
            menu_principal()
            print("Erro, o que você digitou não é uma opção")
            sleep(2)
            os.system('cls')


if __name__ == '__main__':
    main()
