# Projeto Django - Guia Inicial

---

## Visão Geral

Este guia foi criado para orientar desenvolvedores que desejam começar um projeto utilizando o framework Django. Ele fornece uma série de passos básicos para configurar um ambiente de desenvolvimento e iniciar um novo projeto.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o seguinte em sua máquina:

- Python (versão 3.x recomendada)
- Pip (gerenciador de pacotes Python)
- Um ambiente virtual (opcional, mas altamente recomendado para isolar dependências do projeto)

## Passo 1: Configuração do Ambiente Virtual (Opcional)

Se preferir, crie um ambiente virtual para o seu projeto Django. Isso ajudará a isolar as dependências do projeto e evitará conflitos com outros projetos Python em sua máquina.

```bash
# Instale o pacote 'virtualenv', se ainda não estiver instalado
pip install virtualenv

# Crie um novo ambiente virtual (substitua 'meu_projeto' pelo nome do seu projeto)
virtualenv meu_projeto_env

# Ative o ambiente virtual
# No Windows
meu_projeto_env\Scripts\activate
# No macOS e Linux
source meu_projeto_env/bin/activate
