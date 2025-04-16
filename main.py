from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models import Tarefa, TarefaBase
from salvar import salvar_tarefas, carregar_tarefas

app = FastAPI()


tarefas, proximo_id = carregar_tarefas()

#Modelo de dados

class TarefaBase(BaseModel):
    titulo: str
    feita:  bool  = False

class Tarefa(TarefaBase):
    id: int

#banco simulado 

tarefas: List[Tarefa]  = []
proximo_id  = 1

#lista de tarefas (simulando um banco de dados)

titulos_exemplo = [
    {"titulo": "Estudar FastAPI", "feita": False},
    {"titulo": "Criar API de tarefas", "feita": True},
    {"titulo": "Apagar tarefa com DELETE", "feita": False},
    {"titulo": "Editar tarefa com PUT", "feita": False},
    {"titulo": "Salvar tarefas em JSON", "feita": False},
    {"titulo": "Estudar SQLite", "feita": False},
    {"titulo": "Conectar com banco de dados", "feita": False},
    {"titulo": "Separar projeto em módulos", "feita": False},
    {"titulo": "Testar API com Swagger UI", "feita": True},
    {"titulo": "Testar API com Postman", "feita": False},
    {"titulo": "Aprender rotas dinâmicas", "feita": False},
    {"titulo": "Criar autenticação básica", "feita": False},
    {"titulo": "Ler documentação do FastAPI", "feita": True},
    {"titulo": "Criar projeto real de exemplo", "feita": False},
    {"titulo": "Publicar API no Render", "feita": False},
    {"titulo": "Criar rota GET por ID", "feita": False},
    {"titulo": "Criar rota PATCH para atualizar só o status", "feita": False},
    {"titulo": "Adicionar validações com Pydantic", "feita": False},
    {"titulo": "Trabalhar com UUID como ID", "feita": False},
    {"titulo": "Aprender testes automatizados com pytest", "feita": False}]


for  tarefa in titulos_exemplo: 
    tarefas.append(Tarefa(id=proximo_id, **tarefa))
    proximo_id += 1

#Rota apra listar todas  as tarefas

@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.get("/tarefas/{id}",  response_model=Tarefa)
def obter_tarefa(id: int):
    for tarefa  in tarefas:
        if tarefa.id  == id:
            return tarefa  
    return  {"erro": "Tarefa nao encontrada"}

#PUT EDITAR TITULO E STATUS
@app.put("/tarefas/{id}", response_model=Tarefa)
def atualiza_tarefa(id: int, tarefa_atualizada: TarefaBase):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == id:
            nova_tarefa = Tarefa(id=id, **tarefa_atualizada.dict())
            tarefas[i] = nova_tarefa
            return nova_tarefa
    return {"erro": "Tarefa nao encontra"}

#PATCH atualiza o status

@app.patch("/tarefas/{id}", response_model=Tarefa)
def atualizar_status(id: int, feita: bool):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == id:
            tarefa.feita = feita
            return tarefa
        


#rota para criar nova tarefa  

@app.post("/tarefas", response_model=Tarefa)
def criar_tarefa(tarefa: TarefaBase):
   global proximo_id
   nova_tarefa = Tarefa(id=proximo_id, **tarefa.dict())
   tarefas.append(nova_tarefa)
   proximo_id  += 1
   return nova_tarefa

@app.delete("/tarefas/{id}")
def deletor_tarefa(id: int):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == id:
            tarefa_removida = tarefas.pop(i)
            return {"mensagem": "Tarefa removida", "tarefa": tarefa_removida}
    return {"erro": "Tarefa não encontrada"}  

        
