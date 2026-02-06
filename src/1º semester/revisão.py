import random

# Criação das matrizes
m1 = [[0 for i in range(4)] for j in range(4)]
m2 = [[0 for i in range(3)] for j in range(3)]

# Preenchendo as matrizes com valores aleatórios
for i in range(len(m1)):
    for j in range(len(m1[i])):
        m1[i][j] = random.randint(0, 24)
for i in range(len(m2)):
    for j in range(len(m2[i])):
        m2[i][j] = random.randint(0, 24)

# Imprimindo as matrizes
print("Matriz m1:")
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(m1[i][j], end=" ")
    print()
print() 
print("Matriz m2:")
for i in range(len(m2)):
    for j in range(len(m2[i])):
        print(m2[i][j], end=" ")
    print()
v = [0] * ((len(m1) * len(m1[0])) + (len(m2) * len(m2[0])))
idx = 0
for i in range(len(m1)):
    for j in range(len(m1[i])):
        v[idx] = m1[i][j]
        idx += 1
for i in range(len(m2)):
    for j in range(len(m2[i])):
        v[idx] = m2[i][j]
        idx += 1
print()
print("Vetor antes da ordenação:")
for i in range(len(v)):
    print(v[i], end=" ")
print()

for x in range(len(v)):
    for y in range(x + 1, len(v)):
        if v[x] > v[y]:
            aux = v[x]
            v[x] = v[y]
            v[y] = aux

print("Vetor ordenado:")
for i in range(len(v)):
    print(v[i], end=" ")
print()

# Preenchendo a matriz m 5x5 com os valores ordenados de v
m = [[0 for i in range(5)] for j in range(5)]
idx = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if idx < len(v):
            m[i][j] = v[idx]
            idx += 1
        else:
            m[i][j] = 0  # Preenche o resto com zero, se sobrar espaço

print("\nMatriz m preenchida com o vetor ordenado:")
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end="    ")
    print()

