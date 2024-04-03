# Modelo
# O Modelo representa a parte lógica de dados do sistema, gerenciando os dados, a lógica e as regras do aplicativo.
# No contexto deste exemplo, ele armazena e gerencia as notas dos alunos.
class ModeloNotas:
    def __init__(self):
        # Dicionário para armazenar notas dos alunos: aluno -> nota
        self.notas = {}

    def adicionar_nota(self, aluno, nota):
        # Adiciona ou atualiza a nota de um aluno
        self.notas[aluno] = nota

    def obter_nota(self, aluno):
        # Retorna a nota do aluno especificado, se existir
        return self.notas.get(aluno, None)
    def adicionar_a_nota(self, aluno, notaAdicional):
        # Adiciona ou atualiza a nota de um aluno
        self.notas[aluno] = self.notas[aluno] + notaAdicional

# Visão
# A Visão é responsável pela representação dos dados (a saída). Aqui, define como os dados são apresentados ao usuário.
class VisaoNotas:
    @staticmethod
    def exibir_nota_aluno(aluno, nota):
        # Exibe a nota de um aluno específico
        if nota is not None:
            print(f"Nota do aluno {aluno}: {nota}")
        else:
            print(f"Aluno {aluno} não encontrado.")

    @staticmethod
    def exibir_mensagem(mensagem):
        # Exibe uma mensagem genérica
        print(mensagem)

# Controlador
# O Controlador age como um intermediário entre o modelo e a visão. Ele controla as interações entre o modelo e a visão,
# processando as entradas do usuário e atualizando a visão conforme necessário.
class ControladorNotas:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

    def adicionar_nota(self, aluno, nota):
        # Adiciona uma nota para um aluno no modelo e atualiza a visão
        self.modelo.adicionar_nota(aluno, nota)
        self.visao.exibir_mensagem(f"Nota adicionada para o aluno {aluno}.")

    def exibir_nota(self, aluno):
        # Solicita a nota de um aluno do modelo e pede para a visão exibir essa informação
        nota = self.modelo.obter_nota(aluno)
        self.visao.exibir_nota_aluno(aluno, nota)
    def adicional_nota(self, aluno, nota):
        # Adiciona uma nota para um aluno no modelo e atualiza a visão
        self.modelo.adicionar_a_nota(aluno, nota)
        self.visao.exibir_mensagem(f"Nota adicional para o aluno {aluno}.")

# Configuração e Execução
# Aqui configuramos e instanciamos os componentes do MVC. Este bloco de código serve como o ponto de entrada do programa,
# onde o modelo, a visão e o controlador são conectados e utilizados para executar operações específicas.
if __name__ == "__main__":
    # Instanciação dos componentes do MVC
    modelo = ModeloNotas()
    visao = VisaoNotas()
    controlador = ControladorNotas(modelo, visao)

    # Demonstração do uso do MVC para adicionar e exibir notas de alunos
    controlador.adicionar_nota("Maria", 8.5)
    controlador.adicionar_nota("João", 9.0)
    # Exibindo as notas dos alunos
    controlador.exibir_nota("Maria")
    controlador.adicional_nota("Maria", 1.0)
    controlador.exibir_nota("Maria")
    controlador.exibir_nota("João")
    # Tentativa de exibir a nota de um aluno não cadastrado
    controlador.exibir_nota("Pedro")  # Este aluno não existe, demonstrando a manipulação de erros e entradas inesperadas.
