from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())#prettify() é um método do BeautifulSoup que formata o HTML de uma maneira mais legível, com indentação e quebras de linha, facilitando a visualização da estrutura do documento.
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))
soup.find_all(string="James")


"""
========================================================
Downloading And Scraping The Contents Of A Web Page
========================================================
"""
url = "http://www.ibm.com"
data  = requests.get(url).text #O método requests.get() é usado para enviar uma solicitação HTTP GET para a URL especificada e obter a resposta do servidor. O atributo .text é usado para acessar o conteúdo da resposta como uma string de texto.
soup = BeautifulSoup(data, 'html.parser')
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
"""
=======================
Scrape all images Tags
=======================
"""
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))