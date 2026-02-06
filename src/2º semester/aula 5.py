def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:   
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
    n = int(input("Digite um número inteiro não negativo: "))
    if n < 0:
        print("Por favor, digite um número inteiro não negativo.")
    else:
        print(f"O {n}º número da sequência de Fibonacci é: {fibonacci(n)}")