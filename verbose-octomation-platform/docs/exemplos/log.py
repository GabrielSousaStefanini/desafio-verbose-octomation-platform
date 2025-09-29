from logger_utils import registar_log, registar_log_decorator  # type: ignore


@registar_log_decorator(
    log_level='DEBUG',
    mensagem='Atualizando tudo',
    cultura='pt_BR.UTF-8',
    handler_name='root',
)
def testando_wapper():
    print('Executando a função principal')

    resultado = 'Executando a função principal'
    registar_log(
        log_level='DEBUG',
        mensagem=resultado,
        cultura='pt_BR.UTF-8',
        handler_name='root',
    )


testando_wapper()


@registar_log_decorator(
    log_level='WARNING',
    mensagem='Mensgem outra',
    cultura='ja_JP.UTF-8',
    handler_name='root',
)
def testando_wapper():
    print('Executando a função principal')


testando_wapper()


@registar_log_decorator(
    log_level='INFO',
    mensagem='Eita!',
    cultura='ko_KR.UTF-8',
    handler_name='root',
)
def testando_wapper():
    print('Executando a função principal')


testando_wapper()
