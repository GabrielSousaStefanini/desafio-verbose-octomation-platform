import os.path

def extrair_links_html():
    caminho_arquivo_entrada = input("Informe o caminho do arquivo de entrada")
    caminho_arquivo_saida = input("Informe o caminho do arquivo de Saida")
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
                    
                    if(os.path.isfile(caminho_arquivo_saida)):
                        with open(caminho_arquivo_saida, "r", encoding="utf-8") as instancia_arquivo_saida:
                            arquivo_de_saida = instancia_arquivo_saida.read()
                            if tag_a not in arquivo_de_saida:
                                        links.add(tag_a)
                    else: links.add(tag_a)
                    conteudo = conteudo[fim:]   

            iteracaoArquivo = 'a' if os.path.isfile(caminho_arquivo_saida) else 'w'
            with open(caminho_arquivo_saida,iteracaoArquivo, encoding="utf-8") as file:
                file.write("\n".join(links))

            return (f'Quantidade de Links no arquivo: {quantidadeLinks}',
                    f'Quantidade de Links Únicos: {len(links)}',
                    links)
        else:
            return f'Tipo de Arquivo inválido'
    else:
        return f'O arquivo informado pelo usuário não existe.'






print(extrair_links_html())