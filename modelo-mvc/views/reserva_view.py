class ReservaView:
    @staticmethod
    def mostrar_mensagem_vazio():
        print("\nNenhuma reserva cadastrada.")

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

    @staticmethod
    def mensagem_nao_encontrado(nome):
        print(f"\n{nome} não encontrado")
