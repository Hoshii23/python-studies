from bs4 import BeautifulSoup
import requests
import pandas as pd
try:
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
    tables =   pd.read_html(url)  # essa função "read_html" do pandas é capaz de ler tabelas diretamente de uma página web e retornar uma lista de DataFrames.
    df = tables[0]
    t = 1

    while t ==1 :
        print("voce deseja ecolher a cor pelo:\n1- nome da cor\n2- código hexadecimal\n3- código RGB")
        resposta1 = input()
        if(resposta1 =="nome da cor" or resposta1 == "1"):
            coluna = 2  # Color Name
            print(df[coluna])
            resposta2 = input("digite o nome da cor que deseja escolher\n")
            for i in range(len(df[coluna])):
                if resposta2 == df[coluna].iloc[i]:
                    print(df.iloc[i])
                    v = df.iloc[i].tolist()
                    print(v)
                    break
            else:
                print("Cor não encontrada. Tente novamente")
                
            t = 0
        elif(resposta1 =="código hexadecimal" or resposta1 == "2"):
            coluna = 3  # Hex Code
            print(df[coluna])
            resposta2 = input("digite o código hexadecimal da cor que deseja escolher\n")
            for i in range(len(df[coluna])):
                if resposta2 == df[coluna].iloc[i]:
                    print(df.iloc[i])
                    v = df.iloc[i].tolist()
                    print(v)
                    
                    break
            else:
                print("Cor não encontrada. Tente novamente")
            t = 0
        elif(resposta1 =="código RGB" or resposta1 == "3"):
            coluna = 4  # Decimal Code
            print(df[coluna])
            resposta2 = input("digite o código RGB que deseja escolher\n")
            for i in range(len(df[coluna])):
                if resposta2 == df[coluna].iloc[i]:
                    print(df.iloc[i])
                    v = df.iloc[i].tolist()
                    print(v)
                    break
            else:
                print("Cor não encontrada. Tente novamente")
            t = 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")