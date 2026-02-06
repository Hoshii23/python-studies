def compararMatriz(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if m1[i][j] != m2[i][j]:
                return False
    return True   
