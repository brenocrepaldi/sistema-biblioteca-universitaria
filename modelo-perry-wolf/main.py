# importando as classes
import logging

from model.livro import Livro
from model.reserva import Reserva
from model.usuario import Usuario
from services.autenticacao_service import AutenticacaoConector
from services.catalogo_sevice import CatalogoConector
from services.reserva_service import ReservaConector


# função de configuração do logger
def configurar_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("modelo-perry-wolf/tests/biblioteca.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def main():
    # Configuração do logger
    configurar_logger()

    # Inicialização dos conectores
    catalogo_de_livros = CatalogoConector()
    autenticacao_do_usuario = AutenticacaoConector()
    reserva = ReservaConector()

    # Criando as informações e aplicando os serviços
    livro_info = Livro("1984", "George Orwell", 2022, "1234567890")  # exemplo
    catalogo_de_livros.adicionar_livro(livro_info)

    usuario_info = Usuario("vitor__", "senha1234", "Vitor Silva")  # exemplo
    autenticacao_do_usuario.autenticar_usuario(usuario_info)

    reserva_info = Reserva(livro_info, usuario_info)
    reserva.fazer_reserva(reserva_info)


if __name__ == "__main__":
    main()
