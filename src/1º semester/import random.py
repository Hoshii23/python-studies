import random
#nesse código, vamos criar uma matriz de i linhas e j colunas, preenchê-la com números aleatórios de 0 a 100,
#transformar essa matriz em um vetor, ordenar esse vetor e jogar os valores de volta para a matriz. 

#criação de uma matriz de i linhas e j colunas preenchida com números aleatórios de 0 a 100
m = [[0 for i in range(4)] for j in range(5)]
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = random.randint(1, 100)
#impressão da matriz gerada
print("a matriz gerada é:")
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
    print()
#criação de um vetor com o tamanho da matriz
v = [0] * (len(m) * len(m[0]))
#jogando os valores da matriz para o vetor
k = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        v[k] = m[i][j]
        k += 1
#impressão do vetor com os valkores da matriz
print("o vetor gerado é:")
for i in range(len(v)):
    print(v[i], end=" ")
print()
#ordenando o vetor em ordem crescente
aux= 0
for x in range(len(v)):
    for y in range(x + 1, len(v)):
        if v[x]>v[y]:
            aux = v[x]
            v[x] = v[y]
            v[y] = aux
"""funciona como um triangulo, primeiro armazenamos o valor do primeiro elemento do vetor na variável aux(v[x]=aux),
    depois comparamos o primeiro elemento com o segundo, se o primeiro for maior que o segundo, trocamos os valores(v[x]=v[y]),
    pro fim com o valor armazenado na variável aux, colocamos o valor do segundo elemento no primeiro(v[y]=aux)
"""   
#impressão do vetor ordenado
print("o vetor ordenado é:")
for k in range(len(v)):
    print(v[k], end=" ")
print()
#jogando os valores do vetor de volta para a matriz
k=0
for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        m[i][j] = v[k]
        k=k+1
#impressão da matriz ordenada
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end="  ")
    print()