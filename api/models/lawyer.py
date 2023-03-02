from typing import Optional
from pydantic import BaseModel


class Lawyer(BaseModel):
    nome: str
    email: str
    telefone: str
    oab: str
    escritorio: Optional[str]
    cidade: Optional[str]
    estado: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "nome": "Ana Souza",
                "email": "ana.souza@advogados.com.br",
                "telefone": "(11) 99876-5432",
                "oab": "SP12345",
                "escritorio": "Advogados Associados",
                "cidade": "São Paulo",
                "estado": "SP"
            }
        }