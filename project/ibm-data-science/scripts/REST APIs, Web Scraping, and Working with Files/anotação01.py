"""
Web scraping, também conhecido como coleta de dados da web ou extração de dados da web,
 é uma técnica usada para extrair grandes quantidades de dados de websites. 
Os dados em websites são não estruturados, e o web scraping nos permite convertê-los em uma forma estruturada.
"""

"""
Bibliotecas populares para web scraping em Python incluem:
- BeautifulSoup: Uma biblioteca para extrair dados de arquivos HTML e XML.

from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

- Scrapy: Um framework de web scraping que permite criar spiders para extrair dados de websites.

import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}

- Selenium: Selenium é uma ferramenta usada para controlar 
    navegadores da web através de programas e automatizar tarefas do navegador.

import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}    
"""
"""
========================
WEB SCRAPING COM PANDAS
========================
"""

import pandas as pd
URL = 'http://br.tradingview.com/markets/world-stocks/worlds-largest-banks/'
tables = pd.read_html(URL)#essa função "read_html" do pandas é capaz de ler tabelas diretamente de uma página web e retornar uma lista de DataFrames.
df = tables[0]
df_10 = df.head(10) #para pegar as 10 primeiras linhas da tabela
df_10t = df.tail(10) #para pegar as 10 últimas linhas da tabela
print(df)
print(df_10)
