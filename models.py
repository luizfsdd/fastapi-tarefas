from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo: str
    feita: bool = False

class Tarefa(TarefaBase):
    id: int
