# Projeto-VPL

## Autor: Bruno Boldrim Saboya

- Esse projeto tem como objetivo criar um banco de dados em PostgreSQL com o banco de dados fornecidos pela Atlas
- Em seguida criar uma API em Django que possua endpoint que recebe o CNPJ de qualquer fundo e apresenta o retorno desse fundo no mês de julho de 2024.
- Criar uma página simples utilizando HTML, CSS e Javascript, com uma barra de pesquisa onde seja possível inserir o CNPJ de um fundo junto a um botão para obter o retorno do fundo
utilizando o endpoint criado no passo anterior

Instruções de uso:

### 1 Clone o repositório:
  ```
  git clone https://github.com/BrunoSaboya/Projeto-VPL
  cd calculadora_fundos
  ```

### 2 Criar e ativar um ambiente virtual:
  Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
  Linux/MacOS:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3 Instalar as dependências:
  ```
  pip install -r requirements.txt
  ``` 

### 4 Realizar migrações do Banco de Dados:
  ```
  python manage.py migrate
  ```

### 5 Rodar o servidor de desenvolvimento:
  ```
  python manage.py runserver
  ```

#### Considerações:

- Configurações de Banco de Dados: Se o projeto for apresentado em uma máquina diferente, certifique-se de que o banco de dados PostgreSQL está configurado e acessível. O arquivo settings.py pode precisar ser ajustado para refletir as credenciais do banco de dados na nova máquina.

- O arquivo dados.py precisa ser alterado com as informações de cada máquina caso deseja ser rodado e criado o banco de dados anteriormente com as credenciais pessoais.









