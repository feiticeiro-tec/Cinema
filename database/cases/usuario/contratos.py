from pydantic import BaseModel


class UsuarioCreateContrato(BaseModel):
    nome: str
    email: str
    senha: str
