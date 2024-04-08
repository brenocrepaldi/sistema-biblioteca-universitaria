from models.livro import Livro
from views.livro_view import LivroView


class LivroController:
    catalogo = []

    @classmethod
    def adicionar_livro(cls):
        titulo = input("\nTítulo do Livro: ")
        autor = input("Autor do Livro: ")
        ano = input("Ano de Publicação: ")
        codigo = input("Código: ")

        novo_livro = Livro(titulo, autor, ano, codigo)
        cls.catalogo.append(novo_livro)

        LivroView.mostrar_mensagem_adicao(titulo)

    @classmethod
    def listar_livros(cls):
        if not cls.catalogo:
            LivroView.mostrar_mensagem_vazio()
        else:
            LivroView.mostrar_livros(cls.catalogo)

    @classmethod
    def verificar_livro(cls, titulo):
        for livro in cls.catalogo:
            if titulo == livro.titulo:
                return 1
        return 0

    @classmethod
    def buscar_livro(cls, titulo):
        for livro in cls.catalogo:
            if titulo == livro.titulo:
                return livro
        LivroView.mensagem_livro_nao_encontrado(titulo)
