# servidor

import pickle
import socket
import threading
from datetime import datetime
from sched import scheduler
from time import sleep, time

agendador = scheduler(time)


def loop_agendador():
    while True:
        agendador.run(blocking=False)
        sleep(0.5)


def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 5000))
        s.listen()
        print('Servidor de agendamento ouvindo em localhost:5000')
        while True:
            conn, _ = s.accept()
            with conn:
                data = conn.recv(4096)
                if not data:
                    continue
                evento = pickle.loads(data)
                agendador.enterabs(
                    time=evento['timestamp'],
                    priority=1,
                    action=lambda msg=evento['msg']: print(msg),
                )
                print('Novo agendamento recebido:', evento)


# roda o agendador em paralelo ao servidor
threading.Thread(target=loop_agendador, daemon=True).start()
servidor()
