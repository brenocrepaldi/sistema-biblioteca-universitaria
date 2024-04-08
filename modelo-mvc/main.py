from controllers.livro_controller import LivroController
from controllers.reserva_controller import ReservaController
from controllers.usuario_controller import UsuarioController


def menu(livro_ctrl, reserva_ctrl, usuario_ctrl):
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
                livro_ctrl.adicionar_livro()
            case 2:
                livro_ctrl.listar_livros()
            case 3:
                usuario_ctrl.autenticar_usuario()
            case 4:
                usuario_ctrl.listar_usuarios()
            case 5:
                reserva_ctrl.fazer_reserva()
            case 6:
                reserva_ctrl.listar_reservas()
            case 7:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Por favor, tente novamente.")


def main():
    # Instância dos controladores
    livro_ctrl = LivroController()
    reserva_ctrl = ReservaController()
    usuario_ctrl = UsuarioController()
    menu(livro_ctrl, reserva_ctrl, usuario_ctrl)


if __name__ == "__main__":
    main()
