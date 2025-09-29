from datetime import datetime
from sched import scheduler
from time import time

agendador = scheduler(time)

data_agendada = datetime(2025, 8, 30, 23, 10, 0).timestamp()

agendador.enterabs(
    time=data_agendada,
    priority=1,
    action=(lambda x: print(x)),
    argument=('Executando ação!',),
)

while agendador.queue:
    agendador.run(blocking=False)
