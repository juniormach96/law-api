from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class Clientes(BaseModel):
    name: str
    birth_date: str
    tipo: str
    CPF: str
    RG: str
    orgao_emissor: str
    cep: str
    endereco: Optional[str]
    numero: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    profissao: Optional[str]
    telefone_fixo: Optional[str]
    telefone_whatsapp: Optional[str]
    celular: Optional[str]
    email: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "João da Silva",
                "birth_date": "1990-01-01",
                "tipo": "pessoa física",
                "CPF": "123.456.789-00",
                "RG": "12.345.678-9",
                "orgao_emissor": "SSP/SP",
                "cep": "01234-567",
                "endereco": "Rua A, 123",
                "numero": "456",
                "complemento": "Apto 12",
                "bairro": "Centro",
                "cidade": "São Paulo",
                "uf": "SP",
                "profissao": "Engenheiro",
                "telefone_fixo": "(11) 1234-5678",
                "telefone_whatsapp": "(11) 91234-5678",
                "celular": "(11) 91234-5678",
                "email": "joao.silva@gmail.com"
            }
        }
