# Introdução 

Bem-Vindo a API de E-commerce ! Essa é uma API desenvolvida em Django e DRF(Django RestFramework) baseado em um sistema de um comércio eletrônico.

# Funcionalidades 

1 - Autenticação através de JWT Token.

2 - CRUD completo para registro dos clientes e suas respectivas informações.

3 - CRUD completo para o registro dos pedidos do comércio.

4 - CRUD completo para registro de métodos de pagamentos.

5 - CRUD completo para os produtos.

6 - CRUD completo para avaliações dos produtos.

Além disso a API permite acesso a algumas estatísticas como:

    Média da avaliação de um produto através das avaliações feitas pelos clientes.
    Total de faturamento do e-commerce.
    Total de faturamento do e-commerce em cada método de pagamento.
    Estatisticas de cada método de pagamento(número de pedidos totais e faturamento total)

# Autenticação 

Método de Autenticação : JWT Token

Para acessar os endpoints protegidos da API ,a autenticação por JWT é necessária.Siga
as instruções da documentação.

# Documentação Completa da API 

Para acessar a documentação completa da API feita através da ferramenta PostMan basta acessar o link abaixo :

https://documenter.getpostman.com/view/32598004/2sA2r9Uha5#a9aba167-2d2f-4496-8740-bf3823b5567d

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- **Python**
- **Pip** (gerenciador de pacotes do Python)

## Instalação das Dependências do Projeto

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt) utilize o comando:

**pip install -r requirements.txt**

## Configuração do Banco de Dados 

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

**1 - python manage.py makemigrations**

**2 - python manage.py migrate**

## Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

**python manage.py runserver**
