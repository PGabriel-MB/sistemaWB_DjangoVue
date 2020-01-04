from spam.db import Conexao
from spam.modelos import Usuario


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    user = Usuario(nome='Pablo')
    sessao.salvar(user)
    assert isinstance(user.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


'''
def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    users = [Usuario(nome='Pablo'), Usuario(nome='Luciano')]
    for user in users:
        sessao.salvar(user)
    assert users == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
'''
