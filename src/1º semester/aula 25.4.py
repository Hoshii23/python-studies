'''exercicio 4 lista 4 
print ("a potencia de 2 de 0 a 1000 sao:")
for y in range (0,1001,1):
 x=2**y
 print(2,"^",y,"=",x)
 '''
''' exercicio 5 lista4
x=0
for y in range (0,1001,2):
    x=x+y
print (x)

'''
'''
print("insira um numero para verifica-lo se é primo")
n = int(input())   
for y in range (1,n,1):
    if n / y == 1:
        t=1
    else:
        t=0
if t==1:
    print("é primo")
elif t==0:
    print("não é primo")
'''

'''
a=[4,2,9,1,5,3,8,6,7]
x=0
t=0
for y in range(0,len(a),1):
    if a[y]%2==0:
        x=x+a[y]
        t=t+1
print(x/t)
'''
