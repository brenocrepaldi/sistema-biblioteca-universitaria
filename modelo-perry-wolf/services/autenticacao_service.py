import logging

logger = logging.getLogger(__name__)


class AutenticacaoReceptor:
    def __init__(self):
        pass

    def autenticar_usuario(self, usuario_info):
        # O receptor recebe a solicitação de autenticar um usuário e registra uma mensagem de log
        logger.info(
            f"Recebida solicitação para autenticar usuário: {usuario_info.username}"
        )


class AutenticacaoProcessador:
    def __init__(self, receptor):
        self.receptor = receptor

    def autenticar_usuario(self, usuario_info):
        # O processador delega a tarefa de autenticar o usuário ao receptor
        self.receptor.autenticar_usuario(usuario_info)
        # Após o usuário ser autenticado com sucesso, o processador registra uma mensagem de log
        logger.info(f"Usuário autenticado: {usuario_info.username}")


class AutenticacaoService:
    def __init__(self):
        # Inicializa o receptor e o processador do serviço de autenticação
        self.receptor = AutenticacaoReceptor()
        self.processador = AutenticacaoProcessador(self.receptor)

    def autenticar_usuario(self, usuario_info):
        # O serviço recebe a solicitação de autenticar um usuário e a repassa ao processador
        self.processador.autenticar_usuario(usuario_info)
