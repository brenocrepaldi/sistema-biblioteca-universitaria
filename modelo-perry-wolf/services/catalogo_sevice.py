import logging

logger = logging.getLogger(__name__)


class CatalogoReceptor:
    def __init__(self):
        pass

    def adicionar_livro(self, livro_info):
        # Aqui, o receptor recebe a solicitação de adicionar um livro e registra uma mensagem de log
        logger.info(f"Recebida solicitação para adicionar livro: {livro_info.titulo}")


class CatalogoProcessador:
    def __init__(self, receptor):
        self.receptor = receptor

    def adicionar_livro(self, livro_info):
        # O processador delega a tarefa de adicionar o livro ao receptor
        self.receptor.adicionar_livro(livro_info)
        # Após o livro ser adicionado com sucesso, o processador registra uma mensagem de log
        logger.info(f"Livro adicionado ao catálogo: {livro_info.titulo}")


class CatalogoService:
    def __init__(self):
        # Inicializa o receptor e o processador do serviço de catálogo
        self.receptor = CatalogoReceptor()
        self.processador = CatalogoProcessador(self.receptor)

    def adicionar_livro(self, livro_info):
        # O serviço recebe a solicitação de adicionar um livro e a repassa ao processador
        self.processador.adicionar_livro(livro_info)
