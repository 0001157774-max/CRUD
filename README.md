# Inventário de Jogos

Este projeto consiste em uma API desenvolvida com Flask para gerenciamento de um inventário de jogos. A aplicação permite realizar operações de cadastro, consulta, atualização e exclusão de jogos armazenados em um banco de dados SQLite.

---

## Objetivo

O objetivo do projeto é implementar um sistema CRUD (Create, Read, Update, Delete) utilizando Python, Flask e SQLite, seguindo o padrão REST e utilizando requisições HTTP com respostas em formato JSON.

---

## Como executar o projeto

1. Clone o repositório:
git clone URL_DO_REPOSITORIO

2. Acesse a pasta do projeto:
cd inventario-jogos

3. Crie o ambiente virtual:
python -m venv venv

4. Ative o ambiente virtual:

Windows:
venv\Scripts\activate

5. Instale as dependências:
pip install flask

---

## Banco de Dados

Antes de iniciar a aplicação, é necessário criar o banco de dados.

Execute o comando:

python init_db.py

Esse comando criará o banco `inventario.db` com a tabela `jogos`.

---

## Executando a aplicação

Para iniciar o servidor:

python app.py

A API estará disponível em:
http://127.0.0.1:5000/

---

## Rotas da API

### Listar todos os jogos
GET /jogos

### Buscar jogo por ID
GET /jogos/{id}

### Inserir novo jogo
POST /jogos

### Atualizar jogo
PUT /jogos/{id}

### Remover jogo
DELETE /jogos/{id}

---

## Exemplos de uso com curl

### Inserir jogo:
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\":\"FIFA 24\",\"estoque\":8,\"valor\":299.90}"

### Listar jogos:
curl http://127.0.0.1:5000/jogos

### Buscar por ID:
curl http://127.0.0.1:5000/jogos/1

### Atualizar jogo:
curl -X PUT http://127.0.0.1:5000/jogos/1 -H "Content-Type: application/json" -d "{\"titulo\":\"Minecraft\",\"estoque\":15,\"valor\":99.90}"

### Deletar jogo:
curl -X DELETE http://127.0.0.1:5000/jogos/1

---

## Tecnologias utilizadas

- Python
- Flask
- SQLite

---

## Observações

- A aplicação não possui interface gráfica.
- As interações são feitas via requisições HTTP.
- Pode-se utilizar ferramentas como Postman, Insomnia ou curl para testes.

---

## Conclusão

O sistema implementa um CRUD completo para gerenciamento de jogos, com estrutura simples e funcional. O projeto segue boas práticas no desenvolvimento de APIs REST e manipulação de banco de dados com SQLite.
