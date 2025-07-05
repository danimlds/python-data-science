from bs4 import BeautifulSoup
import requests

url = 'https://danimlds.github.io/python-data-science/'
pagina = requests.get(url)
html = pagina.text


#print(html)

soup = BeautifulSoup(html,'html.parser')
produtos = []
for item in soup.find_all('div', class_='produto'):
    nome = item.find('h2', class_='nome').text
    preco = item.find('span', class_='preco').text
    produtos.append({
    'nome':nome,
    'preco':preco,
    })
    print('PRODUTOS ENCONTRADOS')
    for item in produtos:
        print(f'{item['nome']} - {item['preco']}')
    print('Valores Encontrados')
    with open('produtos.txt', 'w') as arquivo:
        for produto in produtos:
            arquivo.write(f'{produto['nome']} - {produto['preco']}')
    print(produtos)