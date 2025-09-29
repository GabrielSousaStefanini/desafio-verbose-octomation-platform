import os.path


def extrair_links_html(caminho_arquivo_entrada, caminho_arquivo_saida):
    if (os.path.isfile(caminho_arquivo_entrada)):
        if(caminho_arquivo_entrada.endswith((".html", ".htm"))):
            with open(caminho_arquivo_entrada, "r", encoding="utf-8") as file:
                conteudo = file.read()
                links = set()
                inicio_tag = 'href="'
                fim_tag = '"'
                quantidadeLinks = 0
                while inicio_tag in conteudo:

                    inicio = conteudo.index(inicio_tag)+len(inicio_tag)
                    fim = conteudo.index(fim_tag, inicio+len(inicio_tag))


                    tag_a = conteudo[inicio:fim]
                    quantidadeLinks+=1
                    links.add(tag_a)
                    conteudo = conteudo[fim:]
                return (f'Quantidade de Links no arquivo: {quantidadeLinks}',
                        f'Quantidade de Links Únicos: {len(links)}',
                        links)
    else:
        return f'O arquivo informado pelo usuário não existe.'




caminho_entrada = "C:\\Users\\gssousa6\\OneDrive - Stefanini\\Área de Trabalho\\python\\desafio-verbose-octomation-platform\\verbose-octomation-platform\\src\\RPA\\extrair_links_html\\Arquivos\\index.html"
caminho_saida = "C:\\Users\\gssousa6\\OneDrive - Stefanini\\Área de Trabalho\\python\\desafio-verbose-octomation-platform\\verbose-octomation-platform\\src\\RPA\\extrair_links_html\\saida.txt"

print(extrair_links_html(caminho_entrada, caminho_saida))