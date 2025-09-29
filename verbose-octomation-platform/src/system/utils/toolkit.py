from datetime import datetime


def localizar_data_hora(
    datetime: datetime,
    cultura: str,
):
    import locale

    locale.setlocale(locale.LC_TIME, cultura)
    data_hora_atual = datetime
    return data_hora_atual.strftime('%c')
