"""file = open("Amostras.csv", "r")
linhas = file.readlines()
for linha in linhas:
    print(linha.strip())
file.close()"""
"""--> str(i) significa: o valor em i da string"""
file = open("teste1.txt", "xt")
for i in range(3):
    file.write("Linha " + str(i) + "\n")
file.close()