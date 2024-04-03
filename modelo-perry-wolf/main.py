# importando as classes
import logging

from services.autenticacao_service import AutenticacaoProcessador, AutenticacaoReceptor
from services.catalogo_sevice import CatalogoProcessador, CatalogoReceptor
from services.reserva_service import ReservaProcessador, ReservaReceptor


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
    catalogo_receptor = CatalogoReceptor()
    catalogo_processador = CatalogoProcessador(catalogo_receptor)

    autenticacao_receptor = AutenticacaoReceptor()
    autenticacao_processador = AutenticacaoProcessador(autenticacao_receptor)

    reserva_receptor = ReservaReceptor()
    reserva_processador = ReservaProcessador(reserva_receptor)

    # Exemplo de uso dos processadores
    livro_info = {
        "titulo": "Python for Beginners",
        "autor": "John Doe",
        "ano": 2022,
        "isbn": "1234567890",
    }
    catalogo_processador.adicionar_livro(livro_info)

    usuario_info = {"username": "usuario", "password": "senha"}
    autenticacao_processador.autenticar_usuario(usuario_info)

    reserva_info = {"livro": livro_info, "usuario": usuario_info}
    reserva_processador.fazer_reserva(reserva_info)


if __name__ == "__main__":
    main()
