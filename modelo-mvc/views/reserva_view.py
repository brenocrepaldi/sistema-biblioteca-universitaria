from models.reserva import Reserva


class ReservaView:
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
