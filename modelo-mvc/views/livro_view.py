class LivroView:
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
