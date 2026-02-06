'''t=0
while t==0:
    usuario=input("Usuário:")
    senha=input("senha:")
    confirmação=input("confirme sua senha:")
    if usuario==senha:
        print("erro")
    elif senha!=confirmação:
        print("erro")
    else:
        print("entrou")
        t=1
'''

'''
print("este progrma recebe 2 números inteiros e imprime os números inteiros que estão no intervalo compreendido por eles do maior para o menor")
n1=int(input("insira n1"))
n2=int(input("insiran2"))
if n1==n2:
    print ("esses numeros são iguais")
elif n1==n2+1 or n2==n1+1:
    print("não possui número inteiro dentro desse intervalo")
elif n1>n2:
    for i in range(n2+1,n1,1):
        print(i)
elif n2>n1:
    for i in range(n1+1,n2,1):
        print(i)
'''
'''
print("esse algoritimo exibe todos quadrado menores que n,")
n=int(input("insira n"))
for i in range (0,n,1):
    if i**2<n:
        print(i**2)
        '''