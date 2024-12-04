# main.py

from fastapi import FastAPI, HTTPException # type: ignore
from typing import List

app = FastAPI()

# Banco de dados simulado (em memória)
times_db = [
    {"id": 1, "nome": "Flamengo", "jogadores": [{"id": 1, "nome": "Gabigol", "posicao": "Atacante"}, {"id": 2, "nome": "Arrascaeta", "posicao": "Meio-campo"}]},
    {"id": 2, "nome": "Palmeiras", "jogadores": [{"id": 3, "nome": "Rafael Veiga", "posicao": "Meio-campo"}, {"id": 4, "nome": "Dudu", "posicao": "Atacante"}]}
]

partidas_db = [
    {"id": 1, "time_casa": "Flamengo", "time_fora": "Palmeiras", "placar": "2-1"}
]

# Rota para criar um time
@app.post("/times/")
def criar_time(id: int, nome: str, jogadores: List[dict]):
    # Verifica se o time já existe
    if any(t['id'] == id for t in times_db):
        raise HTTPException(status_code=400, detail="Time com este ID já existe.")
    
    # Adiciona o time
    times_db.append({"id": id, "nome": nome, "jogadores": jogadores})
    return {"msg": "Time criado com sucesso!"}

# Rota para listar todos os times
@app.get("/times/")
def listar_times():
    return times_db

# Rota para listar um time específico
@app.get("/times/{time_id}")
def obter_time(time_id: int):
    time = next((t for t in times_db if t["id"] == time_id), None)
    if not time:
        raise HTTPException(status_code=404, detail="Time não encontrado.")
    return time

# Rota para atualizar um time (PUT)
@app.put("/times/{time_id}")
def atualizar_time(time_id: int, nome: str, jogadores: List[dict]):
    time = next((t for t in times_db if t["id"] == time_id), None)
    if not time:
        raise HTTPException(status_code=404, detail="Time não encontrado.")
    
    # Atualiza os dados do time
    time["nome"] = nome
    time["jogadores"] = jogadores
    return {"msg": "Time atualizado com sucesso!"}

# Rota para excluir um time (DELETE)
@app.delete("/times/{time_id}")
def excluir_time(time_id: int):
    global times_db
    times_db = [t for t in times_db if t["id"] != time_id]
    return {"msg": "Time excluído com sucesso!"}

# Rota para criar uma partida
@app.post("/partidas/")
def criar_partida(id: int, time_casa: str, time_fora: str, placar: str):
    # Verifica se a partida já existe
    if any(p['id'] == id for p in partidas_db):
        raise HTTPException(status_code=400, detail="Partida com este ID já existe.")
    
    # Adiciona a partida
    partidas_db.append({"id": id, "time_casa": time_casa, "time_fora": time_fora, "placar": placar})
    return {"msg": "Partida criada com sucesso!"}

# Rota para listar todas as partidas
@app.get("/partidas/")
def listar_partidas():
    return partidas_db

# Rota para listar uma partida específica
@app.get("/partidas/{partida_id}")
def obter_partida(partida_id: int):
    partida = next((p for p in partidas_db if p["id"] == partida_id), None)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada.")
    return partida

# Rota para atualizar uma partida (PUT)
@app.put("/partidas/{partida_id}")
def atualizar_partida(partida_id: int, time_casa: str, time_fora: str, placar: str):
    partida = next((p for p in partidas_db if p["id"] == partida_id), None)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada.")
    
    # Atualiza os dados da partida
    partida["time_casa"] = time_casa
    partida["time_fora"] = time_fora
    partida["placar"] = placar
    return {"msg": "Partida atualizada com sucesso!"}

# Rota para excluir uma partida (DELETE)
@app.delete("/partidas/{partida_id}")
def excluir_partida(partida_id: int):
    global partidas_db
    partidas_db = [p for p in partidas_db if p["id"] != partida_id]
    return {"msg": "Partida excluída com sucesso!"}


