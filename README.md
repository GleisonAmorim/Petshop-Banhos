# Petshop

Este é um projeto de um petshop desenvolvido em Python/Django.

## Descrição

O projeto Petshop é uma aplicação web para gerenciamento de um petshop, permitindo o controle de clientes, serviços, produtos, reservas e outros aspectos relacionados ao funcionamento do estabelecimento.

## Funcionalidades

- Cadastro e gestão de clientes
- Cadastro e gestão de serviços oferecidos pelo petshop
- Cadastro e gestão de produtos disponíveis para venda
- Reserva de serviços e produtos pelos clientes
- Geração de relatórios de vendas e serviços realizados

## Estrutura do Projeto

- `__pycache__`: Diretório gerado pelo Python para armazenar arquivos compilados em bytecode.
- `base`: Contém arquivos de configurações gerais, modelos de banco de dados e utilitários comuns.
- `reserva`: Contém o código relacionado a reservas de serviços ou produtos no petshop.
- `rest_api`: Contém o código para uma API REST que permite interações com o sistema do petshop.
- `staticfiles`: Armazena arquivos estáticos como folhas de estilo, arquivos JavaScript e imagens.
- `venv`: Diretório para a virtual environment do Python, isolando as dependências do projeto.
- `db.sqlite3`: Arquivo de banco de dados SQLite3 que armazena os dados do projeto.
- `manage.py`: Script Django para tarefas de gerenciamento do projeto.
- `pytest.ini`: Arquivo de configuração para o Pytest.
- `requirements.txt`: Lista de dependências do projeto.

## Instalação

1. Clone o repositório:
git clone <URL_do_repositório>

arduino
Copiar código

2. Navegue até o diretório do projeto:
cd petshop

arduino
Copiar código

3. Crie e ative uma virtual environment:
python3 -m venv venv
source venv/bin/activate

csharp
Copiar código

4. Instale as dependências do projeto:
pip install -r requirements.txt

csharp
Copiar código

5. Execute as migrações do banco de dados:
python manage.py migrate

markdown
Copiar código

6. Inicie o servidor de desenvolvimento:
python manage.py runserver

less
Copiar código

7. Acesse o projeto em seu navegador em [http://localhost:8000](http://localhost:8000).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
