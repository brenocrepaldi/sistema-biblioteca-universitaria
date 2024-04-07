from controllers.livro_controller import LivroController
from controllers.reserva_controller import ReservaController
from controllers.usuario_controller import UsuarioController


def menu(livro_ctrl):
    print("\nBiblioteca Universitária - Menu Principal")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case 1:
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            ano = input("Ano de Publicação: ")
            isbn = input("ISBN: ")

            livro_ctrl.adicionar_livro(titulo, autor, ano, isbn)
            main()
        case 2:
            livro_ctrl.listar_livros()
            main()
        case 3:
            print("Saindo do sistema...")
            pass
        case _:
            print("Opção inválida. Por favor, tente novamente.")


def main():
    # Instância do controlador
    livro_ctrl = LivroController()
    menu(livro_ctrl)


if __name__ == "__main__":

    main()
