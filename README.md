# Projeto-VPL

## Autor: Bruno Boldrim Saboya

- Esse projeto tem como objetivo criar um banco de dados em PostgreSQL com o banco de dados fornecidos pela Atlas
- Em seguida criar uma API em Django que possua endpoint que recebe o CNPJ de qualquer fundo e apresenta o retorno desse fundo no mês de julho de 2024.
- Criar uma página simples utilizando HTML, CSS e Javascript, com uma barra de pesquisa onde seja possível inserir o CNPJ de um fundo junto a um botão para obter o retorno do fundo
utilizando o endpoint criado no passo anterior

Instruções de uso:

### 1 Clone o repositório:
  ´´´ python
  git clone https://github.com/BrunoSaboya/Projeto-VPL
  ´´´
  ´cd calculadora_fundos´

### 2 Criar e ativar um ambiente virtual:
  Windows:
  ´python -m venv venv´
  ´venv\Scripts\activate´
  Linux/MacOS:
  ´python3 -m venv venv´
  ´source venv/bin/activate´

### 3 Instalar as dependências:
  ´pip install -r requirements.txt´

### 4 Realizar migrações do Banco de Dados:
  ´python manage.py migrate´

### 5 Rodar o servidor de desenvolvimento:
  ´python manage.py runserver´
