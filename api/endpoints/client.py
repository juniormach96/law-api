from typing import List
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from models.client import Clientes
from models.process import Processos

router = APIRouter()

# Conectando ao banco de dados
client = MongoClient("mongodb://localhost:27017")
db = client["clientes"]
client_collection = db["clientes"]
process_collection = db["processos"]


@router.get("/clients", response_model=List[Clientes])
async def read_clients():
    clients = []
    for client in client_collection.find():
        clients.append(Clientes(**client))
    return clients


@router.post("/clients", response_model=Clientes)
async def create_client(client: Clientes):
    client_dict = client.dict()
    inserted_id = client_collection.insert_one(client_dict).inserted_id
    client_dict["_id"] = inserted_id
    return Clientes(**client_dict)


@router.get("/clients/{client_id}", response_model=Clientes)
async def read_client(client_id: str):
    client = client_collection.find_one({"_id": ObjectId(client_id)})
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return Clientes(**client)


@router.put("/clients/{client_id}", response_model=Clientes)
async def update_client(client_id: str, client: Clientes):
    client_dict = client.dict(exclude_unset=True)
    result = client_collection.update_one({"_id": ObjectId(client_id)}, {"$set": client_dict})
    if not result.modified_count:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return Clientes(**client_dict)


@router.delete("/clients/{client_id}", response_model=Clientes)
async def delete_client(client_id: str):
    client = client_collection.find_one({"_id": ObjectId(client_id)})
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    client_collection.delete_one({"_id": ObjectId(client_id)})
    return Clientes(**client)


# process
@router.get("/clients/{client_id}/processes", response_model=List[Processos])
async def read_processes(client_id: str):
    processes = []
    for process in process_collection.find({"cliente_id": client_id}):
        processes.append(Processos(**process))
    return processes


@router.post("/clients/{client_id}/processes", response_model=Processos)
async def create_process(client_id: str, process: Processos):
    process_dict = process.dict()
    process_dict["cliente_id"] = client_id
    inserted_id = process_collection.insert_one(process_dict).inserted_id
    process_dict["_id"] = inserted_id
    return Processos(**process_dict)


@router.delete("/clients/{client_id}/processes/{process_id}", response_model=Processos)
async def delete_process(client_id: str, process_id: str):
    process = process_collection.find_one({"_id": ObjectId(process_id), "cliente_id": client_id})
    if not process:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    process_collection.delete_one({"_id": ObjectId(process_id)})
    return Processos(**process)
