from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from models.task import Tarefas


class Processos(BaseModel):
    numero: str
    data: str
    status: str
    tipo: str
    assunto: str
    advogado_id: ObjectId = Field(..., alias="advogado")
    cliente_id: ObjectId = Field(..., alias="cliente")
    parte: str
    contra_parte: str
    comarca: str
    valor: float
    honorarios: float
    observacoes: Optional[str]
    link: Optional[str]
    anotacoes: Optional[str]
    tarefas: Optional[List[Tarefas]]

    class Config:
        schema_extra = {
            "example": {
                "numero": "0001/2022",
                "data": "2022-01-01",
                "status": "Ativo",
                "tipo": "Cível",
                "assunto": "Ação de cobrança",
                "advogado_id": "61b090d4e4a4d8e6d0c1a95f",
                "cliente_id": "61b090d4e4a4d8e6d0c1a95c",
                "parte": "Ativo",
                "contra_parte": "Empresa X",
                "comarca": "São Paulo",
                "valor": 5000.00,
                "honorarios": 1000.00,
                "observacoes": "Cliente deseja realizar acordo extrajudicial",
                "link": "https://meusite.com/processo0001",
                "anotacoes": "Reunir documentos para a audiência",
                "tarefas": [
                    {
                        "titulo": "Prazo para entrega de documentos",
                        "descricao": "O prazo para entrega de documentos é até o dia 15/03/2023"
                    },
                    {
                        "titulo": "Enviar notificação para a contra parte",
                        "descricao": "Enviar notificação para a empresa X sobre o andamento do processo"
                    }
                ]
            }
        }
