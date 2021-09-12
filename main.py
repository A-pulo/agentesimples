import numpy as np
import matplotlib.pyplot as plt
import random


# Função que exibe o ambiente na tela
def exibir(I):

    global posxy
    posxy = [random.randint(1, 5), random.randint(1, 5)]

    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.jet()

    # Coloca o agente no ambiente 
    plt.plot(posxy[0], posxy[1], marker='h', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)
    plt.clf()


def agenteReativoSimples(percepcao):
    pass


espaco = [[0 for n in range(7)] for n in range(7)]

for y in [0, 6]:
    for x in range(7):
        espaco[y][x] = 1
        espaco[x][y] = 1


while True:
    exibir(espaco)
