class Reserva:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario

    def __str__(self):
        return f"{self.livro} {self.usuario}"
