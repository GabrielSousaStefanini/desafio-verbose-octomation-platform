import os
import sys

# garante que src esteja no sys.path mesmo quando executado diretamente
CAMINHO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if CAMINHO_SRC not in sys.path:
    sys.path.insert(0, CAMINHO_SRC)

import logging
import logging.config
from datetime import datetime
from functools import wraps
from pathlib import Path

from system.config.config_file import DIRETORIO_RAIZ
from system.utils.toolkit import localizar_data_hora


def alterar_caminho_arquivo_log(logger: logging.Logger, novo_arquivo):
    for handler_index, handler in enumerate(logger.handlers):
        if isinstance(handler, logging.FileHandler):
            # cria novo handler com mesmo modo, encoding e nível
            novo_handler = logging.FileHandler(
                novo_arquivo,
                mode=handler.mode,
                encoding=handler.encoding,
                delay=handler.delay,
            )
            # mantém nível, filtros e formatador
            novo_handler.setLevel(handler.level)
            novo_handler.setFormatter(handler.formatter)
            for filtro in handler.filters:
                novo_handler.addFilter(filtro)

            # substitui o antigo pelo novo
            logger.handlers[handler_index] = novo_handler

 
def definir_log_config(
    log_level: str,
    cultura: str,
    nome_handler: str,
    arquivo_config: str,
    arquivo_log: str | Path,
):
    if not isinstance(nome_handler, str):
        raise ValueError('Você precisa definir um Handler para o log.')

    LEVELNAMESMAPPING = list(logging.getLevelNamesMapping().keys())
    if not log_level in LEVELNAMESMAPPING:
        raise ValueError(
            'Você precisa definir um '
            f'dos seguintes níveis: {LEVELNAMESMAPPING}.'
        )

    logging.config.fileConfig(arquivo_config)
    logger = logging.getLogger(nome_handler)
    if log_level.upper() == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)
        logging_with_level = logger.critical
    elif log_level.upper() == 'FATAL':
        logger.setLevel(logging.FATAL)
        logging_with_level = logger.fatal
    elif log_level.upper() == 'ERROR':
        logger.setLevel(logging.ERROR)
        logging_with_level = logger.error
    elif (log_level.upper() == 'WARN') or (log_level.upper() == 'WARNING'):
        logger.setLevel(logging.WARNING)
        logging_with_level = logger.warning
    elif log_level.upper() == 'INFO':
        logger.setLevel(logging.INFO)
        logging_with_level = logger.info
    elif log_level.upper() == 'DEBUG':
        logger.setLevel(logging.DEBUG)
        logging_with_level = logger.debug
    elif log_level.upper() == 'NOTSET':
        logger.setLevel(logging.NOTSET)

        def logging_with_level(msg, **kwargs):
            logger.log(logging.NOTSET, msg, **kwargs)

    else:
        raise ValueError('Nìvel não mapeado.')

    if arquivo_log is not None:
        validacao_alterar_caminho = verificar_alteracao_caminho_log(
            caminho_arquivo_config=arquivo_config
        )
        if validacao_alterar_caminho:
            alterar_caminho_arquivo_log(logger, arquivo_log)

    data_hora_atual = localizar_data_hora(
        datetime=datetime.now(), cultura=cultura
    )
    extra_log_config = {'data_hora_atual': data_hora_atual}

    return logging_with_level, extra_log_config


def criar_estrutura_log(
    data_hora: datetime,
    cultura: str,
    diretorio_base: str,
    inverter_data: bool = True,
):
    try:
        from pathlib import Path

        data_atual = localizar_data_hora(data_hora, cultura).split(' ')[0]

        if inverter_data:
            data_atual = '/'.join(data_atual.split('/')[::-1])

        caminho_criado = Path(diretorio_base / 'logs' / data_atual).mkdir(
            parents=True, exist_ok=True
        )

        caminho_criado = True
    except Exception as erro:
        caminho_criado = False

    return caminho_criado


def registar_log(
    log_level: str,
    mensagem: str,
    cultura: str,
    nome_handler: str,
    arquivo_config: str = None,
    arquivo_log: str | Path = None,
):
    try:
        erro_logging = None
        logging_with_level = None
        extra = {}

        if not arquivo_config:
            arquivo_config = f'{DIRETORIO_RAIZ}/system/config/logging.ini'

        logging_with_level, extra = definir_log_config(
            log_level,
            cultura,
            nome_handler,
            arquivo_config,
            arquivo_log=arquivo_log,
        )
        logging_with_level(msg=mensagem, extra=extra)
    except Exception as erro:
        erro_logging = erro
        if (not logging_with_level) or (not extra):
            raise LookupError(
                'Um erro aconteceu na configuração do log'
            ) from erro_logging

        logging_with_level(msg=str(erro_logging), extra=extra)
    finally:
        if erro_logging is not None:
            raise erro_logging


def registar_log_decorator(
    log_level: str,
    mensagem: str,
    cultura: str,
    nome_handler: str,
    arquivo_config: str = f'{DIRETORIO_RAIZ}/logging.ini',
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            registar_log(
                log_level, mensagem, cultura, nome_handler, arquivo_config
            )
            resultado = func(*args, **kwargs)

            return resultado

        return wrapper

    return decorator


def verificar_alteracao_caminho_log(
    caminho_arquivo_config: str | Path, encoding: str = 'utf-8'
) -> bool:
    import ast
    from configparser import ConfigParser

    retorno_identificador = False
    Configurador = ConfigParser()

    with open(caminho_arquivo_config, encoding=encoding) as arquivo_config:
        Configurador.read_file(arquivo_config)

    nomes_handler = (
        Configurador['logger_root']['handlers'].strip('\'"').split(',')
    )
    for nome_handler in nomes_handler:
        try:
            nome_handler_session = f'handler_{nome_handler.strip()}'
            handler_args = Configurador[nome_handler_session]['args']
            if not len(handler_args.split(',')) == 3:
                continue

            handler_fileHandler_args = ast.literal_eval(handler_args)

            if handler_fileHandler_args[0].upper() == 'CAMINHO_LOG':
                retorno_identificador = True
        except Exception as erro:
            raise erro

    return retorno_identificador
