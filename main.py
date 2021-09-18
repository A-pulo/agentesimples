import numpy as np
import matplotlib.pyplot as plt

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


# Função de ação do agente
def agenteReativoSimples(x, y, estado):

    #  Variáveis de mapeamento do ultimo movimento do agente
    global x_dir  # 0 = esquerda, 1 = direita
    global y_dir  # 0 = acima, 1 = abaixo
    acoes = ["acima", "abaixo", "esquerda", "direita", "aspirar"]

    # Funções de escolha do movimento
    def vert():
        global y_dir
        if (y == 1 and y_dir == 0) or (y == 5 and y_dir == 1):
            y_dir = 0 ** y_dir
        return acoes[y_dir]

    def hori():
        global x_dir
        if (x == 1 and x_dir == 0) or (x == 5 and x_dir == 1):
            x_dir = 0 ** x_dir
            return vert()
        return acoes[x_dir + 2]

    def escolher_acao():
        if estado == 2:
            return acoes[4]
        return hori()

    # Ponto de execução da escolha do agente
    return escolher_acao()


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
posxy = [1, 1]

#  Variáveis de mapeamento do ultimo movimento
x_dir = 1 # 0 = esquerda, 1 = direita
y_dir = 1 # 0 = acima, 1 = abaixo

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
