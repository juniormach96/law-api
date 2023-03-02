from typing import List, Optional
from pydantic import BaseModel


class Advogados(BaseModel):
    name: str
    birth_date: str
    CPF: str
    especializacoes: List[str]
    RG: str
    orgao_emissor: str
    cep: str
    endereco: Optional[str]
    numero: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    oab_numero: str
    oab_uf: str
    telefone_fixo: Optional[str]
    telefone_whatsapp: Optional[str]
    celular: Optional[str]
    email: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Ana Souza",
                "birth_date": "1980-01-01",
                "CPF": "123.456.789-00",
                "especializacoes": ["Direito Civil", "Direito Trabalhista"],
                "RG": "12.345.678-9",
                "orgao_emissor": "SSP/SP",
                "cep": "01234-567",
                "endereco": "Rua A, 123",
                "numero": "456",
                "complemento": "Apto 12",
                "bairro": "Centro",
                "cidade": "São Paulo",
                "uf": "SP",
                "oab_numero": "SP12345",
                "oab_uf": "SP",
                "telefone_fixo": "(11) 1234-5678",
                "telefone_whatsapp": "(11) 91234-5678",
                "celular": "(11) 91234-5678",
                "email": "ana.souza@advogados.com.br"
            }
        }
