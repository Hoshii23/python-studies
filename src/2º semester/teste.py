from compararMatriz import *
def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print() 
def criarMatriz(a,b):
    m= [[0 for i in range(a)] for j in range(b)]
    return m
def sortearMatriz(x,y,matriz):
    import random
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(x,y)
    return matriz
def matrizTransposta(matriz):
    mt = [[0 for i in range(len(matriz))] for j in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mt[j][i] = matriz[i][j]
    return mt
def preecnherMatriz(matriz,w):
    import random
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = w
if __name__ == "__main__":
    a=int(input("Digite o número de linhas: "))
    b=int(input("Digite o número de colunas: "))
    x=int(input("Digite o valor mínimo: "))
    y=int(input("Digite o valor máximo: "))
    m1=criarMatriz(a,b)
    printMatriz(m1)
    print()
    sortearMatriz(x,y,m1)
    printMatriz(m1)
    print()
    mt=matrizTransposta(m1)
    printMatriz(mt)
    print(compararMatriz(m1,mt))