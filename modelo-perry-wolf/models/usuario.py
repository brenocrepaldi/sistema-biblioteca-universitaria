class Usuario:
    def __init__(self, username, password, nome_completo):
        self.username = username
        self.password = password
        self.nome_completo = nome_completo.title()

    def __str__(self):
        return f"Usuário: {self.username}, Nome Completo: {self.nome_completo}"
