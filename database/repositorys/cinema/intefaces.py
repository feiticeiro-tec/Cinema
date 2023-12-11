from pydantic import BaseModel


class Endereco(BaseModel):
    cep: str
    uf: str
    cidade: str
    bairro: str
    rua: str
    numero: int
    complemento: str = None
    referencia: str = None
