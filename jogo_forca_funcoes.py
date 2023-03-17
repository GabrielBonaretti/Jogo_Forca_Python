from random import choice
from time import sleep
import inquirer
import csv
import sys
import os


def menu(escolha_dificuldade_param):
    '''
    A função menu tem como objetivo mostar o menu dependedo de onde o usuário está, no qual ele faz a escolha a partir das setas. 
    :param escolha_dificuldade_param: escolha do menu que está sendo utilizado.
    :return: print do menu e escolha do usuário com a biblioteca inquirer.
    '''

    if escolha_dificuldade_param == 0:
        sys.path.append(os.path.realpath("."))
        menu_principal = [
            inquirer.List(
            "escolha",
            message="Dificuldade",
            choices=["Fácil", "Médio", "Difícil", "Sair"],
            ),
        ]
        answers = inquirer.prompt(menu_principal)
        resposta = answers.get("escolha")   

    elif escolha_dificuldade_param == 1:
        sys.path.append(os.path.realpath("."))
        menu_facil = [
            inquirer.List(
            "escolha",
            message="Opções",
            choices=["Começar o jogo", "Mostrar lista", "Sair"],
            ),
        ]
        answers = inquirer.prompt(menu_facil)
        resposta = answers.get("escolha")      

    elif escolha_dificuldade_param == 2:
        sys.path.append(os.path.realpath("."))
        menu_medio = [
            inquirer.List(
            "escolha",
            message="Opções",
            choices=["Começar o jogo", "Adicionar palavra + dica", "Remover palavra + dica", "Mostrar lista", "Sair"],
            ),
        ]   
        answers = inquirer.prompt(menu_medio)
        resposta = answers.get("escolha")   

    elif escolha_dificuldade_param == 3:
        sys.path.append(os.path.realpath("."))
        menu_dificil = [
            inquirer.List(
            "escolha",
            message="Opções",
            choices=["Começar o jogo", "Adicionar palavra + dica", "Remover palavra + dica", "Mostrar lista", "Sair"],
            ),
        ]   
        answers = inquirer.prompt(menu_dificil)
        resposta = answers.get("escolha")   
    
    print(resposta)
    return resposta


def mostrar_lista(lista_palavras_param, lista_dicas_param):
    '''
    Função para printar a lista de palavras para o usuário
    :param lista_palavras_param: A lista de palavras armazenada
    :param lista_dicas_param: A lista de dicas armazenda
    :return: printar as listas.
    '''
    print("A lista de palavras é: {}".format(lista_palavras_param))
    print("A lista de dicas é: {}".format(lista_dicas_param))
    os.system('pause')
    os.system('cls')


def inicio_jogo(lista_palavras_param, lista_dicas_param, vidas_param):
    """
    Toda lógica de funcionamento do jogo, no qual eu crio uma palavra semelhante a original, uma "palavra falsa" da
    que foi sorteada na lista, apenas com underlines.
    Então a partir do chute do usuário comparo as variáveis para assim se necessario acrescentar o chute do usuário a
    palavra falsa, além de acrecestar a uma lista de letras
    corretas.
    Caso o chute do usuário não tenha na palavra original o usuario perde uma vida e o chute é acrescentado na lista de
    erros.
    Caso o usuário chute uma letra repetida ou algo que não é uma letra o código não aceita. Caso seu numero de vidas
    chegue a zero ele perde,
    caso suas vidas acabem ele perde o jogo.

    :param lista_palavras_param: lista de palvras para serem sorteadas
    :param lista_dicas_param: lista de dicas das palavras
    :param vidas_param: quantidade de vida do usuário (por ser 3 ou 6) depende da dificuldade
    :return: o jogo
    """
    os.system('cls')

    # puxando as variáveis
    letras_corretas = []
    letras_erradas = []
    palavra = ''
    palavra_escolhida = choice(lista_palavras_param[:])
    vidas = vidas_param

    # criando a palavra falsa
    separado = palavra_escolhida.split()
    for i in range(len(separado)):
        palavra = palavra + " " + '_' * len(separado[i])
        palavra_arrumada = palavra.strip()

    # aqui a logica acontece de chutar uma letra
    while palavra_arrumada.find('_') != -1:  # caso ainda tenha underline na palavra falsa continua.
        print("-" * 30)
        print("Letras corretas: {}".format(letras_corretas))
        print("Letras erradas: {}".format(letras_erradas))
        print("Vidas: {}".format(vidas))
        print(palavra_arrumada)
        tentativa = input("Chute uma letra ou 'dica': ").lower()  # chute do usuário
        os.system('cls')
        novo_i = 0

        if len(tentativa) == 0:
            print("-" * 30)
            print("Digite novamente, precisa ser uma letra. ")
            sleep(1.5)
            os.system('cls')
            continue

        # caso nao seja alpha, ou algarismo
        if not tentativa[0].isalpha():
            print("-" * 30)
            print("Digite novamente, precisa ser uma letra. ")
            sleep(1.5)
            os.system('cls')
            continue

        # printa a dica pelo index, caso o usuário escreva dica
        if tentativa == "dica":
            print("-" * 30)
            print("A dica da palavra é: '{}'".format(lista_dicas_param[lista_palavras_param.index(palavra_escolhida)]))
            sleep(2)
            os.system('cls')

        # se a pessoa tentar a palavra certa
        elif tentativa == palavra_escolhida:
            palavra_arrumada = palavra_escolhida

        # se a tentativa ja estiver na lista correta ou lista errada, não entra
        elif tentativa[0] not in letras_corretas and tentativa[0] not in letras_erradas:
            count = -1
            quantidade_antes = palavra_arrumada.count('_')

            # verificar se a pessoa acertou
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

            # verificar se a pessoa errou
            if quantidade_antes == quantidade_depois:
                letras_erradas.append(tentativa[0])
                vidas -= 1

            # se a vida chegar a zero
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
    '''
    Acrescentar palavra mais dica na lista no python.
    :param lista_palabras_param: lista palavras
    :param lista_dicas_param: lista de dicas das palavras
    :return: lista com as palavras adicionadas
    '''
    lista_palabras_param.append(input("Digite a palavra: "))
    lista_dicas_param.append(input("Digite a dica: "))
    print(lista_palabras_param)
    print(lista_dicas_param)
    sleep(2)
    os.system('cls')


def remover_lista(lista_palavras_param, lista_dicas_param):
    '''
    Remover palavras + dicas da lista de palavras e dicas
    :param lista_palavras_param: lista de palavras
    :param lista_dicas_param: lista de dicas
    :return: lista com as palavras e dicas removidas
    '''
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
    '''
    Puxando as palavras e dicas de um arquivo externo ".csv" e adicionando-os em suas respectivas listas
    :param lista_palavras_param: lista de palavras
    :param lista_dicas_param: lista de dicas das palavras
    :return: lista de palavras e dicas atualizadas de acordo com o arquivo ".csv"
    '''
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
    '''
    Adicionar uma palavra + dica no arquivo ".csv"
    :return: Arquivo ".csv" atualizado
    '''
    lista = open("lista.csv", "a", newline="")
    tup = [input("Digite a palavra: "), input("Digite a dica: ")]
    writer = csv.writer(lista)
    writer.writerow(tup)
    lista.close()
    print("Palavra e dica registrada com sucesso!")
    sleep(2)
    os.system('cls')


def apagar_csv(lista_palavras_param, lista_dicas_param):
    '''
    Apaga uma palavra + dica do arquivo ".csv".
    Remove e a palavra digitada pelo usuário da lista de palavras + dicas, muito semelhante a
    função "remover_lista".
    Após isso a função analisa a lista de palavras e dicas que foi preenchida pela funcão
    "puxando_csv" e partir dela reescreve o arquivo ".csv" com o conteudo cintido nas listas.

    :param lista_palavras_param:
    :param lista_dicas_param:
    :return:
    '''
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


def facil():
    '''
    Dificuldade facil do jogo da forca, no qual puxa as funcoes de "inicio_de_jogo" ou
    "mostrar_lista" a apartir do retorno da função "menu" do menu da dificuldade
    fácil.
    :return: retorna o jogo na dificuldade fácil
    '''
    lista_palavras_facil = ["front end", "exame", "ferrari"]
    lista_dicas_facil = ["sinonimo de perder tempo", "teste", "carro de uma cor bem marcante"]

    while True:
        escolha_media = menu(1)
        os.system('cls')
        print("-" * 30)

        if escolha_media == "Começar o jogo":
            inicio_jogo(lista_palavras_param=lista_palavras_facil, lista_dicas_param=lista_dicas_facil,
                        vidas_param=6)

        elif escolha_media == "Mostrar lista":
            mostrar_lista(lista_palavras_param=lista_palavras_facil, lista_dicas_param=lista_dicas_facil)

        elif escolha_media == "Sair":
            break

        else:
            print("Erro")


def medio():
    '''
    Dificuldade médiado jogo da forca, no qual puxa as funções de "acrescentar_lista", "remover_lista",
    "inicio_de_jogo" ou "mostrar_lista" a apartir do retorno da função "menu" do menu da dificuldade
    média.
    :return: retorna o jogo na dificuldade média
    '''
    lista_palavras_medio = ["front end", "exame", "ferrari"]
    lista_dicas_medio = ["sinonimo de perder tempo", "teste", "carro de uma cor bem marcante"]

    while True:
        escolha_media = menu(2)
        os.system('cls')
        print("-" * 30)

        if escolha_media == "Adicionar palavra + dica":
            acrescentar_lista(lista_palabras_param=lista_palavras_medio, lista_dicas_param=lista_dicas_medio)

        elif escolha_media == "Remover palavra + dica":
            remover_lista(lista_dicas_param=lista_dicas_medio, lista_palavras_param=lista_palavras_medio)

        elif escolha_media == "Mostrar lista":
            mostrar_lista(lista_dicas_param=lista_dicas_medio, lista_palavras_param=lista_palavras_medio)

        elif escolha_media == "Sair":
            os.system('cls')
            break

        elif escolha_media == "Começar o jogo":
            inicio_jogo(lista_palavras_param=lista_palavras_medio, lista_dicas_param=lista_dicas_medio,
                        vidas_param=3)

        else:
            print("erro")


def dificil():
    '''
    Dificuldade dificil do jogo da forca, no qual primeiramente puxa a função "puxando_csv". E após isso a partir do
    retorno da função "menu" do menu da dificuldade média pode chamar as funções de "escrever_csv",
    "apagar_csv", "inicio_de_jogo" ou "mostrar_lista" média.
    :return: retorna o jogo na dificuldade difícil
    '''
    while True:
        lista_palavras_dificil = []
        lista_dicas_dificil = []
        lista_palavras_dificil.clear()
        lista_dicas_dificil.clear()
        puxando_csv(lista_palavras_param=lista_palavras_dificil, lista_dicas_param=lista_dicas_dificil)

        escolha_media = menu(3)
        os.system('cls')
        print("-" * 30)

        if escolha_media == "Adicionar palavra + dica":
            escrever_csv()

        elif escolha_media == "Remover palavra + dica":
            apagar_csv(lista_dicas_param=lista_dicas_dificil, lista_palavras_param=lista_palavras_dificil)

        elif escolha_media == "Mostrar lista":
            mostrar_lista(lista_palavras_param=lista_palavras_dificil, lista_dicas_param=lista_dicas_dificil)

        elif escolha_media == "Sair":
            break

        elif escolha_media == "Começar o jogo":
            inicio_jogo(lista_dicas_param=lista_dicas_dificil, lista_palavras_param=lista_palavras_dificil,
                        vidas_param=3)

        else:
            print("erro")
