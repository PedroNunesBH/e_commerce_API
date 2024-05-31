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

Para acessar a documentação completa da API feita através da ferramenta Postman basta acessar o link abaixo :

https://documenter.getpostman.com/view/32598004/2sA2r9Uha5#a9aba167-2d2f-4496-8740-bf3823b5567d

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- **Python**
- **Pip** (gerenciador de pacotes do Python)

## Instalação das Dependências do Projeto

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt) utilize o comando:

```bash
pip install -r requirements.txt
```

## Criando um Super Usuário(Administrador)

Para configurar um administrador no Django,no terminal,utilize o seguinte comando:

```bash
python manage.py createsuperuser
```

Após isso siga os passos descritos no terminal para configurar o mesmo.

## Configuração do Banco de Dados 

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

```bash
python manage.py runserver
```

## Docker

O projeto contém os arquivos `Dockerfile` e `docker-compose.yml`  para a conteinerização da aplicação. Neste projeto, utilizaremos o Docker Compose para rodar a aplicação containerizada e conectá-la a um banco de dados PostgreSQL, também em um container.

**Passos para realizar o processo de conteinerização:**

1. **Instalar o Docker:**
   - Certifique-se de ter o Docker instalado e funcionando corretamente em sua máquina. Siga as instruções oficiais para [instalar o Docker](https://docs.docker.com/get-docker/).

2. **Configurar o Banco de Dados no Django:**
   - No arquivo `settings.py` da aplicação Django, substitua a configuração padrão da variável `DATABASES` pela seguinte configuração:
     

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
    ```

3. **Subir os Containers:**
   - Abra o terminal e, no diretório da aplicação, execute o seguinte comando:

 ```bash
docker compose -p nomedoprojeto up
```

## Observações Adicionais:

Comando para parar e remover os containers:

```bash
docker compose down
```
