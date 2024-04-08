from models.usuario import Usuario


class UsuarioReceptor:
    @staticmethod
    def receber_dados():
        username = input("\nNome de usuário: ")
        password = input("Senha: ")
        nome_completo = input("Nome Completo: ").title()
        return {
            "username": username,
            "password": password,
            "nome_completo": nome_completo,
        }


class UsuarioProcessador:
    lista_usuarios = []

    @classmethod
    def processar_dados(cls, dados):
        novo_usuario = Usuario(
            dados["username"], dados["password"], dados["nome_completo"]
        )
        if (
            novo_usuario.username != ""
            and novo_usuario.password != ""
            and novo_usuario.nome_completo != ""
        ):
            if UsuarioLogger.mensagem_autenticacao_recebida(novo_usuario.username):
                cls.lista_usuarios.append(novo_usuario)
                UsuarioLogger.mensagem_autenticado(novo_usuario.username)
        else:
            UsuarioLogger.mensagem_erro(novo_usuario.username)

    @classmethod
    def listar_usuarios(cls):
        if not cls.lista_usuarios:
            UsuarioLogger.mostrar_mensagem_vazio()
        else:
            UsuarioLogger.mostrar_usuarios(cls.lista_usuarios)

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
        UsuarioLogger.mensagem_usuario_nao_encontrado(username)


class UsuarioLogger:
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


class UsuarioConector:
    @classmethod
    def autenticar_usuario(cls):
        receptor = UsuarioReceptor()
        processador = UsuarioProcessador()

        dados = receptor.receber_dados()
        processador.processar_dados(dados)

    @staticmethod
    def listar_usuarios():
        UsuarioProcessador.listar_usuarios()

    @staticmethod
    def verificar_usuario(username):
        return UsuarioProcessador.verificar_usuario(username)

    @staticmethod
    def buscar_usuario(username):
        return UsuarioProcessador.buscar_usuario(username)
