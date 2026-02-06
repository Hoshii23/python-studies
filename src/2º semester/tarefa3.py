arquivo = 'Amostras.csv'
contador=0
somaValores=0.0
max=0.0
min=999999999.9
delimitador= ';'

def trocarTexto(texto):
    texto = texto.replace(",", ".")
    return texto

with open(arquivo, encoding='utf-8') as arquivo:
	next(arquivo) 
	for linha in arquivo:
		linha = linha.strip().split(delimitador)
		if linha[2] != " " :
			x = trocarTexto(linha[2])
			valor = float(x)
			contador += 1
			somaValores += valor
			if max < valor:
				max = valor
			if valor < min:
				min = valor
arquivo.close()
media = somaValores / contador
media = round(media, 2)
print(f'Média: {media}\nMáximo: {max}\nMínimo: {min}\nTotal de amostras: {contador}')
