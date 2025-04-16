import json
import os
from models import Tarefa

ARQUIVO_TAREFAS = "tarefas.json"

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump([tarefa.dict() for tarefa in tarefas], f, ensure_ascii=False, indent=2)

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        try:
            with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
                tarefas_carregadas = json.load(f)
                tarefas = [Tarefa(**t) for t in tarefas_carregadas]
                proximo_id = max(t.id for t in tarefas) + 1 if tarefas else 1
                return tarefas, proximo_id
        except json.JSONDecodeError:
            print("⚠️ Arquivo JSON vazio ou corrompido. Iniciando com lista vazia.")
    return [], 1  # retorna lista vazia e ID inicial
