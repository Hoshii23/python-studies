print("vamos ver qual deve ser seu reajuste salarial?")
print("insira seu salario atual")
x=float(input())
if x < 500 :
    y = x * 1.15
    print("seu novo salario com um reajuste de 15% é",y)
elif x < 1000:
    u = x  * 1.1
    print("seu novo salario com um reajuste de 10% é",u) 
elif x>=1000: 
    b = x * 1.05 
    print("seu novo salario com um reajuste de 5% é",b)