from pydantic import BaseModel


class Empresa(BaseModel):
    nome: str
    endereco: str
    cnpj: str
    telefone: str

    class Config:
        schema_extra = {
            "example": {
                "nome": "Empresa XYZ LTDA",
                "endereco": "Rua A, 123",
                "cnpj": "12.345.678/0001-90",
                "telefone": "(11) 1234-5678"
            }
        }
