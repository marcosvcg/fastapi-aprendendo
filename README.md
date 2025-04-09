# 🚀 Primeira API usando FastAPI — Projeto de Estudo

Este é o meu primeiro projeto com [FastAPI](https://fastapi.tiangolo.com/), feito com o objetivo de aprender os fundamentos da construção de APIs modernas em Python. Ele implementa uma API simples para cadastro e listagem de usuários, com armazenamento em um banco de dados SQLite em memória.

---

## 🛠️ Tecnologias utilizadas

- **FastAPI** — Framework moderno e rápido para construção de APIs com Python 💻
- **SQLite** — Banco de dados leve, usado aqui na versão em memória (pode ser persistido) 📊
- **Pydantic** — Tipagem e validação automática de dados ✍
- **Uvicorn** — Servidor ASGI leve e de alta performance ⚡
- **Python 3.10+** — Linguagem principal utilizada 🐍

---

## 📦 Estrutura básica do projeto

``` bash
fastapi-aprendendo/
├── controller/              # Endpoints (rotas da API)
│   └── user_controller.py   # Rotas relacionadas aos usuários
│
├── model/                   # Modelos de dados com Pydantic
│   └── user.py              # UserIn e UserOut
│
├── repo/                    # Repositório de dados (acesso ao banco)
│   └── user_repo.py         # Operações CRUD para usuários
│
├── service/                 # Lógica de negócio
│   └── user_service.py      # Regras de negócio para criação e listagem de usuários
│
├── util/                    # Utilitários auxiliares
│   ├── database.py          # Conexão SQLite (em memória)
│   └── hasher.py            # Função para gerar hash das senha
│
├── main.py                  # Ponto de entrada da aplicação FastAPI
└── README.md                # Documentação do projeto 
```

## 🧪 Como rodar o projeto localmente

1. Clone o repositório:

``` bash
git clone https://github.com/marcosvcg/fastapi-aprendendo.git
cd fastapi-aprendendo
```

2. Crie um Ambiente Vitual (.venv):

``` bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:

``` bash
pip install -r requirements.txt
``` 

4. Inicie o servidor:

``` bash
fastapi dev main.py
``` 

5. Acessar a documentação da API:

``` bash
http://localhost:8000/docs
``` 

## 📬 Endpoints disponíveis

- `GET /users` — Lista todos os usuários cadastrados
- `POST /user` — Cadastra um novo usuário (passando `username` e `password`)
- `GET /user/{id}` — Retorna os dados de um usuário específico