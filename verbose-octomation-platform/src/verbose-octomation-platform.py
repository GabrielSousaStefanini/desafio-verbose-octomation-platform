import datetime
import runpy
import sched
import threading
import time
from pathlib import Path
from pprint import pprint

import docker

from system.config.config_file import DIRETORIO_RAIZ

automacoes = {
    'soma': Path('docs/exemplos/soma.py'),
    'renomear_arquivos_em_lote': Path(
        f'{DIRETORIO_RAIZ}/RPA/renomear_arquivos_em_lote/renomear_arquivos_em_lote.py'
    ),
    # Adicione outras automações aqui
}

instancias_ativas = {}


def cls():
    import os

    os.system('cls')


def executar_automacao(nome):
    caminho = automacoes.get(nome)
    if not caminho:
        print(f"Automação '{nome}' não encontrada.")
        return
    print(f'Executando: {nome}')
    resultado_modulo = runpy.run_path(str(caminho))
    return resultado_modulo


def agendar_automacao(nome, delay_segundos):
    thread = threading.Timer(delay_segundos, executar_automacao, args=(nome,))
    instancias_ativas[nome] = thread


def iniciar_automacao(thread):
    thread.start()


def listar_automacoes():
    print('Automações disponíveis:')
    for nome in automacoes:
        print(f'- {nome}')


def executar_automacao_docker(nome):
    client = docker.from_env()
    image = f'meu_repo/{nome}:latest'
    try:
        container = client.containers.run(image, detach=True)
        print(f'Container {container.short_id} iniciado para {nome}')
    except Exception as e:
        print(f'Erro ao iniciar container: {e}')


def scheduler_run(agendador, blocking=False):
    tempo_para_proxima_exeucao = agendador.run(blocking=blocking) or 0.0
    return tempo_para_proxima_exeucao


if __name__ == '__main__':
    """listar_automacoes()
    agendar_automacao('soma', 5)  # Exemplo: agenda para daqui 5 segundos
    agendar_automacao(
        'renomear_arquivos_em_lote', 5
    )  # Exemplo: agenda para daqui 5 segundos
    # breakpoint()
    for thread in instancias_ativas:
        iniciar_automacao(instancias_ativas[thread])
        # executar_automacao_docker(thread)

    while any(t.is_alive() for t in instancias_ativas.values()):
        time.sleep(1)

    print('Todas as automações agendadas finalizaram.')"""

    cls()

    agendador = sched.scheduler(timefunc=time.time)

    minuto_inicial = datetime.datetime.now().minute + 1
    quantidade_agendamentos = int(
        input('digite a quantidade de agendamentos: ')
    )

    minuto_final = minuto_inicial + quantidade_agendamentos
    for minuto in range(
        minuto_inicial,
        minuto_final,
    ):
        target_time = datetime.datetime(2025, 8, 30, 17, minuto, 0).timestamp()

        agendador.enterabs(
            time=target_time,
            priority=1,
            action=executar_automacao,
            argument=('renomear_arquivos_em_lote',),
        )

    # pprint(scheduler.queue)
    # breakpoint()

    print(
        '\n',
        f'Faltam {agendador.queue.__len__()} agendamentos!',
    )
    quantidade_agendamentos = agendador.queue.__len__()
    while agendador.queue:
        scheduler_run(agendador, blocking=False)

        if (
            quantidade_agendamentos != agendador.queue.__len__()
            and agendador.queue.__len__() != 0
        ):
            quantidade_agendamentos = agendador.queue.__len__()
            print(
                '\n',
                f'Faltam {quantidade_agendamentos} agendamentos!',
            )

            time.sleep(1)
        elif agendador.queue.__len__() == 0:
            quantidade_agendamentos = agendador.queue.__len__()
            print(
                '\n',
                f'Agendamentos finalizados!',
            )

            time.sleep(1)
