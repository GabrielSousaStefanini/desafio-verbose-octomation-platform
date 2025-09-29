import os
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

with open(ARQUIVO_CONFIG_RENAME_RULES, encoding='utf-8') as arquivo_JSON:
    arquivo_config_rename_rules_json = load(arquivo_JSON)

# MOCK
arquivo_config_rename_rules_json[
    'diretorioEntrada'
] = 'C:\\users\\aranseiki\\Downloads'
# FIM DO MOCK

diretorioEntrada = arquivo_config_rename_rules_json['diretorioEntrada']
lista_arquivos = [
    item for item in Path(diretorioEntrada).glob('**/*.*') if item.is_file
]

modo_ativo_renomeacao = arquivo_config_rename_rules_json['renomeacao'][
    'modoAtivo'
]
parametro_renomeacao = [
    parametro
    for parametro in arquivo_config_rename_rules_json['renomeacao'][
        'parametros'
    ]
    if parametro['nome'].upper() == modo_ativo_renomeacao.upper()
]

if not modo_ativo_renomeacao.upper() in [
    'PREFIXO',
    'SUFIXO',
    'NUMERACAOSEQUENCIAL',
]:
    raise ValueError(
        f'Modo de renomeação {modo_ativo_renomeacao} não implementado.'
    )

parametro_renomeacao = parametro_renomeacao[0]
prefixo = str(parametro_renomeacao['valor'])
sufixo = str(parametro_renomeacao['valor'])

for arquivo in lista_arquivos:
    nome_arquivo = arquivo.stem
    extensao_arquivo = arquivo.suffix
    novo_nome_arquivo = ''

    if modo_ativo_renomeacao.upper() == 'PREFIXO':
        prefixo_arquivo = identificar_prefixo_arquivo(
            nome_arquivo=nome_arquivo,
            separador='_',
        )

        if prefixo_arquivo == prefixo:
            prefixo = PREFIXO_DUPLICADO
        elif prefixo_arquivo == PREFIXO_DUPLICADO:
            prefixo = ''

        if not prefixo == '':
            prefixo = f'{prefixo}_'

        novo_nome_arquivo = f'{prefixo}{nome_arquivo}'
    elif modo_ativo_renomeacao.upper() == 'SUFIXO':
        sufixo_arquivo = identificar_sufixo_arquivo(
            nome_arquivo=nome_arquivo,
            separador='_',
        )

        if sufixo_arquivo == sufixo:
            sufixo = SUFIXO_DUPLICADO
        elif sufixo_arquivo == SUFIXO_DUPLICADO:
            sufixo = ''

        if not sufixo == '':
            sufixo = f'_{sufixo}'

        novo_nome_arquivo = f'{nome_arquivo}{sufixo}'
    elif modo_ativo_renomeacao.upper() == 'NUMERACAOSEQUENCIAL':
        contador = identificar_contador_arquivo(
            nome_arquivo=nome_arquivo,
            separador='_',
        )

        novo_contador = gerar_contador_arquivo(
            nome_arquivo=nome_arquivo,
            separador='_',
        )

        nome_arquivo = nome_arquivo.removesuffix(str(contador))
        nome_arquivo = nome_arquivo.removesuffix('_')

        contador = novo_contador
        novo_nome_arquivo = f'{nome_arquivo}_{str(contador)}'

    arquivo.rename(arquivo.parent / (novo_nome_arquivo + extensao_arquivo))

registar_log(
    log_level='DEBUG',
    mensagem=f'Finalizando a automação {NOME_AUTOMACAO}',
    cultura='pt_BR.UTF-8',
    nome_handler='root',
    arquivo_log=ARQUIVO_LOG_PROJETO,
)
