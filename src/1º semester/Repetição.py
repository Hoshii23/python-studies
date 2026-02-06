import random
v1=[0]*80
for i in range(80):
    v1[i]=random.randint(0,80)
print("Vetor original:")
print(v1)
for y in range(80):
    for x in range(80):
        if v1[y]<v1[x]:
            v1[y],v1[x]=v1[x],v1[y]
print("Vetor ordenado:")
print(v1)
repetição=0
for i in range(80):
    for j in range(i+1,80):
        if v1[i]==v1[j]:
            repetição+=1
print("\nRepetição:",repetição)