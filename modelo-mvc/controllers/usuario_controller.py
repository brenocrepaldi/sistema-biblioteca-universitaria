from models.usuario import Usuario
from views.usuario_view import UsuarioView


class UsuarioController:
    lista_usuarios = []

    @classmethod
    def autenticar_usuario(cls):
        username = input("\nNome de usuário: ")
        password = input("Senha: ")
        nome_completo = input("Nome Completo: ").title()

        novo_usuario = Usuario(username, password, nome_completo)

        if (
            novo_usuario.username != ""
            and novo_usuario.password != ""
            and novo_usuario.nome_completo != ""
        ):
            if UsuarioView.mensagem_autenticacao_recebida(novo_usuario.username):
                cls.lista_usuarios.append(novo_usuario)
                UsuarioView.mensagem_autenticado(novo_usuario.username)
        else:
            UsuarioView.mensagem_erro(novo_usuario.username)

    @classmethod
    def listar_usuarios(cls):
        if not cls.lista_usuarios:
            UsuarioView.mostrar_mensagem_vazio()
        else:
            UsuarioView.mostrar_usuarios(cls.lista_usuarios)

    @classmethod
    def verificar_usuario(cls, username):
        for usuario in cls.lista_usuarios:
            if username == usuario.username:
                return 1
        return 0

    @classmethod
    def buscar_usuario(cls, username):
        for usuario in cls.lista_usuarios:
            if username == usuario.username:
                return usuario
        UsuarioView.mensagem_livro_nao_encontrado(username)
