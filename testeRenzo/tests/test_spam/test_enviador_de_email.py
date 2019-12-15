from spam.enviador_de_email import Enviador


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'pablogrbarbosa@gmail.com',
        'alchepablomist@gmail.com',
        'Teste de remetente - Python Pro',
        'Primeiro teste de remetente imaginário'
    )
    assert 'pablogrbarbosa@gmail.com' in resultado
