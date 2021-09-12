import numpy as np
import matplotlib.pyplot as plt
import random


# Função que exibe o ambiente na tela
def exibir(I):

    global posxy
    posxy = [random.randint(1, 5), random.randint(1, 5)]

    # Mostra o ambiente de acordo com a matriz I
    plt.imshow(I, 'gray')
    # Paleta de cores
    plt.jet()

    # Coloca o agente no ambiente 
    plt.plot(posxy[0], posxy[1], marker='h', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)
    plt.clf()


def agenteReativoSimples(percepcao):
    pass

# # Preparação do espaço

# Gera o espaço da sala como uma matriz 6x6
espaco = [[0 for n in range(7)] for n in range(7)]

# Delimita as paredes
for y in [0, 6]:
    for x in range(7):
        espaco[y][x] = 1
        espaco[x][y] = 1

# Execução do ambiente
while True:
    exibir(espaco)
