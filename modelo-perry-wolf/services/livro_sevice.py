from models.livro import Livro


class LivroReceptor:
    @staticmethod
    def receber_dados():
        titulo = input("\nTítulo do Livro: ")
        autor = input("Autor do Livro: ")
        ano = input("Ano de Publicação: ")
        codigo = input("Código: ")
        return {"titulo": titulo, "autor": autor, "ano": ano, "codigo": codigo}


class LivroProcessador:
    catalogo = []

    @classmethod
    def processar_dados(cls, dados):
        novo_livro = Livro(
            dados["titulo"], dados["autor"], dados["ano"], dados["codigo"]
        )
        cls.catalogo.append(novo_livro)

        LivroLogger.mostrar_mensagem_adicao(novo_livro.titulo)

    @classmethod
    def listar_livros(cls):
        if not cls.catalogo:
            LivroLogger.mostrar_mensagem_vazio()
        else:
            LivroLogger.mostrar_livros(cls.catalogo)

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
        LivroLogger.mensagem_livro_nao_encontrado(titulo)


class LivroLogger:
    @staticmethod
    def mostrar_livros(catalogo):
        print("\nLista de Livros:")
        for livro in catalogo:
            print(
                f"Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano} | Código: {livro.codigo}"
            )

    @staticmethod
    def mostrar_mensagem_vazio():
        print("\nNenhum livro cadastrado.")

    @staticmethod
    def mostrar_mensagem_adicao(titulo):
        print(f"\nLivro '{titulo}' adicionado com sucesso!")

    @staticmethod
    def mensagem_livro_nao_encontrado(titulo):
        print(f"\nLivro {titulo} não encontrado")


class LivroConector:
    @classmethod
    def adicionar_livro(cls):
        receptor = LivroReceptor()
        processador = LivroProcessador()

        dados = receptor.receber_dados()
        processador.processar_dados(dados)

    @staticmethod
    def listar_livros():
        LivroProcessador.listar_livros()

    @staticmethod
    def verificar_livro(titulo):
        return LivroProcessador.verificar_livro(titulo)

    @staticmethod
    def buscar_livro(titulo):
        return LivroProcessador.buscar_livro(titulo)
