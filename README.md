# 📋 FastAPI Tarefas

Uma API simples de gerenciamento de tarefas desenvolvida com **FastAPI**. Ideal para estudos e pequenos projetos backend com Python.

![image](https://github.com/user-attachments/assets/86dbd26e-6520-40f3-99f8-61996a3885e6)
![image](https://github.com/user-attachments/assets/fca23004-0b96-4755-88aa-4baac16b7f48)



## 🚀 Tecnologias

- Python 3.10+
- FastAPI
- Uvicorn

## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/luizfsdd/fastapi-tarefas.git
cd fastapi-tarefas

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS

# Instale as dependências
pip install -r requirements.txt


 ▶️ Executando o projeto

#bash

uvicorn main:app --reload
Acesse: http://127.0.0.1:8000

 📚 Documentação automática
Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

📌 Funcionalidades

Criar tarefa (POST /tarefas)

Listar tarefas (GET /tarefas)

Atualizar status (PATCH /tarefas/{id})

Deletar tarefa (DELETE /tarefas/{id})

Persistência automática em arquivo .json

 💾 Exemplo de tarefa

json

{
  "id": 1,
  "titulo": "Estudar FastAPI",
  "feita": false
}

🧠 Autor

Luiz – github.com/luizfsdd
