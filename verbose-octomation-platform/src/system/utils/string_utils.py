def gerar_contador_arquivo(
    nome_arquivo: str,
    separador: str = '_',
    contador: int = 1,
    acrescimo: int = 1,
) -> int:
    contador_atual = identificar_contador_arquivo(
        nome_arquivo=nome_arquivo,
        separador=separador,
    )

    if str(contador_atual).isdigit():
        contador = int(contador_atual) + acrescimo

    return contador


def identificar_contador_arquivo(nome_arquivo: str, separador: str) -> int:
    contador = 0
    nome_arquivo_particionado = nome_arquivo.rpartition(separador)
    contador_atual = nome_arquivo_particionado[-1]

    if str(contador_atual).isdigit():
        contador = int(contador_atual)

    return contador


def identificar_prefixo_arquivo(nome_arquivo: str, separador: str) -> int:
    nome_arquivo_particionado = nome_arquivo.partition(separador)
    prefixo_atual = nome_arquivo_particionado[0]

    return prefixo_atual


def identificar_sufixo_arquivo(nome_arquivo: str, separador: str) -> int:
    nome_arquivo_particionado = nome_arquivo.rpartition(separador)
    sufixo_atual = nome_arquivo_particionado[-1]

    return sufixo_atual
