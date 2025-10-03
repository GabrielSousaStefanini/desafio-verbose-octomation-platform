from bs4 import BeautifulSoup
from pathlib import Path
from utils.arquivoUtils import ler_arquivo, escrever_arquivo

def extrair_links_html(NOME_AUTOMACAO, ARQUIVO_LOG_CONFIG, ARQUIVO_LOG_PROJETO, registar_log, arquivoEntrada, arquivoSaida):
    registar_log(
        log_level='INFO',
        mensagem=f'Iniciando a automação {NOME_AUTOMACAO}',
        cultura='pt_BR.UTF-8',
        nome_handler='root',
        arquivo_config=ARQUIVO_LOG_CONFIG,
        arquivo_log=ARQUIVO_LOG_PROJETO,
    )
    
    caminho_arquivo_entrada = Path(arquivoEntrada)
    caminho_arquivo_saida = Path(arquivoSaida)
    
    if caminho_arquivo_entrada.is_file():
        if caminho_arquivo_entrada.suffix.lower() in (".html", ".htm"):
            links = set()
            registar_log(
                log_level='INFO',
                mensagem='Iniciando extração dos links.',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
            )
            conteudo = ler_arquivo(caminho_arquivo_entrada)
            soup = BeautifulSoup(conteudo, 'html.parser')
            linksExtraidos = soup.find_all('a')
            listaLinks = [linkAtual.get('href') for linkAtual in linksExtraidos]
            quantidadeLinks = len(listaLinks)
            arquivoSaidaExiste = caminho_arquivo_saida.is_file()
            arquivo_de_saida = set(ler_arquivo(caminho_arquivo_saida).splitlines()) if arquivoSaidaExiste else set()
        
            for tag_a in listaLinks:
                if arquivoSaidaExiste:
                    if tag_a not in arquivo_de_saida:
                        links.add(tag_a)                  
                else:
                    links.add(tag_a)
            
            registar_log(
                log_level='DEBUG',
                mensagem=f'Total de Links encontrados: {quantidadeLinks}, Links Adicionados: {len(links)}',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
            )
            registar_log(
                log_level='INFO',
                mensagem='Finalizando extração dos links.',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
            ) 

            escrever_arquivo(caminho_arquivo_saida, links)

            registar_log(
                log_level='INFO',
                mensagem=f'Finalizando a automação {NOME_AUTOMACAO}',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
            )    
            return (f'Quantidade de Links no arquivo: {quantidadeLinks}',
                    f'Quantidade de Links Únicos: {len(links)}')
        else:
            registar_log(
                log_level='ERROR',
                mensagem='Tipo de Arquivo inválido',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
            )        
    else:
        registar_log(
            log_level='ERROR',
            mensagem='O arquivo informado pelo usuário não existe.',
            cultura='pt_BR.UTF-8',
            nome_handler='root',
            arquivo_config=ARQUIVO_LOG_CONFIG,
            arquivo_log=ARQUIVO_LOG_PROJETO,
        )
    
    # Mover a mensagem de finalização para fora de todas as condições
    registar_log(
        log_level='INFO',
        mensagem=f'Finalizando a automação {NOME_AUTOMACAO}',
        cultura='pt_BR.UTF-8',
        nome_handler='root',
        arquivo_config=ARQUIVO_LOG_CONFIG,
        arquivo_log=ARQUIVO_LOG_PROJETO,
    )    
    return