from models.usuario import Usuario


class UsuarioView:
    @staticmethod
    def mostrar_usuarios(usuarios):
        print("\nLista de Usuários:")
        for usuario in usuarios:
            print(
                f"Nome: {usuario.nome_completo} | Nome de Usuário: {usuario.username}"
            )

    @staticmethod
    def mostrar_mensagem_vazio():
        print("\nNenhum usuário cadastrado.")

    @staticmethod
    def mensagem_autenticacao_recebida(username):
        print(f"\nRecebida solicitação para autenticar usuário: {username}")
        return 1

    @staticmethod
    def mensagem_autenticado(username):
        print(f"\nUsuário autenticado: {username}")

    @staticmethod
    def mensagem_erro(username):
        print(f"\nErro na autenticação: {username}")

    @staticmethod
    def mensagem_usuario_nao_encontrado(username):
        print(f"\nUsuário {username} não encontrado")
