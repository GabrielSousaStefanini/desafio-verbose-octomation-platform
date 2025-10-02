from bs4 import BeautifulSoup
from pathlib import Path
import sys
from json import load

CAMINHO_SRC = Path(__file__).resolve().parents[2]
CAMINHO_SRC_STR = str(CAMINHO_SRC)

if CAMINHO_SRC_STR not in sys.path:
    sys.path.insert(0, CAMINHO_SRC_STR)

from datetime import datetime

from shared.shared_config import (
    DIRETORIO_RPA,
    criar_estrutura_log,
    localizar_data_hora,
    registar_log,
)

NOME_AUTOMACAO = Path(__file__).stem
DIRETORIO_PROJETO = DIRETORIO_RPA / NOME_AUTOMACAO

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

DATA_ATUAL = datetime.strptime(DATA_HORA_EXECUCAO, '%d/%m/%Y %H:%M:%S')
DATA_ATUAL_INVERTIDA = DATA_ATUAL.strftime('%Y/%m/%d')
DIRETORIO_LOG = DIRETORIO_PROJETO / 'logs' / DATA_ATUAL_INVERTIDA
ARQUIVO_LOG_PROJETO = DIRETORIO_LOG / NOME_ARQUIVO_LOG_PROJETO
DIRETORIO_CONFIG = DIRETORIO_PROJETO / 'config'
ARQUIVO_LOG_CONFIG = DIRETORIO_CONFIG / 'logging.ini'
ARQUIVO_CONFIG_RENAME_RULES = DIRETORIO_CONFIG / 'rename_rules.json'
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
    arquivo_config=ARQUIVO_LOG_CONFIG,
    arquivo_log=ARQUIVO_LOG_PROJETO,
)

with ARQUIVO_CONFIG_RENAME_RULES.open(encoding='utf-8') as arquivo_JSON:
    arquivo_config_rename_rules_json = load(arquivo_JSON)

def ler_arquivo(caminho_arquivo):
     caminho_arquivo = Path(caminho_arquivo)
     return caminho_arquivo.read_text(encoding="utf-8")
def escrever_arquivo(caminho_arquivo, links):
    caminho_arquivo = Path(caminho_arquivo)
    modo = 'a' if caminho_arquivo.is_file() else 'w'

    with caminho_arquivo.open(modo, encoding="utf-8") as file:
        file.write("\n".join(links))

def extrair_links_html():
    caminho_arquivo_entrada = Path(arquivo_config_rename_rules_json['arquivoEntrada'])
    caminho_arquivo_saida = Path(arquivo_config_rename_rules_json['arquivoSaida'])
    if caminho_arquivo_entrada.is_file():
        if caminho_arquivo_entrada.suffix.lower() in (".html", ".htm"):
            conteudo = ler_arquivo(caminho_arquivo_entrada)
            soup = BeautifulSoup(conteudo, 'html.parser')
            linksExtraidos = soup.find_all('a')
            links = set()
            quantidadeLinks = 0
            registar_log(
                log_level='DEBUG',
                mensagem=f'Iniciando extração dos links.',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
                )

            
            quantidadeLinks+=1
                
            listaLinks = [linkAtual.get('href') for linkAtual in linksExtraidos]
            
            for tag_a in listaLinks:
                # Verifica se o arquivo de saída existe
                if caminho_arquivo_saida.is_file():
                    arquivo_de_saida = ler_arquivo(caminho_arquivo_saida)
                    # Verifica se tag_a não está no conteúdo do arquivo
                    if tag_a not in arquivo_de_saida:
                        links.add(tag_a)                  
                else:
                    # Se o arquivo não existe, adiciona o link
                    links.add(tag_a)

                # Registra log sobre o link encontrado
                registar_log(
                    log_level='DEBUG',
                    mensagem=f'Link Encontrado: {tag_a}',
                    cultura='pt_BR.UTF-8',
                    nome_handler='root',
                    arquivo_config=ARQUIVO_LOG_CONFIG,
                    arquivo_log=ARQUIVO_LOG_PROJETO,
                )
            registar_log(
                log_level='DEBUG',
                mensagem=f'Total de Links encontrandos: {quantidadeLinks}, Links Adicionados: {len(links)}',
                cultura='pt_BR.UTF-8',
                nome_handler='root',
                arquivo_config=ARQUIVO_LOG_CONFIG,
                arquivo_log=ARQUIVO_LOG_PROJETO,
                ) 

            escrever_arquivo(caminho_arquivo_saida, links)

            return (f'Quantidade de Links no arquivo: {quantidadeLinks}',
                    f'Quantidade de Links Únicos: {len(links)}')
        else:
            registar_log(
            log_level='ERROR',
            mensagem=f'Tipo de Arquivo inválido',
            cultura='pt_BR.UTF-8',
            nome_handler='root',
            arquivo_config=ARQUIVO_LOG_CONFIG,
            arquivo_log=ARQUIVO_LOG_PROJETO,
            )
           
    else:
        registar_log(
        log_level='ERROR',
        mensagem=f'O arquivo informado pelo usuário não existe.',
        cultura='pt_BR.UTF-8',
        nome_handler='root',
        arquivo_config=ARQUIVO_LOG_CONFIG,
        arquivo_log=ARQUIVO_LOG_PROJETO,
        )
        return
       


print(extrair_links_html())

registar_log(
    log_level='DEBUG',
    mensagem=f'Finalizando a automação {NOME_AUTOMACAO}',
    cultura='pt_BR.UTF-8',
    nome_handler='root',
    arquivo_config=ARQUIVO_LOG_CONFIG,
    arquivo_log=ARQUIVO_LOG_PROJETO,
    )    
