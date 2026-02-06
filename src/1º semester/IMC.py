import math
print("este progrma cálcula seu indice de massa corpórea")
print("insira seus dados: nome, peso(em Kg) e altura(em metros)")
nome=input()
p = float(input())
altura=float(input())

IMC = p/(math.pow(altura,2))
print("Bom dia",nome,"seu índice de Massa Corpórea é",IMC)