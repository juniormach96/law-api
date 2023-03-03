from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

class Tarefas(BaseModel):
    titulo: str
    descricao: str
    prazo: str
    concluida: Optional[bool]
    processo_id: ObjectId = Field(..., alias="processo")
    advogado_id: Optional[ObjectId] = Field(None, alias="advogado")

    class Config:
        schema_extra = {
            "example": {
                "titulo": "Preparar documentos para audiência",
                "descricao": "Reunir documentos necessários para a audiência de conciliação",
                "prazo": "2022-02-01",
                "concluida": False,
                "processo_id": "61b090d4e4a4d8e6d0c1a95a",
                "advogado_id": "61b090d4e4a4d8e6d0c1a95f"
            }
        }
