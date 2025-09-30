import os.path
import sys

CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from datetime import datetime
from json import load
from pathlib import Path

from shared.shared_config import (
    DIRETORIO_RPA,
    criar_estrutura_log,
    gerar_contador_arquivo,
    identificar_contador_arquivo,
    identificar_prefixo_arquivo,
    identificar_sufixo_arquivo,
    localizar_data_hora,
    registar_log,
    registar_log_decorator,
)

NOME_AUTOMACAO = os.path.basename(__file__).removesuffix('.py')
DIRETORIO_PROJETO = DIRETORIO_RPA / NOME_AUTOMACAO
DIRETORIO_CONFIG = DIRETORIO_PROJETO / 'config'
ARQUIVO_CONFIG_RENAME_RULES = DIRETORIO_CONFIG / 'rename_rules.json'
PREFIXO_DUPLICADO = 'dup'
SUFIXO_DUPLICADO = 'dup'

DATA_HORA_EXECUCAO = localizar_data_hora(
    datetime=datetime.now(),
    cultura='pt_BR',
)
DATA_HORA_LOG = (
    DATA_HORA_EXECUCAO.rpartition(':')[0]
    .replace('/', '_')
    .replace(':', '')
    .replace(' ', '-')
)
NOME_ARQUIVO_LOG_PROJETO = f'{NOME_AUTOMACAO}-{DATA_HORA_LOG}.log'

DATA_ATUAL = DATA_HORA_EXECUCAO.split(' ')[0]
DATA_ATUAL_INVERTIDA = '/'.join(DATA_ATUAL.split('/')[::-1])
DIRETORIO_LOG = DIRETORIO_PROJETO / 'logs' / DATA_ATUAL_INVERTIDA
ARQUIVO_LOG_PROJETO = DIRETORIO_LOG / NOME_ARQUIVO_LOG_PROJETO

caminho_criado = criar_estrutura_log(
    data_hora=datetime.now(),
    cultura='pt_BR',
    diretorio_base=DIRETORIO_PROJETO,
)

registar_log(
    log_level='DEBUG',
    mensagem=f'Iniciando a automação {NOME_AUTOMACAO}',
    cultura='pt_BR.UTF-8',
    nome_handler='root',
    arquivo_log=ARQUIVO_LOG_PROJETO,
)


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
                    registar_log(
                    log_level='Debug',
                    mensagem=f'Link encontrando. Quantidade Atual: {quantidadeLinks}',
                    cultura='pt_BR.UTF-8',
                    nome_handler='root',
                    arquivo_log=ARQUIVO_LOG_PROJETO,
                    )
                   
                    if(os.path.isfile(caminho_arquivo_saida)):
                        with open(caminho_arquivo_saida, "r", encoding="utf-8") as instancia_arquivo_saida:
                            arquivo_de_saida = instancia_arquivo_saida.read()
                            if tag_a not in arquivo_de_saida:
                                        links.add(tag_a)
                                        registar_log(
                                        log_level='Debug',
                                        mensagem=f'Colocando link Único',
                                        cultura='pt_BR.UTF-8',
                                        nome_handler='root',
                                        arquivo_log=ARQUIVO_LOG_PROJETO,
                                        )
                    else: links.add(tag_a)
                    conteudo = conteudo[fim:]  

            iteracaoArquivo = 'a' if os.path.isfile(caminho_arquivo_saida) else 'w'
            with open(caminho_arquivo_saida,iteracaoArquivo, encoding="utf-8") as file:
                file.write("\n".join(links))

            return (f'Quantidade de Links no arquivo: {quantidadeLinks}',
                    f'Quantidade de Links Únicos: {len(links)}',
                    links)
        else:
            registar_log(
            log_level='ERROR',
            mensagem=f'Tipo de Arquivo inválido',
            cultura='pt_BR.UTF-8',
            nome_handler='root',
            arquivo_log=ARQUIVO_LOG_PROJETO,
            )
           
    else:
        registar_log(
        log_level='ERROR',
        mensagem=f'O arquivo informado pelo usuário não existe.',
        cultura='pt_BR.UTF-8',
        nome_handler='root',
        arquivo_log=ARQUIVO_LOG_PROJETO,
        )
       


print(extrair_links_html())

registar_log(
    log_level='DEBUG',
    mensagem=f'Finalizando a automação {NOME_AUTOMACAO}',
    cultura='pt_BR.UTF-8',
    nome_handler='root',
    arquivo_log=ARQUIVO_LOG_PROJETO,
    )    
