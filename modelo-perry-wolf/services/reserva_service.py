import logging

logger = logging.getLogger(__name__)


class ReservaReceptor:
    def __init__(self):
        pass

    def fazer_reserva(self, reserva_info):
        # O receptor recebe a solicitação de fazer uma reserva e registra uma mensagem de log
        logger.info(
            f"Recebida solicitação para fazer reserva: {reserva_info['livro']['titulo']} por {reserva_info['usuario']['username']}"
        )


class ReservaProcessador:
    def __init__(self, receptor):
        self.receptor = receptor

    def fazer_reserva(self, reserva_info):
        # O processador delega a tarefa de fazer a reserva ao receptor
        self.receptor.fazer_reserva(reserva_info)
        # Após a reserva ser feita com sucesso, o processador registra uma mensagem de log
        logger.info(
            f"Reserva realizada com sucesso: Livro: {reserva_info['livro']['titulo']}, Usuário: {reserva_info['usuario']['username']}"
        )


class ReservaService:
    def __init__(self):
        # Inicializa o receptor e o processador do serviço de reserva
        self.receptor = ReservaReceptor()
        self.processador = ReservaProcessador(self.receptor)

    def fazer_reserva(self, reserva_info):
        # O serviço recebe a solicitação de fazer uma reserva e a repassa ao processador
        self.processador.fazer_reserva(reserva_info)
