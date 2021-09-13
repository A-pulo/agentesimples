import numpy as np
import matplotlib.pyplot as plt
import random
import struct

# Função que exibe o ambiente na tela
def exibir(I):

    global posxy

    # Mostra o ambiente de acordo com a matriz I
    plt.imshow(I, 'gray')
    # Paleta de cores
    plt.jet()

    # Coloca o agente no ambiente 
    plt.plot(posxy[0], posxy[1], marker='h', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(1)
    plt.clf()

def agenteReativoSimples(x, y, estado):
    acoes = ["acima", "abaixo", "esquerda", "direita", "aspirar"]
    if estado == 2:
        return acoes[4]
    #Fazer parte do mapeamento
    #Teste
    if x == 1 and y == 1:
        return acoes[1]

def geraAmbiente():
    pass

# # Preparação do espaço
# Gera o espaço da sala como uma matriz 6x6
espaco = [[0 for n in range(7)] for n in range(7)]

# Gera sujeira
espaco = (np.random.rand(7, 7) > 0.7) * 2

# Delimita as paredes
for y in [0, 6]:
    for x in range(7):
        espaco[y][x] = 1
        espaco[x][y] = 1

#Pegar perceppção
posxy = [1,1]
exibir(espaco)
plt.pause(1)

acoes = ["acima", "abaixo", "esquerda", "direita", "aspirar"]
pontos = 0

# Execução do ambiente
while True:
    acao = agenteReativoSimples(posxy[0], posxy[1],espaco[posxy[1]][posxy[0]])
    if(acao == "acima"):
        posxy = [posxy[0], (posxy[1]-1)]
    elif(acao == "abaixo"):
        posxy = [posxy[0], (posxy[1]+1)]
    elif(acao == "esquerda"):
        posxy = [(posxy[0]-1), posxy[1]]
    elif(acao == "direita"):
        posxy = [(posxy[0]+1), posxy[1]]
    elif(acao == "aspirar"):
        espaco[posxy[1]][posxy[0]] = 0
    exibir(espaco)
