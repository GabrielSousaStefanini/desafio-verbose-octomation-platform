# pip install beautifulsoup4
from bs4 import BeautifulSoup

diretorio_raiz = __file__.replace(__file__.rpartition('\\')[-1], '')

arquivo_html = '\\'.join(
    (
        diretorio_raiz,
        'data',
        'relatorio.html',
    )
)


with open(arquivo_html, 'r', encoding='utf-8') as f:
    conteudo = f.read()

soup = BeautifulSoup(conteudo, 'html.parser')

links = soup.find_all('a')

[print(link.get('href')) for link in links]
