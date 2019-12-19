from spam.enviador_de_email import Enviador
import pytest

def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br','pablogrbarbosa@gmail.com' ]
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
