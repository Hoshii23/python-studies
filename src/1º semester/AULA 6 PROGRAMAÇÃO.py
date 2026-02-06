import math

print("esse programa caucula a area de um triangulo ABC qualquer com apenas seus lados")
print("insira seus lados")
A = float(input())
B = float(input())
C = float(input())

p=(A+B+C)/2
x = (p*(p-A)*(p-B)*(p-C))
area = math.sqrt(x)
print("a area do triangulo é", area)