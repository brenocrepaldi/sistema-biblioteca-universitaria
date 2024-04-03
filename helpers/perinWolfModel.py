# Módulo Receptor
# Este módulo é responsável por receber mensagens. Ele exemplifica um módulo no sentido
# de Perry e Wolf, sendo uma unidade funcional distinta dentro da arquitetura do sistema.
class Receptor:
    def receber_mensagem(self):
        # Aqui, simulamos o recebimento de uma mensagem de uma fonte externa.
        mensagem = "Olá turma de Arquitetura de Software"
        return mensagem

# Módulo Processador
# Este módulo processa as mensagens recebidas. Isso pode envolver uma variedade de operações,
# dependendo da aplicação específica. Neste exemplo, simplesmente convertemos a mensagem para letras maiúsculas.
class Processador:
    def processar_mensagem(self, mensagem):
        mensagem_processada = mensagem.upper()
        return mensagem_processada

# Módulo Logger
# O módulo Logger é utilizado para registrar eventos ou mensagens. Neste caso, ele registra
# as mensagens processadas, ilustrando como um módulo pode ser utilizado para suporte ou
# operações auxiliares dentro de uma arquitetura.
class Logger:
    def log_mensagem(self, mensagem):
        print(f"Log: {mensagem}")

# Conectores
# Os conectores são responsáveis pela comunicação e coordenação entre módulos. Neste exemplo,
# a classe Conector atua como um conector ao organizar a interação entre o Receptor, o Processador
# e o Logger, chamando métodos desses módulos para executar o fluxo de processamento de mensagem.
class Conector:
    def __init__(self):
        self.receptor = Receptor()
        self.processador = Processador()
        self.logger = Logger()
    
    def processar_e_logar(self):
        # O método processar_e_logar coordena as operações entre os módulos:
        # 1. Recebe uma mensagem.
        # 2. Processa essa mensagem.
        # 3. Registra a mensagem processada no log.
        mensagem = self.receptor.receber_mensagem()
        mensagem_processada = self.processador.processar_mensagem(mensagem)
        self.logger.log_mensagem(mensagem_processada)

# Configuração e Execução
# A configuração do sistema define como os módulos e conectores são organizados e como eles interagem.
# Neste caso, a execução do script instância o conector (que, por sua vez, instância os módulos) e
# executa o processo de receber, processar e logar uma mensagem.
if __name__ == "__main__":
    sistema = Conector()
    sistema.processar_e_logar()
