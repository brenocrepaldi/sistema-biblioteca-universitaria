from models.reserva import Reserva
from services.livro_sevice import LivroConector
from services.usuario_service import UsuarioConector


class ReservaReceptor:
    @staticmethod
    def receber_dados():
        titulo = input("\nTítulo do livro a ser reservado: ")
        if not LivroConector.verificar_livro(titulo):
            ReservaLogger.mensagem_nao_encontrado(titulo)
        livro = LivroConector.buscar_livro(titulo)

        username = input("Nome de usuario para realizar a reserva: ")
        if not UsuarioConector.verificar_usuario(username):
            ReservaLogger.mensagem_nao_encontrado(username)
        usuario = UsuarioConector.buscar_usuario(username)

        return {"livro": livro, "usuario": usuario}


class ReservaProcessador:
    reservas = []

    @classmethod
    def processar_dados(cls, dados):
        nova_reserva = Reserva(dados["livro"], dados["usuario"])
        cls.reservas.append(nova_reserva)

        ReservaLogger.mostrar_mensagem_reserva(nova_reserva)

    @classmethod
    def listar_reservas(cls):
        if not cls.reservas:
            ReservaLogger.mostrar_mensagem_vazio()
        else:
            ReservaLogger.mostrar_reservas(cls.reservas)


class ReservaLogger:
    @staticmethod
    def mensagem_nao_encontrado(nome):
        print(f"\n{nome} não encontrado")

    @staticmethod
    def mostrar_mensagem_reserva(reserva):
        print(
            f"\nReserva realizada com sucesso: livro: {reserva.livro.titulo}, usuário: {reserva.usuario.username}"
        )

    @staticmethod
    def mostrar_reservas(reservas):
        print("\nLista de Reservas:")
        for reserva in reservas:
            print(
                f"Nome: {reserva.usuario.nome_completo} | Livro: {reserva.livro.titulo}"
            )


class ReservaConector:
    @staticmethod
    def fazer_reserva():
        receptor = ReservaReceptor()
        processador = ReservaProcessador()

        dados = receptor.receber_dados()
        processador.processar_dados(dados)

    @staticmethod
    def listar_reservas():
        ReservaProcessador.listar_reservas()
