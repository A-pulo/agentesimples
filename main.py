import numpy as np
import matplotlib.pyplot as plt

# Função que exibe o ambiente na tela
def exibir(I):

    global posxy
    global position

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

def calcularDistancia(x,y,xobjetivo,yobjetivo):
    distancia = 0
    while x != xobjetivo:
        if x > xobjetivo:
            x -= 1
            distancia +=1
        else:
            x+=1
            distancia += 1
    while y != yobjetivo:
        if y > yobjetivo:
            y -= 1
            distancia +=1
        else:
            y +=1
            distancia += 1
    return distancia

def sujeiraMaisProxima(x,y):

    #Retorna a posição que existe sujeira
    resultado = np.where(espaco == 2)
    contador = 0

    #Retorno do método
    posicaoSujeira = []

    #Número estipulado usando tamanho da matriz
    menorDistancia = 6 * 6

    #Verifica qual é a sujeira mais proxima da posicao x y
    while contador < len(resultado[0]):
        sujeira = [resultado[0][contador], resultado[1][contador]]
        d = calcularDistancia(y,x,sujeira[0], sujeira[1])
        if (d < menorDistancia):
            menorDistancia = d
            posicaoSujeira.clear()
            posicaoSujeira.append(sujeira[0])
            posicaoSujeira.append(sujeira[1])
        contador += 1

    return posicaoSujeira

def posicaoMaisProximaSujeira(x, y, sujeira, espaco):

    #Todos as posições adjacentes da posição atual (x,y) que não são paredes
    listaAdjacente = []

    abaixo = [x, y + 1]
    acima = [x, y -1]
    esquerda = [x - 1,y]
    direita =[x+1, y]

    # Número estipulado usando tamanho da matriz
    menorDistancia = 6 * 6

    #Retorno do método
    retornoAdjacente = []

    if(espaco[acima[1]][acima[0]] != 1):
        #Posicao x, y e acao
        adjacente = [acima[1], acima[0], 0]
        listaAdjacente.append(adjacente)
    if(espaco[abaixo[1]][abaixo[0]] != 1):
        # Posicao x, y e acao
        adjacente = [abaixo[1], abaixo[0], 1]
        listaAdjacente.append(adjacente)
    if (espaco[esquerda[1]][esquerda[0]] != 1):
        # Posicao x, y e acao
        adjacente = [esquerda[1], esquerda[0], 2]
        listaAdjacente.append(adjacente)
    if (espaco[direita[1]][direita[0]] != 1):
        # Posicao x, y e acao
        adjacente = [direita[1], direita[0], 3]
        listaAdjacente.append(adjacente)

    #Buscar posição adjacente com menor distância da sujeira
    for item in listaAdjacente:
        d = calcularDistancia(item[0], item[1], sujeira[0], sujeira[1])
        if(d < menorDistancia):
            menorDistancia = d
            retornoAdjacente.clear()
            retornoAdjacente.append(item[0])
            retornoAdjacente.append(item[1])
            retornoAdjacente.append(item[2])

    return retornoAdjacente

def agenteObjetivo(x, y, estado, objObtido, espaco, sujeira):
    acoes = ["acima", "abaixo", "esquerda", "direita", "aspirar", "NoOp"]

    if(objObtido == 0):
        return acoes[5]
    elif (estado == 2):
        return acoes[4]

    #Verifica qual é o próximo passo
    proximaPosicao = posicaoMaisProximaSujeira(x,y, sujeira, espaco)

    return acoes[proximaPosicao[2]]

def checkObj(espaco):
    for lista in espaco:
        for elemento in lista:
            if(elemento == 2):
                return 1
    return 0

def geraAmbiente():
    pass

#Pergunta
agente  = input("Escolha um agente: Agente Reativo Simples (1) ou Agente Baseado em Objetivo(2)")

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

pontos = 0
sujeira = 0

# Execução do ambiente
while True:

    #Verifica qual agente utilizar
    if(agente == "1"):
        acao = agenteReativoSimples(posxy[0], posxy[1],espaco[posxy[1]][posxy[0]])
    elif(agente == "2"):

        #Verifica se ainda tem sujeira
        check = checkObj(espaco)

        #Busca sujeira mais próxima da posição atual
        if(sujeira == 0):
            sujeira = sujeiraMaisProxima(posxy[0], posxy[1])

        percepcao = espaco[posxy[1]][posxy[0]]
        acao = agenteObjetivo(posxy[0], posxy[1], percepcao, check, espaco, sujeira)


        if(acao != "NoOp"):
            pontos += 1
            print(f"Estado da percepcao: {percepcao} Ação escolhida: {acao}")
        if(acao == "aspirar"):
            sujeira = 0


    #Verifica as ações
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
    elif(acao == "NoOp"):
        print(f"Pontos: {pontos}")
        break
    exibir(espaco)
