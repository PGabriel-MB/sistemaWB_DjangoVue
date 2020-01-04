from spam.enviador_de_email import Enviador
from spam.enviador_de_email import EmailInvalido
import pytest


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'pablogrbarbosa@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'alchepablomist@gmail.com',
        'Teste de remetente - Python Pro',
        'Primeiro teste de remetente imaginário'
    )
    assert resultado in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'pablo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'alchepablomist@gmail.com',
            'Teste de remetente - Python Pro',
            'Primeiro teste de remetente imaginário'
        )
