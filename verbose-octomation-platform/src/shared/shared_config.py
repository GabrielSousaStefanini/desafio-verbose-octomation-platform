# src/shared/shared_config.py
import os
import sys

# garante que src esteja no sys.path mesmo quando executado diretamente
CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

from system.config.config_file import DIRETORIO_RAIZ as DIRETORIO_RPA
from system.utils.logger_utils import (
    criar_estrutura_log,
    localizar_data_hora,
    registar_log,
    registar_log_decorator,
)
from system.utils.string_utils import (
    gerar_contador_arquivo,
    identificar_contador_arquivo,
    identificar_prefixo_arquivo,
    identificar_sufixo_arquivo,
)

DIRETORIO_RPA = DIRETORIO_RPA / 'rpa'
