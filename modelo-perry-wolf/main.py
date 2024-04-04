# importando as classes
import logging

from model.livro import Livro
from model.reserva import Reserva
from model.usuario import Usuario
from services.autenticacao_service import AutenticacaoService
from services.catalogo_sevice import CatalogoService
from services.reserva_service import ReservaService


# função de condiguração do logger
def configurar_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("biblioteca.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def main():
    # Configuração do logger
    configurar_logger()

    # Inicialização dos receptores e processadores
    catalogo_de_livros = CatalogoService()
    autenticacao_do_usuario = AutenticacaoService()
    reserva_de_livros = ReservaService()

    # Exemplo de uso dos processadores
    livro_info = Livro("1984", "George Orwell", 2022, "1234567890")
    catalogo_de_livros.adicionar_livro(livro_info)

    usuario_info = Usuario("vitor__", "senha1234", "Vitor Silva")
    autenticacao_do_usuario.autenticar_usuario(usuario_info)

    reserva_info = Reserva(livro_info, usuario_info)
    reserva_de_livros.fazer_reserva(reserva_info)


if __name__ == "__main__":
    main()
