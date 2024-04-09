# Modelo de Arquitetura Perry e Wolf

Este repositório contém a implementação de um modelo de arquitetura de um sistema de biblioteca baseado nos conceitos propostos por Perry e Wolf, apresentando uma estrutura organizada para o desenvolvimento de sistemas de informação. Abaixo está uma descrição detalhada dos módulos que compõem esse modelo.

## Descrição dos módulos

### Modelo de Informação (/models)
O módulo de Modelo de Informação descreve os dados manipulados pelo sistema e como eles estão organizados. Ele fornece uma visão clara dos principais elementos de dados, incluindo informações sobre livros, usuários e reservas. Esta seção é essencial para entender a estrutura e a natureza dos dados que o sistema irá manipular.

### Modelo de Processamento (/services)
O módulo de Modelo de Processamento descreve como o sistema realiza suas operações e processa os dados. Ele implementa as funcionalidades essenciais relacionadas à gestão do catálogo de livros, autenticação de usuários e gerenciamento de reservas. Este módulo é composto por três principais classes:

- **Classe Receptora**: Responsável por receber os dados do ambiente externo ou de outras partes do sistema.
- **Classe Processadora**: Responsável por processar os dados recebidos de acordo com a lógica de negócios e as regras estabelecidas.
- **Classe Conectora**: Responsável por conectar as classes receptora e processadora, facilitando a comunicação entre elas e garantindo o funcionamento adequado do sistema como um todo.

Essa estrutura modular proporciona uma separação clara de responsabilidades e facilita a manutenção, escalabilidade e extensibilidade do sistema.

## Diagrama da Arquitetura
