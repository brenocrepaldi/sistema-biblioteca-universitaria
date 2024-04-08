from controllers.livro_controller import LivroController
from controllers.usuario_controller import UsuarioController
from models.reserva import Reserva
from views.reserva_view import ReservaView


class ReservaController:
    reservas = []

    @classmethod
    def fazer_reserva(cls):

        username = input("\nNome de usuario para realizar a reserva: ")
        if not UsuarioController.verificar_usuario(username):
            ReservaView.mensagem_nao_encontrado(username)
        usuario = UsuarioController.buscar_usuario(username)

        titulo = input("Título do livro a ser reservado: ")
        if not LivroController.verificar_livro(titulo):
            ReservaView.mensagem_nao_encontrado(titulo)
        livro = LivroController.buscar_livro(titulo)

        nova_reserva = Reserva(livro, usuario)

        cls.reservas.append(nova_reserva)
        ReservaView.mostrar_mensagem_reserva(nova_reserva)

    @classmethod
    def listar_reservas(cls):
        if not cls.reservas:
            ReservaView.mostrar_mensagem_vazio()
        else:
            ReservaView.mostrar_reservas(cls.reservas)
