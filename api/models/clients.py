from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class Client(BaseModel):
    nome: str
    email: str
    telefone: str
    cpf: str
    endereco: Optional[str]
    cidade: Optional[str]
    estado: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "nome": "João da Silva",
                "email": "joao.silva@gmail.com",
                "telefone": "(11) 91234-5678",
                "cpf": "123.456.789-00",
                "endereco": "Rua A, 123",
                "cidade": "São Paulo",
                "estado": "SP"
            }
        }