from services.livro_sevice import LivroConector
from services.reserva_service import ReservaConector
from services.usuario_service import UsuarioConector


def menu(usuario_con, livro_con, reserva_con):
    print("\nBiblioteca Universitária - Menu Principal")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Adicionar Usuário")
    print("4. Listar Usuários")
    print("5. Fazer Reserva")
    print("6. Listar Reservas")
    print("7. Sair")

    while True:
        opcao = int(input("\nEscolha uma opção: "))

        match opcao:
            case 1:
                livro_con.adicionar_livro()
            case 2:
                livro_con.listar_livros()
            case 3:
                usuario_con.autenticar_usuario()
            case 4:
                usuario_con.listar_usuarios()
            case 5:
                reserva_con.fazer_reserva()
            case 6:
                reserva_con.listar_reservas()
            case 7:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Por favor, tente novamente.")


def main():
    # Instância dos controladores
    usuario_con = UsuarioConector()
    livro_con = LivroConector()
    reserva_con = ReservaConector()

    menu(usuario_con, livro_con, reserva_con)


if __name__ == "__main__":
    main()
