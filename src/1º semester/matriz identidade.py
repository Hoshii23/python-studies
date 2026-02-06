m = [[0 for i in range(5)] for j in range(5)]
for i in range(0,len(m)-1,1):
    for j in range(0,len(m[i])-1,1):
        if i==j:
            m[i][j]=1
for i in range(0,len(m),1):
    for j in range(0,len(m[i]),1):
        print(m[i][j], end="  ")
    print()